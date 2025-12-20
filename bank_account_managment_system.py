user = {
    "amal": {"pin": "1234", "balance": "6000"},
    "kamal": {"pin": "3456", "balance": "8000"},
    "sadun": {"pin": "8976", "balance": "7000"}}
username = input("Enter your username: ")
if username in user:
    input_pin = input("Enter your pin: ")
    if user[username]["pin"] == input_pin:
        current_balance = int(user[username]["balance"])
        print(f"Current balance is: {current_balance}")
        withdraw = input("Do you want to withdraw? (yes/no): ")
        if withdraw == "yes":
            withdrawal_amount = int(input("Enter your withdrawal amount: "))
            if current_balance >= withdrawal_amount:
                print("Here is your cash!")
                user[username]["balance"] = str(current_balance - withdrawal_amount)
                print(f"New balance: {user[username]['balance']}")
            else:
                print("Transaction Failed: Insufficient balance")
    else:
        print("Incorrect PIN!")
else:
    print("User not found!")
