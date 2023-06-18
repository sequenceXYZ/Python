"""
Write a program that counts the number of words in a sentence.
"""
"""
Create a new file called word_count.py. 
In the file, define a function called count_words. 
The function should take one argument (the sentence to count words in) 
and return the number of words in the sentence. 
In the main part of the program, prompt the user to enter a sentence and call the count_words function. 
Print the number of words to the console.
"""


def count_words():
    print("Words counted in the text =", len(sentence.split()))
    return


sentence = (str(input('Please, enter some text here for word counting: ')))

count_words()
