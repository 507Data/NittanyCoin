# Nittany Coin

# Implementation
```python
chain = chain()
chain.getTop() # should return Genesis block
genesis_hash = hash(chain.getTop)
chain.addBlock('This is my second block')
next_block_hash = chain.getTop().previous_hash # returns hash of the genesis block
genesis_hash == next_block_hash
```