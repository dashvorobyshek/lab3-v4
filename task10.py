class PowerIterator:
    """Класс-итератор, возвращающий последовательность чисел,
    возведенных в заданную степень.
    """

    def __init__(self, limit: int, power: int = 2):
        """
        Инициализация итератора.
        :param limit: Количество элементов для генерации.
        :param power: Степень, в которую
        возводятся числа (по умолчанию - квадрат).
        """
        if limit < 0:
            raise ValueError(
                "Количество элементов не может "
                "быть отрицательным."
            )
        self.limit = limit
        self.power = power
        self.current = 1

    def __iter__(self):
        """Возвращает сам итератор для использования в циклах."""
        return self

    def __next__(self) -> int:
        """Вычисляет и возвращает следующее значение последовательности."""
        if self.current > self.limit:
            raise StopIteration
        result = self.current ** self.power
        self.current += 1
        return result


if __name__ == "__main__":
    try:
        print("Квадраты чисел от 1 до 5:")
        for value in PowerIterator(limit=5, power=2):
            print(value)
    except ValueError as e:
        print(f"Ошибка инициализации итератора: {e}")
