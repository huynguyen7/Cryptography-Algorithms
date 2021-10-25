import unittest
from vigenere_cipher import encrypt, decrypt


class VigenereCipherTest(unittest.TestCase):
    def test_empty(self):
        plain_data = ''
        encrypted_data = encrypt(plain_data.encode())
        assert len(encrypted_data) == 0
        decrypted_data = decrypt(encrypted_data)
        assert len(decrypted_data) == 0

    def test_digits(self):
        key = [1,2]
        plain_data = '123678'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == '24488:'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data

    def test_chars(self):
        key = [3,4]
        plain_data = 'ade'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == 'dhh'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data

    def test_digits_chars(self):
        key = [1,2]
        plain_data = 'ade123'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == 'bff335'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data

    def test_boundary(self):
        key = [257,258]
        plain_data = 'ade123'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == 'bff335'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data


if __name__ == "__main__":
    unittest.main()
