class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{self.position} {self._income}"


a = Position("Павел", "Сурин", "Директор", {"wage": 120, "bonus": 130})
print(a.get_full_name())
print(a.get_total_income())
