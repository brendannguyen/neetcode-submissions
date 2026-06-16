class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # UNION FIND
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]

        def find(node):
            # find root by going up the tree
            cur = node
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]

            return cur

        for a, b in edges:
            
            # if parents are same, skip
            aParent, bParent = find(a), find(b)
            if aParent == bParent:
                return [a, b]

            # check parent of bigger component
            if rank[bParent] > rank[aParent]:
                aParent, bParent = bParent, aParent
            
            # make smaller component node's parent as bigger parent
            # change parent in array
            # change rank
            parent[bParent] = parent[aParent]
            rank[aParent] = rank[aParent] + rank[bParent]


        