# -*- coding: utf-8 -*-
#!/usr/bin/python

import csv
import trie

"""
This is a utility class to take large csv word dictionaries and 
"""
class PyTrieLoader:
    
    def __init__(self):
      self.trie_data = None
    
    #reads in a csv file and returns a list of words.  
    def loadCSV(self,csvFile):
      words = list()
      
      reader = csv.reader(open(csvFile,'rb'))
      for row in reader:
        words.append(row[0])
        
      return words
    
    #given a csv file, load the csv and return a new trie populated with the words in the csv.  
    def generateTrie(self,csv):
      dictionary = trie.PyTrie()
      words = self.loadCSV(csv)
      # have to start counter at 1 cause of None evaluating to <= 0
      counter = 1
      
      for word in words:
        
        dictionary.add(word,counter)
        counter += 1
       
      return dictionary
      
    
    
      
loader = PyTrieLoader()
words = loader.generateTrie("MostFrequent1000.csv")
print words.lookup("the")
print words.wordCount()

      
