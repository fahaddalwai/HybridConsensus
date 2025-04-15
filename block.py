# block.py

import time
import hashlib

class Block:
    def __init__(self, index, previous_hash, message, miner_id):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.message = message
        self.miner_id = miner_id
        self.nonce = 0
        self.hash = None

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.message}{self.miner_id}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine(self, difficulty_prefix):
        """Proof-of-Work mining: find a nonce so that the hash starts with the required prefix."""
        self.nonce = 0
        computed_hash = self.compute_hash()
        iterations = 0
        while not computed_hash.startswith(difficulty_prefix):
            self.nonce += 1
            iterations += 1
            computed_hash = self.compute_hash()
        self.hash = computed_hash
        return iterations  # Number of iterations (hash attempts) required
