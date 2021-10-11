def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    upperalph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    loweralph = 'abcdefghijklmnopqrstuvwxyz'
    for j in range (len(keyword)):
        b = ord(keyword[j])
        if keyword[j].isupper():
            key = b - 64
        elif keyword[j].islower():
            key = b - 96
    for i in plaintext:
        ind = upperalph.find(i)
        newind = ind + key
        if i in upperalph:
            ciphertext += upperalph[newind]  
        else:
            ciphertext += i
        ind = loweralph.find(i)
        newind = ind + key
        if i in loweralph:
            ciphertext += loweralph[newind]  
        else:
            ciphertext += i
    return ciphertext
print (encrypt_vigenere('PYTHON', 'A'))

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
