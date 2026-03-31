def display_balance(balance):
    print(f"\nCurrent Balance: ₹{balance:.2f}")

def deposit(balance):
    amount = float(input("\nEnter amount to deposit:"))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
    else:
        print("Invalid deposit amount!")

    return balance

def withdraw(balance):
    amount = float(input("\nEnter amount to withdraw: ₹"))

    if amount > 0 and amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        print("Invalid withdrawal amount!")

    return balance

def main():
    balance = 1000.0 

    while True:
        print("\n BANK MENU")
        print("1. Display Balance")
        print("2. Deposit Amount") 
        print("3. Withdraw Amount")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_balance(balance)

        elif choice == '2':
            balance = deposit(balance)

        elif choice == '3':
            balance = withdraw(balance)

        elif choice == '4':
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice! Please try again.")

main()
