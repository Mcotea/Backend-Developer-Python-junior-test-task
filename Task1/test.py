# test.py
import unittest
from solution import strict


class TestStrictDecorator(unittest.TestCase):

    def test_correct_types(self):
        # Функция с аннотациями типов
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        # Тестируем корректный вызов
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(10, 5), 15)

    def test_type_error_on_incorrect_type(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        # Тестируем передачу некорректного типа
        with self.assertRaises(TypeError):
            sum_two(1, "2")  # Второй аргумент должен быть int, а не str

        with self.assertRaises(TypeError):
            sum_two("1", 2)  # Первый аргумент должен быть int, а не str

    def test_type_error_on_wrong_number_of_arguments(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        # Тестируем на недостаток аргументов
        with self.assertRaises(TypeError):
            sum_two(1)  # Не хватает второго аргумента

        # Тестируем на лишние аргументы
        with self.assertRaises(TypeError):
            sum_two(1, 2, 3)  # Лишний третий аргумент

    def test_no_return_type_check(self):
        # Функция, возвращающая тип, не связанный с аннотациями (не проверяется в декораторе по условию)
        @strict
        def sum_two(a: int, b: int) -> int:
            return "not an int"  # Возвращаем не int

        # Проверка на корректный тип аргументов
        self.assertEqual(sum_two(1, 2), "not an int")

    def test_multiple_function_calls(self):
        @strict
        def multiply(a: int, b: float) -> float:
            return a * b

        # Тестируем несколько корректных вызовов
        self.assertEqual(multiply(2, 3.5), 7.0)
        self.assertEqual(multiply(5, 1.2), 6.0)

        # Тестируем некорректный вызов
        with self.assertRaises(TypeError):
            multiply(2, "3.5")  # Ошибка, потому что второй аргумент должен быть float


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
