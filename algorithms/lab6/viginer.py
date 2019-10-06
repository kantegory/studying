def encrypt_vigenere(plaintext, keyword):
    nonCaps = [i for i in range(65, 91)]
    caps = [i for i in range(97, 123)]
    for i in range(len(nonCaps)):
        nonCaps[i] = chr(nonCaps[i])
        caps[i] = chr(caps[i])
    while len(plaintext) > len(keyword):
        keyword += keyword
    while len(keyword) > len(plaintext):
        keyword = keyword[:-1]
    ciphertext = ''
    shift = [0] * len(keyword)
    for i in range(0, len(keyword)):
        if keyword[i] in nonCaps:
            shift[i] = nonCaps.index(keyword[i])
            if (ord(plaintext[i]) + shift[i] > 63) and (ord(plaintext[i]) + shift[i] < 91):
                ciphertext += chr(ord(plaintext[i]) + shift[i])
            else:
                ciphertext += chr(ord(plaintext[i]) + shift[i] - 26)
        elif keyword[i] in caps:
            shift[i] = caps.index(keyword[i])
            if (ord(plaintext[i]) + shift[i] > 96) and (ord(plaintext[i]) + shift[i] < 123):
                ciphertext += chr(ord(plaintext[i]) + shift[i])
            else:
                ciphertext += chr(ord(plaintext[i]) + shift[i] - 26)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    nonCaps = [i for i in range(65, 91)]
    caps = [i for i in range(97, 123)]
    for i in range(len(nonCaps)):
        nonCaps[i] = chr(nonCaps[i])
        caps[i] = chr(caps[i])
    while len(ciphertext) > len(keyword):
        keyword += keyword
    while len(keyword) > len(ciphertext):
        keyword = keyword[:-1]
    plaintext = ''
    shift = [0] * len(keyword)
    for i in range(0, len(keyword)):
        if keyword[i] in nonCaps:
            shift[i] = nonCaps.index(keyword[i])
            if (ord(ciphertext[i]) - shift[i] > 63) and (ord(ciphertext[i]) - shift[i] < 91):
                plaintext += chr(ord(ciphertext[i]) - shift[i])
            else:
                plaintext += chr(ord(ciphertext[i]) - shift[i] + 26)
        elif keyword[i] in caps:
            shift[i] = caps.index(keyword[i])
            if (ord(ciphertext[i]) - shift[i] > 96) and (ord(ciphertext[i]) - shift[i] < 123):
                plaintext += chr(ord(ciphertext[i]) - shift[i])
            else:
                plaintext += chr(ord(ciphertext[i]) - shift[i] + 26)
        else:
            plaintext += ciphertext[i]
    return plaintext
