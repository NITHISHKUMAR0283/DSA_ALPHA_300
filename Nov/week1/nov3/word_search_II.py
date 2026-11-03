class TrieNode():
    def __init__(self):
        self.childrens = {}
        self.is_end = False
class Trie():
    def __init__(self,words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    def insert(self,word):
        root = self.root
        for w in word:
            if w not in root.childrens:
                root.childrens[w]=TrieNode()
            root = root.childrens[w]
        root.is_end=True


class Solution(object):
    def explore (self,board,root,solution,si,sj,word):
        if root.is_end and word not in solution:
            solution.add(word)
        directions = {(0,1),(0,-1),(1,0),(-1,0)}
        n = len(board)
        m = len(board[0])
        for ri,rj in directions:
            ni,nj = si+ri,sj+rj
            if 0<=ni<n and 0<=nj<m and board[ni][nj] in root.childrens:
                char = board[ni][nj]
                board[ni][nj]="-1"
                self.explore(board,root.childrens[char],solution,ni,nj,word+char)
                board[ni][nj] = char
            

    def findWords(self, board, words):
        
        Tries = Trie(words).root
        n = len(board)
        m = len(board[0])
        solution = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] in  Tries.childrens:
                    char = board[i][j]
                    board[i][j]="-1"
                    self.explore(board,Tries.childrens[char],solution,i,j,char)
                    board[i][j] = char
        return list(solution)
        