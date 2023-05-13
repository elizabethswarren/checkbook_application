
import os
import time
import csv

def view_balance():
    #checking if file exists
    if os.path.exists('banking_info.csv'):
        with open('banking_info.csv', 'r') as f:
            banking_info = f.readlines()
    #if not, making file        
    else:
        cols = ['transaction_type', 'value', 'time_stamp']
        transaction = {
            'transaction_type':  'balance',
            'value': '5000.00',
            'time_stamp': time.time(),
        }
        with open('banking_info.csv', 'w') as f:
           writer = csv.DictWriter(f, fieldnames=cols),
           writer.writeheader(),
           writer.writerow(transaction)
    

 
print('Welcome to Gringotts Banking Online.\nProudly serving (coding) Wizards since 1474.\n')
print('How can we help you today?\n')
print('Menu Options:\n1 View Current Balance\n2 Make a withdrawal\n3 Make a deposit\n4 Exit') 
          

user_prompt = ''

while user_prompt != '4':
    user_prompt = input('Enter your selection here: ')
    if user_prompt == '1':
        view_balance()
        break
    elif user_prompt == '2':
        print("Making a withdrawal.")
        break
    elif user_prompt == '3':
        print('Making a deposit.')
        break
    elif user_prompt == '4':
        print('\nThank you for choosing Gringotts Bank.\nHave a nice day.')
        break
    else:
        print('\nInvalid selection. Please choose an option from the menu.')
