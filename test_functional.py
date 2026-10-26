"""Unit-тесты для проверки модуля functional_tasks.py."""

import unittest
from functional_tasks import (
    apply_multiple_funcs,
    pipe_map,
    filter_even_numbers,
    time_it,
    my_reduce,
    curry,
)


class TestFunctionalTasks(unittest.TestCase):

    def test_apply_multiple_funcs(self):
        funcs = [lambda x: x + 1, lambda x: x * 2]
        result = apply_multiple_funcs(funcs, [1, 2, 3])
        self.assertEqual(result, [(2, 2), (3, 4), (4, 6)])

    def test_pipe_map(self):
        funcs = [lambda x: x * 2, lambda x: x - 1]
        result = pipe_map(funcs, [2, 5])
        # (2*2)-1 = 3; (5*2)-1 = 9
        self.assertEqual(result, [3, 9])

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])
        self.assertEqual(filter_even_numbers([-4, -3, -2, 0]), [-4, -2, 0])

    def test_time_it_decorator(self):
        @time_it
        def add(a, b):
            return a + b

        self.assertEqual(add(10, 25), 35)
        self.assertEqual(add.__name__, "add")  # благодаря @wraps

    def test_my_reduce_sum_and_mul(self):
        self.assertEqual(my_reduce(lambda a, b: a + b, [1, 2, 3, 4]), 10)
        self.assertEqual(my_reduce(lambda a, b: a * b, [1, 2, 3, 4], 1), 24)

    def test_my_reduce_empty_raises(self):
        with self.assertRaises(TypeError):
            my_reduce(lambda a, b: a + b, [])

    def test_curry(self):
        def calc(a, b, c):
            return a * 100 + b * 10 + c

        c_calc = curry(calc)
        self.assertEqual(c_calc(1)(2)(3), 123)
        self.assertEqual(c_calc(1, 2)(3), 123)
        self.assertEqual(c_calc(1)(2, 3), 123)
        self.assertEqual(c_calc(1, 2, 3), 123)


if __name__ == "__main__":
    unittest.main()
