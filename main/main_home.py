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

#login message 
login_message = 0
user= 0
admin = 0

#input error 
def Inputerror():
    global login_message
    print("\ninput error")
    systemfunction.loading()
    systemfunction.clean_window()
    mainpage(login_message)
    
#main page 
def mainpage(login_message):
    if login_message == 0:
        message = 'not login account'
    elif login_message == 1:
        message = 'user'
    elif login_message == 2:
        message = 'admin'
    else:
        message = 'login_message error'
    print("main page test\n\n1.join 2.login 3.exit")
    '''print(admin,user)'''
    print(f"\nyou are {message}")
    userinput = input('\ninput = ')
    if userinput == '1':
        join()
    elif userinput == '2':
        login()
    elif userinput == '3':
        exit()
    elif userinput == 'root':
        root_login()
        
def login():
    global login_message,user
    user = 0
    systemfunction.clean_window()
    userid = input("ID : ")
    userpw = input("Password : ")
    systemfunction.clean_window()
    search_account = User(userid,userpw)  
    search_account.account_search()

    login_message = 1
    user = 1
    
    print("\n1.home")
    userinput = input('\ninput = ')
    del search_account
    if userinput == '1':
        systemfunction.clean_window()
        mainpage(login_message)
    else:

        Inputerror()

def join():
    systemfunction.clean_window()
    print("join\n")
    userid = input("ID : ")
    userpw = input("Password : ")
    systemfunction.clean_window()
    database = UserDatabase(userid,userpw,admin)
    database.User_new_account_request()
    print("\n1.home")
    userinput = input('\ninput = ')
    del database
    if userinput == '1':
        systemfunction.clean_window()
        mainpage(login_message)
    else:
        Inputerror()


def root_login():
    global login_message,admin
    admin = 0
    systemfunction.clean_window()
    print("admin login\n")
    userid = input("ID : ")
    userpw = input("Password : ")
    User.root_login(userid,userpw)
    admin += 1
    login_message = 2 
    root_home(admin)

def root_home(admin):
    systemfunction.clean_window()
    UserDatabase.User_account_info(admin)
    print("\n1.home 2.remove account")
    userinput = input('\ninput = ')
    if userinput == '1':
        systemfunction.clean_window()
        mainpage(login_message)
    elif userinput == '2':
        remove_userid = input('remove id : ')
        UserDatabase.remove_User_account(remove_userid)
        systemfunction.loading()
        systemfunction.clean_window()
        root_home(admin)
    else:
        Inputerror()


mainpage(login_message)
        




