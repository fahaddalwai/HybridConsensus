# config.py

# Mining parameters
DIFFICULTY_PREFIX = "00000"     # Required prefix for a valid PoW hash

# Energy parameters (values chosen for simulation purposes)
POWER_CONSUMPTION_W = 100       # Power consumption in watts (for simulation)
HASH_ENERGY_J = 1e-6            # Estimated energy per hash (in Joules)

# Approval Cluster parameters
NUM_APPROVAL_NODES = 10         # Total nodes in the approval cluster
VOTING_THRESHOLD = 0.6          # Minimum approval ratio required (60%)

# Simulation parameters
NUM_ROUNDS = 50                 # Number of mining rounds (blocks)
MESSAGE = "ABC"                 # Message to be included in each block
