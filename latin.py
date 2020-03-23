def pig_latin(text):
  say = " "
  list1=[]
  # Separate the text into words
  words = text.split()
  #print(words)
  for word in words:
      word1=list(word)
      word2=word[1:]+word[0]+'ay'
      list1.append(word2)
      #list1.append(word)
      #print (list1)
  #print(list1)

  return say.join(list1)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"