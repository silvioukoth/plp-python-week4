# ATM Menu
# This program checks a PIN and processes a withdrawal.

balance = 1000
correct_pin = "1234"

try:
    pin = input("Enter your 4-digit PIN: ")

    # Check whether the PIN entered by the user is correct.
    if pin == correct_pin:
        try:
            amount = int(input("Enter amount to withdraw: "))

            # Check whether the withdrawal amount is within the available balance.
            if amount <= balance:
                balance = balance - amount
                print(f"Withdrawal successful. New balance: {balance}")
            else:
                print("Insufficient funds")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    else:
        print("Incorrect PIN")

except ValueError:
    print("Invalid input. Please enter a number.")