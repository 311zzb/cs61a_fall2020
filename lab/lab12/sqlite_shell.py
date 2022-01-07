#!/usr/bin/env python

# Licensed under the MIT license

# A simple SQLite shell that uses the built-in Python adapter.

import argparse
import io
import os
import re
import sys
import sqlite3

try: import readline
except ImportError: pass

try: FileNotFoundError
except NameError: FileNotFoundError = OSError

def sql_commands(read_line):
	counter = 0
	in_string = None
	j = i = 0
	prev_line = None
	line = None
	concat = []
	while True:
		if line is None:
			while True:  # process preprocessor directives
				counter += 1
				not_in_the_middle_of_any_input = not in_string and i == j and all(len(chunk_) == 0 for chunk_ in concat)
				line = read_line(counter - 1, not_in_the_middle_of_any_input, prev_line)
				prev_line = line
				if not line:
					break
				if not_in_the_middle_of_any_input and line.startswith("."):
					yield line
					line = None
				else:
					break
			if not line:
				break
			j = i = 0
		if j < len(line):
			if not in_string:
				j = min(map(lambda k: k if k >= 0 else len(line), [line.find('"', j), line.find("'", j), line.find(';', j)]))
				if i < j: concat.append(line[i:j]); i = j
				if j < len(line):
					ch = line[j]
					j += 1
					if ch == ';':
						i = j
						concat.append(ch)
						# Eat up any further spaces until a newline
						while j < len(line):
							ch = line[j]
							if not ch.isspace(): break
							j += 1
							if ch == '\n': break
						if i < j: concat.append(line[i:j]); i = j
						yield "".join(concat)
						del concat[:]
					else:
						in_string = ch
			else:
				j = min(map(lambda k: k if k >= 0 else len(line), [line.find(in_string, j)]))
				if i < j: concat.append(line[i:j]); i = j
				if j < len(line):
					ch = line[j]
					assert ch == in_string
					j += 1
					i = j
					concat.append(ch)
					in_string = None
		else:
			if i < j: concat.append(line[i:j]); i = j
			line = None

class SuppressKeyboardInterrupt(object):
	def __init__(self, base):
		self.base = base
		self.ex = None
	def __getattr__(self, key):
		return getattr(self.base, key)
	def mark_interrupt(self, ex):
		self.ex = ex
	def flush(self, *args):
		while True:
			try: return self.base.flush(*args)
			except KeyboardInterrupt as ex: self.mark_interrupt(ex)
	def write(self, *args):
		while True:
			try: return self.base.write(*args)
			except KeyboardInterrupt as ex: self.mark_interrupt(ex)
	def writelines(self, *args):
		while True:
			try: return self.base.writelines(*args)
			except KeyboardInterrupt as ex: self.mark_interrupt(ex)

def parse_escaped_strings(s, encoding='utf-8', pattern=re.compile("(?:[^\"\'\\s]+|\"((?:[^\"]+|\\\\.)*)(?:\"|$)|\'((?:[^\']+|\\\\.)*)(?:\'|$))"), escape_pattern=re.compile("\\\\(.)")):
	for match in pattern.finditer(s):
		m = match.group(0)
		if len(m) > 0 and m[0] in "\'\"'":
			m = escape_pattern.sub(lambda m: (lambda decoded: m.group(1) if m.group(0) == decoded else decoded)(m.group(0).encode(encoding).decode('string-escape')), match.group(1))
		yield m

class Database(object):
	def __init__(self, name, *args, **kwargs):
		self.cursor = sqlite3.connect(name, *args, **kwargs).cursor()
		self.name = name  # assign name only AFTER cursor is created

def isatty(stream):
	return stream.isatty()

def can_call_input_for_stdio(stream):
	return stream == sys.stdin

def prompt(stdin, stdout=None, *args):
	if can_call_input_for_stdio(stdin) and sys.version_info[0] >= 3:
		result = ""
		try:
			result = input(*args)
			result += "\n"
		except EOFError: pass
	else:
		for arg in args:
			stdout.write(arg)
		result = stdin.readline()
	if not result and stdout:
		stdout.write("\n")
	return result

