# Python program for solution of M Coloring
# problem using backtracking

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]\
							for row in range(vertices)]

	# A utility function to check
	# if the current color assignment
	# is safe for vertex v
	def is_safe(self, v, colour, c):
		for i in range(self.V):
			if self.graph[v][i] == 1 and colour[i] == c:
				return False
		return True
	
	# A recursive utility function to solve m
	# coloring problem
	def graph_colour_util(self, m, colour, v):
		if v == self.V:
			return True

		for c in range(1, m + 1):
			if self.is_safe(v, colour, c) == True:
				colour[v] = c
				if self.graph_colour_util(m, colour, v + 1) == True:
					return True
				colour[v] = 0

	def graph_colouring(self, m):
		colour = [0] * self.V
		if self.graph_colour_util(m, colour, 0) == None:
			return False

		# Print the solution
		#print("Solution exist and Following are the assigned colours:", end=' ')
		#for c in colour:
		#	print(c, end=" ")
		return colour

