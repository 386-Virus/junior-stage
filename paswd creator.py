#our password must contain the following
print('Create your password for the account')
upper = set('ABCDEFGHIJKLMNOPGRSTUVWXYZ')
lower = set('abcdefghijklmnopqrstuvwxyz')
num = set('0123456789')
alnum = set('!@#$%^&*()_+}|<>?,.?"')
#here is where the condion for password we create
while True:
    pass1 = input('Enter your password:\t')
    if len(pass1) >= 8 and any(char in upper for char in pass1) and any(char in alnum for char in pass1) and any(char in lower for char in pass1) and any(char in num for char in pass1):
        conf_pass1 = input('Confirm your password:\t')
        if pass1 == conf_pass1:
            print('password confirmed')
            break
        else:
            print('password do not match')
    else:
        print(""""WEAK PASSWORD
                  Your password should contain atleast 8 characters with upper case, lower case and numbers""")
