test = {
  'name': 'div_interval',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Type AssertionError if you think an AssertionError is raised
          >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
          '-0.25 to 0.5'
          >>> str_interval(div_interval(interval(4, 8), interval(-1, 2)))
          AssertionError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw03
      >>> from hw03 import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing for abstraction violations
          >>> # Your code should not check for which implementation is used
          >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
          '-0.25 to 0.5'
          >>> str_interval(div_interval(interval(4, 8), interval(-1, 2)))
          AssertionError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw03
      >>> old_abstraction = hw03.interval, hw03.lower_bound, hw03.upper_bound
      >>> hw03.interval = lambda a, b: lambda x: a if x == 0 else b
      >>> hw03.lower_bound = lambda s: s(0)
      >>> hw03.upper_bound = lambda s: s(1)
      >>> from hw03 import *
      """,
      'teardown': r"""
      >>> hw03.interval, hw03.lower_bound, hw03.upper_bound = old_abstraction
      """,
      'type': 'doctest'
    }
  ]
}
