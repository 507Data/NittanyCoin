from time import time
import hashlib as hasher
sha = hasher.sha256
import random

target = 10000 # Number of NittanyCoins there should be in circulation


class block():
	def __init__(self, index, timestamp, data, previous_hash, nonce):
		self.__index = index 				# Index of the block, genesis block is 0
		self.__timestamp = timestamp   		# The change in time from the creation of the genesis block
		self.data = data 					# The data, hashable data
		self.previous_hash = previous_hash 	# The hash of the previous block, genesis is set to a random 256 Hex
		self.nonce = nonce
		self.next = None 					# Linked list of blocks, next points to next block in chain, no previous
	def __hash__(self):						# returns hash of the block
		return hash((str(self.__index)+ 	# Sum the strings of the blocks properties
					str(self.__timestamp)+	
					str(self.data)+
					str(self.previous_hash) +
					str(self.nonce)))
	def __eq__(self, other):				# Are two blocks the same? This should not happen
		return isinstance(other, block)

class chain():
	length = 0
	def __init__(self):									# Initialize the chain
		self.g_time = time()
		chain.length += 1
		self.genesis = block(0, self.g_time, 'Hello World', random.getrandbits(256), 9)
		self.recent_block = self.genesis				# set top of the chain as genesis block
		self.next_blocks_index = 1
	def __mine__(self):
		begin = time()
		last_proof = self.recent_block.nonce
		incrementor = last_proof + 1
		# proof of work is defined as :
		while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
			if ((time() - begin) % 60 == 0):
				print "Time Elapsed: {}".format(time()-begin)
			incrementor += 1
		print "New Block Created!"
		print "Total Time: {}".format(time()-begin)
		return incrementor
	def newBlock(self, data):
		nonce = self.__mine__()
		new_b = block(chain.length, time(), data, hash(self.recent_block), nonce)
		self.recent_block.next = new_b
		self.recent_block = new_b
		chain.length += 1
	def getTop(self):
		return self.recent_block




















