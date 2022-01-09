from super_increasing_sequence import gen_super_increasing_sequence, \
        get_seq_available_size, \
        get_chosen_elements


"""

    Using modular-inverse multiplication method for encrypting and decrypting.
    Why modular-inverse? Since inversing problem can easily be recognized in grade school. Such as 8 * (1/8) = 1. In this case, for example, everyone can acknowledge that the inverse of 8 is 1/8. However, with modular-inverse, it turns into a much consuming problem to find the inverse. Such as (3 * 7) % 10.

    For example: If our message we are trying to hide is 4.
    Simple inverse:   4 * 8 * (1/8) = 4.
    Modular-inverse:  (4 * 3 * 7) % 10
                      = (2 * 7) % 10 (we can mask this)
                      = 4

    Because there are an infinite number of modulo and an infinite number of inverse pairs, cryptographers can CHOOSE a pair that, unless you know the secret generating numbers, will be very, very difficult to find!

    *We have private key A, public chosen value B and modulo C. A and B can also be considered as an inverse pair in modular-inverse.
    In this example, my inverse pair is 22*23, and the modulo value is 101.
    *The reason why super increasing sequence is used in this case is it is a special case for my chosen inverse pair value (22*23) and modulo value 101 since they yields the generated public keys into super increasing sequence. Additionally, super increasing sequence removes the statistical pattern, so malicious attackers can only use brute-force approach to find the public key.
    
    *NOTES: The value I have chosen in this code is not efficient, this works fine for messages that are in range [1,100].

"""


# Private properties.
private_key = 23  # Alice/key distributor 's private key.
num_possibilities = 101  # Number of possibilities, also the value of modulo C in the math formula.
private_seq = gen_super_increasing_sequence(n=101)  # Generating super increasing sequence for Alice (key distributor).

# Public properties.
my_public_key = 22  # The value that Bob chose.


def encrypt(msg):  # Input as an int value between [1,100] using chosen public key.
    assert isinstance(msg, int)  # Check if it is an int value.
    return (msg*my_public_key)%num_possibilities


def decrypt(x):  # Input as a numerical value (a message that has been encrypted)
    assert isinstance(x, int)  # Check if it is an int value.
    return (x*private_key)%num_possibilities


def test():  # Unit test.
    msgs = [x for x in range(1,101)]  # Testing messages.
    for msg in msgs:
        encrypted_msg = encrypt(msg)
        decrypted_msg = decrypt(encrypted_msg)
        assert(msg == decrypted_msg), f"%d != %d" % (msg, decrypted_msg)  # Check if they are the same.

if __name__ == "__main__":
    test()
