import doctest
from abc import ABC, abstractmethod

class Furniture(ABC):
    def __init__(self, material: str, weight: float):
        """
        Создание и подготовка к работе объекта "Мебель".
        :param material: Материал мебели (например, дерево, металл)
        :param weight: Вес мебели в килограммах
        Примеры:
        >>> table = Table("wood", 36.0)
        >>> table.material
        'wood'
        >>> table.weight
        36.0
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой.")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        self.material = material
        self.weight = weight
        
    @abstractmethod
    def clean(self) -> str:
        """
        Метод очистки мебели.
        """
        pass


class Table(Furniture):
    """
    Класс, представляющий стол.
    """

    def clean(self) -> str:
        """
        Метод очистки стола.
        :return: Инструкция по чистке.
        Примеры:
        >>> table = Table("wood", 36.0)
        >>> table.clean()
        'Протереть влажной тряпкой.'
        """
        return "Протереть влажной тряпкой."

class Tree:
    """
    Класс, представляющий дерево.
    """

    def __init__(self, species: str, age: int):
        """
        Создание и подготовка к работе объекта "Дерево".
        :param species: Вид дерева
        :param age: Возраст дерева в годах
        Примеры:
        >>> oak = Tree("oak", 50)
        >>> oak.species
        'oak'
        >>> oak.age
        50
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным целым числом.")
        self.species = species
        self.age = age

    def photosynthesize(self) -> str:
        """
        Процесс фотосинтеза.
        :return: Описание процесса фотосинтеза.
        Примеры:
        >>> oak = Tree("oak", 50)
        >>> oak.photosynthesize()
        'Поглощение углекислого газа и выделение кислорода.'
        """
        return "Поглощение углекислого газа и выделение кислорода."


class FacebookAccount:
    """
    Класс, представляющий аккаунт Facebook.
    """

    def __init__(self, username: str, friends_count: int):
        """
        Создание и подготовка к работе объекта "Facebook аккаунт".
        :param username: Имя пользователя
        :param friends_count: Количество друзей
        Примеры:
        >>> account = FacebookAccount("user2525", 100)
        >>> account.username
        'user2525'
        >>> account.friends_count
        100
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if not isinstance(friends_count, int) or friends_count < 0:
            raise ValueError("Количество друзей должно быть положительным целым числом.")
        self.username = username
        self.friends_count = friends_count

    def post_status(self, status: str) -> str:
        """
        Публикация статуса.
        :param status: Содержимое статуса
        :return: Подтверждение публикации
        Примеры:
        >>> account = FacebookAccount("user2525", 100)
        >>> account.post_status("Hello, world!")
        'Статус опубликован: Hello, world!'
        """
        if not isinstance(status, str):
            raise TypeError("Статус должен быть строкой.")
        return f"Статус опубликован: {status}"

if __name__ == "__main__":
    doctest.testmod()
