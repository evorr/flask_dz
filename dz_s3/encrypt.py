def encrypt(password):
    new_res = ''
    for i in range(len(password) - 1):
        if password[i].isdecimal():
            new_res += chr(int(password[i]))
        else:
            new_res += str(ord(password[i]))
    return new_res