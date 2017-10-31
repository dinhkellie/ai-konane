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
	# Moves are a tuple of four integers [row1, col1, row2, col2]
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
		elif board[self.size-1][self.size-1] == '.':
			legalMoves.append([self.size-1, self.size]*2)
			legalMoves.append([self.size, self.size-1]*2)
			return legalMoves
		elif board[self.size/2][self.size/2] == '.':
			print "ya"
			m = self.size/2
			legalMoves.append([m+1, m]*2)
			legalMoves.append([m+2, m+1]*2)
			legalMoves.append([m+1, m+2]*2)
			legalMoves.append([m, m+1]*2)
			return legalMoves
		else:
			print "no"
			m = self.size/2 + 1
			legalMoves.append([m-1, m-2]*2)
			legalMoves.append([m, m-1]*2)
			legalMoves.append([m-1, m]*2)
			legalMoves.append([m-2, m-1]*2)
			return legalMoves

	# Checks if the board is at a beginning state by checking whether it contains '.' since that is the symbol for an empty space
	def openingMove(self, board):
		count = 0
		for x in range(self.size):
			for y in range (self.size):
				if board[x][y] == ".":
					count += 1
		return count <= 1

	# Checks if inputted [row, column] position is within board's boundaries 1-8
	def valid(self, move):
		return move[0] >= 1 and move[1] >= 1 and move[0] <= self.size and move[1] <= self.size

	# Returns all the legal moves for the given player at the current board confguration
	def getLegalMoves(self, board, player):
		legalMoves = []
		# Determines whether the current move is first or second based on symbols on the board
		if self.openingMove(board):
			# Dark always goes first
			if player.symbol == 'X':
				return self.firstMove(board)
			else:
				return self.secondMove(board)
		else:
			for r in range(self.size):
				for c in range(self.size):
					print [r, c]
					if board[r][c] == player.symbol:
						# Top
						# Check whether piece is in 3rd row or more
						if c > 1:
							print self.boardToString(board)
							print [r, c-1], board[r][c-1]
							if board[r][c-1] == self.opponent(player.symbol) and board[r][c-2] == '.':
								legalMoves.append([r+1, c+1, r+1, c-1])
								print "a", [r+1, c+1, r+1, c-1]
						# Right
						# Check whether piece is at least 2 less than length
						if r < (self.size - 2):
							print [r+1, c], board[r+1][c]
							if board[r+1][c] == self.opponent(player.symbol) and board[r+2][c] == '.':
								legalMoves.append([r+1, c+1, r+3, c+1])
								print "b", [r+1, c+1, r+3, c+1]
						#Left
						# Check whether piece is at least 2 more than 0
						if r > 1:
							print [r-1, c], board[r-1][c]
							if board[r-1][c] == self.opponent(player.symbol) and board[r-2][c] == '.':
								legalMoves.append([r+1, c+1, r-1, c+1])
								print "c", [r+1, c+1, r-1, c+1]

						#Bottom
						# Check whether the piece is at least 2 less than length
						if c < (self.size - 2):
							print [r, c+1], board[r][c+1]
							if board[r][c+1] == self.opponent(player.symbol) and board[r][c+2] == '.':
								legalMoves.append([r+1, c+1, r+1, c+3])
								print "d", [r+1, c+1, r+1, c+3]
				print "\n"
			print "\n"
		return legalMoves

	# Updates board based on move if the move is valid to the board and is a legal move
	def attemptMove(self, board, player, move):
		# how to get which player's turn?
		legalMoves = self.getLegalMoves(board, player)

		if not self.valid(move):
			raise ValueError('Invalid move.')
		elif move not in legalMoves:
			raise ValueError('Illegal move.')
		else:
			# Had to subtract 1 since user is inputting based on 1-8 grid not 0-7
			board[move[2]-1][move[3]-1] = board[move[0]-1][move[1]-1]
			board[move[0]-1][move[1]-1] = '.'

			if not self.openingMove(board):

				if move[0] == move[2]:
					#[1, 3, 1, 1]
					if move[1] > move[3]:
						board[move[0]-1][move[1] - move[3] - 1] = '.'
					#[1, 1, 1, 3]
					else:
						board[move[0]-1][move[3] - move[1] - 1] = '.'
				if move[1] == move[3]:
					#[3, 1, 1, 1]
					if move[0] > move[2]:
						board[move[0] - move[2] - 1][move[1]] = '.'
					#[1, 3, 3, 3]
					else: 
						board[move[2] - move[0] - 1][move[1]] = '.'
			return board

	def play(self, player1, player2):
		self.start()
		print "Welcome to Konane!"
		print self
		move = 0
		while (move != -1):
			print "Turn:", player1.symbol
			print "Legal moves:", self.getLegalMoves(self.board, player1)
			move = player1.getMove(self.board)
			try:
				self.baord = self.attemptMove(self.board, player1, move)
			except ValueError:
				print "Unable to make move."
				break;
			self.boardToString(self.board)
			print self.boardToString(self.board)

			print "Turn:", player2.symbol
			print "Legal moves:", self.getLegalMoves(self.board, player2)
			move = player2.getMove(self.board)
			try:
				self.board = self.attemptMove(self.board, player2, move)
			except ValueError:
				print "Unable to make move."
				break;
			self.boardToString(self.board)
			print self.boardToString(self.board)
		print "Game over"

class Player(Konane):
	def __init__(self, symbol):
		self.symbol = symbol
		self.name = "Human"

	def getMove(self, board):
		r1, c1, r2, c2 = input("Your move: ")
		if []:
			return -1;
		else:
			return [r1, c1, r2, c2]

playerX = Player('X')
playerO = Player('O')
game = Konane(8)
game.play(playerX, playerO)
