class Car:
    speed = 70
    color = "black"
    name = "BMW X6"
    is_police = True

    def show_speed(self):
        return self.speed

    def go(self, input_go):
        return input_go

    def stop(self, input_stop):
        return "Stop " + input_stop

    def turn(self, input_turn):
        if input_turn == "left":
            return "You turn left"
        elif input_turn == "right":
            return "You turn right"
        else:
            return "You drive straight"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость")
        return self.speed


class SportCar(Car):
    def sportcar(self, model):
        return model


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Вы превысили скорость")
        return self.speed


class PoliceCar(Car):
    def policecar(self, model):
        return model


a = Car()
print(a.show_speed())
print(a.turn('left'))
print(a.stop('now'))

b = TownCar()
print(b.show_speed())

