import hashlib as hasher
import datetime as date

class Block:

	# initialize the different parts to each block
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	# begin setting up hashing library for hashing,
	# combines diffent elements and outputs hash in hex
	def hash_block(self):
		sha = hasher.sha384()
		sha.update(str(self.index) +
				   str(self.timestamp) +
				   str(self.data) +
				   str(self.previous_hash))
		return sha.hexdigest()

# we need to create our first block in the chain, contains special properties
# has index of 0 and a random set previous hash since it is first
def create_genesis_block():
	return Block(0, date.datetime.now(), "Genesis Block, will be worth millions", "0")

#creating every consecutive block
def next_block(last_block):
	this_index = last_block.index + 1
	this_timestamp = date.datetime.now()
	this_data = "Test" + str(this_index)
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)



