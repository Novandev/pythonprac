'''
A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
'''
# to get the loop to work check the current word being checked and see if it matches the previous word, if it does then skip it
source_text= "one fish two fish red fish blue fish".split(" ")

def histogram(source_text):
    tokens = []
    #listo = []
    #for i in range(len(source_text)):
        #listo.append(sum(x == source_text[i] for x in source_text))
    #print(listo)
    print(source_text[0])
    '''
    for i in listo:
         if i not in tokens:
             tokens.append(i)
    print(tokens)
#for word in source_text:
'''
histogram(source_text)
'''
A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
'''

'''
A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
'''
