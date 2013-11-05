# -*- coding: utf-8 -*-
#!/usr/bin/python
from collections import defaultdict

class PyTrie:
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
    print new_node.letter
    #if rest is used up should be None
    if not rest:
      new_node.value = value
      self.numWords += 1
      return
    self.root[head].add(rest,value)
    
  def remove(self,word):
    pass
     
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
    
  def size(self)
    pass

