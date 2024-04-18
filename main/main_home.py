import os,time 
from main_login import User
from database import UserDatabase

class systemfunction:
    #Loading
    def loading():
        time.sleep(1)

    #Clean Window
    def clean_window():
        os.system('clear')

#Loading function 
'''def loading():
    systemfunction.clean_window()
    systemfunction.clean_window()'''
#input error 
def Inputerror():
    print("\ninput error")
    systemfunction.loading()
    systemfunction.clean_window()
    mainpage()

def mainpage():
    print("main page test\n\n1.join 2.login 3.exit")
    userinput = input('\ninput = ')

    #join
    if userinput == '1':
        systemfunction.clean_window()
        print("join\n")
        userid = input("ID :")
        userpw = input("Password : ")
        systemfunction.clean_window()
        database = UserDatabase(userid,userpw,userinput)
        database.User_new_account_request()
        print("\n1.home")
        userinput = input('\ninput = ')
        if userinput == '1':
            systemfunction.clean_window()
            mainpage()
        else:
            Inputerror()
    
    #login
    elif userinput == '2':
        systemfunction.clean_window()
        userid = input("ID : ")
        userpw = input("Password : ")
        systemfunction.clean_window()
        search_account = User(userid,userpw,userinput)  
        search_account.account_search()     
        print("\n1.home")
        userinput = input('\ninput = ')
        if userinput == '1':
            systemfunction.clean_window()
            mainpage()
        else:
            Inputerror()
    #exit
    elif userinput == '3':
       exit()

    #admin login 
    elif userinput == 'rootlogin':
        admin = 0
        systemfunction.clean_window()
        print("admin login\n")
        userid = input("ID : ")
        userpw = input("Password : ")
        if userid == 'root':
            if userpw == 'root':
                admin += 1
            else:
                Inputerror()
        else:
            pass
        systemfunction.clean_window()
        info = UserDatabase(userid,userpw,admin)
        info.User_account_info()
        print("\n1.home")
        userinput = input('\ninput = ')
        if userinput == '1':
            systemfunction.clean_window()
            mainpage()
        else:
            Inputerror()
    else:
        Inputerror()

mainpage()
        




