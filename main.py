
import time
from functional_tasks import (
    apply_multiple_funcs,
    pipe_map,
    filter_even_numbers,
    time_it,
    my_reduce,
    curry,
)


@time_it
def compute_heavy_task(n: int) -> int:
    """Тестовая нагрузочная функция."""
    time.sleep(0.05)  # Имитация расчётов
    return sum(i * i for i in range(n))


def main() -> None:
    print("=" * 65)
    print("      ЛАБОРАТОРНАЯ РАБОТА № 4: ФУНКЦИОНАЛЬНЫЙ PYTHON (ВАР 10)")
    print("=" * 65)

    print("\n[1] Задание 10 (Средн.): Применение нескольких функций через map")
    nums = [1, 2, 3, 4, 5]
    transformations = [
        lambda x: x ** 2,      
        lambda x: x * 10,       
        lambda x: f"num_{x}"    
    ]
    multi_res = apply_multiple_funcs(transformations, nums)
    print(f"Исходный список: {nums}")
    print("Результат применения кортежа функций к каждому элементу:")
    for num, res in zip(nums, multi_res):
        print(f"  {num} -> квадрат: {res[0]}, *10: {res[1]}, строка: {res[2]}")

    piped_res = pipe_map([lambda x: x + 1, lambda x: x * 2], nums)
    print(f"Конвейер map (+1, затем *2): {piped_res}")

    print("\n[2] Задание 2 (Средн.): Фильтрация чётных чисел")
    raw_data = [12, 5, 8, 19, 24, 33, 40, 7, 2]
    evens = filter_even_numbers(raw_data)
    print(f"Исходный список: {raw_data}")
    print(f"Только чётные:    {evens}")

    print("\n[3] Задание 8 (Средн.): Декоратор замера времени работы")
    val = compute_heavy_task(100_000)
    print(f"Результат работы функции: {val}")

    print("\n[4] Задание 10 (Повыш.): Собственный reduce")
    sample_list = [1, 2, 3, 4, 5]
    total_sum = my_reduce(lambda acc, x: acc + x, sample_list)
    factorial_5 = my_reduce(lambda acc, x: acc * x, sample_list, 1)
    print(f"Список: {sample_list}")
    print(f"Сумма через my_reduce: {total_sum}")
    print(f"Произведение (факториал 5!) через my_reduce: {factorial_5}")

    print("\n[5] Задание 3 (Повыш.): Функция-карринг")
    
    def volume(length: float, width: float, height: float) -> float:
        """Объём параллелепипеда."""
        return length * width * height

    curried_volume = curry(volume)
    
    vol1 = curried_volume(2)(3)(4)
    base_box = curried_volume(2)(3)
    vol2 = base_box(10)
    vol3 = curried_volume(5, 4)(2)

    print(f"Вызов по одному curry(2)(3)(4): {vol1}")
    print(f"Частичное применение base_box(10): {vol2}")
    print(f"Смешанный вызов curry(5, 4)(2):  {vol3}")

    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
