class Stationery:
    title = "Newton"

    def draw(self, some_text):
        return "Запуск отрисовки"


class Pen(Stationery):
    def draw(self, some_text):
        return some_text + "Pen's unique message"


class Pencil(Stationery):
    def draw(self, some_text):
        return some_text + "Pencil's unique message"


class Handle(Stationery):
    def draw(self, some_text):
        return some_text + "Handle's unique message"


a = Pen()
print(a.draw('Wow, '))

b = Pencil()
print(b.draw("Hello, "))

c = Handle()
print(b.draw("Hi, "))
