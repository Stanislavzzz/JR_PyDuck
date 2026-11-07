class UserException(Exception):
    """Базовое исключение для пользовательских ошибок."""
    pass


class UserAgeError(UserException):
    """Исключение для ошибок с возрастом пользователя."""
    pass


class UserNameError(UserException):
    """Исключение для ошибок с именем пользователя."""
    pass


class User:
    MIN_LEN = 3
    MAX_LEN = 30

    def __init__(self, name: str, age: int):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(f"Имя пользователя должно быть от {self.MIN_LEN} до {self.MAX_LEN} символов.")

        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError("Возраст пользователя должен быть положительным числом.")
        else:
            self.age = age


user = User("BobBob", -25)