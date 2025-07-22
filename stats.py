def words_count(text):
     return len(text.split())


def char_count(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1
            
    char_list = list(char_dict.items())  # convert to list of tuples
    char_list.sort(key=lambda item: item[1], reverse=True)
    return char_list