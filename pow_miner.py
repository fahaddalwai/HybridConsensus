# pow_miner.py

from block import Block
import config

def mine_block(block, difficulty_prefix):
    """
    Perform PoW mining on a block.
    
    Returns:
      iterations: Number of hash attempts required.
      energy_consumption: Estimated energy consumed (in Joules).
    """
    iterations = block.mine(difficulty_prefix)
    energy_consumption = iterations * config.HASH_ENERGY_J
    return iterations, energy_consumption
