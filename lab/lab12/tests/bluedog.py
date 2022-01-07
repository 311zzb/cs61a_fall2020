test = {
  'name': 'bluedog',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM bluedog;
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          sqlite> SELECT * FROM bluedog_songs;
          blue|dog|Smells like Teen Spirit
          blue|dog|The Middle
          blue|dog|Clair De Lune
          blue|dog|Smells like Teen Spirit
          blue|dog|Everytime We Touch
          blue|dog|Dancing Queen
          blue|dog|Clair De Lune
          blue|dog|Clair De Lune
          blue|dog|The Middle
          blue|dog|Down With The Sickness
          blue|dog|thank u, next
          blue|dog|All I want for Christmas is you
          blue|dog|Everytime We Touch
          blue|dog|Clair De Lune
          blue|dog|Everytime We Touch
          blue|dog|thank u, next
          blue|dog|All I want for Christmas is you
          blue|dog|Smells like Teen Spirit
          blue|dog|The Middle
          blue|dog|Clair De Lune
          blue|dog|Dancing Queen
          blue|dog|All I want for Christmas is you
          blue|dog|Dancing Queen
          blue|dog|Clair De Lune
          blue|dog|Dancing Queen
          blue|dog|Dancing Queen
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
