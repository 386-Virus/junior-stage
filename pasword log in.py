
psword = "conf_pass1"
lock = ''
up_limit = False
limit = 5
count = 0
while lock != psword and not up_limit:
     if count < limit:
        count += 1
        lock = input('enter the password:\t')
     else:
        up_limit = True

if not up_limit:
    print('Welcome to our site')
else:
    print('Wrong entry\v Account is blocked due to large attempt of password entry!')