import math

ari_scale = {

    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},

    2: {'ages': '6-7', 'grade_level': '1st Grade'},

    3: {'ages': '7-8', 'grade_level': '2nd Grade'},

    4: {'ages': '8-9', 'grade_level': '3rd Grade'},

    5: {'ages': '9-10', 'grade_level': '4th Grade'},

    6: {'ages': '10-11', 'grade_level': '5th Grade'},

    7: {'ages': '11-12', 'grade_level': '6th Grade'},

    8: {'ages': '12-13', 'grade_level': '7th Grade'},

    9: {'ages': '13-14', 'grade_level': '8th Grade'},

    10: {'ages': '14-15', 'grade_level': '9th Grade'},

    11: {'ages': '15-16', 'grade_level': '10th Grade'},

    12: {'ages': '16-17', 'grade_level': '11th Grade'},

    13: {'ages': '17-18', 'grade_level': '12th Grade'},

    14: {'ages': '18-22', 'grade_level': 'College'}

}


def count_words(file):
    num_words = 0

    for word in file.read().split():
        num_words += 1

    return num_words


def count_characters(file):
    file.seek(0)

    number_chars = 0

    blanks = 0

    for line in file:

        number_chars += len(line)

        for char in line:

            if char == ' ' or char == '\n':
                blanks += 1

    return number_chars - blanks


def count_sentences(file):
    file.seek(0)

    count = 0

    for line in file:

        for c in line:

            if c == '.' or c == '!' or c == '?':
                count += 1

    return count


def open_file(text):
    return open(text, 'r', encoding="utf-8-sig")

    # print(type(text))


def calculate_ari(x, y, z):
    return 4.71 * x / y + 0.5 * y / z - 21.43


def longest_words():
    """Returns a list of the 10 longest words"""
    return 0


def shortest_words():
    """Returns a list of the 10 shortest non article words"""
    return 0


def unique_word_count():
    """Counts the number of unique words in bookx returns integer count"""
    return 0


def rarest_words():
    """Returns list of top 10 rarest words"""
    for i in range(0,10):
         # do stuff
    return 0


def word_frequency(a_word):
    """Returns count of user input word."""


def average_length_sentence(): # feels bad man
    """Returns the average length in words and characters, maybe."""


def minimum_sentence_length():
    """minimum sentence length returns it does."""


def max_sentence_length():
    """Returns maximum sentence length, yah wind bag."""


def mimic():
    """TBD"""


def count_syllables():
    """"Returns total number of syllables in book."""


def lexical_density():
    """Returns lexical density."""