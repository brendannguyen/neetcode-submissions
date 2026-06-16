class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # UNION FIND
        result = n
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            cur = node
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]

            return cur

        for a, b in edges:
            
            # if parents are same, skip
            aParent, bParent = find(a), find(b)
            if aParent == bParent:
                continue

            # check parent of bigger component
            if rank[bParent] > rank[aParent]:
                aParent, bParent = bParent, aParent
            
            # make smaller component node's parent as bigger parent
            # change parent in array
            # change rank
            parent[bParent] = parent[aParent]
            rank[aParent] = rank[aParent] + rank[bParent]

            # if union was made, decrement result by 1
            result -= 1


        return result