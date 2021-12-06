test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> free_bacon(0)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(1)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(2)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(3)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(4)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(13)
          10
          >>> # ban indexing
          >>> test.check('hog.py', 'free_bacon', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          >>> # check pi is not changed
          >>> FIRST_101_DIGITS_OF_PI == 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(44)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(37)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(40)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(24)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(46)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(99)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(10)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(47)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(67)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(92)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(9)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(25)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(75)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(82)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(88)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(72)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(41)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(15)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(42)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(93)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(99)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(73)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(4)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(83)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(34)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(4)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(53)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(19)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(1)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> free_bacon(85)
          3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
