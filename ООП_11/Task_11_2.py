class ExceptionError:
    def __int__(self, division):
        self.division = division

    @staticmethod
    def div_by_zero(num_1, num_2):
        if num_2 == 0:
            print("На ноль делить нельзя")
        else:
            print(num_1/num_2)


ExceptionError.div_by_zero(20,0)
ExceptionError.div_by_zero(20,10)
