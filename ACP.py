class IOString:
    def __init__(self):
        self.str1=""

    def getString(self):
        self.str1=input("Enter a string: ")

    def printString(self):
        print("Result is :",self.str1.upper())

S=IOString()
S.getString()
S.printString()                