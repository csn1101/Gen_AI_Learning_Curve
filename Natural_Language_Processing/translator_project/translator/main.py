from translator.user_input import get_user_input
from translator.translate import translate

def main():
    text, src_lang, tgt_lang = get_user_input()
    translated_text = translate(text, src_lang, tgt_lang)
    print(f"Translated Text: {translated_text}")

if __name__ == "__main__":
    main()
