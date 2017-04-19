#binary search tree implementation
#find maxdepth function with recursion/while loop(nonrecursion)
#Amazon

class Node:
	def __init__(self,val):
		self.l = None
		self.r = None
		self.v = val
	
class Tree:
	def __init__(self):
		self.root = None
	def add(self,val):
		if(self.root == None):
			self.root = Node(val) else:
			self._add(val,self.root)
	def _add(self, val, node):
		if(val < node.v):
			if (node.l!=None):
				self._add(val,node.l)
			else:
				node.l = Node(val)
		else:
			if(node.r!=None):
				self._add(val,node.r)
			else:
				node.r = Node(val)
	def find(self,val):
		if(self.root!= None):
			return self._find(val,self.root)
		else:
			return None
	def _find(self,val,node):
		if(val == node.v):
			return node
		elif(val<node.v and node.l!= None):
			self._find(val,node.l)
		elif(val >node.v and node.r!=None):
			self._find(val,node.r)
	def deleteTree(self):
		self.root = None

	def printTree(self):
		if (self.root!=None):
			self._printTree(self.root)

	def _printTree(self,node):
		if (node!=None):
			self._printTree(node.l)

			print str(node.v)+" "
			self._printTree(node.r)
	#mac depth implementation with recursion
	def maxDepthRec(self):
		return self._maxDepthRec(self.root)
	def _maxDepthRec(self, root):
		if root == None:
			return 0	
		return max(self._maxDepthRec(root.l),self._maxDepthRec(root.r))+1
		
	#max depth implementation without recursion
	def maxDepth(self):
		mynodes = []
		if(self.root == None):
			return 0
		else:
			mynodes.append(self.root)
		curLevel = 0
		while mynodes:
			curLevel += 1
			newNodes = []
			for i in mynodes:
				if (i.l!= None):
					newNodes.append(i.l)
				if(i.r!=None):
					newNodes.append(i.r)
			mynodes = newNodes
		return curLevel
		
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(9)
tree.add(2)
tree.printTree()
print (tree.find(3)).v
print tree.find(10)
print tree.maxDepth(),"levels"
print tree.maxDepthRec()," recursive levels"
tree.deleteTree()
tree.printTree()