def run(stdin, stdout, stderr, parsed_args=None):
	db = None
	if parsed_args and parsed_args.version:
		stdout.write("%s\n" % (sqlite3.sqlite_version,)); stdout.flush()
	else:
		db = Database(":memory:", isolation_level=None)
	def exec_script(db, filename, ignore_io_errors):
		try:
			with io.open(filename, 'r', encoding='utf-8') as f:
				for command in sql_commands(lambda *args: (lambda s: s or None)(prompt(f))):
					result = exec_command(db, command, False and ignore_io_errors)
					if result is not None:
						return result
		except IOError as ex:
			stderr.write(str(ex) + "\n"); stderr.flush()
			if not ignore_io_errors: return ex.errno
	def raise_invalid_command_error(command):
		raise RuntimeError("Error: unknown command or invalid arguments:  %s." % (repr(command.rstrip()),))
	def exec_command(db, command, ignore_io_errors):
		results = None
		query = None
		query_parameters = {}
		if command.startswith("."):
			try:
				args = list(parse_escaped_strings(command))
				if args[0] in (".quit", ".exit"):
					return 0
				elif args[0] == ".help":
					stderr.write("""
.exit                  Exit this program
.help                  Show this message
.cd DIRECTORY          Change the working directory to DIRECTORY
.quit                  Exit this program
.open FILE             Close existing database and reopen FILE
.read FILENAME         Execute SQL in FILENAME
.tables                List names of tables
.schema ?PATTERN?      Show the CREATE statements matching PATTERN
                       Add --indent for pretty-printing
""".lstrip()); stderr.flush()
				elif args[0] == ".cd":
					if len(args) != 2: raise_invalid_command_error(command)
					os.chdir(args[1])
				elif args[0] == ".tables":
					query = "SELECT name FROM sqlite_master WHERE type = 'table';"
				elif args[0] == ".open":
					if len(args) <= 1: raise_invalid_command_error(command)
					filename = args[-1]
					for option in args[+1:-1]:
						raise ValueError("option %s not supported" % (repr(option),))
					db.__init__(filename)
				elif args[0] == ".read":
					if len(args) != 2: raise_invalid_command_error(command)
					exec_script(db, args[1], ignore_io_errors)
				elif args[0] == ".schema":
					if len(args) > 2: raise_invalid_command_error(command)
					pattern = args[1] if len(args) > 1 else None
					query_parameters['type'] = 'table'
					if pattern is not None:
						query_parameters['pattern'] = pattern
					query = "SELECT sql || ';' FROM sqlite_master WHERE type = :type" + (" AND name LIKE :pattern" if pattern is not None else "") + ";"
				else:
					raise_invalid_command_error(command)
			except (RuntimeError, OSError, FileNotFoundError) as ex:
				stderr.write(str(ex) + "\n")
				stderr.flush()
		else:
			query = command
		if query is not None:
			try:
				results = db.cursor.execute(query, query_parameters)
			except sqlite3.OperationalError as ex:
				stderr.write(str(ex) + "\n")
				stderr.flush()
		if results is not None:
			for row in results:
				stdout.write("|".join(map(str, row)) + "\n")
			stdout.flush()
	if db:
		if parsed_args and parsed_args.init:
			stderr.write("-- Loading resources from " + parsed_args.init + "\n"); stderr.flush()
			exec_script(db, parsed_args.init, False)
		def read_stdin(index, not_in_the_middle_of_any_input, prev_line):
			show_prompt = True
			to_write = []
			if isatty(stdin) and show_prompt:
				if not_in_the_middle_of_any_input:
					show_prompt = False
					if index == 0:
						to_write.append("SQLite version %s (adapter version %s)\nEnter \".help\" for instructions\nEnter SQL statements terminated with a \";\"\n" % (sqlite3.sqlite_version, sqlite3.version))
						if db.name == ":memory:":
							to_write.append("Connected to a transient in-memory database.\nUse \".open FILENAME\" to reopen on a persistent database.\n")
				if index > 0 and not prev_line:
					to_write.append("\n")
				to_write.append("%7s " % ("sqlite%s>" % ("",) if not_in_the_middle_of_any_input else "...>",))
			try:
				line = prompt(stdin, stdout, "".join(to_write))
			except KeyboardInterrupt:
				line = ""
				raise  # just kidding, don't handle it for now...
			return line
		for command in sql_commands(read_stdin):
			result = exec_command(db, command, True)
			if result is not None:
				return result

def main(program, *args, **kwargs):  # **kwargs = dict(stdin=file, stdout=file, stderr=file); useful for callers who import this module
	argparser = argparse.ArgumentParser(
		prog=os.path.basename(program),
		usage=None,
		description=None,
		epilog=None,
		parents=[],
		formatter_class=argparse.RawTextHelpFormatter)
	argparser.add_argument('-version', '--version', action='store_true', help="show SQLite version")
	argparser.add_argument('-init', '--init', metavar='FILE', help="read/process named file")
	(stdin, stdout, stderr) = (kwargs.pop('stdin', sys.stdin), kwargs.pop('stdout', sys.stdout), kwargs.pop('stderr', sys.stderr))
	if False and len(args) == 0: return argparser.print_usage(stderr)
	return run(stdin, stdout, SuppressKeyboardInterrupt(stderr) if isatty(stderr) else stderr, argparser.parse_args(args))

if __name__ == '__main__':
	import sys
	exit_code = main(*sys.argv)
	if exit_code not in (None, 0): raise SystemExit(exit_code)
