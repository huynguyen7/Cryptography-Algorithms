import unittest
from caesar_cipher import encrypt, decrypt


class CaesarCipherTest(unittest.TestCase):
    def test_empty(self):
        plain_data = ''
        encrypted_data = encrypt(plain_data.encode())
        assert len(encrypted_data) == 0
        decrypted_data = decrypt(encrypted_data)
        assert len(decrypted_data) == 0

    def test_digits(self):
        key = 2
        plain_data = '123678'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == '34589:'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data
    
    def test_chars(self):
        key = 3
        plain_data = 'ade'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == 'dgh'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data

    def test_digits_chars(self):
        key = 1
        plain_data = 'ade123'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == 'bef234'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data

    def test_boundary(self):
        key = 257
        plain_data = 'ade123'
        encrypted_data = encrypt(plain_data.encode(), key)
        assert encrypted_data == 'bef234'.encode()
        decrypted_data = decrypt(encrypted_data, key)
        assert decrypted_data.decode() == plain_data


if __name__ == "__main__":
    unittest.main()
