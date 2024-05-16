def function(word):
    for i in word:
        if word.find(i) % 2 == 0:
            return word.upper()
        else:
            return word.capitalize()
  
print(function("rati"))