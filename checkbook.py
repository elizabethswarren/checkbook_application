import os

def isfloat(num):
    try:
        float(num) 
        return True
    except ValueError:
        return False    

def view_balance():
    if os.path.exists('banking_info.txt'):
        with open('banking_info.txt', 'r') as f:
            lines = f.readlines()
            print(f'Your balance is {round(float(lines[0]), 2)}')
    else:
        with open('banking_info.txt', 'w') as f:
            f.write('5000.00')

        with open('banking_info.txt', 'r') as f:
            lines = f.readlines()
            print(f'Your balance is {round(float(lines[0]), 2)}')

def debit():
    debit_input = ''

    while isfloat(debit_input) is False:
        debit_input = input('Amount to withdraw: ')
        if isfloat(debit_input) is True:
            continue
        else:
            print('\nInvalid selection. Please input the amount you wish to withdraw.')
        

    if os.path.exists('banking_info.txt'):
        with open('banking_info.txt', 'r' ) as f:
            lines = f.readlines()
            new_balance = float(lines[0]) - float(debit_input)
        
        with open('banking_info.txt', 'w') as f:
            f.write(str(new_balance))

        with open('banking_info.txt', 'r') as f:
            lines = f.readlines()
            print(f'Your balance is {round(float(lines[0]), 2)}\n')

    else:
        with open('banking_info.txt', 'w') as f:
            lines = f.write('5000.00')

        with open('banking_info.txt', 'r' ) as f:
            lines = f.readlines()
            new_balance = float(lines[0]) - float(debit_input)
        
        with open('banking_info.txt', 'w') as f:
            f.write(str(new_balance))

        with open('banking_info.txt', 'r') as f:
            lines = f.readlines()
            print(f'Your balance is {round(float(lines[0]), 2)}\n')
    


    

def credit():
    
    credit_input = ''

    while isfloat(credit_input) is False:
        credit_input = input('Amount to deposit: ')
        if isfloat(credit_input) is True:
            continue
        else:
            print('\nInvalid selection. Please input the amount you wish to deposit.')
    
    if os.path.exists('banking_info.txt'):
        with open('banking_info.txt', 'r' ) as f:
            lines = f.readlines()
            new_balance = float(lines[0]) + float(credit_input)
        
        with open('banking_info.txt', 'w') as f:
            f.write(str(new_balance))

        with open('banking_info.txt', 'r') as f:
            lines = f.readlines()
            print(f'Your balance is {round(float(lines[0]), 2)}')

    else:
        with open('banking_info.txt', 'w') as f:
            lines = f.write('5000.00')

        with open('banking_info.txt', 'r' ) as f:
            lines = f.readlines()
            new_balance = float(lines[0]) + float(credit_input)
        
        with open('banking_info.txt', 'w') as f:
            f.write(str(new_balance))

        with open('banking_info.txt', 'r') as f:
            lines = f.readlines()
            print(f'Your balance is {round(float(lines[0]), 2)}')

def exit():
    print('\nThank you for choosing Gringotts Bank. \nHave a nice day.\n')



print('\nWelcome to Gringotts Online Checkbook.\nProudly serving (coding) Wizards since 1474.\n')
print('How can we help you today?')
          

user_prompt = ''

while user_prompt != '4':
    user_prompt = input('\nMenu Options:\n1 View Current Balance\n2 Make a withdrawal\n3 Make a deposit\n4 Exit\n\nEnter your selection here: ')
    if user_prompt == '1':
        view_balance()
    elif user_prompt == '2':
        debit()
    elif user_prompt == '3':
        credit()
    elif user_prompt == '4':
        exit()
        break
    else:
        print('\nInvalid selection. Please choose an option from the menu.')