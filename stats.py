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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

