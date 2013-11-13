# -*- coding: utf-8 -*-
#!/usr/bin/python

import csv
import trie
import json
import cPickle as pickle
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
      self.trie_data = trie.TrieNode()
      
      words = self.loadCSV(csv)
      print "Number of words loaded from csv: ", len(words)
      
      # have to start counter at 1 cause of None evaluating to <= 0
      counter = 1
      
      for word in words:
        self.trie_data.add(word,counter)
        counter += 1
        self.num_words += 1
      
      return self.trie_data
      
    def serialize_dictionary(self,dictionary_name):
      pickle.dump(self.trie_data,open(dictionary_name,"wb"))
      
    def deserialize_dictionary(self,file_path):
      self.trie_data = pickle.load(open(file_path,"rb"))
    
"""
Some tests of the PyTrie Object. This will be removed from this script and moved into their own unit tests.
"""

loader = PyTrie()
words = loader.generateTrie("MostFrequent1000.csv")
print words.lookup("is")
print "Number of words in trie", words.num_words()
words.add("bobby",words.num_words()+1)
print words.lookup("bobby")
print words.num_words()
print words.remove("bobby")
print words.num_words()
print "trying to find bobby...", words.lookup("bobby")
print "Pickling data..." , loader.serialize_dictionary("1000CommonWords.p")
      
