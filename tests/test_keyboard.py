from src.Keyboard import Keyboard
import unittest


class KeyboardTests(unittest.TestCase):
    def setUp(self):
        self.keyboard = Keyboard("Wireless Keyboard", 29.99, 10)

    def test_keyboard_properties(self):
        self.assertEqual(self.keyboard.name, "Wireless Keyboard")
        self.assertEqual(self.keyboard.price, 29.99)
        self.assertEqual(self.keyboard.quantity, 10)

    def test_keyboard_language_default(self):
        self.assertEqual(self.keyboard.language, "EN")

    def test_keyboard_change_language(self):
        self.keyboard.change_lang()
        self.assertEqual(self.keyboard.language, "RU")
        self.keyboard.change_lang()
        self.assertEqual(self.keyboard.language, "EN")


if __name__ == "__main__":
    unittest.main()
