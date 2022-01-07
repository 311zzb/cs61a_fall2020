test = {
  'name': 'sevens',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          7
          7
          You're not the boss of me!
          7
          the number 7 below.
          7
          Choose this option instead
          You're not the boss of me!
          the number 7 below.
          You're not the boss of me!
          the number 7 below.
          7
          7
          You're not the boss of me!
          Choose this option instead
          7
          the number 7 below.
          You're not the boss of me!
          7
          You're not the boss of me!
          the number 7 below.
          7
          the number 7 below.
          the number 7 below.
          7
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
