#""
# USER AUTHENTICATION
# initial setup
balance = 10000
password = 1001
attempts = 0

while attempts < 3:

    passcode = int(input("Enter your 4 digit PIN: "))
    if passcode == password:
        print("\n ---✅ Login Successful---")
        break
    else:
        attempts += 1
        print(f"❌ Incorrect Passcode Try again ",3 - attempts,"left")

        if attempts ==3:
              print("⚠️ Too many attempts Try again after 3 Hours")
              exit()

# ---ATM Menu Display---
if attempts < 3:
    while True:
            print("1. Check Balance")
            print("2. Withdrawal")
            print("3. Deposit")
            print("4. Exit")

            choice = input("\n---Select an option---\n")

            if choice == "1":
                print(f"----\nYour current Balance is {balance}\n----")


            elif choice == "2":
                amount = int(input("Enter the amount to withdraw : "))
                if amount <=0:
                    print("Please Enter a valid amount!")
                    continue
                elif amount > balance:
                    print("Insufficient Balance")
                    continue
                else:
                    balance -= amount
                    print(f"Amount of {amount} is Withdrawn Successfully")
                    question = input("Would you like to see your current balance? (yes/no)").strip().lower()
                    if question == "yes":
                        print(f"Your current balance is {balance}")
                    elif question == "No":
                        print(f"Thank you for banking with Us!")

            elif choice == "3":
                amount = int(input("Enter the Deposit amount: "))
                if amount <=0:
                    print("Amount must not be 0")
                    continue
                else:
                    balance += amount
                    print(f"Amount of {amount} deposited successfully!!!")
                    question = input("Would you like to see your current balance? (yes/no)").strip().lower()
                    if question == "yes":
                        print(f"Your current balance is {balance}")
                    elif question == "No":
                        print(f"Thank you for banking with Us!")


            elif choice == "4":
                print("Exited successfully")
                print("\n---Thank you for Banking with Us!---\n")
                break
            else:
                print("---Please select a valid option---")






