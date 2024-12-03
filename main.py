def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    chars_dict = lettercount(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End of report ---")


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def wordcount(text):
    words = text.split()
    return len(words)

def lettercount(text):
    count = {}
    lowercase = text.lower()
    for letter in lowercase:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count
main()