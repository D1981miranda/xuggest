from typing import Tuple, Dict, Any, List
import curses
import os
import heapq


data = ['girl wedding', 'boy', 'hack', 'girl', 'girl', 'girl',
        'children', 'workers', 'girly', 'clothing', 
        'red', 'william', 'red dress', 'ready', 'red wine',
        'rain', 'read', 'redding', 'gill', 'gurly', 'gurly'
       ]


class Node:

    def __init__(self, value) -> Any:
        
        self.children: Dict[str, Node] = {}
        self.value: str = value
        self.terminal: bool = False
        self.hit_count = 0


class AutoSuggest:
    
    def __init__(self, words=None):
        self.data = words if words else data
        self.root = Node('')
        self.make_trie() 

    def find(self, key: str) -> Any:
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def get_top_suggestions(self, suggestions: 
                            List[Tuple[int, str]]) -> List[str]:
        n_suggestions = len(suggestions) 
        return [heapq.heappop(suggestions)[-1] 
                for _ in range(n_suggestions)]

    def get_prefix_children(self, prefix: str) -> List[List[str]]:
        def _dfs(node: Node) -> None:
            if node.terminal:
                heapq.heappush(paths, (-node.hit_count, node.value))
                return 
            for child in node.children:
                _child = node.children[child]
                _dfs(_child)
            
        paths = []
        # find prefex
        node =  self.find(prefix)
        if not node:
            return paths
        paths = []
        _dfs(node)
        return self.get_top_suggestions(paths)
        # walk do dfs 

    def insert(self, key: str) -> Any:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.value = key 
        node.terminal = True
        node.hit_count+=1
    
    def make_trie(self) -> Any:
        for word in self.data:
            self.insert(word)

