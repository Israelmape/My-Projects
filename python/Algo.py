def depthFirstSearch(tree):
    if tree is None:
        return
    
    print(tree.value)

    for child in tree.children:
        depthFirstSearch(child)

    


def bfs(root):
    queue = []
    queue.append(root)
    while queue:
        n = len(queue)
        for _ in range(n):
            node =queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)  


