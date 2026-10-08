import math


class Figure:
    """Класс, описывающий геометрическую фигуру (круг)."""

    def __init__(self, radius: float):
        """
        Инициализация круга.
        :param radius: Радиус круга.
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.radius = radius

    def area(self) -> float:
        """Возвращает площадь круга."""
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """Возвращает длину окружности (периметр)."""
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    try:
        circle = Figure(5.5)
        print(f"Площадь круга: {circle.area():.2f}")
        print(f"Длина окружности: {circle.perimeter():.2f}")
    except ValueError as e:
        print(f"Ошибка при создании фигуры: {e}")
