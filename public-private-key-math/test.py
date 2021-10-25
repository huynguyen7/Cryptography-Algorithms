from super_increasing_sequence import is_super_increasing_sequence, \
            gen_super_increasing_sequence, \
            get_chosen_elements
from public_secret_cipher import encrypt, decrypt, private_seq
import unittest


class SuperIncrSeq(unittest.TestCase):
    def test_empty(self):
        seq = gen_super_increasing_sequence(n=0)
        assert(is_super_increasing_sequence(seq))

    def test_1(self):
        seq = gen_super_increasing_sequence(n=5)
        assert(is_super_increasing_sequence(seq))

    def test_2(self):
        seq = gen_super_increasing_sequence(init_seq=[1,3,6], n=100)
        assert(is_super_increasing_sequence(seq))

    def test_3(self):
        seq = gen_super_increasing_sequence(init_seq=[1,3,5], n=128)
        assert(is_super_increasing_sequence(seq))


class EncDecTest(unittest.TestCase):
    def test_1(self):
        # Original message.
        msg = set([0,1,2])
        encrypted_msg = encrypt(msg)
        decrypted_msg = decrypt(encrypted_msg)
        assert(msg == decrypted_msg)


if __name__ == "__main__":
    unittest.main()
