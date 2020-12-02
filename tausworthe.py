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
	def __init__(self, shape: Tuple[int]) -> None:
		"""
		Parameters
	    ----------
	    shape : Tuple[int]
	        shape of generated PRN array
		"""
		self.r = self.q = self.l = 0
		self.shape = shape


	def get_bits(self) -> numpy.ndarray:
		"""
		Get raw bits 

		"""
		return self.B


	def seed(self, r: int=3, q: int=5, l: int=4):
		"""
		Define a seed for the PRN generator
		Seeds are defined by r, q and l

		Parameters
	    ----------
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


	def convert(self, bits: numpy.ndarray) -> numpy.ndarray:
		"""
		Convert bits into decimals

		Parameters
	    ----------
	    bits : numpy.ndarray
	        bits to be converted
		"""
		res = 0
		for index, bit in enumerate(bits):
			res += bit * np.power(2, (len(bits)-index-1))
		return res


	def random(self) -> numpy.ndarray:
		"""
		Generate random numbers using Tauworthe method
		"""

		# check whether seed was initialized
		if self.r == 0 or self.q == 0 or self.l == 0:
			self.seed()
			
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















