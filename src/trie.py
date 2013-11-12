# -*- coding: utf-8 -*-
#!/usr/bin/python
from collections import defaultdict

class TrieNode:
  def __init__(self):
    self.root = defaultdict(PyTrie)
    self.letter = None
    self.value = None
    self.numWords = 0
  
  """
      Add word and set it to the given value.
  """
  def add(self,word,value):
    # strip off the first char in the word and add it to root.
    head,rest = word[0],word[1:]
    
    new_node = self.root[head]
    new_node.letter =  head
    
    #if rest is used up should be None
    if not rest:
      new_node.value = value
      return
    self.root[head].add(rest,value)
    
  def remove(self,word):
    pass
     
  def lookup(self,word):
    # look up first char in dict
    
    head,rest = word[0],word[1:]
    curr = self.root[head]
    print curr.letter, curr.value
    if rest:
      
      return curr.lookup(rest)
    
    return curr.value or None
    
  def prefix(self,pre):
    #if pre has been exhausted true!
    if not pre:
      return True;  
      
    head, rest = pre[0], pre[1:]
    # Since root is a dictionary can just look and see if head exists
    if head not in self.root:
      return False
    node = self.root[head]  
    node.prefix(rest)
  
  # perform a depth-first search 
  def wordCount(self, level):
    count = 0
    
    for key in self.root:

      if self.root[key].value:
        count += 1 + self.root[key].wordCount(level+1)
      else:
        count += 0 + self.root[key].wordCount(level+1)
       
    return count
    

