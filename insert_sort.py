#coding = utf-8
#从第二个数开始小于则放至左边

def Insert_Sort(items):
    length = len(items)
    for i in range(1,length):
        for j in range(i,0,-1):
            if items[j] < items[j-1]:
                items[j],items[j-1] = items[j-1],items[j]
    return items

if __name__ == '__main__':
    items = [5,1,7,3,6,11,3,4]
    print(Insert_Sort(items))