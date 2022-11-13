from collections import Counter

numberOfShoes = int(input())
listOfAllShoesSizes = Counter(map(int, input().split()))
numberOfCustomers = int(input())

income = 0

for i in range(numberOfCustomers):
    size, price = map(int, input().split())
    if listOfAllShoesSizes[size]:
        income += price
        listOfAllShoesSizes[size] -= 1

print(income)
