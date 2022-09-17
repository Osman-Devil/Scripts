import re


def email_parse(email_address):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(email_address)
    try:
        return result.groupdict()
    except AttributeError:
        print(f"ValueError: wrong email:{email_address}")


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
