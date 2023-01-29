BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int!")
        if id_ <= 0:
            raise ValueError("Идентификатор книги не может быть меньше или равен 0!")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должено быть типа str!")
        if name is None:
            raise ValueError("Название книги не может быть пустой строкой!")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должен быть типа int!")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть меньше или равен 0!")
        self.pages = pages


    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
