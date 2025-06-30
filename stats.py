def get_num_words(text):
    split_text = text.split()
    word_count = len(split_text)
    return word_count

def get_num_char_sym(text):
    lower_case_text = text.lower()
    char_count = {}
    for char in lower_case_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_dict(char_count):
    char_count.sort()
