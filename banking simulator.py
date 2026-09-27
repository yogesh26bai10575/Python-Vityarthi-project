accounts = {}


def create_account():
  acc_num = input("Enter Account Number: ")

  if acc_num in accounts:
    print("Account already exists!")
    return

  name = input("Enter Account Holder Name: ")
  balance = float(input("Enter Initial Deposit: "))

  accounts[acc_num] = {
      "name": name,
      "balance": balance,
      "history": [f"Account opened with {balance}"],
  }
  print(f"Account created successfully for {name}!")


def deposit_money():
  acc_num = input("Enter Account Number: ")

  if acc_num not in accounts:
    print("Account not found!")
    return

  amount = float(input("Enter amount to deposit: "))
  accounts[acc_num]["balance"] += amount
  accounts[acc_num]["history"].append(f"Deposited {amount}")

  print(f"Deposited {amount}. New Balance: {accounts[acc_num]['balance']}")


def withdraw_money():
  acc_num = input("Enter Account Number: ")

  if acc_num not in accounts:
    print("Account not found!")
    return

  amount = float(input("Enter amount to withdraw: "))

  if amount > accounts[acc_num]["balance"]:
    print("Insufficient balance!")
  else:
    accounts[acc_num]["balance"] -= amount
    accounts[acc_num]["history"].append(f"Withdrew {amount}")
    print(
        f"Withdrew {amount}. Remaining Balance: {accounts[acc_num]['balance']}"
    )


def check_balance():
  acc_num = input("Enter Account Number: ")

  if acc_num not in accounts:
    print("Account not found!")
    return

  print(f"Name: {accounts[acc_num]['name']}")
  print(f"Current Balance: {accounts[acc_num]['balance']}")


def view_history():
  acc_num = input("Enter Account Number: ")

  if acc_num not in accounts:
    print("Account not found!")
    return

  print(f"History for {accounts[acc_num]['name']}:")
  for statement in accounts[acc_num]["history"]:
    print("-", statement)


while True:
  print("\n=== SIMPLE BANK MENU ===")
  print("1. Create Account")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Check Balance")
  print("5. View History")
  print("6. Exit")

  choice = input("Enter choice (1-6): ")

  if choice == "1":
    create_account()
  elif choice == "2":
    deposit_money()
  elif choice == "3":
    withdraw_money()
  elif choice == "4":
    check_balance()
  elif choice == "5":
    view_history()
  elif choice == "6":
    print("Thank you for using the bank app!")
    break
  else:
    print("Invalid choice, try again.")