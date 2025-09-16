#Name: Ryan Nielson
#ID: 86219673
#Email: rnielson@unomaha.edu
class ArrayList:
    def __init__(self, c):
        self.array = [0] * c
        self.capa = c
        self.n = 0

    ###########################################################
    # Implement three functions below.
    # You are not allowed to change any function declaration, e.g., name, parameters, and return value.
    ###########################################################
    def insertTail(self, value):
        pass

    def insert(self, idx, value):
        pass

    def get(self, idx):
        pass
    ###########################################################
    # Given implemented code below.
    ###########################################################
    def display(self):
        for i in range(0, self.n):
            print(str(self.array[i]), end=' ')

        print("\n")

    def insertHead(self, value):
        if self.n == self.capa:
            self.doubleArray()

        for i in range(self.n-1, -1, -1):
            self.array[i+1] = self.array[i]

        self.array[0] = value
        self.n = self.n + 1

    def getSize(self):
        return self.n

    def getName(self):
        return "ArrayList"

    def doubleArray(self):
        self.capa = self.capa * 2
        new_array = [0] * self.capa

        for i in range(0, self.n):
            new_array[i] = self.array[i]

        self.array = new_array