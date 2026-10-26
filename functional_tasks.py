

import time
import inspect
from functools import wraps
from typing import Callable, Iterable, Any


# Задание 10 (Средняя сложность)

def apply_multiple_funcs(funcs: list[Callable[[Any], Any]], items: list[Any]) -> list[tuple]:
    """Применяет кортеж/список функций к каждому элементу списка через map.
    Возвращает список кортежей с результатами вычислений.
    """
    return list(map(lambda item: tuple(f(item) for f in funcs), items))


def pipe_map(funcs: list[Callable[[Any], Any]], items: list[Any]) -> list[Any]:
    """Последовательно прогоняет список данных через цепочку функций map."""
    result = items
    for f in funcs:
        result = list(map(f, result))
    return result


# Задание 2 (Средняя сложность)

def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Фильтрует список, оставляя только чётные числа (с использованием filter)."""
    return list(filter(lambda x: x % 2 == 0, numbers))


# Задание 8 (Средняя сложность)

def time_it(func: Callable) -> Callable:
    """Декоратор, измеряющий и выводящий время выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"[TIME] Функция '{func.__name__}' выполнена за {execution_time:.6f} сек.")
        return result
    return wrapper

# Задание 10 (Повышенная сложность)

def my_reduce(function: Callable[[Any, Any], Any], iterable: Iterable[Any], initializer: Any = None) -> Any:
    """Пользовательская реализация functools.reduce.
    Последовательно сворачивает элементы итерируемого объекта бинарной функцией.
    """
    it = iter(iterable)
    if initializer is None:
        try:
            accumulator = next(it)
        except StopIteration:
            raise TypeError("my_reduce() получил пустой список без начального значения") from None
    else:
        accumulator = initializer

    for element in it:
        accumulator = function(accumulator, element)

    return accumulator


# Задание 3 (Повышенная сложность)

def curry(func: Callable) -> Callable:
    """Преобразует функцию от нескольких аргументов в каррированную функцию,
    позволяющую передавать аргументы по одному или группами.
    """
    total_args = len(inspect.signature(func).parameters)

    @wraps(func)
    def curried(*args):
        if len(args) >= total_args:
            return func(*args[:total_args])
        return lambda *more_args: curried(*(args + more_args))

    return curried
