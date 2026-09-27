CLI Bank Simulator
A lightweight, terminal-based financial application built in Python. It simulates essential banking operations—such as opening accounts, processing deposits and withdrawals, inspecting real-time balances, and viewing transaction logs—using standard Python data structures.
Features
Account Creation: Registers new bank accounts with unique account numbers, holder names, and initial deposits. Prevents duplicate account creation.
Deposit Funds: Credits funds to existing accounts and updates the transaction log.
Withdraw Funds: Debits funds with overdraft protection, preventing withdrawals exceeding available balances.
Balance Inquiry: Displays holder details and current balance.
Transaction History: Displays a complete, chronological audit log of all account activities.
Project Structure
Plaintext
.
├── banking_simulator.py  # Main Python program file
└── README.md             # Project documentation
System Requirements
Python: Version 3.6 or higher.
Dependencies: None (built entirely using Python Standard Library modules).
Operating System: Windows, macOS, or Linux.
Setup & Installation
Step 1: Clone or Download the Repository
Download the source file directly or clone the repository using Git:
git clone https://github.com/your-username/cli-bank-simulator.git
cd cli-bank-simulator
Step 2: Verify Python Installation
Ensure Python is installed on your system by running:

Bash
python --version
How to RunExecute the script directly from your terminal or command prompt:   
python banking_simulator.py
Usage Guide
When you launch the application, an interactive menu will appear:
=== SIMPLE BANK MENU ===
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. View History
6. Exit
Example Workflow
Create an Account: Select option 1, enter an account number (e.g., 12345), enter the holder's name (e.g., Yogesh), and enter an initial deposit amount (e.g., 1000).
Deposit Funds: Select option 2, enter account number 12345, and enter deposit amount 500.   
Withdraw Funds: Select option 3, enter account number 12345, and enter withdrawal amount 200.
Check Balance: Select option 4 to view the updated total balance (1300).
View History: Select option 5 to view all chronological logs associated with account 12345.
Exit: Select option 6 to quit the application.
