from typing import List, Optional, TreeNode
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        bfs_queue = deque([root])  # Use deque for efficient popping
        output = []
        
        while bfs_queue:
            level_size = len(bfs_queue)
            level_nodes = []
            
            for _ in range(level_size):  # Process all nodes in the current level
                current_node = bfs_queue.popleft()
                level_nodes.append(current_node.val)
                
                if current_node.left:
                    bfs_queue.append(current_node.left)
                if current_node.right:
                    bfs_queue.append(current_node.right)
            
            output.append(level_nodes)
        
        return output
       
