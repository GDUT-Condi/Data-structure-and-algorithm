from timeit import Timer
def text1():
    l=[]
    for i in range(1000):
        l = l + [i]

def text2():
    l=[]
    for i in range(1000):
        l.append(i)

def text3():
    l = [i for i in range(1000)]

def text4():
    l = list(range(1000))

t1 = Timer('text1()','from __main__ import text1')
print('concat',t1.timeit(number=1000),'seconds')
t2 = Timer('text2()','from __main__ import text2')
print('append',t2.timeit(number=1000),'seconds')
t3 = Timer('text3()','from __main__ import text3')
print('for',t3.timeit(number=1000),'seconds')
t4 = Timer('text4()','from __main__ import text4')
print('list',t4.timeit(number=1000),'seconds')