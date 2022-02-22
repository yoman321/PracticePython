#Math: pentagonal numbers
def getPentagonalNumber(n, array):
    num = n * (3*n - 1) / 2
    array.append(num)

array = []
for x in range(1, 101):
    getPentagonalNumber(x, array)

count = 0
for x in array:
    if count % 10 == 0:
        print()
        print(array[count], end = " ")
    else:
        print(array[count], end = " ")
        
    count += 1