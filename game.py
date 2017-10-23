class Konane:
	def __init__(self, n):
		self.size = n
		self.start()

	# Start state of board
	def start(self):
		self.board = []
		value = 'X'
		for i in range(self.size):
			row = []
			for j in range(self.size):
				row.append(value)
				value = self.opponent(value)
			self.board.append(row)
			if self.size % 2 == 0:
				value = self.opponent(value)

	# Given symbol, returns opponent's symbol either 'X' or 'O'	
	def opponent(self, symbol):
		if symbol == 'X':
			return 'O'
		else:
			return 'X'

	def __str__(self):
		return self.boardToString(self.board)

	# Return string representation of board
	def boardToString(self, board):
		result = "  "
		for i in range(self.size):
			result += str(i+1) + " "
		result += "\n"
		for i in range(self.size):
			result += str(i+1) + " "
			for j in range(self.size):
				result += str(board[i][j]) + " "
			result += "\n"
		return result

	def play(self, n):
		self.start()
		for i in range (0, n):
			print self

game = Konane(8)
game.play(1)