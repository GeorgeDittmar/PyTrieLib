# -*- coding: utf-8 -*-
#!/usr/bin/python

import csv
import trie

"""
This is a utility class to take large csv word dictionaries and create a trie from it. 
"""
class PyTrie:
    
    def __init__(self):
      # init an empty trie with this object
      self.trie_data = trie.TrieNode()
      self.num_words = 0
    
    #reads in a csv file and returns a list of words.  
    def loadCSV(self,csvFile):
      words = list()
      
      reader = csv.reader(open(csvFile,'rb'))
      for row in reader:
        words.append(row[0])
        
      return words
    
    #given a csv file, load the csv and return a new trie populated with the words in the csv.  
    def generateTrie(self,csv):
      dictionary = trie.TrieNode()
      
      words = self.loadCSV(csv)
      print "Number of words loaded from csv: ", len(words)
      
      # have to start counter at 1 cause of None evaluating to <= 0
      counter = 1
      
      for word in words:
        dictionary.add(word,counter)
        counter += 1
        
        self.num_words += 1

      return dictionary
      
    def size(self):
      return self.num_words
    
      
loader = PyTrie()
words = loader.generateTrie("MostFrequent1000.csv")
print words.lookup("is")
print "Number of words in trie", words.num_words()
words.add("bobby",words.num_words()+1)
print words.lookup("bobby")
print words.num_words()

      
