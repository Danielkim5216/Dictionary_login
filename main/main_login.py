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

    def root_login(userid,userpw):
        if userid == "root" and userpw == "root":
            print("root login success!")
        else:
            print("login Fail")
            '''checkroot = (item for item in account_list if item['userid'] == userid == 'root' and item['userpw'] == userpw == 'root')
        check = (next(checkroot,False))
        if check == False:
            print("login Fail")
        else:
            print("root login success!")
'''



        



         
