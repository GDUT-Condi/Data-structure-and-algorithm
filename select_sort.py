#coding=utf-8
#遍历选出最大，放到右边
#选出次大，放到次右边
def Select_Sort(lists):
    max_lists = len(lists)

    for j in range(max_lists):
        temp = 0
        for i in range(1,max_lists-j):
            if lists[i] > lists[temp]:
                temp = i

        lists[temp],lists[max_lists-1-j] =  lists[max_lists-1-j],lists[temp]
    return lists

if __name__ == '__main__':
    lists = [11,1,8,9,9,7,5,2,4]
    print(Select_Sort(lists))


