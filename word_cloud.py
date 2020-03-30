'''This program counts the number of occurances in a string.
it ignores puntuations, words with numbers'''

file_contents = "I am Ajay Kumar9 kommaraju with Dollors$$ and Pounds### and lot of Gold 124 ajay dollar kommaraju" 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
for punctuation in punctuations:
    if punctuation in file_contents:
        file_contents=file_contents.replace(punctuation,"")
print(file_contents)
word_count={}
file_contents=file_contents.lower()
print(file_contents)

for word in file_contents.split(" "):
    if word not in uninteresting_words and word.isalpha():
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] =1
print(word_count)
        
