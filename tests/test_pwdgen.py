import unittest

import pwdgen


class TestGenerate(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(pwdgen.generate()), 16)

    def test_custom_length(self):
        self.assertEqual(len(pwdgen.generate(20)), 20)

    def test_no_ambiguous_chars(self):
        for _ in range(200):
            self.assertFalse(set(pwdgen.generate(24)) & pwdgen.AMBIGUOUS)

    def test_no_symbols_when_disabled(self):
        pw = pwdgen.generate(64, symbols=False)
        self.assertFalse(set(pw) & set(pwdgen.SYMBOLS))

    def test_contains_all_char_classes(self):
        pw = pwdgen.generate(20, symbols=True)
        self.assertTrue(any(c.isupper() for c in pw))
        self.assertTrue(any(c.islower() for c in pw))
        self.assertTrue(any(c.isdigit() for c in pw))

    def test_short_length_rejected(self):
        with self.assertRaises(ValueError):
            pwdgen.generate(3)

    def test_generated_passwords_are_unique(self):
        self.assertEqual(len({pwdgen.generate() for _ in range(50)}), 50)


if __name__ == "__main__":
    unittest.main()
