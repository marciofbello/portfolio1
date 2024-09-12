from code import morse_dictionary

# Morse code project


#Gets the word/expression from user
word = input ("Please enter the desired expression to bem morse encoded : ")

#puts the word in uppercase
word_uppercase = word.upper()
print(word_uppercase)
# converts to morse code comparing to a dictionary.
coded_word = []

for digit in word_uppercase:
    coded_digit = morse_dictionary[digit]
    coded_word.append(coded_digit)

#print to user
print(f"The morse code for your expression is: \n {coded_word} ")