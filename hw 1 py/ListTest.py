#Name: Ryan Nielson
#ID: 86219673
#Email: rnielson@unomaha.edu

########################################################
#You are not allowed to change this code except removing comments for printing lists.
#In addition, you are not allowed to import additional library files (jars).
#Please let the instructor knows if there is any bug.
from LinkedList import LinkedList
from ArrayList import ArrayList
import time
import sys

def insertHeadTest (list, cnt):
    startTime = time.perf_counter()
    for i in range(0, cnt):
        list.insertHead(i)

    elapsedTime = (time.perf_counter() - startTime)
    print(list.getName() + ": insertHeadTest() elapsed time: " + str(elapsedTime * 1e3) + " ms")

def insertTailTest (list, cnt):
    startTime = time.perf_counter()
    for i in range(0, cnt):
        list.insertTail(i)

    elapsedTime = (time.perf_counter() - startTime)
    print(list.getName() + ": insertTailTest() elapsed time: " + str(elapsedTime * 1e3) + " ms")

#Internally add to tail
def fillList(list, cnt):
    for i in range(0, cnt):
        list.insertTail(i)

def insertTest(list, cnt):
    startTime = time.perf_counter()

    #insert middle
    for i in range(0, cnt):
        list.insert(int(cnt/2), i)

    elapsedTime = (time.perf_counter() - startTime)
    print(list.getName() + ": insertTest() elapsed time: " + str(elapsedTime * 1e3) + " ms")

def getTest(list, cnt):
    startTime = time.perf_counter()

    #insert middle
    for i in range(0, cnt):
        list.get(int(cnt/2))

    elapsedTime = (time.perf_counter() - startTime)
    print(list.getName() + ": get() elapsed time: " + str(elapsedTime * 1e3) + " ms")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("You must pass two command line parameters.")
        sys.exit()

    cnt = int(sys.argv[1])
    testcase = int(sys.argv[2])

    arrayList = ArrayList(cnt)
    linkedList = LinkedList()

    if testcase == 0:
        insertHeadTest(arrayList, cnt)
        #arrayList.display()  # for testing, you can call the display function by uncommenting
        insertHeadTest(linkedList, cnt)
        #linkedList.display() # for testing, you can call the display function by uncommenting
    elif testcase == 1:
        insertTailTest(arrayList, cnt)
        #arrayList.display()  # for testing, you can call the display function by uncommenting
        insertTailTest(linkedList, cnt)
        #linkedList.display()  # for testing, you can call the display function by uncommenting
    elif testcase == 2:
        # Fill the half of the list first
        # Executiontime is not considered
        fillList(arrayList, int(cnt/2))
        fillList(linkedList, int(cnt/2))

        insertTest(arrayList, int(cnt/2))
        #arrayList.display(); # for testing, you can call the display function by uncommenting
        insertTest(linkedList, int(cnt/2))
        #linkedList.display(); # for testing, you can call the display function by uncommenting
    elif testcase == 3:
        fillList(arrayList, cnt)
        fillList(linkedList, cnt)

        getTest(arrayList, cnt)
        getTest(linkedList, cnt)
    elif testcase == 4:
        for i in range(0, 10):
            arrayList.insert(i, i);
            #arrayList.display() # for testing, you can call the display function by uncommenting
            linkedList.insert(i, i);
            #linkedList.display() # for testing, you can call the display function by uncommenting
    else:
        print("Unknown testcase")