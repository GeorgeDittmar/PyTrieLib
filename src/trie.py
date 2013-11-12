# -*- coding: utf-8 -*-
#!/usr/bin/python
from collections import defaultdict

class TrieNode:
  def __init__(self):
    self.root = defaultdict(TrieNode)
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
      new_node.numWords += 1
      
      return
    self.root[head].add(rest,value)
  
  # remove a word from the trie by just setting the nodes value to NONE.  
  def remove(self,word):
    head,rest = word[0],word[1:]
    curr = self.root[head]
    
    if rest:
      return curr.remove(rest)
    
    if curr.value:
      curr.value = None
      curr.numWords -= 1
      return True
    return False
     
  def lookup(self,word):
    # look up first char in dict
    
    head,rest = word[0],word[1:]
    curr = self.root[head]

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

  def num_words(self):
    count = self.numWords
    for key in self.root:
      count = count + self.root[key].num_words()
    return count

