l = [[1, 2], [3, 4], [5, 6, 7]]

def reverseList(main_list):
    left = 0
    right = len(main_list)-1

    while (left < right):
        temp = main_list[left]
        main_list[left] = main_list[right]
        main_list[right] = temp
        left += 1
        right -= 1
    return main_list

for i in range(len(l)):
    (l[i]) = l[i][::-1]

res = reverseList(l)
print(res)
