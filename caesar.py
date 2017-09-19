def encrypt_caesar(plaintext, shift):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'def encrypt_caesar(plaintext, shift):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(0, len(plaintext)):
        if ((ord(plaintext[i]) + shift > 63) and (ord(plaintext[i]) + shift < 91)) or ((ord(plaintext[i]) + shift > 96) and (ord(plaintext[i]) + shift < 123)):
            ciphertext += chr(ord(plaintext[i]) + shift)
        elif ((ord(plaintext[i]) + shift < 65) or (ord(plaintext[i]) + shift > 91)) or ((ord(plaintext[i]) + shift < 96) or (ord(plaintext[i]) + shift > 122)):
            ciphertext += chr(ord(plaintext[i]) + shift - 26)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(0, len(ciphertext)):
        if ((ord(ciphertext[i]) - shift > 63) and (ord(ciphertext[i]) - shift < 91)) or ((ord(ciphertext[i]) - shift > 96) and (ord(ciphertext[i]) - shift < 123)):
            plaintext += chr(ord(ciphertext[i]) - shift)
        elif ((ord(ciphertext[i]) - shift < 65) or (ord(ciphertext[i]) - shift > 91)) or ((ord(ciphertext[i]) - shift < 96) or (ord(ciphertext[i]) - shift > 123)):
            plaintext += chr(ord(ciphertext[i]) - shift + 26)
        else:
            plaintext += ciphertext[i]
    return plaintext

    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(0, len(plaintext)):
        if ((ord(plaintext[i]) + shift > 63) and (ord(plaintext[i]) + shift < 91)) or ((ord(plaintext[i]) + shift > 96) and (ord(plaintext[i]) + shift < 123)):
            ciphertext += chr(ord(plaintext[i]) + shift)
        elif ((ord(plaintext[i]) + shift < 65) or (ord(plaintext[i]) + shift > 91)) or ((ord(plaintext[i]) + shift < 96) or (ord(plaintext[i]) + shift > 122)):
            ciphertext += chr(ord(plaintext[i]) + shift - 26)
		else:
			ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(0, len(ciphertext)):
        if ((ord(ciphertext[i]) - shift > 63) and (ord(ciphertext[i]) - shift < 91)) or ((ord(ciphertext[i]) - shift > 96) and (ord(ciphertext[i]) - shift < 123)):
            plaintext += chr(ord(ciphertext[i]) - shift)
        elif ((ord(ciphertext[i]) - shift < 65) or (ord(ciphertext[i]) - shift > 91)) or ((ord(ciphertext[i]) - shift < 96) or (ord(ciphertext[i]) - shift > 123)):
            plaintext += chr(ord(ciphertext[i]) - shift + 26)
		else:
			plaintext += ciphertext[i]
    return plaintext
