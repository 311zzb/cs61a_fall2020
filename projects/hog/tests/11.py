test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> extra_turn_strategy(10, 19, cutoff=8, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(30, 54, cutoff=7, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(17, 36, cutoff=100, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(24, 5, cutoff=1, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(extra_turn_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> extra_turn_strategy(47, 64, cutoff=3, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(66, 78, cutoff=14, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(75, 7, cutoff=2, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(24, 3, cutoff=8, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(46, 55, cutoff=5, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(65, 55, cutoff=3, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(73, 99, cutoff=10, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(46, 56, cutoff=2, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(31, 20, cutoff=13, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(92, 54, cutoff=1, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(31, 57, cutoff=4, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(32, 45, cutoff=12, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(33, 30, cutoff=0, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(48, 74, cutoff=16, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(59, 16, cutoff=15, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(12, 5, cutoff=0, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(60, 65, cutoff=10, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(84, 89, cutoff=3, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(19, 69, cutoff=17, num_rolls=3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(22, 34, cutoff=5, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(96, 40, cutoff=19, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(66, 71, cutoff=1, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(33, 76, cutoff=8, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(68, 22, cutoff=11, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(3, 64, cutoff=17, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(23, 44, cutoff=18, num_rolls=9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(76, 83, cutoff=19, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(90, 76, cutoff=7, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(48, 62, cutoff=14, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(34, 40, cutoff=0, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(17, 46, cutoff=3, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(87, 16, cutoff=2, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(50, 57, cutoff=5, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(7, 88, cutoff=2, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(32, 56, cutoff=10, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(11, 11, cutoff=8, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(98, 30, cutoff=8, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(51, 75, cutoff=16, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(78, 30, cutoff=14, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(1, 66, cutoff=1, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(91, 7, cutoff=5, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(35, 12, cutoff=2, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(51, 92, cutoff=14, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(64, 49, cutoff=16, num_rolls=4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(35, 45, cutoff=3, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(24, 12, cutoff=17, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(2, 22, cutoff=8, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(72, 95, cutoff=1, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(51, 81, cutoff=4, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(45, 40, cutoff=18, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(96, 11, cutoff=13, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(57, 96, cutoff=9, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(48, 30, cutoff=0, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(61, 33, cutoff=2, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(14, 26, cutoff=2, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(75, 98, cutoff=15, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(24, 12, cutoff=2, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(16, 40, cutoff=7, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(31, 19, cutoff=19, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(11, 36, cutoff=7, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(72, 50, cutoff=9, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(78, 54, cutoff=18, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(24, 81, cutoff=9, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(11, 87, cutoff=18, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(38, 54, cutoff=17, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(63, 40, cutoff=7, num_rolls=9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(51, 74, cutoff=13, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(66, 80, cutoff=15, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(27, 72, cutoff=11, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(75, 73, cutoff=11, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(86, 24, cutoff=0, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(58, 42, cutoff=5, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(19, 46, cutoff=10, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(18, 46, cutoff=10, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(91, 9, cutoff=9, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(19, 81, cutoff=8, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(15, 72, cutoff=16, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(70, 81, cutoff=15, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(84, 91, cutoff=0, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(61, 74, cutoff=3, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(94, 39, cutoff=19, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(91, 95, cutoff=15, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(45, 84, cutoff=4, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(23, 39, cutoff=0, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(89, 56, cutoff=14, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(32, 13, cutoff=4, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(96, 44, cutoff=3, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(77, 59, cutoff=15, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(32, 79, cutoff=17, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(54, 15, cutoff=17, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(74, 96, cutoff=11, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(46, 82, cutoff=14, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(42, 67, cutoff=18, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(85, 77, cutoff=8, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(58, 64, cutoff=1, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(41, 19, cutoff=5, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(90, 38, cutoff=12, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(35, 51, cutoff=7, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(42, 52, cutoff=1, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> extra_turn_strategy(62, 17, cutoff=9, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
