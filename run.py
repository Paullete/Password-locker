from json.tool import main
import random
from user import User

def main():
    
 while True:
        print("welcome to password locker!!!")
        print('/n')
        print("Select a short code to navigte through:to create new user use 'nu':To login to your account 'lg' or 'ex' to exit")
        short_code=input().lower()
        print('/n')
        
        if short_code == 'nu':
            print('create username')
            created_user_name = input()
            
            print('create password')
            created_user_password = input()
            
            print('confirm password')
            confirm_password = input()
            
            while confirm_password != created_user_password:
                print('Invalid password! Passwords do not match!')
                print('Enter your password!')
                created_user_password = input()
                print('Confirm your password!')
            