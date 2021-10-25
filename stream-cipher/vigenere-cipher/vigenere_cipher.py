"""
    
    @author: Huy Nguyen
    - Implementation for Vigenere's Cipher method (encrypting and decrypting).

"""


def encrypt(plain_data, key=[1]):  # Return bytes.
    assert isinstance(key, list) and len(key) > 0, '[Error] Invalid key.'
    assert plain_data is not None and (isinstance(plain_data, bytes) or isinstance(plain_data, bytearray))

    encrypted_data = bytearray()  # Buffer memory for result.
    i = 0
    n = len(key)
    for val in plain_data:
        step = key[i%n]
        encrypted_data.append((val+step)%256)
        i += 1

    return encrypted_data


def decrypt(encrypted_data, key=[1]):  # Return bytes.
    assert isinstance(key, list) and len(key) > 0, '[Error] Invalid key.'
    assert encrypted_data is not None and (isinstance(encrypted_data, bytes) or isinstance(encrypted_data, bytearray))

    decrypted_data = bytearray()  # Buffer memory for result.
    i = 0
    n = len(key)
    for val in encrypted_data:
        step = key[i%n]
        decrypted_data.append((val-step)%256)
        i += 1

    return decrypted_data
