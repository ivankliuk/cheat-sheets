__doc__ = """Meta class usage examples
"""

import unittest


def _sum(a, b):
    return a + b


class TestDataProviderMeta(type):
    equal_data = (
        ('test_sum_1_2_ok', 1, 2, 3),
        ('test_sum_5_2_ok', 5, 2, 7),
        ('test_sum_1_4_ok', 1, 4, 5),
        ('test_sum_5_6_ok', 5, 6, 11),
    )
    not_equal_data = (
        ('test_sum_1_2_failed', 1, 2, 12),
        ('test_sum_5_2_failed', 5, 2, 8),
        ('test_sum_1_4_failed', 1, 4, 7),
        ('test_sum_5_6_failed', 5, 6, 5),
    )

    def __new__(meta, classname, bases, class_dict):
        def create_test_method(data, is_equal):
            def test_method(self):
                if is_equal:
                    self.assertEqual(_sum(data[1], data[2]), data[3])
                else:
                    self.assertNotEqual(_sum(data[1], data[2]), data[3])

            return test_method

        for data in meta.equal_data:
            class_dict[data[0]] = create_test_method(data, True)

        for data in meta.not_equal_data:
            class_dict[data[0]] = create_test_method(data, False)

        return type.__new__(meta, classname, bases, class_dict)


class SumFunctionUnitTest(unittest.TestCase):
    __metaclass__ = TestDataProviderMeta


if __name__ == '__main__':
    unittest.main()
