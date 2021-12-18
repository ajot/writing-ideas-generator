import sys
import ideas #import the ideas database file. Feel free to edit this to your taste to add or remove template phrases.
sys.stdout = open('output.txt', 'w') #prints the output to the file specified here

# Words you want to replace the placeholder text in the ideas database with
keywords = ["Lego","Python"]

spark_ideas = [] #create an empty list that will store the ideas once the placeholder has been replaced with the keywords above.
for idea in ideas.ideas:
  for word in keywords:
    spark_string = idea.replace("[placeholder]",word) #replace the text - [placeholder] with the keyword
    spark_ideas.append(spark_string) #add the idea to the list

print(spark_ideas)

sys.stdout.close() #prints the output to the file specified above