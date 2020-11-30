#!/usr/bin/env python


'''
A python implementation of the tausworthe generator (TG)

Tausworthe Generator (TG) is a kind of multiplicative recursive generator
which produces random bits

An introduction to TG:
https://homes.luddy.indiana.edu/kapadia/project2/node9.html

TG belongs to LFSRs (linear feedback shift registers).
'''


import numpy as np
from typing import Tuple


__author__ = "Jingquan Wang"
__email__ = "jq.wang1214@gmail.com"


class TG(object):
	def __init__(self, shape: Tuple[int], r: int=3, q: int=5, l: int=4) -> None:
		"""
		Parameters
	    ----------
	    shape : Tuple[int]
	        shape of generated PRN array
	    r : int
	       	as defined in 
	       	B[i] = (B[i−r] +B[i−q]) mod 2 = B[i−r] XOR B[i−q] (0 < r < q)
	    q : int
	        as defined in 
	       	B[i] = (B[i−r] +B[i−q]) mod 2 = B[i−r] XOR B[i−q] (0 < r < q)
	    l : int
	        lengths of bits in base 2
	        Use (l-bits in base 2)/2^l and convert to base 10
		"""
		
		self.r = r
		self.q = q
		self.l = l

		# length is the number of bits we need
		self.length = np.prod(shape) * self.l

		# initialize the array B
		self.B = np.ones(self.length)

		# extend array B
		for i in range(q, self.length):
			new_bit = 1 if self.B[i - self.r] != self.B[i - self.q] else 0
			self.B.append(new_bit)

		self.B = np.split(self.B, self.l)
		self.decimal = self.convert(self.B)


	def get_bits(self) -> numpy.ndarray:
		"""
		Return
		----------
		B_copy (np.ndarray): 

		"""
		B_copy = self.B
		return B_copy


	def convert(self, array: numpy.ndarray) -> numpy.ndarray:
















