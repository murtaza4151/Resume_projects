status = True
balance = 5000

while status:
    print("1 Enter your credited Amout")
    print("2 Enter your Debited Amount")
    print("3 check your Balance")
    choice = int(input("Enter your choice="))
    if choice == 1:
        credit = int(input("Enter your credit amount="))
        balance = balance + credit
        print("credited Amount=",balance)
        ch = input("Enter credit or debit amount yes or no=")
        if ch == "yes" or ch == "y":
            status = True
        else:
            print("============================================")
            status = False
    elif choice == 2:
        debit = int(input("Enter your Debit amount="))
        balance = balance-debit
        print("Debited Amount",balance)
        ch = input("Enter credit or debit amount yes or no=")
        if ch == "yes" or ch == "y":
            status = True
        else:
            print("============================================")
            status = False
    elif choice == 3:
        print("Total Account Balance=",balance)
        ch = input("Enter credit or debit amount yes or no=")
        if ch == "yes" or ch == "y":
            status = True
        else:
            print("============================================")
            status = False
    else:
        print("Invalid choice")

