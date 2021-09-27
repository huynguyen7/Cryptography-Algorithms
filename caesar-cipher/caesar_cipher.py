"""
    
    @author: Huy Nguyen
    - Implementation for Caesar's Cipher method (encrypting and decrypting).
    - The encrypting phase moves up the byte in ascii format by <key> value. Then, decrypt by moving down the encrypted byte by <key> value.
    - Source: https://en.wikipedia.org/wiki/Caesar_cipher

"""


def encrypt(plain_data, key=1):  # Return bytes.
    assert isinstance(key, int) and key > 0, '[Error] Invalid key.'
    assert plain_data is not None and (isinstance(plain_data, bytes) or isinstance(plain_data, bytearray))

    encrypted_data = bytearray()  # Buffer memory for result.
    for val in plain_data:
        encrypted_data.append((val+key)%256)

    return encrypted_data


def decrypt(encrypted_data, key=1):  # Return bytes.
    assert isinstance(key, int) and key > 0, '[Error] Invalid key.'
    assert encrypted_data is not None and (isinstance(encrypted_data, bytes) or isinstance(encrypted_data, bytearray))

    plain_data = bytearray()  # Buffer memory for result.
    for val in encrypted_data:
        plain_data.append((val-key)%256)

    return plain_data
