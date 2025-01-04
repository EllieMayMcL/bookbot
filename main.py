def main():
    book_path = "books/frankenstein.txt"
    book_text = get_file_contents(book_path)
    words = num_words(book_text)
    char_count = count_letters(book_text)
    new_list = convert_dict(char_count)
    sorted_list = sort_on(new_list)
    return report(book_path, words, sorted_list)


def get_file_contents(path):
    with open(path) as f:
        return f.read()
    
def num_words(text):
    word_count = len(text.split())
    return word_count
 
def count_letters(text):
    count_dict = {}
    for c in text:
        if c.isalpha():
            low_c = c.lower()
            if low_c in count_dict:
                count_dict[low_c] += 1
            else:
                count_dict[low_c] = 1
    return count_dict

def convert_dict(dict_name):
    to_list = []
    for key, value in dict_name.items():
        new_dict = {"char" : key, "count": value}    
        to_list.append(new_dict)
    return to_list

def sort_on(list_name): 
    list_name.sort(key=lambda x: x["count"], reverse=True)
    return list_name


def report(path, num_words, sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} found in the document")
    print(" ")
    for item in sorted_list:
        letter = item["char"]
        count = item["count"]
        print(f"The '{letter}' character was found {count} times")


main()


