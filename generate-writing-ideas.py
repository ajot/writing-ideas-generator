import sys
import headlines #import the ideas database file. Feel free to edit this to your taste to add or remove template phrases.
sys.stdout = open('output.txt', 'w') #prints the output to the file specified here

# Words you want to replace the placeholder text in the ideas database with
keywords = ["Lego","Python"]

ideas = [] #create an empty list that will store the ideas once the placeholder has been replaced with the keywords above.
for headline in headlines.text:
  for word in keywords:
    headline = headline.replace("[placeholder]",word) #replace the text - [placeholder] with the keyword
    ideas.append(headline) #add the idea to the list

print(ideas)

sys.stdout.close() #prints the output to the file specified above