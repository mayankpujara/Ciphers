import re
import copy
import sys
x_length = 19
y_length = 22
z_length = 23

key_one = ""
x = []
y = []
z = []


def load_registers(key):
    i = 0
    while (i < x_length):
        x.insert(i, int(key[i]))  # takes first 19 elements from key
        i = i + 1
    j = 0
    p = x_length
    while (j < y_length):
        y.insert(j, int(key[p]))  # takes next 22 elements from key
        p = p + 1
        j = j + 1
    k = y_length + x_length
    r = 0
    while (r < z_length):
        z.insert(r, int(key[k]))  # takes next 23 elements from key
        k = k + 1
        r = r + 1


def set_key(key):
    if (len(key) == 64 and re.match("^([01])+", key)):
        key_one = key
        load_registers(key)
        return True
    return False


def get_key():
    return key_one


def to_binary(plain):
    s = ""
    i = 0
    for i in plain:
        binary = str(' '.join(format(ord(x), 'b') for x in i))
        j = len(binary)
        while (j < 8):
            binary = "0" + binary
            s = s + binary
            j = j + 1
    binary_values = []
    k = 0
    while (k < len(s)):
        binary_values.insert(k, int(s[k]))
        k = k + 1
    return binary_values


def get_majority(x, y, z):
    if (x + y + z > 1):
        return 1
    else:
        return 0


def get_keystream(length):
    x_temp = copy.deepcopy(x)
    y_temp = copy.deepcopy(y)
    z_temp = copy.deepcopy(z)
    keystream = []
    i = 0
    while i < length:
        majority = get_majority(x_temp[8], y_temp[10], z_temp[10])
        if x_temp[8] == majority:
            new = x_temp[13] ^ x_temp[16] ^ x_temp[17] ^ x_temp[18]
            x_temp_two = copy.deepcopy(x_temp)
            j = 1
            while (j < len(x_temp)):
                x_temp[j] = x_temp_two[j-1]
                j = j + 1
            x_temp[0] = new

        if y_temp[10] == majority:
            new_one = y_temp[20] ^ y_temp[21]
            y_temp_two = copy.deepcopy(y_temp)
            k = 1
            while (k < len(y_temp)):
                y_temp[k] = y_temp_two[k-1]
                k = k + 1
            y_temp[0] = new_one

        if z_temp[10] == majority:
            new_two = z_temp[7] ^ z_temp[20] ^ z_temp[21] ^ z_temp[22]
            z_temp_two = copy.deepcopy(z_temp)
            m = 1
            while (m < len(z_temp)):
                z_temp[m] = z_temp_two[m-1]
                m = m + 1
            z_temp[0] = new_two
        keystream.insert(i, x_temp[18] ^ y_temp[21] ^ z_temp[22])
        i = i + 1
    return keystream


def to_str(binary):
    s = ""
    length = len(binary) - 8
    i = 0
    while (i <= length):
        s = s + chr(int(binary[i:i+8], 2))
        i = i + 8
    return str(s)


def encrypt(plain):
    s = ""
    binary = to_binary(plain)
    keystream = get_keystream(len(binary))
    i = 0
    while (i < len(binary)):
        s = s + str(binary[i] ^ keystream[i])
        i = i + 1
    return s


def decrypt(cipher):
    s = ""
    binary = []
    keystream = get_keystream(len(cipher))
    i = 0
    while (i < len(cipher)):
        binary.insert(i, int(cipher[i]))
        s = s + str(binary[i] ^ keystream[i])
        i = i + 1
    return to_str(str(s))


def inp_key():
    tha_key = str(input('Enter a 64-bit key: '))
    if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
        return tha_key
    else:
        while (len(tha_key) != 64 and not re.match("^([01])+", tha_key)):
            if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
                return tha_key
            tha_key = str(input('Enter a 64-bit key: '))
    return tha_key


def choice():
    inp = str(
        input('\n[1]: Implement A51 Cipher\n[2]: Exit\nOption: '))
    if (inp == '1' or inp == '2'):
        return inp
    else:
        while (inp != '1' or inp != '2'):
            if (inp == '1' or inp == '2'):
                return inp
            inp = str(
                input('\n[1]: Implement A51 Cipher\n[2]: Exit\nOption: '))
    return inp


def text():
    try:
        inp = str(input('Enter the plaintext: '))
    except:
        inp = str(input('Try again: '))
    return inp


def main():
    key = str(inp_key())
    set_key(key)
    first_choice = choice()
    if (first_choice == '1'):
        plaintext = str(text())
        print("\nPlainText:", plaintext)
        a = encrypt(plaintext)
        print("\nEncrypted Text:", a)
        ciphertext = a
        print("\nDecrypted Text:", decrypt(ciphertext))
    elif (first_choice == '2'):
        print("\nTerminal Closed")
        sys.exit(0)

# 64-bit key: 1101011001010010110101110001100101101001001000110110110010110111


main()
