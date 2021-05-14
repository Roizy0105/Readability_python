import cs50

# promt user for input
text = cs50.get_string("enter text: ")

# initialize the counter varuables
letter = 0
# word will be one cause there is no space befor the sentence
word = 1 
sentence = 0

# itarate throught the sentence and add a one to letter each time we land on a ltter
for i in range(len(text)):
    if text[i].isalnum() == True:
        letter += 1
    # add to word each time we land on a space    
    elif text[i] == " ":
        word += 1
    # add to sentence each time we land on a punctuation    
    elif text[i] == (".") or text[i] == ("!") or text[i] == ("?"):
        sentence += 1
        
# use a formula to colculate the grade level based on the amount of words letters and sentences        
l = float(letter) / float(word) * 100   
s = float(sentence) / float(word) * 100
index = 0.0588 * l - 0.296 * s - 15.8
grade = round(index)


# print the appropriate grade level
if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print("Grade " + str(grade))