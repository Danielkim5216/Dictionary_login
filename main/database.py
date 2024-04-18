#계정 생성
account_list = [

]

class UserDatabase:
    def __init__(self,userid,userpw,admin):
        self.userid = userid
        self.userpw = userpw
        self.admin = admin
    def User_new_account_request(self):
        #check id 
        checkid = (item for item in account_list if item['userid'] == self.userid == self.userid)
        check = (next(checkid,False))
        if check == False:
            new_account = {}
            new_account['userid'] = self.userid
            new_account['userpw'] = self.userpw
            account_list.append(new_account)
            #success message
            print("Join success!")
        else:
            print("this id is already join!")
    def User_account_info(self):
        if  self.admin == 1:
            print(f"{account_list}\n",end= ' ')
        else:
            print("\nyou are not admin")

 
