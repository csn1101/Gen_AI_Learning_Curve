from translator.model_loader import load_model_and_tokenizer
import torch

def translate(text, src_lang, tgt_lang):
    model, tokenizer = load_model_and_tokenizer(src_lang, tgt_lang)
    
    # Tokenize the input text
    tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
    
    # Perform the translation
    with torch.no_grad():
        translation_tokens = model.generate(**tokenized_text)
    
    # Decode the translation
    translated_text = tokenizer.batch_decode(translation_tokens, skip_special_tokens=True)
    
    return translated_text[0]

