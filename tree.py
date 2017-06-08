#!/usr/bin/python3
# Red Black Tree Python Implementation
# Felipe S. Dantas Silva <felipedantas@gmail.com>

import sys
import node

class Tree(object):
  def __init__(self):
    self.root = None
    self.NIL = None

  def RB_getHeight(self, x):
    height = 0
    while x.left != self.NIL:
        x = x.left
        if x.getColor() == "BLACK":
            height += 1
    height += 1
    return height

  def RB_Transplant(self, u, v):
    if u.p == self.NIL:
        self.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != self.NIL:
        v.p = u.p

  def RBDelete_Fixup(self, x):
    while x != self.root and x.getColor() == "BLACK":
        if x == x.p.left:
            w = x.p.right
            if w.getColor() == "RED":
                w.setColor("BLACK")
                x.p.setColor("RED")
                self.Left_Rotate(self, x.p)
                w = x.p.right
            if w.left.getColor() == "BLACK" and w.right.getColor() == "BLACK":
                w.setColor("RED")
                x = x.p
            elif w.right.getColor() == "BLACK":
                w.left.setColor("BLACK")
                w.setColor("RED")
                self.Right_Rotate(self, w)
                w = x.p.right
            w.color = x.p.color
            x.p.setColor("BLACK")
            w.right.setColor("BLACK")
            self.Left_Rotate(self, x.p)
            x = self.root
        else:
            w = x.p.left
            if w.getColor() == "RED":
                w.setColor("BLACK")
                x.p.setColor("RED")
                self.Right_Rotate(self, x.p)
                w = x.p.left
            if w.right.getColor() == "BLACK" and w.left.getColor() == "BLACK":
                w.setColor("RED")
                x = x.p
            elif w.left.getColor() == "BLACK":
                w.right.setColor("BLACK")
                w.setColor("RED")
                self.Left_Rotate(self, w)
                w = x.p.left
            w.setColor(x.p.getColor)
            x.p.setColor("BLACK")
            w.left.setColor("BLACK")
            self.Right_Rotate(self, x.p)
            x = self.root
    x.setColor("BLACK")

  def RBDelete(self, z):
    y = z
    y_original_color = y.getColor()
    if z.left == self.NIL:
        x = z.right
        self.RB_Transplant(z, z.right)
    elif z.right == self.NIL:
        x = z.left
        self.RB_Transplant(z, z.left)
    else:
        y = self.Tree_Minimum(z.right)
        y_original_color = y.getColor()
        x = y.right
        if y.p == z and x != self.NIL:
            x.p = y
        else:
            self.RB_Transplant(y, y.right)
            if z.right != self.NIL:
                y.right = z.right
                y.right.p = y
        self.RB_Transplant(z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if y_original_color == "BLACK":
        self.RBDelete_Fixup(x)

  def Left_Rotate(self, x):
      y = x.right
      x.right = y.left
      if y.left != self.NIL:
          y.left.p = x
      y.p = x.p
      if x.p == self.NIL:
        self.root = y
      elif x == x.p.left:
          x.p.left = y
      else:
          x.p.right = y
      y.left = x
      x.p = y

  def Right_Rotate(self, x):
    y = x.left
    x.left = y.right
    if y.right != self.NIL:
        y.right.p = x
    y.p = x.p
    if x.p == self.NIL:
      self.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y

  def RBInsert_Fixup(self, z):
    while z != self.root and z.p.color == "RED":
      if z.p == z.p.p.left:
        y = z.p.p.right
        if y != self.NIL and y.color == "RED":
          z.p.setColor("BLACK")
          y.setColor("BLACK")
          z.p.p.setColor("RED")
          z = z.p.p
        else:
          if z == z.p.right:
            z = z.p
            self.Left_Rotate(z)
          z.p.setColor("BLACK")
          z.p.p.setColor("RED")
          self.Right_Rotate(z.p.p)
      else:
            y = z.p.p.left
            if y and y.color == "RED":
              z.p.setColor("BLACK")
              y.setColor("BLACK")
              z.p.p.setColor("RED")
              z = z.p.p
            else:
              if z == z.p.left:
                z = z.p
                self.Right_Rotate(z)
              z.p.setColor("BLACK")
              z.p.p.setColor("RED")
              self.Left_Rotate(z.p.p)
    self.root.setColor("BLACK")

  def RBInsert(self, z):
    y = self.NIL
    x = self.root
    while x != self.NIL:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    z.p = y
    if y == self.NIL:
      self.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = self.NIL
    z.right = self.NIL
    z.setColor("RED")
    self.RBInsert_Fixup(z)

  def RBPrint(self):
    self.Inorder_Tree_Walk(self.root)

  def NilNode(self, x):
      return ('NIL' if x == None else x)

  def RBCheck(self, x):      # Preorder traversal: Root-Left-Right
    if x != self.NIL:
        print("(" + self.NilNode(self.getKey(x.p)), self.NilNode(x.key), x.getColor(), self.RB_getHeight(x), self.NilNode(self.getKey(x.left)), self.NilNode(self.getKey(x.right)) + ")")
        self.RBCheck(x.left)
        self.RBCheck(x.right)

  def getKey(self, node):
    if node != self.NIL:
      return node.key
    else:
      return None

  def RBElement_Search(self, x, k):
      while x != self.NIL and k != x.key:
          if k < x.key:
              x = x.left
          else:
              x = x.right
      return x

  def Inorder_Tree_Walk(self, x=None):
        if x != self.NIL:
            self.Inorder_Tree_Walk(x.left)
            print(x.key, end=' ')
            self.Inorder_Tree_Walk(x.right)

  def Tree_Minimum(self, x = None):
    if x == self.NIL:
        x = self.root
    while x.left != self.NIL:
      x = x.left
    return x

  def getRoot(self):
    return self.root
