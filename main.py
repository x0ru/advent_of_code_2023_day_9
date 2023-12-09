import csv
from icecream import ic

arr = []

with open('file.csv') as file:
    file = csv.reader(file)
    for line in file:
        for item in line:
            arr.append(item.split(' '))
    for i in range(len(arr)):
        arr[i] = [int(x) for x in arr[i]]

"""PART 1"""

    # res = 0
    #
    # def division(n):
    #     for i in range(len(arr[n]) - 1):
    #         arr[n][i] = int(arr[n][i + 1]) - int(arr[n][i])
    #     arr[n].pop()
    #     return arr[n][len(arr[n]) - 1]
    #
    #
    # def mingle_the_array(n):
    #     while any(ele for ele in arr[n]):
    #         reconstruction.append(division(n))
    #     return reconstruction
    #
    #
    # for i in range(len(arr)):
    #     reconstruction = []
    #     last_element = arr[i][len(arr[i]) - 1]
    #     mingle_the_array(i)
    #     ic(reconstruction)
    #     a = sum(reconstruction)
    #     ic(a, last_element)
    #     res += a + last_element
    #
    # ic(res)

"""PART 2"""

res = 0
beg = []


def division(n):
    for i in range(len(arr[n]) - 1):
        arr[n][i] = int(arr[n][i + 1]) - int(arr[n][i])
    val.append(arr[n][0])
    arr[n].pop()
    return val


def mingle_the_array(n):
    while any(ele for ele in arr[n]):
        a = division(n)
    reconstruction.append(a)


for i in range(len(arr)):
    beg.append(arr[i][0])
    val = []
    reconstruction = []
    mingle_the_array(i)
    start = reconstruction[0][len(reconstruction[0]) - 2]
    for j in range(len(reconstruction[0]) - 3, -1, -1):
        start = reconstruction[0][j] - start
    res += int(beg[i]) - start
ic('final', res)
