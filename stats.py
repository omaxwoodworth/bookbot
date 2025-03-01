def get_num_words(string):
    word_list = string.split()
    return len(word_list)

def get_characters(string):
    lower_string = string.lower()
    dictionary = {}
    for character in lower_string:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary

def get_sorted_list(dictionary):
    list_of_dictionaries = []
    for k in dictionary:
        value = dictionary[k]
        new_dictionary = dict(character = k, count = value)
        list_of_dictionaries.append(new_dictionary)
    list_of_dictionaries.sort(reverse=True, key=lambda x: x["count"])
    return list_of_dictionaries