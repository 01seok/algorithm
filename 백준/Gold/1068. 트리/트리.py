def dfs(cur_node):
    global leaf_cnt

    if cur_node == delete_node:
        return

    valid_node = [child for child in tree[cur_node] if child != delete_node]

    # 유효한 노드인데, 자식 노드가 없으면 리프노드
    if not valid_node:
        leaf_cnt += 1
        return

    # 자식 있으면 유효한 자식에 대해 dfs
    for child in valid_node:
        dfs(child)


N = int(input())
parents = list(map(int, input().split()))   # 각 노드의 부모 인덱스
delete_node = int(input())  # 삭제할 노드 번호

tree = [[] for _ in range(N)]
root = -1

for i in range(N):
    parent = parents[i]
    if parent == -1:
        root = i
    else:
        tree[parent].append(i)

leaf_cnt = 0

while True:
    if delete_node == root:
        print(0)
        break

    if root != -1:
        dfs(root)

    print(leaf_cnt)
    break
