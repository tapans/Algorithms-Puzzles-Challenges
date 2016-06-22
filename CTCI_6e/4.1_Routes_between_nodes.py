#!/usr/bin/python
import unittest
import logging

class Node:
	def __init__(self, name):
		self.visited = False
		self.name = name

	def __str__(self):
		return str(self.name)

class Directed_Acylic_Graph:
	'''
		Simple adjacency list implmentation of a DAG
	'''
	def __init__(self):
		self.nodes = {}

	def add_node(self, node):
		if node in self.nodes:
			raise "node %s already exists!" % node
		self.nodes[node] = []

	def add_edge(self, source_node, dest_node):
		if source_node not in self.nodes:
			raise "source node does not exist!"
		self.nodes[source_node].append(dest_node)

	def __str__(self):
		s = ""
		for node in self.nodes.keys():
			adj_lst = [str(nde) for nde in self.nodes[node]]
			s += str(node) + ": " + str(adj_lst) + "\n"
		return s 

	def path_exists_bfs(self, source, dest):
		'''
			Return True if there's a path from source node to dest node using BFS.
			Also, print path from source to dest if it exists
			Time Comlexity: Let n be # of nodes, e be # of edges => O(n + e)
			Space Complexity: O(n + e)
		'''

		def path_exists_bfs_helper(source, dest, prev):
			Q = [source]
			while len(Q) > 0:
				source = Q.pop(0)
				if source == dest:
					return True, prev
				for node in self.nodes[source]:
					prev[node] = source
					if node == dest:
						return True, prev
					if not node.visited:						
						Q.append(node)
					else:
						node.visited = True
			return None, prev


		prev = {}
		exists, prev = path_exists_bfs_helper(source, dest, prev)
		if exists:
			self.print_path(source, dest, prev) 
			return True
		else:
			return False

	
	def path_exists_dfs(self, source, dest):
		''' 
			Return True if there's a path from source node to dest node using DFS.
			Also, print path from source to dest if it exists
			Time Comlexity: Let n be # of nodes, e be # of edges => O(n + e)
			Space Complexity: O(n + e)
		'''

		def path_exists_dfs_helper(source, dest, prev, visited=[]):
			if (len(self.nodes[source]) == 0):
				return None, prev
			else:
				for node in self.nodes[source]:
					if node.visited:
						continue
					prev[node] = source					
					if node == dest:
						return True, prev
					else:
						exists, prev = path_exists_dfs_helper(node, dest, prev)
						node.visited = True
						if exists :
							return True, prev
				return None, prev

		prev = {}
		exists, prev = path_exists_dfs_helper(source, dest, prev)
		if exists:
			self.print_path(source, dest, prev) 
			return True
		else:
			return False

	def print_path(self, source, dest, prev):
		path = []
		orig_dest = dest
		path.append(str(dest))
		while dest != source:
			dest = prev[dest]
			path.append(str(dest))
		path.reverse()
		print "Path from %s to %s: %s" % (str(source), str(orig_dest), path)

class Test_Route_between_nodes(unittest.TestCase):

	def setUp(self):		
		logging.basicConfig()
		self.log = logging.getLogger("LOG")
		self.log.setLevel(logging.DEBUG)
		self.dg = Directed_Acylic_Graph()		
		self.nodes = [None]
		for i in range(1,6):
			node = Node(i)
			self.nodes.append(node)
			self.dg.add_node(node)
		self.dg.add_edge(self.nodes[1],self.nodes[2])
		self.dg.add_edge(self.nodes[2],self.nodes[3])
		self.dg.add_edge(self.nodes[3],self.nodes[5])
		self.dg.add_edge(self.nodes[1],self.nodes[4])
		self.dg.add_edge(self.nodes[4],self.nodes[5])

	def test_path_exists_dfs(self):
		self.log.debug("DFS: \n" + str(self.dg))
		self.assertTrue(self.dg.path_exists_dfs(self.nodes[1],self.nodes[5]))
		self.assertFalse(self.dg.path_exists_dfs(self.nodes[2],self.nodes[4]))
		self.assertFalse(self.dg.path_exists_dfs(self.nodes[3],self.nodes[1]))

	def test_path_exists_bfs(self):
		self.log.debug("BFS: \n" + str(self.dg))
		self.assertTrue(self.dg.path_exists_bfs(self.nodes[1],self.nodes[5]))
		self.assertFalse(self.dg.path_exists_bfs(self.nodes[2],self.nodes[4]))
		self.assertFalse(self.dg.path_exists_bfs(self.nodes[3],self.nodes[1]))


if __name__ == '__main__':    
	unittest.main()