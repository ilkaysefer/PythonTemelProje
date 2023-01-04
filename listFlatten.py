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
