#!/usr/bin/python3
# Red Black Tree Python Implementation
# Felipe S. Dantas Silva <felipedantas@gmail.com>

import argparse
import os
import sys
import node, tree

if __name__ == "__main__":
#  os.system('clear')
  parser = argparse.ArgumentParser(description='Red Black Tree Demonstration: use a two column file dictionary as the program input. The first column must contain the key to insert\
  and the second column must contain the action (1 to insert and 0 to remove).')
  parser.add_argument("-f", metavar='file', type=str, default=30, help='Input file name (e.g. -f dictionary.txt)', required=True)
  args = parser.parse_args()

  rb = tree.Tree()

  def inputFile():
    f = open(sys.argv[2], 'r')
    for line in iter(f):
        word = line[:-2].replace(' ','')
        if line[-2] == '1':
            if not rb.RBElement_Search(rb.getRoot(), word):
                rb.RBInsert(node.Node(word))
            else:
                print("\nA árvore já possui uma palavra " + word)
        else:
            if (rb.RBElement_Search(rb.getRoot(), word)) == None:
                print("A palavra " + word + " foi removida anteriormente ou não foi inserida\n")
            else:
                print("Removendo a palavra " + word)
                rb.RBDelete(rb.RBElement_Search(rb.getRoot(), word))
                rb.RBPrint()
                print()
                rb.RBCheck(rb.getRoot())
    f.close()

  inputFile()
  print("\n######### RBPrint #########")
  rb.RBPrint()
  print("\n\n######### RBCheck #########")
  rb.RBCheck(rb.getRoot())
