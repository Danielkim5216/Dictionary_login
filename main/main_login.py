from database import *

class User:
    def __init__(self,userid,userpw):
        self.userid = userid
        self.userpw = userpw
        
    def __del__(self):
        pass

    def account_search(self):
        findaccout  = (item for item in account_list if item['userid'] == self.userid and item['userpw'] == self.userpw)
        check = (next(findaccout,False))
        if check == False:
            print("no account!")
        else:
            print(f'login is success! hello "{self.userid}"')

    def root_login(self):
        '''checkroot = (item for item in account_list if item['userid'] == userid == 'root' and item['userpw'] == userpw == 'root')
        check = (next(checkroot,False))
        if check == False:
            print("error!")
        else:
            admin += 1'''
        if self.userid == "root" and self.userpw == "root":
            print("root login success!")
        else:
            print("login Fail")




        



         
