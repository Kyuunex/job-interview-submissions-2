#!/usr/bin/env python3


def bigger_Is_greater(w):
    l = list(w)

    i = len(l) - 1
    while i > 0 and l[i - 1] >= l[i]:
        i -= 1

    if i <= 0:
        return "no answer"

    j = len(l) - 1
    while l[j] <= l[i - 1]:
        j -= 1

    l[i - 1], l[j] = l[j], l[i - 1]

    l[i:] = l[len(l) - 1:i - 1:-1]

    return "".join(l)


def main():
    amount_of_words_str = input()
    if not amount_of_words_str.isdigit():
        print("The first input must be an integer and must be the amount of words you want to enter")
        return
    amount_of_words = int(amount_of_words_str)

    if not 1 <= amount_of_words <= 10 ** 5:
        print("The first input must be between 1 and 10^5")
        return

    word_buffer = []
    for _ in range(amount_of_words):
        tmp_input = input()

        if not 1 <= len(tmp_input) <= 100:
            print("Each word length must be in the bounds of 1 and 100")
            return

        if not tmp_input.isascii():
            print("All the words must be composed of ASCII characters")
            return

        word_buffer.append(tmp_input)

    for word in word_buffer:
        print(bigger_Is_greater(word))


if __name__ == '__main__':
    main()
