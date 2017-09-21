# -*- coding: utf-8 -*-
#密码保存程序
import sys
import shelve
import pyperclip
shelfFile=shelve.open('mydata')
print('PASSWORD COPY SYSTEM\n')
print('add [account] [password] -add item\n copy [account] -copy password to clip\n change [account] [password] -change existed item\n del [account] -delete item\n clear all -delete all items\n list all -show all the items existed\n')
if len(sys.argv)<2:
    print('Usage：type password.py [order]...to use.\n')
    sys.exit()
order=sys.argv[1]
account=sys.argv[2]
list1=list(shelfFile.keys())
if account in list1 and order=='copy':
    #print(shelfFile.values(account))
    #list2=list(shelfFile.values())
    pyperclip.copy(shelfFile[account])
    #print(shelfFile[account])
    print('password for '+account+' copied to clipboard.')
    shelfFile.close()
elif account not in list1 and order=='copy':
    print('Error:account not exist')
else:
    if order=='add' and account not in list1:
        password=sys.argv[3][0:]
        shelfFile[account]=password
        #print(password)
        print('password for '+ account +' has been saved.')
        shelfFile.close()
    elif order=='add' and account in list1:
        print('password for '+account+' have been existed')
    elif order=='change' and account in list1:
        password=sys.argv[3][0:]
        shelfFile[account]=password
        print('password for '+ account +' has been changed.')
        shelfFile.close()
    elif order=='del' and account in list1:
        shelfFile.pop(account)
        print('password for '+account+' has been deleted.')
        shelfFile.close()
    elif order=='del' and account not in list1:
        print('no such account to delete.\n')
    elif order=='clear':
        shelfFile.clear()
        print('all items have been cleared')
        shelfFile.close()
    elif order=='list':
        for item in list1:
            print(item)
        shelfFile.close()
    else:
        print('There is no order '+ order +' please type --help for more infomation.')






