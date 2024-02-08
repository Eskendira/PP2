"""Write a function that accepts string from user,
 return a sentence with the words reversed.
 We are ready -> ready are We"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

input_sentence = input('enter sentence:')
output_sentence = reverse_sentence(input_sentence)
print(output_sentence)


