# time1 + time2


class Time:
    def __init__(self, minute, second):
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if not isinstance(other, Time):
            print("Нельзя складывать")
            return None

        m = self.minute + other.minute
        s = self.second + other.second

        m += s // 60
        s = s % 60

        return Time(m,s)

    def __iadd__(self, other):
        if not isinstance(other, Time):
            print("Нельзя складывать")
            return None

        m = self.minute + other.minute
        s = self.second + other.second

        m += s // 60 + 100
        s = s % 60

        self.minute = m
        self.second = s

        return self

    def __sub__(self, other):
        if not isinstance(other, Time):
            print("Нельзя вычитать")
            return None

        m = self.minute - other.minute
        s = self.second - other.second

        return Time(m, s)

    # def __mul__(self, other):  x * y
    # def __truediv__(self, other):(self, other): x / y
    # def __floor__(self, other):(self, other): x // y
    # def __mod__(self, other):(self, other): x % y
    # def __pow__(self, other): x ** y

    def __str__(self):
        return f'{self.minute} мин : {self.second} сек'


time1 = Time(minute=5, second=30)
time2 = Time(minute=3, second=37)
print(time1)
print(time2)

# time3 = time1 + time2
# print(time3)

print(id(time1))
time1 += time2
print(id(time1))
print(time1)

time3 = time1 - time2
print(time3)