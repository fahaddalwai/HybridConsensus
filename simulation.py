# simulation.py

import time
import matplotlib.pyplot as plt
import config
from blockchain import Blockchain
from block import Block
from pow_miner import mine_block
from approval_cluster import create_cluster, run_approval_cluster

def simulate():
    # Initialize blockchain and approval cluster
    blockchain = Blockchain(config.DIFFICULTY_PREFIX)
    approval_nodes = create_cluster(config.NUM_APPROVAL_NODES)

    pow_energy_list = []      # Energy consumption for PoW only
    hybrid_energy_list = []   # Energy consumption for hybrid (PoW + approval overhead)
    iterations_list = []      # Store iteration counts (for PoW)

    # Define a fixed extra energy overhead per approval phase (assumed negligible)
    approval_overhead_energy = 1e-4  # in Joules (adjust as needed)

    for round_num in range(1, config.NUM_ROUNDS + 1):
        previous_block = blockchain.get_last_block()
        # Create a new block with current round info and a dummy miner ID (round number as string)
        new_block = Block(index=round_num,
                          previous_hash=previous_block.hash,
                          message=config.MESSAGE,
                          miner_id=str(round_num))

        # --- Phase 1: Proof of Work (Mining)
        iterations, energy_pow = mine_block(new_block, config.DIFFICULTY_PREFIX)
        pow_energy_list.append(energy_pow)
        iterations_list.append(iterations)

        # --- Phase 2: Approval Cluster Voting (Proof of Authority-like review)
        approved, approval_ratio = run_approval_cluster(approval_nodes, new_block, config.VOTING_THRESHOLD)
        # Add the fixed overhead for the approval process to the energy consumption for the hybrid system.
        energy_hybrid = energy_pow + approval_overhead_energy
        hybrid_energy_list.append(energy_hybrid)

        # Log round details
        print(f"Round {round_num}:")
        print(f"  PoW iterations: {iterations} | Energy (PoW): {energy_pow:.6f} J")
        print(f"  Approval Ratio: {approval_ratio:.3f} - Block {'APPROVED' if approved else 'REJECTED'}")
        if approved:
            blockchain.add_block(new_block)
            print("  Block added to blockchain.")
        else:
            print("  Block rejected. (Miner may be penalized in a real system.)")
        print("-" * 50)
        time.sleep(0.1)  # slight delay for readability

    # Calculate average energy consumption over all rounds
    avg_pow_energy = sum(pow_energy_list) / len(pow_energy_list)
    avg_hybrid_energy = sum(hybrid_energy_list) / len(hybrid_energy_list)

    print("\nSimulation complete.")
    print(f"Average Energy Consumption (PoW only): {avg_pow_energy:.6f} J")
    print(f"Average Energy Consumption (Hybrid): {avg_hybrid_energy:.6f} J")

    # Plot energy consumption per round for visualization
    rounds = list(range(1, config.NUM_ROUNDS + 1))
    plt.figure(figsize=(10, 6))
    plt.plot(rounds, pow_energy_list, label="PoW Energy (J)")
    plt.plot(rounds, hybrid_energy_list, label="Hybrid Energy (J)", linestyle="--")
    plt.xlabel("Round Number")
    plt.ylabel("Energy Consumption (Joules)")
    plt.title("Energy Consumption per Round: PoW vs Hybrid Mechanism")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate()
