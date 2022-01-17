# Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Using dictionaries.
string = 'mississippi!'


def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def most_frequent(string):
    letters = [letter.lower() for letter in string if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter, count)

most_frequent(string)
