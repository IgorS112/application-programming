import unittest
from mod2.task3 import decrypt


class TestCorrectDecryption(unittest.TestCase):
    def test_get_correct_decryption_with_one_point(self):
        self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')
        self.assertEqual(decrypt('.'), '')

    def test_get_correct_decryption_with_two_point(self):
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')

    def test_get_correct_decryption_with_three_and_more_point(self):
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра........'), '')
        self.assertEqual(decrypt('абр......а.'), 'абр......а')
        self.assertEqual(decrypt('1..2.3'), '123')
        self.assertEqual(decrypt('1.......................'), '')

