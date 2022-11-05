class TrieNode:
    def __init__(self, char=None, letterToChild=None, word=None, prev=None):
        self.char = char # this node's current character
        self.letterToChild = letterToChild # dictionary that maps child's letter to child's node
        self.word = word #  when a word is complete from start to this node, we set what the word is from start to here (note that there can stll be more words down this path)
        self.prev = prev # to backtrack and remove words that are already searched

class Solution:
    #24ms (faster than 98.86% Python 3) ~ O(MN * numPaths * 3^(longestWordLength)) runtime, O(totalWordLength * numWords) worst case memory
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board[0]) == 0 or not words:
            return []

        def buildTrie(words: List[str]):
            #print("using words: {}".format(words))
            # root node is character "/"
            root = TrieNode(char="/")
            for word in words:
                # given a word, construct path of the word in Trie
                index = 0
                curNode = root
                while index < len(word):
                    #print("word[index]: {}".format(word[index]))
                    # prepare childNode
                    char = word[index]
                    if not curNode.letterToChild:
                        curNode.letterToChild = {}
                    if char not in curNode.letterToChild:
                        # if childNode doesn't exist, create it
                        childNode = TrieNode(char=char,letterToChild={},prev=curNode) #for some reason I need the {} otherwise it's stealing from previous node
                        curNode.letterToChild[char] = childNode
                        #print("curNode's child: {}".format(curNode.letterToChild))
                    else:
                        childNode = curNode.letterToChild[char]
                    
                    # if at end of word, update the child node
                    if index == len(word) - 1:
                        childNode.word = word
                        break

                    index += 1
                    curNode = childNode
            return root
        #build the Trie
        root = buildTrie(words)

        #iterate through the board
        rows = len(board)
        cols = len(board[0])
        
        resultList = []
        def dfs(x,y,curNode:TrieNode):
            #print("(x,y)=({},{})".format(x,y))
            boardLetter = board[x][y]
            if boardLetter in curNode.letterToChild:
                board[x][y] = "*" #modify the board letter so we don't reuse during dfs search
                # letter matches, get the childNode
                nextNode = curNode.letterToChild[boardLetter]
                # check if nextNode is at the end of a word; if so, add that to our resultList. Note that there may be more words further along this path.
                if nextNode.word:
                    resultList.append(nextNode.word)
                    nextNode.word = None
                    # delete the branch that is no longer needed (to avoid creating the same word again on next board iteration)
                    if len(nextNode.letterToChild) == 0:
                        #no more children below so need to backtrack and delete
                        #backtrack stops if there are 2+ paths down, or if we're at the root node
                        parentNode = curNode
                        usedChar = nextNode.char
                        while len(parentNode.letterToChild) == 1:
                            #cut mapping of parentNode to used-childNode
                            del parentNode.letterToChild[usedChar]
                            usedChar = parentNode.char
                            if usedChar == "/":
                                #reached the top so no need to backtrack anymore
                                break
                            parentNode = parentNode.prev                            

                # keep dfs traversing until end of word(s) in this Trie path
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    adjX, adjY = x+dx, y+dy 
                    # check if adjacent position is in board
                    if 0 <= adjX < rows and 0 <= adjY < cols:
                        dfs(adjX,adjY,nextNode)
            # no match with board or no more letters along this path
            # revert back the letter modified by dfs (backtrack)
            board[x][y] = boardLetter
            return

        for x in range(rows):
            for y in range(cols):
                #check if word match; if so, traverse dfs
                curNode = root 
                dfs(x,y,curNode)
        return resultList