from collections import UserList
import selectors
from typing_extensions import Self


class User:
    '''
    class that generate new instance of user
    '''
    UserList=[]
    
    def_init_(self,user_name,password):
    Self.user_name=user_name
    Self.password=password
        
    def save_user(self):
        '''
        save_user method saves a ne user object to the user list
        '''
           
            
        User.User_List.append(self)
