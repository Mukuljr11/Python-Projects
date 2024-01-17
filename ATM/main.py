while True:
    balance=10000
    Withdraw=0
    Deposit=0
    print("    ATM     ")
    print("""
    1).    BALANCE
    2).    WITHDRAW
    3).    DEPOSIT
    4).    QUIT
    """)
    try:
        Option=int(input("Enter Option : "))
    except Exception as e:
        print("ERROR",e)
        print("Enter 1,2,3 or 4 only")
        continue
    if Option==1:
        print("BALANCE == ",balance)
    if Option==2:
        print("BALANCE == ",balance)
        Withdraw=float(input("Enter WITHDRAW amount : "))
        if Withdraw<balance:
                forewardbalance=(balance-Withdraw)
                print("FOREWARD BALANCE :",forewardbalance)
        else:
                print("AGEE CHAL BHIKARI")
    if Option==3:
        print("BALANCE =",balance)
        Deposit=float(input("Enter deposit amount : "))
        if Deposit>0:
            forewardbalance=(balance+Deposit)
            print("Forewardbalance : ",forewardbalance)
        else:
            print("NO TRASACTIONS MADE : ")
    if Option==4:
        exit()
