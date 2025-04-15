# blockchain.py

from block import Block

class Blockchain:
    def __init__(self, difficulty_prefix):
        self.chain = []
        self.difficulty_prefix = difficulty_prefix
        # Create genesis block
        genesis_block = Block(index=0, previous_hash="0", message="Genesis Block", miner_id="0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        self.chain.append(block)

    def is_valid(self):
        """Check the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.previous_hash != previous.hash:
                return False
            if current.hash != current.compute_hash():
                return False
        return True
