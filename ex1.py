#!/usr/bin/env python3

def main():
    # First we grab an input from the user, validate their input and determine how many words they want to input
    amount_of_words_str = input()
    if not amount_of_words_str.isdigit():
        print("The first input must be an integer and must be the amount of words you want to enter")
        return
    amount_of_words = int(amount_of_words_str)

    if not 1 <= amount_of_words <= 10 ** 5:
        print("The first input must be between 1 and 10^5")
        return

    # Next we create a buffer to store the words the under will enter, and let the user enter them and validate them
    word_buffer = []
    for _ in range(amount_of_words):
        tmp_input = input()

        if not (tmp_input.islower() and tmp_input.isalpha()):
            print("All the words must be composed of lowercase English letters only")
            return

        word_buffer.append(tmp_input)

    # Then we check the sum of the lengths of all the words and validate it
    sum_of_all_letters = 0
    for word in word_buffer:
        sum_of_all_letters += len(word)

    if sum_of_all_letters > 10 ** 6:
        print("The sum of the lengths of all the words must not exceed 10^6")
        return

    # Compute number of occurrences for each distinct word
    word_dict_buffer = {}
    for word in word_buffer:
        if word not in word_dict_buffer:
            word_dict_buffer[word] = 1
        else:
            word_dict_buffer[word] += 1

    # Compute amount of distinct words
    print(len(word_dict_buffer))

    # Print number of occurrences for each distinct word as required by the exercise
    string_ints = [str(one_int) for one_int in word_dict_buffer.values()]
    print(" ".join(string_ints))


if __name__ == '__main__':
    main()
