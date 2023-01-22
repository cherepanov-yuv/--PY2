import doctest


class Diver:
    def __init__(self, percent_oxygen: float, percent_voids: float):
        """
        Создание и подготовка к работе объекта "Баллон дайвера"
        :param percent_oxygen: Процентное содержание кислорода в баллоне дайвера
        :param percent_voids: Процентное содержание остатка в баллоне дайвера
        Примеры:
        >>> balloon = Diver(100, 0) # инициализация экземпляра класса
        """
        if not isinstance(percent_oxygen, (int, float)):
            raise TypeError("Процентное содержание кислорода в баллоне должно быть типа int или float")
        if percent_oxygen > 100:
            raise ValueError("Процентное содержание кислорода в баллоне не может быть больше 100!")
        if percent_oxygen < 0:
            raise ValueError("Процентное содержание кислорода в баллоне не может быть меньше 0!")
        self.percent_oxygen = percent_oxygen

        if not isinstance(percent_voids, (int, float)):
            raise TypeError("Процентное содержание остатка в баллоне должно быть типа int или float")
        if percent_voids > (100-percent_oxygen):
            raise ValueError("Процентное содержание кислорода и остатка в сумме не может превышать 100!")
        if percent_voids < 0:
            raise ValueError("Процентное содержание остатка в баллоне не может быть меньше 0!")
        self.percent_voids = percent_voids

    def use_diver(self) -> bool:
        """
        Функция которая проверяет достаточно ли дайверу кислорода в баллоне
        :return: Достаточно ли кислорода в баллоне
        Примеры:
        >>> balloon = Diver(75, 25)
        >>> balloon.use_diver()
        """
        ...

    def add_oxygen_to_balloon(self, oxygen_1: float) -> None:
        """
        Добавление процентного соотношения кислорода в баллон.
        :param oxygen_1: на сколько процентов увеличим кислород в баллоне
        :raise ValueError: Если процентное соотношение кислорода превышает 100 то вызываем ошибку
        Примеры:
        >>> balloon = Diver(15, 85)
        >>> balloon.add_oxygen_to_balloon(70)
        """
        if not isinstance(oxygen_1, (int, float)):
            raise TypeError("Добавляемые проценты кислорода должен быть типа int или float")
        if oxygen_1 < 0:
            raise ValueError("Добавляемые проценты кислорода должны быть положительными")
        ...

    def drop_oxygen_from_balloon(self, oxygen_2: float) -> None:
        """
        Уменьшение процентного соотношения кислорода.

        :param oxygen_2: на сколько процентов уменьшим кислород, но увеличим остаток
        :raise ValueError: Если уменьшаем на больший процент кислорода, чем имеется,
        то возвращается ошибка.
        :return: Получившееся процентное соотношение после уменьшения кислорода в баллоне.

        Пример:
        >>> balloon = Diver(90, 10)
        >>> balloon.drop_oxygen_from_balloon(90)
        """
        ...


