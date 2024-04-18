from database import *

class User:
    def __init__(self,userid,userpw,userinput):
        self.userid = userid
        self.userpw = userpw
        self.userinput = userinput

    def account_search(self):
        findaccout  = (item for item in account_list if item['userid'] == self.userid and item['userpw'] == self.userpw)
        check = (next(findaccout,False))
        if check == False:
            print("no account!")
        else:
            print(f'login is success! hello "{self.userid}"')


        
        


        



         