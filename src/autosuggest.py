from typing import Tuple, Dict, Any, List
import curses
import os
import heapq

class Node:

    def __init__(self, value) -> Any:
        
        self.children: Dict[str, Node] = {}
        self.value: str = value
        self.terminal: bool = False
        self.hit_count = 0

def find(node: Node, key: str) -> Tuple[Node, str]:
    

    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node


def get_top_suggestions(suggestions):
    n_suggestions = len(suggestions) 
    return [heapq.heappop(suggestions)[-1] for _ in range(n_suggestions)]

def get_prefix_children(node: Node, prefix: str) -> List[List[str]]:
     
    def _dfs(node: Node) -> None:
        if node.terminal:
            heapq.heappush(paths, (-node.hit_count, node.value))
            return 
        for child in node.children:
            _child = node.children[child]
            _dfs(_child)

    paths = []
    heapq.heapify(paths)
    # find prefex
    node =  find(node, prefix)
    if not node:
        return paths
    _dfs(node)
    return get_top_suggestions(paths)
    # walk do dfs 

def insertall(node: Node, keys: List[str]) -> None:
    [insert(x) for x in keys]
    return

def insert(node: Node, key: str) -> Any:
    for char in key:
        if char not in node.children:
            node.children[char] = Node(char)
        node = node.children[char]
    node.value = key 
    node.terminal = True
    node.hit_count+=1


class WordStack(list):

    pass 


if __name__ == '__main__':

    def main(win):             
        
        def make_trie():
            root = Node('')
            words = ['girl wedding', 'boy', 'hack', 'girl', 'girl', 'girl',
                     'children', 'workers', 'girly', 'clothing', 
                     'red', 'william', 'red dress', 'ready', 'red wine',
                     'rain', 'read', 'redding', 'gill', 'gurly', 'gurly'
                    ]
            for word in words:
                insert(root, word)


            assert find(root, 'boy')
            assert find(root, 'gurly')
            assert not find(root, 'man')
            return root
        node = make_trie()
        win.nodelay(False)
        key=""
        win.clear()
        win.addstr('Detected Key: ')
        word = ''
        # mininum key string before drawing sugges
        min_draw = 2

        while 1:
            try:
                key = win.getkey()
                char = str(key)
                # key to input stack
                if ord(char) == 127:
                    if word: 
                        word = word[:-1]
                    # Ugly backspace, count get delch() to work
                    win.clear()
                    win.addstr(f'Detected Key: {word}')
                else:
                    word += char
                    win.addstr(char) 
                if key == os.linesep:
                    break
            except Exception as ex:
                win.addstr(ex.__repr__())
            finally:
                # print suggestions to screen 

                if len(word) > min_draw:
                    suggestions = get_prefix_children(node, word)
                    for suggestion in suggestions:
                        win.addstr(suggestion)
    curses.wrapper(main)    
