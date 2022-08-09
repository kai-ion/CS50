def main() :
    x = 50

    while x > 0 :
        print("Amount Due:", x)
        coin = int(input("Insert Coin: "))

        if coin in [5, 10, 25] :
            x -= coin


    print("Changed Owed:", abs(x))

main()