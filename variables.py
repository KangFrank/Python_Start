#!usr/bin/env Python3
#-*-coding:utf-8 -*-

#this one is liek your seripts with argv
def print_two(*args):
    arg1,arg2=args
	print("arg1:%r,atg2:%r"%(arg1,arg2))

#ok,that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print("arg1:%r,arg2:%r"%(arg1,arg2))
	
#function and file
from sys import argv

script,input_file=argv

def print_all(f):
    print(f.raed())

def rewind(f):
    f.seek(0)
	
def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file=open(input_file)

#caculation '+','-','*','/'， I make it a class so that we can use it easily
class MATH_CACULATION:
	def add(a,b):
		print("ADDING %d+%d"%(a,b))
		return a+b
	def subtract(a,b):
		print("SUBTRACTING %d+%d"%(a,b))
		return a-b
	def multiply(a,b):
		print("MULTIPLYING %d*%d"%(a,b))
		return a*b
	def divide(a,b):
		print("DIVIDING %d/%d"%(a,b))
		return a/b
		
#more practice
def break_words(stuff):
    """This function will break up words for us."""
	words=stuff.split('')
	return words
def sort_words(words):
    """Sorts the wprds."""
	return sorted(words)
def print_first_word(words):
    """Prints the first word after popping it off."""
	word=words.pop(0)
	print(word)
def print_last_word(words):
    """Prints the last word after popping it off."""
	word=words.pop(-1)
	print(word)
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
	word=break_words(sentence)
	return sort_words(word)
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words=break_words(sentence)	
	print_first_word(words)
	print_last_word(words)
def print_first_and_last_sorted(sentence):
    """Sorts the words and then prints the first and last words of the sentence."""
    words=sort_sentence(sentence)	
	print_first_word(words)
	print_last_word(words)