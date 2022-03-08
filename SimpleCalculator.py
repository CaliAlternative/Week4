class Calculate():
    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x+y
        else:
            raise TypeError("Invalid typetype please enter integers")

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2,5)
    print(result)
    




























