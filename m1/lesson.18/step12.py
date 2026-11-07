class UserException(Exception):
    """Базовое исключение для пользовательских ошибок."""
    pass


class UserAgeError(UserException):
    """Исключение для ошибок с возрастом пользователя."""
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"""Ошибка с возрастом пользователя.
        Возраст должен быть больше 0 и числом"""


class UserNameError(UserException):
    """Исключение для ошибок с именем пользователя."""
    def __init__(self, name: str, lower: int, upper: int):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        length = len(self.name)
        if length <= self.lower:
            detail = f"""меньше или равно нижней границе"""
        elif length >= self.lower:
            detail = f"""больше или равно нижней границе"""
        else:
            detail = f"""внутри диапазона"""

        return f"""Ошибка с именем пользователя {self.name}.
            Имя пользователя должно быть от {self.lower} до {self.upper} символов.
            Это {detail}"""



class User:
    MIN_LEN = 3
    MAX_LEN = 30

    def __init__(self, name: str, age: int):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)

        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


user = User("Bob123", "qaz")