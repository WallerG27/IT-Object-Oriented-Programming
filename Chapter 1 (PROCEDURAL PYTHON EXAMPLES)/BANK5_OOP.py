from Account import *

accountsList = []

# Creates two sample accounts
print("Joe's account is account number:", len(accountsList))
oAccJoe = Account("Joe", 100, 'soup') # 'o' in oAccJoe is just for object it looks stupid, but it's fitting for me
accountsList.append(oAccJoe)
      
print("Mary's account is account number:", len(accountsList))
accountsList.append(Account("Mary", 12345, 'nuts')) #Does it in one line

while True: # whileLoop from Bank5_Dictionary
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    try:   #// I added the 'try' and 'except' to solve the 'just pressing enter breaks it'
        action = action[0] # just use first letter
        action = action.lower() # force lowercase
    except:
        print()
    
    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = accountsList[userAccountNumber].getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber= input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = accountsList[userAccountNumber].deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
        
    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('What is the amount of your initial deposit? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = len(accountsList)
        accountsList.append(Account(userName, userStartingAmount, userPassword))
        print('Your new account number is:', userAccountNumber)

    elif action == 's':   #show all
        print('Show:')
        for a in accountsList:
            a.show()



    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
 
        newBalance = accountsList[userAccountNumber].withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)       





print('done')