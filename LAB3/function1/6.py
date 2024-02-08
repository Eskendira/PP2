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


"""We define a function called reverse_sentence that takes a single parameter sentence, which represents the input string.

Inside the function, we use the split() method to split the sentence into a list of words. By default, split() splits the string at whitespace characters.

Next, we use slicing with the [::-1] notation to reverse the order of the words in the list. This notation creates a new list that starts from the last element and goes backwards with a step of -1.

After reversing the words, we use the join() method to concatenate the words back into a single string, using a space as the separator.

Finally, we return the reversed sentence as the output of the function."""