import unittest

from wormbox.encapsulation import marshal, unmarshal
from wormbox.encryption import InvalidCiphertext, decrypt, encrypt
from wormbox.key import Key
from wormbox.wormbox import TEST_KEY


class WormBoxTest(unittest.TestCase):
    '''Simple tests for the wormbox implementation'''

    def test_decrypt(self):
        '''This should decrypt the given string with default key'''
        # Load the TEST_KEY and decrypt a know-good string
        key = Key(TEST_KEY)
        ciphertext = 'LGQMV UEIQP DAGCL MPLTS MFUCL'
        marshaled = decrypt(ciphertext, key.key)
        plaintext = unmarshal(marshaled)
        self.assertEquals(plaintext, 'ANTTI LAEHE KALJALLE')

    def test_full_round(self):
        key = Key.random_key()
        plaintext = 'Punk IPA on parsast olutta'
        marshaled = marshal(plaintext)
        ciphertext = encrypt(marshaled, key.key)
        marshaled = decrypt(ciphertext, key.key)
        plaintext = unmarshal(marshaled)
        self.assertEquals(plaintext, 'PUNK IPA ON PARSAST OLUTTA    ')
