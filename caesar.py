def encrypt_caesar(plaintext,shift):
    ciphertext = ""
    for i in range(0,len(plaintext)):
        if ((ord(plaintext[i])+shift>63) and (ord(plaintext[i])+shift<91)) or ((ord(plaintext[i])+shift>96) and (ord(plaintext[i])+shift<123)):
            ciphertext += chr(ord(plaintext[i])+shift)
        else:
            ciphertext += chr(ord(plaintext[i])+shift-26)
        if (ord(plaintext[i])<63) or ((ord(plaintext[i])>91) and (ord(plaintext[i])<96)) or (ord(plaintext[i])>123):
            return print('Error. This symbol is incorrect.')
    return print(ciphertext)

plaintext = input()
shift = int(input())
encrypt_caesar(plaintext,shift)

def decrypt_caesar(ciphertext,shift):
    plaintext = ""
    for i in range(0,len(ciphertext)):
        if ((ord(ciphertext[i])-shift>63) and (ord(ciphertext[i])-shift<91)) or ((ord(ciphertext[i])-shift>96) and (ord(ciphertext[i])-shift<123)):
            plaintext += chr(ord(ciphertext[i])-shift)
        else:
            plaintext += chr(ord(ciphertext[i])-shift+26)
        if (ord(ciphertext[i])<63) or ((ord(ciphertext[i])>91) and (ord(ciphertext[i])<96)) or (ord(ciphertext[i])>123):
            return print('Error. This symbol is incorrect.')
    return print(plaintext)

ciphertext = input()
decrypt_caesar(ciphertext,shift)