class Concrete:
    def __init__(self, percent_water: float, percent_concrete: float):
        """
        Создание и подготовка к работе объекта "Бетонная смесь"
        :param percent_water: Процентное содержание воды
        :param percent_concrete: Процентное содержание бетона
        Примеры:
        >>> mixer = Concrete(40, 60) # инициализация экземпляра класса
        """
        if not isinstance(percent_water, (int, float)):
            raise TypeError("Процентное содержание воды должно быть типа int или float")
        if percent_water > 100:
            raise ValueError("Процентное содержание воды не может быть больше 100!")
        if percent_water < 0:
            raise ValueError("Процентное содержание воды не может быть меньше 0!")
        self.percent_water = percent_water

        if not isinstance(percent_concrete, (int, float)):
            raise TypeError("Процентное содержание бетона должно быть типа int или float")
        if percent_concrete > (100-percent_water):
            raise ValueError("Процентное содержание бетона в сумме не может превышать 100!")
        if percent_concrete < 0:
            raise ValueError("Процентное содержание бетона не может быть меньше 0!")
        self.percent_concrete = percent_concrete

    def use_mixer_concrete(self) -> bool:
        """
        Функция которая проверяет достаточно ли бетона для качественной бетонной смеси
        :return: Достаточно ли бетона
        Примеры:
        >>> mixer = Concrete(35, 65)
        >>> mixer.use_mixer_concrete()
        """
        ...

    def add_concrete_to_mixer(self, concrete1: float) -> None:
        """
        Добавление процентного соотношения бетона в смесь.
        :param concrete1: на сколько процентов увеличим количество бетона
        :raise ValueError: Если процентное соотношение бетона превышает 100 то вызываем ошибку
        Примеры:
        >>>mixer = Concrete(35, 65)
        >>> mixer.add_concrete_to_mixer(20)
        """
        if not isinstance(concrete1, (int, float)):
            raise TypeError("Добавляемые проценты бетона должен быть типа int или float")
        if concrete1 < 0:
            raise ValueError("Добавляемые проценты бетона должны быть положительными")
        ...

    def drop_concrete_to_mixer(self, concrete2: float) -> None:
        """
        Уменьшение процентного соотношения бетона.

        :param concrete2: на сколько процентов уменьшим бетон
        :raise ValueError: Если уменьшаем на больший процент бетон, чем имеется,
        то возвращается ошибка.
        :return: Получившееся процентное соотношение после уменьшения бетона.

        Пример:
        >>>mixer = Concrete(35, 65)
        >>> mixer.drop_concrete_to_mixer(30)
        """
        ...


class Unique:
    def __int__(self, height: float, span: float, console: float):
        """
        Создание и подготовка объекта "Уникальное здание"

        :param height: Высота здания
        :param span: Пролет здания
        :param console: Консоль здания

        Пример:
        >>> characteristics = Unique(102, 3, 9) # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Данная переменная должна быть типом int или float")
        if height < 0:
            raise ValueError("Высота здания должна быть больше 0")
        self.height = height

        if not isinstance(span, (int, float)):
            raise TypeError("Данная переменная должна быть типом int или float")
        if span <= 0:
            raise ValueError("Пролет здания должен быть положительным числом")
        self.span = span

        if not isinstance(console, (int, float)):
            raise TypeError("Данная переменная должна быть типом int или float")
        if console <= 0:
            raise ValueError("Консоль здания должна быть положительным числом")
        self.console = console

    def check_(self) -> bool:
        """
        Функция которая проверяет является ли здание уникальным
        :return: Является ли здание уникальным
        Пример:
        >>> characteristics = Unique(102, 4, 12)
        >>> characteristics.check_()
        """
        ...

    def add_characteristics_height(self, height_1: float) -> None:
        """
        Увеличение характеристик до уникальности здания по высоте.
        :param height_1: добавляемая высота

        Пример:
        >>> characteristics = Unique(80, 21, 7)
        >>> characteristics.add_characteristics_height(25)
        """
        if not isinstance(height_1, (int, float)):
            raise TypeError("Добавляемая высота должна быть типа int или float")
        if height_1 < 0:
            raise ValueError("Добавляемая высота должна положительным числом")
        ...

    def add_characteristics_span(self, span_1: float) -> None:
        """
        Увеличение характеристик до уникальности здания по пролету.
        :param span_1: добавляемая длина пролета

        Пример:
        >>> characteristics = Unique(80, 80, 9)
        >>> characteristics.add_characteristics_span(25)
        """
        ...

    def add_characteristics_console(self, console_1: float) -> None:
        """
        Увеличение характеристик до уникальности здания по консоле.
        :param console_1: добавляемая длина пролета

        Пример:
        >>> characteristics = Unique(80, 80, 10)
        >>> characteristics.add_characteristics_console(15)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    # тестирование примеров, которые находятся в документации
