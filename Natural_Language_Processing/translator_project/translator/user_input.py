def get_user_input():
    text = input("Enter the text to be translated: ")
    src_lang = input("Enter the source language code (e.g., 'en' for English): ")
    tgt_lang = input("Enter the target language code (e.g., 'fr' for French): ")
    return text, src_lang, tgt_lang