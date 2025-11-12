import sys
from stats import get_num_words, count_characters, get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count ----------')
    print('Found ' + str(get_num_words(book_text)) + ' total words')
    print('--------- Character Count -------')
    char_count = count_characters(book_text)
    sorted_char_count = get_sorted_list(char_count)
    for dictionary in sorted_char_count:
        if dictionary["char"].isalpha():
            print(f'{dictionary["char"]}: {dictionary["num"]}')
    print('============= END ===============')

main()