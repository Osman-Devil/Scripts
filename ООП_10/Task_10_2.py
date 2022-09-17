from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self,coat):
        self.V = coat

    def __str__(self):
        return f"Общий разход ткани на пальто {self.calc_cloth}"

    @property
    def calc_cloth(self):
        return self.V / 6.5 + 0.5


class Costome(Clothes):
    def __init__(self,coat):
        self.H = coat

    def __str__(self):
        return f"Общий разход ткани на костюм {self.calc_cloth}"

    @property
    def calc_cloth(self):
        return 2 * self.H + 0.3


a = Coat(65)
print(a)
v = Costome(175)
print(v)
print("Обищий разход всей ткани " + str(a.calc_cloth + v.calc_cloth))
