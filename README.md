# PassWord
超简易密码保存程序（AES加密保护）
## 依赖包
pyperclip, shelve, pycrypto
## 安装
1. 拷贝到任意目录
2. 终端：
```
sudo vi ~/.bash_profile 
```
添加:
```
export PATH=$PATH:……（程序保存目录）
alias password="程序保存目录/password.py"
```
!如果系统默认python版本为2.X,前述命令改为
```
alias password="python3 程序保存目录/password.py"
```
3. 使用：终端直接输入
```
password 参数1 参数2 参数3
```
```
add [account] [password] -add item
copy [account] -copy password to clip
change [account] [password] -change existed item
del [account] -delete item
clear all -delete all items
list all -show all the items existed
encrypt all -encrypt database use AES256
decrypt all -decrypt database
```
