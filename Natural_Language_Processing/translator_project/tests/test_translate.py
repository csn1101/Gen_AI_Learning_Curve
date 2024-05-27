import unittest
from translator.translate import translate

class TestTranslate(unittest.TestCase):
    def test_translation(self):
        text = "Hello, how are you?"
        src_lang = 'en'
        tgt_lang = 'fr'
        result = translate(text, src_lang, tgt_lang)
        self.assertEqual(result, "Bonjour, comment ça va?")

if __name__ == "__main__":
    unittest.main()
