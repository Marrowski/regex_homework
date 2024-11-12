import re

def analyse_text(text: str):
    pattern = re.findall(r'\b\w+\b', text)
    num_words = len(pattern)
    return set(pattern), num_words

print(analyse_text('Oleh Ivan Petro Danylo Alex Olexander, Oleh'))
