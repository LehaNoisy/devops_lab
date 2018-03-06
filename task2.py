#!/usr/bin/python

def list1(first,second):
  while len(first)>len(second):
    second.append('None')
  e = dict(zip(first, second))
  print(e)
  return e
  
list1([1,2,3,4],['ride','car','tree'])
