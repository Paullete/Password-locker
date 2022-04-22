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
                confirm_password = input()
                
            else:
                print('Congratulations{created_user_name}! Account creation successful!')
                print('/n')
                print('Proceed to log in!')
                print('Username!')
                entered_username = input()
                print("your password")
                entered_password = input()
                
            while entered_username != created_user_name or entered_password != created_user_password: 
                print('Invalid username or password!')
                print('Username!')
                entered_username =input()
                print('Your password!') 
                entered_password =input()
                
            else:
                print(f"welcome:{entered_username} to your account")
                print('/n')      
            
        elif short_code == 'lg':
            print("welcome")
            print("enter user name")
            default_user_name = input()