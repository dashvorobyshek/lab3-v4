from abc import ABC, abstractmethod


class Employee(ABC):
    """Абстрактный базовый класс для сотрудников."""

    def __init__(self, name: str):
        """
        Инициализация сотрудника.
        :param name: Имя сотрудника.
        """
        self.name = name

    @abstractmethod
    def calculate_salary(self) -> float:
        """
        Абстрактный метод для расчета заработной платы.
        Должен быть реализован в дочерних классах.
        """
        pass

    def get_info(self) -> str:
        """Возвращает базовую информацию о сотруднике."""
        return (f"Сотрудник: {self.name}, "
                f"Зарплата: {self.calculate_salary():.2f} руб.")


class HourlyEmployee(Employee):
    """Класс сотрудника с почасовой оплатой, наследующий Employee."""

    def __init__(self, name: str, hours_worked: float, hourly_rate: float):
        """
        Инициализация почасового сотрудника.
        :param name: Имя сотрудника.
        :param hours_worked: Отработанные часы.
        :param hourly_rate: Ставка в час.
        """
        super().__init__(name)
        if hours_worked < 0 or hourly_rate < 0:
            raise ValueError("Часы и ставка не могут быть отрицательными.")
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self) -> float:
        """
        Реализация абстрактного метода расчета
        зарплаты для почасового работника.
        """
        return self.hours_worked * self.hourly_rate


if __name__ == "__main__":
    try:
        # emp = Employee("Тест")  # Вызовет TypeError (класс абстрактный)
        worker = HourlyEmployee("Дарья Сергеевна", 40.0, 850.50)
        print(worker.get_info())
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
