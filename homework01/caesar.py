import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    chiphertext = ''
    for i in range (len(plaintext)):
        if plaintext[i].isalpha():
            a = ord(plaintext[i])
            if plaintext[i].isupper() and a >= 88:
                chiphertext += chr(a-23)
            elif plaintext[i].islower() and a >= 120:
                chiphertext += chr(a-23)
            else:
                chiphertext += chr(a+3)
        elif plaintext.isspace():
            continue
        else:
            chiphertext += plaintext[i]
    return chiphertext

def decrypt_caesar(chiphertext: str, shift: int = 3) -> str:
    """
    Decrypts a chiphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for i in range (len(chiphertext)):
        if chiphertext[i].isalpha():
            a = ord(chiphertext[i])
            if chiphertext[i].isupper() and a <= 67:
                plaintext += chr(a+23)
            elif chiphertext[i].islower() and a <= 99:
                plaintext += chr(a+23)
            else:
                plaintext += chr(a-3)
        elif chiphertext.isspace():
            continue
        else:
            plaintext += chiphertext[i]
    return plaintext

def caesar_breaker_brute_force(chiphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
