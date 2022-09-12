
total = 50
owed = -50
denominations = [5, 10, 25]

while(total > 0):
    print(f"Amount Due: {total}")
    coin = int(input("Insert Coin: "))
    if coin not in denominations:
        continue
    else:
        owed += coin
        total = total - coin
print(f"Change Owed: {owed}")
