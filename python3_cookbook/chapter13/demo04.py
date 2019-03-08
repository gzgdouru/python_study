'''
运行时弹出密码输入提示
'''
import getpass

if __name__ == "__main__":
    user = getpass.getuser()
    password = getpass.getpass()

    print(user, password)