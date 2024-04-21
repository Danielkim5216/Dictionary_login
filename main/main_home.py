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

def UI(userinput):
    if userinput == '1':
        print("\n******************JOIN*****************\n")
    elif userinput == '2':
        print("\n*****************LOGIN*****************\n")
    elif userinput == 'root':
        print("\n******************ROOT******************\n")
    else:
        print("\n******************MAIN******************\n\n\t1.join 2.login 3.exit")

#input error 
def Inputerror():
    global login_message
    print("\ninput error")
    systemfunction.loading()
    systemfunction.clean_window()
    mainpage(login_message)
    
#main page 
def mainpage(login_message):
    userinput = 'home'
    if login_message == 0:
        message = 'not login account'
    elif login_message == 1:
        message = 'user'
    elif login_message == 2:
        message = 'admin'
    else:
        message = 'login_message error'
    UI(userinput)
    '''print(admin,user)'''
    print(f"\n      you are {message}")
    userinput = input('\n\tinput = ')
    if userinput == '1':
        join(userinput)
    elif userinput == '2':
        login(userinput)
    elif userinput == '3':
        exit()
    elif userinput == 'root':
        root_login(userinput)
        
def login(userinput):
    global login_message,user
    user = 0
    systemfunction.clean_window()
    UI(userinput)
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

def join(userinput):
    systemfunction.clean_window()
    UI(userinput)
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


def root_login(userinput):
    global login_message,admin
    admin = 0
    systemfunction.clean_window()
    UI(userinput)
    userid = input("ID : ")
    userpw = input("Password : ")
    User.root_login(userid,userpw)
    admin += 1
    login_message = 2 
    root_home(admin)

def root_home(admin):
    systemfunction.clean_window()
    UserDatabase.User_account_info(admin)
    print("\n1.home 2.remove account 3.save data 4.load data")
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
    elif userinput == '3':
        UserDatabase.save_data_in_txt()
        systemfunction.loading()
        systemfunction.clean_window()
        root_home(admin)
    elif userinput == '4':
        UserDatabase.load_data_in_txt()
        systemfunction.loading()
        systemfunction.clean_window()
        root_home(admin)
    else:
        Inputerror()


mainpage(login_message)
        




