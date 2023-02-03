alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt_row_cipher(plain_text, matrix_size, key_list, plain_text_length):
    rows = matrix_size[0]
    columns = matrix_size[1]
    list_slicer = 0
    cipher_text = []
    plain_text_matrix = []
    if ((rows * columns) >= plain_text_length and rows == len(key_list)):
        extra_space = (rows * columns) - plain_text_length
        for i in range(extra_space):
            plain_text.append(alphabets[len(alphabets) - 1 - i])
        for i in range(0, rows):
            plain_text_matrix.append(
                plain_text[list_slicer:list_slicer + columns])
            list_slicer += columns
        for i in key_list:
            cipher_text.append(plain_text_matrix[i - 1])
        cipher_text = ["".join(text) for text in zip(*cipher_text)]
        return "".join(map(str, cipher_text))
    else:
        return "Error!"


def decrypt_row_cipher(cipher_text, matrix_size, key_list, plain_text_length):
    rows = matrix_size[0]
    columns = matrix_size[1]
    list_slicer = 0
    plain_text = []
    cipher_text_column = []
    cipher_text_matrix = []
    if ((rows * columns) >= len(cipher_text) and rows == len(key_list)):
        for i in range(list_slicer, rows):
            for j in range(i, len(cipher_text), rows):
                cipher_text_column.append(cipher_text[j])
            list_slicer += 1
        list_slicer = 0

        for i in range(0, rows):
            cipher_text_matrix.append(
                cipher_text_column[list_slicer:list_slicer + columns])
            list_slicer += columns
        for i in key_list[::-1]:
            plain_text.append(cipher_text_matrix[i - 1])
        plain_text = ["".join(text) for text in plain_text]
        plain_text = "".join(map(str, plain_text))
        extra_alphabets = (rows * columns) - plain_text_length
        plain_text = list(plain_text[: -extra_alphabets or None])
        return "".join(map(str, plain_text))

    else:
        return "Error!"


def encrypt_column_cipher(plain_text, matrix_size, key_list, plain_text_length):
    rows = matrix_size[0]
    columns = matrix_size[1]
    list_slicer = 0
    cipher_text = []
    plain_text_matrix = []
    if ((rows * columns) >= plain_text_length and columns == len(key_list)):
        extra_space = (rows * columns) - plain_text_length
        for i in range(extra_space):
            plain_text.append(alphabets[len(alphabets) - 1 - i])
        for i in range(0, rows):
            plain_text_matrix.append(
                plain_text[list_slicer:list_slicer + columns])
            list_slicer += columns
        for i in key_list:
            for j in plain_text_matrix:
                cipher_text.append(j[i - 1])
        return "".join(map(str, cipher_text))
    else:
        return "Error!"


def decrypt_column_cipher(cipher_text, matrix_size, key_list, plain_text_length):
    rows = matrix_size[0]
    columns = matrix_size[1]
    list_slicer = 0
    plain_text = []
    cipher_text_column = []
    cipher_text_matrix = []
    if ((rows * columns) >= len(cipher_text) and columns == len(key_list)):
        for i in range(list_slicer, rows):
            for j in range(i, len(cipher_text), rows):
                cipher_text_column.append(cipher_text[j])
            list_slicer += 1
        list_slicer = 0
        for i in range(0, rows):
            cipher_text_matrix.append(
                cipher_text_column[list_slicer:list_slicer + columns])
            list_slicer += columns
        for i in range(0, rows):
            for j in range(0, columns):
                key_index = key_list.index(j + 1)
                plain_text.append(cipher_text_matrix[i][key_index])
        extra_alphabets = (rows * columns) - plain_text_length
        plain_text = plain_text[: -extra_alphabets or None]
        return "".join(map(str, plain_text))
    else:
        return "Error!"


print("Transposition Cipher")
menu_driven = True
while menu_driven:
    transposition = int(input(
        "\n1. Implement Row Transposition Cipher\n2. Implement Column Transposition Cipher\n\nAny other Key to Exit: "))
    if transposition == 1:
        print("\nRow Transposition: \n")
        plain_text = list(
            input("Message to Encrypt: ").upper().replace(" ", ""))
        matrix_size = list(map(int, input("Size of the matrix: ").split(" ")))
        key_list = list(map(int, input("Row Keys: ").split(" ")))
        plain_text_length = len(plain_text)

        row_transposition_encryption = encrypt_row_cipher(
            plain_text, matrix_size, key_list, plain_text_length)
        print("The Encrypted Message is:", row_transposition_encryption)

        cipher_text = list(
            input("Message to Decrypt: ").upper().replace(" ", ""))
        matrix_size = list(map(int, input("Size of the matrix: ").split(" ")))
        key_list = list(map(int, input("Row Keys: ").split(" ")))

        transposition_row_decryption = decrypt_row_cipher(
            cipher_text, matrix_size, key_list, plain_text_length)
        print("The Decrypted Message is:", transposition_row_decryption)
    elif transposition == 2:
        print("\nColumn Transposition\n")
        plain_text = list(
            input("Message to Encrypt: ").upper().replace(" ", ""))
        matrix_size = list(
            map(int, input("Size of the matrix: ").split(" ")))
        key_list = list(map(int, input("Column Keys: ").split(" ")))
        plain_text_length = len(plain_text)

        column_transposition_encryption = encrypt_column_cipher(
            plain_text, matrix_size, key_list, plain_text_length)
        print("The Encrypted Message is:", column_transposition_encryption)

        cipher_text = column_transposition_encryption

        transposition_column_decryption = decrypt_column_cipher(
            cipher_text, matrix_size, key_list, plain_text_length)
        print("The Decrypted Message is:", transposition_column_decryption)
    else:
        menu_driven = False
