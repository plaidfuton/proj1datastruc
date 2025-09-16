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
        if self.n == self.capa:
            self.doubleArray()                  #if the capacity of the array is full, double the capacity

        self.array[self.n] = value            #put the value at the tail of the array

        self.n += 1                             #increment the value which we use to check if the capacity is met

    def insert(self, idx, value):
        if self.n == self.capa:
            self.doubleArray()                  #if the capacity of the array is full, double the capacity

        for i in range(self.n-1, idx, -1):      #move each value of the array, starting at the last index in the array, one index to the right
            self.array[i+1] = self.array[i]     #until we reach the index which we wish to insert a value

        self.array[idx] = value                 #put the value in the array at the index we wish to insert it
        self.n += 1                       #increment the value which we use to check if the capacity is met

    def get(self, idx):
        return self.array[idx]                  #return the value at the index provided
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