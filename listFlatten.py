# list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# fList = [i for element in list for i in element]
# print(l)
# print(fList)

# list = [[1,3,"geeks"], [4,5],[6,"best"]]
# res = [i for row in list for i in row]
# print(res)

# l= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# res = [i for row in list for i in row]
# print(res)

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flattenList(main_list):
    if isinstance(main_list, list):
        temp=[]
        for element in main_list:
            temp.extend(flattenList(element))
        return temp
    else:
        return[main_list]

res = flattenList(l)
print(res)
