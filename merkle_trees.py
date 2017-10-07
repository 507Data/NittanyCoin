from time import time
import random


class block():
	def __init__(self, index, timestamp, data, previous_hash):
		self.__index = index 				# Index of the block, genesis block is 0
		self.__timestamp = timestamp   		# The change in time from the creation of the genesis block
		self.__data = data 					# The data, hashable data
		self.previous_hash = previous_hash 	# The hash of the previous block, genesis is set to a random 256 Hex
		self.next = None 					# Linked list of blocks, next points to next block in chain, no previous
	def __hash__(self):						# returns hash of the block
		return hash((str(self.__index)+ 
					str(self.__timestamp)+
					str(self.__data)+
					str(self.previous_hash)))
	def setNext(self, nextBlock):
		self.next = hash(nextBlock)

class chain():
	def __init__(self):
		self.next_blocks_index = 0
		self.genesis = self.__begin__('First Block!')
		self.recent_block = self.genesis
	def __begin__(self, data):
		g_time = time()
		self.next_blocks_index += 1
		return block(0, g_time, data, random.getrandbits(256))
	def newBlock(self, data):
		n_time = time()
		self.recent_block.setNext(block(self.next_blocks_index, n_time, data, hash(self.recent_block)))
		self.next_blocks_index += 1
		self.recent_block = self.recent_block.next
	def getTop(self):
		return self.recent_block















