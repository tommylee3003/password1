# -*- coding: utf-8 -*-
#密码保存程序
import sys
import shelve
import pyperclip
from Crypto.Cipher import AES
import os

def AES_encrypt(msg):

    key = '\x02' * 32
    iv = b'\x4e\x09\x48\x3e\x38\xf5\xff\x72\x80\x12\x7b\x9e\xfb\x5c\x2d\x33'
    mode = AES.MODE_CBC
    encrypt = AES.new(key, mode, iv)
    x = len(msg) % 16
    input_n = msg + ("0" * (16 - x)).encode('utf-8')
    output = encrypt.encrypt(input_n)

    return output

def AES_decrypt(msg):
    key = '\x02' * 32
    iv = b'\x4e\x09\x48\x3e\x38\xf5\xff\x72\x80\x12\x7b\x9e\xfb\x5c\x2d\x33'
    mode = AES.MODE_CBC
    encrypt = AES.new(key, mode, iv)
    x=len(msg)%16
    input_n=msg+("0"*(16-x)).encode('utf-8')
    output=encrypt.decrypt(input_n)
    return output

f=open("flags","r")
state=f.read()

if(state=="en"):
    str=input("please input the main password:")
    if str!="123456":
        print("password wrong")
    else:

        de = open("mydata.db", "rb+")
        msg_d = de.read()
        output = AES_decrypt(msg_d)
        de.write(output)
        de.close()
        '''de = open("mydata.bak", "rb+")
        msg_d = de.read()
        output = AES_decrypt(msg_d)
        de.write(output)
        de.close()
        de = open("mydata.dir", "rb+")
        msg_d = de.read()
        output = AES_decrypt(msg_d)
        de.write(output)
        de.close()'''
        print("decrypt successd")
        f = open("flags", "r+")
        f.write("de")
        f.close()

else:
    shelfFile = shelve.open('mydata')
    print('PASSWORD COPY SYSTEM\n')
    print('add [account] [password] -add item\n '
          'copy [account] -copy password to clip\n '
          'change [account] [password] -change existed item\n '
          'del [account] -delete item\n '
          'clear all -delete all items\n '
          'list all -show all the items existed\n'
          'encrypt all -encrypt the database use AES256\n'
          'decrypt all -decrypt the database\n')

    if len(sys.argv) < 2:
        print('Usage：type password.py [order]...to use.\n')
        sys.exit()
    order = sys.argv[1]
    account = sys.argv[2]
    list1 = list(shelfFile.keys())
    if account in list1 and order == 'copy':

        # print(shelfFile.values(account))
        # list2=list(shelfFile.values())
        pyperclip.copy(shelfFile[account])
        # print(shelfFile[account])
        print('password for ' + account + ' copied to clipboard.')
        shelfFile.close()
    elif account not in list1 and order == 'copy':
        print('Error:account not exist')
    else:
        if order == 'add' and account not in list1:
            password = sys.argv[3][0:]
            shelfFile[account] = password
            # print(password)
            print('password for ' + account + ' has been saved.')
            shelfFile.close()
        elif order == 'add' and account in list1:
            print('password for ' + account + ' have been existed')
        elif order == 'change' and account in list1:
            password = sys.argv[3][0:]
            shelfFile[account] = password
            print('password for ' + account + ' has been changed.')
            shelfFile.close()
        elif order == 'del' and account in list1:
            shelfFile.pop(account)
            print('password for ' + account + ' has been deleted.')
            shelfFile.close()
        elif order == 'del' and account not in list1:
            print('no such account to delete.\n')
        elif order == 'clear':
            shelfFile.clear()
            print('all items have been cleared.\n')
            shelfFile.close()
        elif order == 'list':
            for item in list1:
                print(item)
            shelfFile.close()
        elif order == 'encrypt':
            shelfFile.close()
            en = open("%s/mydata.db" % os.getcwd(), "rb+")
            msg_e = en.read()
            output = AES_encrypt(msg_e)
            en.write(output)
            en.close()
            '''en = open("%s/mydata.bak" % os.getcwd(), "rb+")
            msg_e = en.read()
            output = AES_encrypt(msg_e)
            en.write(output)
            en.close()
            en = open("%s/mydata.dir" % os.getcwd(), "rb+")
            msg_e = en.read()
            output = AES_encrypt(msg_e)
            en.write(output)
            en.close()'''
            f=open("flags","w")
            f.write("en")
            f.close()
            print("encrypt successd")
        elif order == 'decrypt':
            str = input("please input the main password:")
            if str != "123456":
                print("password wrong")
            else:
                shelfFile.close()
                de = open("mydata.db", "rb+")
                msg_d = de.read()
                output = AES_decrypt(msg_d)
                de.write(output)
                de.close()
                '''de = open("mydata.bak", "rb+")
                msg_d = de.read()
                output = AES_decrypt(msg_d)
                de.write(output)
                de.close()
                de = open("mydata.dir", "rb+")
                msg_d = de.read()
                output = AES_decrypt(msg_d)
                de.write(output)
                de.close()'''
                print("decrypt successd")
                en_state = 0

        else:
            print('There is no order ' + order + ' please type --help for more infomation.')











