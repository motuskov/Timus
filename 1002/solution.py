import sys
import queue

letter_digit = {
    'i': '1', 'j': '1',
    'a': '2', 'b': '2', 'c': '2',
    'd': '3', 'e': '3', 'f': '3',
    'g': '4', 'h': '4',
    'k': '5', 'l': '5',
    'm': '6', 'n': '6',
    'p': '7', 'r': '7', 's': '7',
    't': '8', 'u': '8', 'v': '8',
    'w': '9', 'x': '9', 'y': '9',
    'o': '0', 'q': '0', 'z': '0'
}

tokens = list(reversed(sys.stdin.read().split()))

while True:
    # Getting the phone number
    phone_number = tokens.pop()
    if phone_number == '-1':
        break

    # Getting the word count
    word_count = int(tokens.pop())
    if word_count == 0:
        print('No solution.')
        continue

    # Initializing the status of searching process and calculating phone number length
    found = False
    phone_number_length = len(phone_number)

    # Getting the words, sorting them by categories and creating queue for processing them
    seen_numbers = set()
    seen_positions = set()
    word_categories = {}
    sentences = queue.Queue()
    for word in tokens[-word_count:]:
        number = ''.join([letter_digit[letter] for letter in word])
        if number in seen_numbers:
            continue
        number_length = len(number)
        position = 0
        while True:
            position = phone_number.find(number, position)
            if position == -1:
                break
            next_position = position + number_length
            is_last_word = phone_number_length == next_position
            seen_numbers.add(number)
            try:
                word_categories[position].append((
                    number,
                    word,
                    is_last_word,
                    next_position
                ))
            except KeyError:
                word_categories[position] = [(number, word, is_last_word, next_position)]
            if position == 0:
                new_sentence = [word_categories[position][-1]]
                sentences.put(new_sentence)
                seen_positions.add(next_position)
                if number_length == phone_number_length:
                    found = True
                    break
            position += 1
    del tokens[-word_count:]

    # Looking for a shortest sentence
    while not found:
        try:
            sentence = sentences.get(False)
        except queue.Empty:
            break
        for numb_word in word_categories.get(sentence[-1][3], []):
            if numb_word[3] in seen_positions:
                continue
            new_sentence = sentence + [numb_word]
            sentences.put(new_sentence)
            seen_positions.add(numb_word[3])
            if numb_word[2]:
                found = True
                break

    # Outputting the result
    if found:
        print(' '.join([numb_word[1] for numb_word in new_sentence]))
    else:
        print('No solution.')
