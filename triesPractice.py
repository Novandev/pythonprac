

class Trie(object):
    def __init__(self):
        self.head = {}
                # this represents the starting point for searching, adding, or removing words or sentences,
                # it store a reference to the starting letter to track down ( in later methods like add or search)
                # each letter that is seen will hold a dictionary of letters that reference other letters,
                # based on the add _method has added to the dictionary,



    def add(self, word):
        """
        This add function takes pythons iterating over a list of keys as the for loop that it checks for each letter in the word trees dictionary
        For out first example, let's add the word "add" to the Trie

        First we define a variable curr
          # example if I've only added the words "add", addiction" and "apple","apply" the resulting dictioanry would look like

                    # "a" : {
    #                           "d": {
    #                                   "d": {
    #                                           "i": {
    #                                                     "c": {
    #                                                          "t": {
    #                                                                   "i" : {
    #                                                                           "o": {
    #
    #                                                                                   "n": {


                                                                                            }
    #
    #
    #                                                                                   },
    #
    #
    #                                                                   },
    #                                                          },
    #
    #
    #                                           },
    #
    #
    #                                       }
    #
    #                                   },

    #                           "p": {
    #
    #                           }
    #                        }

    we know that ever time we find and empty dictionary that the word has ended.

     if theres still more letters in the  word that were searching for we know its not in the dictionary. will be in the search


        :param word: A string that we want to add its letter references to the current tree
        :return: Nothing, but modifies self. head with new dictonary entries
        """

        curr = self.head

        for ch in word: #For every character in the word that we are trying adding to the dictionary
            if ch not in curr: #Iterate over the list of keys in self.head/ the current dictionary were on and if the character isnt in the keys
                curr[ch] = {}   # we add it as another  dictionary
                print(curr)  # Check to see the current dictionary were on and what keys it has
            curr = curr[ch]  #  Either way check for the next iteration of the for loop it wil now reference


if __name__ == "__main__":
