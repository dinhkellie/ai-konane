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

	# For moves, all add 1 since the board starts 1-8 rather than 0-7
	# Moves are a tuple of four integers [r1, c1, r2, c2]
	# r1, c1 refer to starting position of piece and r2, c2 are end position
	# Opening moves are taken away not moved so r1 and r2 and c1 and c2 are the same

	# Returns legal moves if it's the first turn
	def firstMove(self, board):
		legalMoves = []
		legalMoves.append([1, 1]*2)
		legalMoves.append([self.size, self.size]*2)
		legalMoves.append([self.size/2, self.size/2]*2)
		legalMoves.append([(self.size/2)+1, (self.size/2)+1]*2)
		return legalMoves

	# Returns legal moves if it's the second turn
	def secondMove(self, board):
		legalMoves = []
		if board[0][0] == ".":
			legalMoves.append([1,2]*2)
			legalMoves.append([2,1]*2)
			return legalMoves
		elif board[self.size-1][self.size-1] == ".":
			legalMoves.append([self.size-1, self.size]*2)
			legalMoves.append([self.size, self.size-1]*2)
			return legalMoves
		elif board[self.size/2][self.size/2] == ".":
			m = self.size/2
			legalMoves.append([m, m-1]*2)
			legalMoves.append([m+1, m]*2)
			legalMoves.append([m, m+1]*2)
			legalMoves.append([m-1, m]*2)
			return legalMoves
		else:
			m = self.size/2 + 1
			legalMoves.append([m, m-1]*2)
			legalMoves.append([m+1, m]*2)
			legalMoves.append([m, m+1]*2)
			legalMoves.append([m-1, m]*2)
			return legalMoves

	def valid(self, move):
		return move[0] >= 1 and move[1] >= 1 and move[0] <= self.size and move[1] <= self.size

	def openingMove(self, board):
		count = 0
		for x in range(self.size):
			for y in range (self.size):
				if board[x][y] == ".":
					count += 1
		return count <= 1

	# Returns all the legal moves for the given player at the current board confguration
	def getLegalMoves(self, board, player):
		legalMoves = []
		# Determines whether the current move is first or second based on symbols on the board
		if self.openingMove(board):
			# Dark always goes first
			if player == 'X':
				return self.firstMove(board)
			else:
				return self.secondMove(board)
		else:
			return []


	def play(self, n, player1, player2):
		self.start()
		for i in range (0, n):
			print self
		move = player1.getMove(self.board)
		

class Player(Konane):
	def __init__(self, symbol):
		self.symbol = symbol
		self.name = "Human"

	def getMove(self, board):
		r1, c1, r2, c2 = input("Enter position of piece to move and where to move it. r1, c1, r2, c2 : ")
		if r1 == -1:
			return []
		return [r1, c1, r2, c2]

playerX = Player('X')
playerO = Player('O')
game = Konane(8)
game.play(1, playerX, playerO)