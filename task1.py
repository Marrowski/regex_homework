import re
from collections import Counter


def word_func(text: str):
    result = re.split(r' ', text)
    result_a = re.search(r'Valentyn', text)
    words = re.findall(r'\w+', text)
    cnt = Counter(words).most_common()
    return cnt

print(word_func('Ivan Dmytro Danylo Petro Valentyn Oleh Dmytro Oleh Valentyn Valentyn'))

