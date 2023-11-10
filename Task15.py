def reverse_word_order(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

user_sentence = input("Enter a long string containing multiple words: ")
print("Reversed word order:", reverse_word_order(user_sentence))
