password = input("Enter your password:")

num = "0123456789"
num_count = 0
spc = "!@#$%^&*~`"
spc_count = 0
big = 0

if len(password) < 12:
    print("Weak Password")
else:
    for char in password:
        if char in num:
            num_count += 1
        if char in spc:
            spc_count += 1
        if char.isupper():
            big += 1
    
    if num_count >= 2 and spc_count >= 1 and big >= 2:
        print("Very Strong Password")
    else:
        print("Strong Password")
