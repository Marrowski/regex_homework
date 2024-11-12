import re


def last_words(request: str):
    pattern = r'\b\w{3,}\b'
    matches = re.findall(pattern, request)

    last_three_letters = [word[-3:] for word in matches]
    return last_three_letters

print(last_words(input('Enter a word:')))