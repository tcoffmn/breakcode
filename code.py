# Print a list of valid English words from the permutations of 4 position lock
import sys
import itertools

dial1 = ['M', 'S', 'D', 'R', 'H', 'T', 'F', 'B', 'L', 'P']
dial2 = ['Y', 'N', 'U', 'A', 'I', 'O', 'L', 'E', 'H', 'R']
dial3 = ['O', 'A', 'T', 'E', 'L', 'N', 'I', 'R', 'S', 'K']
dial4 = ['S', 'K', 'A', 'N', 'T', 'E', 'P', 'Y', 'L', 'D']

lock = [dial1, dial2, dial3, dial4]

with open("english_lowercase.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)


def is_english_word(word):
    return word.lower() in english_words


def print_words():
    counter = 0
    for letters in list(itertools.product(*lock)):
        code = ''
        for elem in letters:
            code = code + elem
        if is_english_word(code):
            print(code)
            counter = counter + 1

    print('Total words:' + str(counter))

# for tup in it.permutations([combo1, combo2, combo3, combo4], 4):
#     w, x, y, z = tup
#     st = str(w) + str(x) + str(y) + str(z)
#     if is_english_word(st):
#          print(st)


if __name__ == '__main__':
        print_words()
        sys.exit(0)
