"""
heapify(tree, indext, tree_size)
- tree : 이진 트리를 나타내는 리스트
- index : heapify하려는 노드의 인덱스
- tree_size : 트리로 사용하는 리스트의 길이
"""

def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapity(tree, index, tree_size):
    """heapify 함수 - 정답 코드"""
    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = index * 2
    right_child_index = index * 2 + 1

    # 가장 큰 값을 갖는 노드의 인덱스를 저장하는 변수
    largest = index

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] > tree[right_child_index]:
        largest = right_child_index

    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest) # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapity(tree, largest, tree_size) # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 또 heapify 함수를 호출한다
 
def heapify(tree, index, tree_size):
    """heapify 함수 - 내가 구현한 방식"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    if 0 < left_child_index < tree_size and 0 < right_child_index < tree_size:
        max_index = left_child_index if tree[left_child_index] > tree[right_child_index] else right_child_index

        if tree[max_index] > tree[index]:
            swap(tree, index, max_index)
            heapify(tree, max_index, tree_size)

# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1] # heapify하려고 하는 완전 이진 트리
heapity(tree, 2, len(tree))
print(tree)
