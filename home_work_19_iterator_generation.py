#Task1
def enumerate(itereble, start=0):
    n = start
    for i in itereble:
        yield n, i
        n += 1
print(list(enumerate([1,2,3,4,5])))

#Task2
def range(start:int, stop:int, step=1):
        list1=[]
        while start <=stop:
            yield start
            start += step
            list1.append(start)

print(list(range(1,7,)))
#Task3 взагалі не зрозумів завдання







