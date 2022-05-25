class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearch(object):
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            root = Node(val)
            self.root = root
            return
        
        def _insert(node, val):
            if node is None:
                return Node(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        _insert(self.root, val)
    
    def find(self, val):
        def _find(node, val):
            if node is None:
                return False
            if val == node.val:
                return True
            if val < node.val:
                return _find(node.left, val)
            else:
                return _find(node.right, val)
        return _find(self.root, val)
    
    # 左側の最大値と交換
    def remove(self, val):
        def _remove(node, val):
            if node is None:
                return None
            if val < node.val:
                node.left = _remove(node.left, val)
            elif val > node.val:
                node.right = _remove(node.right, val)
            elif node.left is None:
                res_node = node.right
                del node
                return res_node
            elif node.left.right is None:
                res_node = node.left
                res_node.right = node.right
                del node
                return res_node
            else:
                tmp_node = node.left
                while tmp_node.right.right is not None:
                    tmp_node = tmp_node.right
                res_node = tmp_node.right
                tmp_node.right = res_node.left
                res_node.left = node.left
                res_node.right = node.right
                del node
                return res_node
            return node
        _remove(self.root, val)
    
    # 右側の最小値と交換
    def remove2(self, val):
        def _remove2(node, val):
            if node is None:
                return node
            if val < node.val:
                node.left = _remove2(node.left, val)
            elif val > node.val:
                node.right = _remove2(node.right, val)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.val = temp.val
                node.right = _remove2(node.right, temp.val)
            return node
        _remove2(self.root, val)

    def min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

if __name__ == '__main__':
    bs = BinarySearch()
    bs.insert(7)
    bs.insert(2)
    bs.insert(15)
    bs.insert(1)
    bs.insert(5)
    bs.insert(10)
    bs.insert(17)
    bs.insert(4)
    bs.insert(8)
    bs.insert(11)
    # bs.insert(14)
    bs.insert(16)
    bs.insert(19)

    # bs.remove(15)
    bs.remove2(15)
