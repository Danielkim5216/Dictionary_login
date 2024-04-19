#계정 생성
account_list = [
]

file_path = "/Users/taekyungkim/Documents/workspace/Dictionary_login/main/savedata.txt"

#{'userid':'root','userpw':'root'}
class UserDatabase:
    def __init__(self,userid,userpw,admin):
        self.userid = userid
        self.userpw = userpw
        self.admin = admin
    def __del__(self):
        pass

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

    #for admin        
    def User_account_info(admin):
        if  admin == 1:
            print(f"{account_list}\n",end= ' ')
        else:
            print("\nyou are not admin")

    def remove_User_account(remove_userid):
        for i in range(len(account_list)):
            if account_list[i]['userid'] == remove_userid:
                del account_list[i] 
        print(f"{remove_userid} is remove!\n")
        
    def save_data_in_txt():
        with open(file_path,"w") as file:
                '''file.writelines(str(account_list))'''
                for item in account_list:
                    file.writelines(str(item) + "\n")
                print("Save Success! you can shutdown proggram")

    def load_data_in_txt():
        fiop =  open(file_path,"r")
        data = fiop.read().splitlines()
        for userac in data:
            account_list.append(userac)
            print("Load Success!")
            print(f"0: {account_list[0]}")

            