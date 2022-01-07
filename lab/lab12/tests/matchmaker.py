test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dog|Smells like Teen Spirit|blue|yellow
          dog|Smells like Teen Spirit|blue|blue
          dog|Smells like Teen Spirit|blue|yellow
          dog|Smells like Teen Spirit|blue|blue
          dog|Smells like Teen Spirit|blue|black
          dog|All I want for Christmas is you|maroon|purple
          dog|All I want for Christmas is you|maroon|pink
          dog|All I want for Christmas is you|maroon|pink
          dog|All I want for Christmas is you|maroon|green
          dog|All I want for Christmas is you|maroon|red
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
