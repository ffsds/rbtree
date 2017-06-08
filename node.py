#!/usr/bin/python3
# Red Black Tree Python Implementation
# Felipe S. Dantas Silva <felipedantas@gmail.com>

class Node(object):
  def __init__(self, key, color="RED"):
    self.color = color
    self.key = key
    self.left = None
    self.right = None
    self.p = None

  def getColor(self):
    return self.color

  def setColor(self, color):
    self.color = color
