class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Название книги должено быть типа str!")
        if name is None:
            raise ValueError("Название книги не может быть пустой строкой!")
        self._name = name

        if not isinstance(author, str):
            raise TypeError("Данные об авторе (ФИО) должено быть типа str!")
        if author is None:
            raise ValueError("Данные об авторе (ФИО) не могут быть пустой строкой!")
        self._author = author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property   # Добавляем свойство, чтобы была возможность ТОЛЬКО ВЫВОДА значений защищенных атрибутов _name и _author
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._name


class PaperBook (Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter  # Свойство с проверками при присвоении значения
    def pages(self, pages: int):
        if isinstance(pages, int) and pages > 0:
            self._pages = pages
        else:
            raise ValueError("Количество страниц должны быть больше 0 и принадлежать типу int!")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook (Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter  # Свойство с проверками при присвоении значения
    def duration(self, duration: float):
        if isinstance(duration, float) and duration > 0:
            self._duration = duration
        else:
            raise ValueError("Продолжительность аудиокниги долна быть больше 0 и принадлежать типу float!")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"
