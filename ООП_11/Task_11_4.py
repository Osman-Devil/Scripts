class OfficeEquipment():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def general_id(id_storage, printer, xerox, scanner):
        return f"Id storage: {id_storage}, id printer: {printer}, " \
               f"id xerox: {xerox}, id scanner: {scanner}"

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


class Printer(OfficeEquipment):
    @staticmethod
    def get_printer(printer):
        return f"Id printer: {printer}"


class Xerox(OfficeEquipment):
    @staticmethod
    def get_xerox(xerox):
        return f"Id xerox: {xerox}"


class Scanner(OfficeEquipment):
    @staticmethod
    def get_scanner(scanner):
        return f"Id scanner: {scanner}"


print(OfficeEquipment.general_id(12, 13, 14, 15))
print(OfficeEquipment("Xerox", 134, 12))
