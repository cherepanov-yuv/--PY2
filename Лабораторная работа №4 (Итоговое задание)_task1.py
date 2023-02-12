class Lapstop:
    """Базовый класс Ноутбук"""
    def __init__(self, price: float, colour: str, memory: int):
        """
        Создание и подготовка к работе объекта "Ноутбук"
        :param price: цена в тыс.руб.
        :param colour: цвет
        :param memory: память в Гб.
        """
        self._price = price
        self.colour = colour
        self._memory = memory

    # Для атрибутов цены и температуры пропишем свойства, так как на них накладываются ограничения

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        """Свойство, устанавливающее цену с проверками при присвоении значения"""
        if not isinstance(price, float):
            raise TypeError("Цена должна быть типа float")
        if price <= 0:
            raise ValueError("Цена исключительно положительное значение")

    @property
    def memory(self) -> int:
        return self._memory

    @memory.setter
    def memory(self, memory: int) -> None:
        """Свойство, устанавливающее память ноутбука с проверками при присвоении значения"""
        if not isinstance(memory, int):
            raise TypeError("Память должна быть типа int")
        if memory <= 0:
            raise ValueError("Память исключительно положительное значение")
        self._memory = memory

    def __str__(self) -> str:
        """
        Функция, которая должна возвращать строку
        :return: строка
        """
        return f"Ноутбук стоимостью {self._price} тыс.руб., цвет: {self.colour}," \
               f" память: {self._memory} Гб"

    def __repr__(self) -> str:
        """
        Функция, которая должна возвращать валидную python строку
        :return: валидная строка
        """
        return f"{self.__class__.__name__}(price={self._price}, colour={self.colour!r}," \
               f" memory={self._memory})"

    def comparison(self, price1: float) -> None:
        """Функция, определяющая лучший вариант ноутбука сравнивая цены"""
        if self._price > price1:
            print("Новый вариант ноутбука дешевле, чем был предложен ранее")
        if self._price <= price1:
            print("Новый вариант ноутбука по цене уступает ранее предложенному")


class Acer(Lapstop):
    """Ноутбук Acer. Дочерний класс"""
    def __init__(self, price: float, colour: str, memory: int, material: str):
        """
        Создание и подготовка к работе объекта "Ноутбук Acer"
        :param price: цена в тыс.руб.
        :param colour: цвет
        :param memory: память
        :param material: материал корпуса
        """
        super().__init__(price, colour, memory)
        self._material = material

    def __repr__(self) -> str:
        """
        Перегружаем метод __repr__, так как появился новый атрибут
        :return: валидная строка
        """
        return f"{self.__class__.__name__}(price={self._price}, colour={self.colour!r}," \
               f" memory={self._memory}, material={self._material!r})"


class Asus(Lapstop):
    """Ноутбук Asus. Дочерний класс"""
    def __init__(self, price: float, colour: str, memory: int, power_consumption: int):
        """
        Создание и подготовка к работе объекта "Электрическая плита"
        :param price: цена в тыс.руб.
        :param colour: цвет
        :param memory: память
        :param power_consumption: энергопотребление (Вт)
        """
        super().__init__(price, colour, memory)
        self._power_consumption = power_consumption

    # Для атрибута энергопотребление пропишем свойства, так как на нее накладываются ограничения
    @property
    def power_consumption(self) -> int:
        return self._power_consumption

    @power_consumption.setter
    def power_consumption(self, power_consumption: int) -> None:
        """Свойство, устанавливающее энергопотребление с проверками при присвоении значения"""
        if not isinstance(power_consumption, int):
            raise TypeError("Мощность должна быть типа int")
        if power_consumption <= 0:
            raise ValueError("Мощность исключительно положительное значение")
        self._power_consumption = power_consumption

    def __repr__(self) -> str:
        """
        Перегружаем метод __repr__, так как появился новый атрибут
        :return: валидная строка
        """
        return f"{self.__class__.__name__}(price={self._price}, colour={self.colour!r}," \
               f" memory={self._memory}, power_consumption={self._power_consumption})"

    def comparison(self, price1: float) -> None:
        """Функция, определяющая лучший вариант при сравнении.
        Перегружаем метод, так как при сравнении хотим предупредить,
        что стоит обратить внимание и на энергопотребление"""
        if self._price > price1:
            print("Новый вариант ноутбука дешевле. Однако, стоит обратить внимание на энергопотребление.")
        if self._price <= price1:
            print("Новый вариант ноутбука по цене уступает старому. Однако,"
                  " стоит обратить внимание на энергопотребление.")


if __name__ == "__main__":
    lapstop_1 = Lapstop(85.9, "серый", 512)
    print(lapstop_1)
    print(repr(lapstop_1))
    lapstop_asus1 = Asus(100.7, "черный", 256, 8000)
    lapstop_asus2 = Asus(95.2, "черный", 512, 9600)
    print(lapstop_asus1 == lapstop_asus2)
    lapstop_asus2.comparison(95.2)
    lapstop_asus1.comparison(100.7)
# Перенос строки
