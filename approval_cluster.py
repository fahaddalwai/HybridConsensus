# approval_cluster.py

import random

class ApprovalNode:
    def __init__(self, node_id, weight):
        self.node_id = node_id
        self.weight = weight

    def vote(self, block):
        """
        Simulate a vote on the given block.
        For demonstration, nodes approve valid blocks with a high probability.
        """
        approve_probability = 0.95  # high chance to approve if the block appears valid
        vote = 1 if random.random() < approve_probability else 0
        return vote

def create_cluster(num_nodes):
    """
    Create an approval node cluster with random weights for each node.
    """
    nodes = []
    for i in range(num_nodes):
        # Assign weights between 0.8 and 1.2 arbitrarily to simulate node importance differences
        weight = random.uniform(0.8, 1.2)
        nodes.append(ApprovalNode(i, weight))
    return nodes

def run_approval_cluster(nodes, block, voting_threshold):
    """
    Aggregate votes from the cluster nodes. Returns:
      approved: True if the weighted vote exceeds the threshold.
      approval_ratio: The ratio of the weighted score to total possible weight.
    """
    total_weight = sum(node.weight for node in nodes)
    weighted_score = sum(node.weight * node.vote(block) for node in nodes)
    approval_ratio = weighted_score / total_weight
    approved = approval_ratio >= voting_threshold
    return approved, approval_ratio
