class CustomStr():
    def __init__(self, value):
        if value.isnumeric:
            self.value = str(value)
        else:
            return "Please supply a numeric value as a string type"

    def __add__(self, b):
        return str(int(self.value) + int(b))

    def __repr__(self):
        return self.value

    def __int__(self):
        return int(self.value)


cstring = CustomStr("4")
cstring2 = CustomStr("1")

print(cstring)
print(cstring + cstring2)

