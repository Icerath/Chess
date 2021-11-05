import pygame
import os
import random
c_path = os.getcwd()
if c_path[-5:] == "Saves":
    path = path = os.path.join("\\Users","User","Documents","Python Saves","Fun Projects","Tier_1","current","pygame","chess")
    os.chdir(path)
else:
    print(c_path[-6:-1])
pygame.init()

display_info = pygame.display.Info()
WIDTH, HEIGHT = display_info.current_w, display_info.current_h
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 45
ALPHA = 64
pygame.display.set_caption("Chess")

MIN_WH = min(WIDTH, HEIGHT)
div = 2
wh = MIN_WH * 0.75
BOARD_rect = pygame.Rect(WIDTH // div -  wh // 2, (HEIGHT // div - wh // 2) + WIDTH // 25, wh, wh)
PIECE_WIDTH, PIECE_HEIGHT = BOARD_rect.w // 8, BOARD_rect.h // 8
PIECE_ADJUST = (BOARD_rect.w //8 - PIECE_WIDTH) // 2
LINE_WIDTH = BOARD_rect.w // 200
#region Setting up text, images and sound
fonts = {"monospace": pygame.font.SysFont("monospace", 50), "arial": pygame.font.SysFont("arial", 50)}
turn_text_pos = 0, 0

SQUARE_IMAGE = pygame.image.load(os.path.join("Assets","GREEN.jpg"))
SQUARE_IMAGE = pygame.transform.smoothscale(SQUARE_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
SQUARE_IMAGE.set_alpha(32)

CHESS_BOARD_IMAGE = pygame.image.load(os.path.join("Assets","Boards", "brown.jpg"))
CHESS_BOARD_IMAGE = pygame.transform.smoothscale(CHESS_BOARD_IMAGE, (BOARD_rect.w, BOARD_rect.h))
CHESS_BOARD_ALPHA_IMAGE = CHESS_BOARD_IMAGE.copy()
CHESS_BOARD_ALPHA_IMAGE.set_alpha(ALPHA)

WHITE_PAWN_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_PAWN.png"))
WHITE_PAWN_IMAGE = pygame.transform.smoothscale(WHITE_PAWN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

WHITE_BISHOP_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_BISHOP.png"))
WHITE_BISHOP_IMAGE = pygame.transform.smoothscale(WHITE_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

WHITE_KNIGHT_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_KNIGHT.png"))
WHITE_KNIGHT_IMAGE = pygame.transform.smoothscale(WHITE_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

WHITE_ROOK_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_ROOK.png"))
WHITE_ROOK_IMAGE = pygame.transform.smoothscale(WHITE_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

WHITE_KING_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_KING.png"))
WHITE_KING_IMAGE = pygame.transform.smoothscale(WHITE_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

WHITE_QUEEN_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_QUEEN.png"))
WHITE_QUEEN_IMAGE = pygame.transform.smoothscale(WHITE_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()


BLACK_PAWN_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_PAWN.png"))
BLACK_PAWN_IMAGE = pygame.transform.smoothscale(BLACK_PAWN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

BLACK_BISHOP_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_BISHOP.png"))
BLACK_BISHOP_IMAGE = pygame.transform.smoothscale(BLACK_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

BLACK_KNIGHT_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_KNIGHT.png"))
BLACK_KNIGHT_IMAGE = pygame.transform.smoothscale(BLACK_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

BLACK_ROOK_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_ROOK.png"))
BLACK_ROOK_IMAGE = pygame.transform.smoothscale(BLACK_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

BLACK_KING_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_KING.png"))
BLACK_KING_IMAGE = pygame.transform.smoothscale(BLACK_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

BLACK_QUEEN_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_QUEEN.png"))
BLACK_QUEEN_IMAGE = pygame.transform.smoothscale(BLACK_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()

#Sound effects

START_SOUND = pygame.mixer.Sound('Assets/Sound/START.wav')
MOVE_SOUND = pygame.mixer.Sound('Assets/Sound/MOVE.wav')
CAPTURE_SOUND = pygame.mixer.Sound('Assets/Sound/CAPTURE.wav')
#CASTLE_SOUND = pygame.mixer.Sound('Assets/Sound/CAPTURE.wav')
CASTLE_SOUND = MOVE_SOUND
CHECK_SOUND = pygame.mixer.Sound('Assets/Sound/SILENCE.wav')
CHECKMATE_SOUND = pygame.mixer.Sound('Assets/Sound/GENERIC_NOTIFY.wav ')
DRAW_SOUND = pygame.mixer.Sound('Assets/Sound/GENERIC_NOTIFY.wav')
#endregion
#Classes
class Chess_Board():
    def __init__(self):
        self.image = CHESS_BOARD_IMAGE
        self.score = 0
        self.square_positions = self.set_squares()
        self.square_pieces = self.set_pieces()
        self.pieces = [i for i in self.square_pieces.values() if i != None]
        self.can_move = True
        self.promoting_piece = None
        self.pawn_or_cap_count = 0
        self.pro_rects = []
        self.move = ("","")
        self.board_options = {"white": {},
                              "black": {}}
        self.turn = "white"
        self.alt_turn = "black"
        self.turn_num = 0
        self.ply_info = {}
        self.ply_pieces = {}
        self.ply_turn = {}
        self.store_ply()
        #promoting rects
        self.white_pro_rects = [WHITE_QUEEN_IMAGE, WHITE_ROOK_IMAGE, WHITE_KNIGHT_IMAGE, WHITE_BISHOP_IMAGE]
        self.black_pro_rects = [BLACK_QUEEN_IMAGE, BLACK_ROOK_IMAGE, BLACK_KNIGHT_IMAGE, BLACK_BISHOP_IMAGE]

        self.selected_piece = None
        self.victory = False
    def set_squares(self):
        squares = {}
        for num in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            for let in ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8"]:
                x = ((int(let[1])-1) * BOARD_rect.h//8) + BOARD_rect.x
                y = ((int(num)-8) * - BOARD_rect.w//8) + BOARD_rect.y
                width = BOARD_rect.w//8
                height = BOARD_rect.h//8
                squares[let[0]+num] = pygame.Rect(x, y, width, height)
        return squares

    def set_pieces(self):
        square_pieces = {}
        for sq in self.square_positions:
            square_pieces[sq] = None
        
        for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            square_pieces[i + "2"] = Pawn(i + "2", "white")
            square_pieces[i + "7"] = Pawn(i + "7", "black")

        square_pieces["B1"] = Knight("B1", "white")
        square_pieces["G1"] = Knight("G1", "white")
        square_pieces["B8"] = Knight("B8", "black")
        square_pieces["G8"] = Knight("G8", "black")

        square_pieces["C1"] = Bishop("C1", "white")
        square_pieces["F1"] = Bishop("F1", "white")
        square_pieces["C8"] = Bishop("C8", "black")
        square_pieces["F8"] = Bishop("F8", "black")

        square_pieces["A1"] = Rook("A1", "white")
        square_pieces["H1"] = Rook("H1", "white")
        square_pieces["A8"] = Rook("A8", "black")
        square_pieces["H8"] = Rook("H8", "black")

        square_pieces["D1"] = Queen("D1", "white")
        square_pieces["D8"] = Queen("D8", "black")

        square_pieces["E1"] = King("E1", "white")
        square_pieces["E8"] = King("E8", "black")
        return square_pieces
    def change_turn(self, bot = False):
        temp_turn = self.turn
        self.turn = self.alt_turn
        self.alt_turn = temp_turn
        self.pieces = [i for i in self.square_pieces.values() if i != None] # get pieces
        self.get_board_options() # get movement options
        self.turn_num += 1
        self.pawn_or_cap_count += 1
        self.store_ply() # store new turn
        #print(len(self.ply_info))
        #self.is_repeating()
        #set every piece to the correct x and y
        get_check = self.get_check(self.alt_turn)
        valid_moves = self.valid_moves(self.turn)
        
        sound = self.check_state()
        if sound != None and not bot:
            sound.play()
        
        for piece in self.pieces:
            square_positions = self.square_positions
            piece.rect.x, piece.rect.y = square_positions[piece.square].x + PIECE_ADJUST, square_positions[piece.square].y + PIECE_ADJUST
        if self.victory != False:
            self.can_move = False
        if not bot:
            if self.turn == "black":
                self.og_score = self.score
                #self.ai_try_moves()
                move, val = self.ai_test_move()
                #self.get_turn()
                if move != None:
                    p, m = move
                    self.move_piece(self.square_pieces[p], m)
                else:
                    print(1)
                #print(move)
    def flip(self):
        """flips the board arround so that the squares match up to the flipped positions"""
        #BOARD.image = pygame.transform.flip(BOARD.image, True, False)
        squares = self.square_positions
        pieces = self.pieces
        y_values = []
        x_values = []
        for sq in squares.values():
            y_values.insert(0, sq.y)
            x_values.insert(0, sq.x)
        count = 0
        for sq in squares.values():
            sq.y = y_values[count]
            sq.x = x_values[count]
            count += 1
        
        for piece in pieces:
            pos = self.square_positions[piece.square]
            piece.rect.x, piece.rect.y = pos.x + PIECE_ADJUST, pos.y + PIECE_ADJUST
        
        self.pieces = pieces
    def store_ply(self):
        ply_pieces = []
        for piece in self.pieces:
            if piece.name == "pawn":
                ply_pieces.append(Pawn(piece.square, piece.colour))
            elif piece.name == "knight":
                ply_pieces.append(Knight(piece.square, piece.colour))
            elif piece.name == "bishop":
                ply_pieces.append(Bishop(piece.square, piece.colour))
            elif piece.name == "rook":
                ply_pieces.append(Rook(piece.square, piece.colour))
            elif piece.name == "queen":
                ply_pieces.append(Queen(piece.square, piece.colour))
            elif piece.name == "king":
                ply_pieces.append(King(piece.square, piece.colour))
            ply_pieces[-1].has_moved = piece.has_moved
        square_pieces = {}
        for sq in self.square_positions:
            square_pieces[sq] = None
        for piece in ply_pieces:
            square_pieces[piece.square] = piece
        #placement
        sp = self.square_pieces
        placement = {}
        for s, p in sp.items():
            if p != None:
                placement[s] = p.name
        self.ply_info[self.turn_num] = (ply_pieces, self.turn, square_pieces.copy(), self.score, self.move, placement, self.promoting_piece, self.can_move, self.pawn_or_cap_count)
    def get_turn(self, turn_num = None):
        if turn_num == None:
            self.turn_num -= 1
        else:
            self.turn_num = turn_num
        self.pro_rects = []
        self.pieces, self.turn, self.square_pieces, self.score, self.move, placement, self.promoting_piece, self.can_move, self.pawn_or_cap_count = self.ply_info[self.turn_num]
        if self.turn == "white":
            self.alt_turn = "black"
        else:
            self.alt_turn = "white"
        self.store_ply()
        self.ply_info.pop(max(self.ply_info))
        for piece in self.pieces:
            square_positions = self.square_positions
            piece.rect.x, piece.rect.y = square_positions[piece.square].x + PIECE_ADJUST, square_positions[piece.square].y + PIECE_ADJUST
    
    def check_state(self):
        get_check = self.get_check(self.alt_turn)
        valid_moves = self.valid_moves(self.turn)
        sound = None
        if not get_check and valid_moves:
            sound = DRAW_SOUND
            self.victory = None
        elif valid_moves:
            sound = CHECKMATE_SOUND
            self.victory = self.alt_turn
        elif get_check:
            sound = CHECK_SOUND
        if self.is_repeating():
            sound = DRAW_SOUND
            self.victory = None
        if self.pawn_or_cap_count >= 50:
            sound = DRAW_SOUND
            self.victory = None
        return sound
    def move_piece(self, piece, spos, bot = False):
        sq = self.square_positions[spos]
        sound = MOVE_SOUND
        piece.rect.x, piece.rect.y = sq.x + PIECE_ADJUST, sq.y + PIECE_ADJUST
        self.square_pieces[piece.square] = None
        to_piece = self.square_pieces[spos]
        if piece.name == "pawn": #reset pocc
            self.pawn_or_cap_count = 0
        if to_piece != None:
            if to_piece.colour == "white": 
                self.score -= to_piece.value
            else:
                self.score += to_piece.value
            sound = CAPTURE_SOUND
            self.pawn_or_cap_count = 0
        self.move = (piece.square, spos)
        piece_square = piece.square
        old_piece = self.square_pieces[spos]
        self.square_pieces[spos] = piece
        piece.square = spos
        #en passant
        if piece.name == "pawn" and piece.square[0] != piece_square[0] and old_piece == None:
            self.square_pieces[piece.square[0] + piece_square[1]] = None
            if piece.colour == "white": 
                self.score += 1
            else:
                self.score -= 1
            sound = CAPTURE_SOUND

        #castling
        if piece.name == "king" and not piece.has_moved and spos[0] in ["C", "G"] and spos[1] in ["1", "8"]:
            if spos[0] == "C":
                #get queen side rook's movement
                square_from = "A"+ spos[1]
                square_to = "D" + spos[1]
            elif spos[0] == "G":
                #get king side rook's movement
                square_from = "H" + spos[1]
                square_to = "F" + spos[1]
            if self.square_pieces[square_from] != None:
                if not self.square_pieces[square_from].has_moved:
                    self.square_pieces[square_to] = self.square_pieces[square_from]
                    self.square_pieces[square_from] = None
                    self.square_pieces[square_to].square = square_to
                    sound = CASTLE_SOUND
        #queening
        if piece.name == "pawn" and spos[1] in ("1", "8"):
            self.promoting_piece = piece
        piece.has_moved = True
        if self.promoting_piece == None:
            self.change_turn(bot)
        
    def test_move(self, piece, spos, turn):
        piece_square = piece.square
        to_piece = self.square_pieces[spos]
        #move pieces
        self.square_pieces[piece.square] = None
        self.square_pieces[spos] = piece
        piece.square = spos

        pieces = [i for i in self.square_pieces.values() if i != None]# get pieces

        valid = True
        for p in pieces:
            if p.colour == turn:
                continue
            if not valid:
                break
            for square in p.movement():
                if square == None:
                    continue
                check_piece = self.square_pieces[square]
                if check_piece != None:
                    if check_piece.name == "king":
                        valid = False
                        break
        piece.square = piece_square
        self.square_pieces[piece.square] = piece #from prev pos
        self.square_pieces[spos] = to_piece
        return valid
    def get_board_options(self, pieces = None):
        if pieces == None:
            pieces = self.pieces
        board_options = {"white": {}, "black": {}}
        for piece in pieces:
            sq = piece.square
            board_options[piece.colour][sq] = []
            for move in piece.movement():
                if self.test_move(piece, move, piece.colour):
                    board_options[piece.colour][sq] += [move]
        self.board_options = board_options
    def get_check(self, turn):
        """return True if turn's team is giving check"""
        board_options = self.board_options.copy()
        #print(board_options)
        for squares in board_options[turn].values():
            for square in squares:
                piece = self.square_pieces[square]  
                if piece != None:   
                    if piece.name == "king":
                        return True
        return False

    def valid_moves(self, turn):
        """returns True if turn is in checkmate"""
        for moves in self.board_options[turn].values():
            if moves != []:
                return False
        return True 
    def is_repeating(self):
        placementS = []
        for t in self.ply_info:
            pieces, turn, square_pieces, score, move, placement, promoting_piece, can_move, pawn_or_cap_count = self.ply_info[t]
            placementS += [placement]
        
        for p in placementS:
            if placementS.count(p) >= 3:
                return True
    def get_promote(self):
        self.can_move = False
        piece = self.promoting_piece
        square = piece.square

        #Draw and select
        #create rects
        w = piece.rect.w
        half = w // 2
        if self.pro_rects == []:
            q_x, q_y = (piece.rect.x - piece.rect.w - half, piece.rect.y - piece.rect.h)
            r_x, r_y = (piece.rect.x - half, piece.rect.y - piece.rect.h)
            n_x, n_y = (piece.rect.x + piece.rect.w - half, piece.rect.y - piece.rect.h)
            b_x, b_y = (piece.rect.x + piece.rect.w*2 - half, piece.rect.y - piece.rect.h)

            q_rect = pygame.Rect(q_x, q_y, piece.rect.w, piece.rect.h)
            r_rect = pygame.Rect(r_x, r_y, piece.rect.w, piece.rect.h)
            n_rect = pygame.Rect(n_x, n_y, piece.rect.w, piece.rect.h)
            b_rect = pygame.Rect(b_x, b_y, piece.rect.w, piece.rect.h)
            self.pro_rects.append(q_rect)
            self.pro_rects.append(r_rect)
            self.pro_rects.append(n_rect)
            self.pro_rects.append(b_rect)
        if piece.colour == "white":
            cl_pro_rects = self.white_pro_rects
        else:
            cl_pro_rects = self.black_pro_rects
        count = 0
        for rect in self.pro_rects: #DRAW THE PIECES
            WIN.blit(cl_pro_rects[count], (rect.x, rect.y, rect.w, rect.h))
            count += 1
    def promote(self, pro_rect):
        self.can_move = True
        piece = self.promoting_piece

        index = self.pro_rects.index(pro_rect)
        if index == 0:
            self.square_pieces[piece.square] = Queen(piece.square, piece.colour)
        elif index == 1:
            self.square_pieces[piece.square] = Rook(piece.square, piece.colour)
        elif index == 2:
            self.square_pieces[piece.square] = Knight(piece.square, piece.colour)
        elif index == 3:
            self.square_pieces[piece.square] = Bishop(piece.square, piece.colour)
        new_piece = self.square_pieces[piece.square]
        new_piece.has_moved = True
        if new_piece.colour == "white": 
            self.score += new_piece.value - 1
        else:
            self.score -= new_piece.value - 1
        self.pieces.append(new_piece)
        self.promoting_piece = None
        self.pro_rects == []
        self.change_turn()
    def ai_try_moves(self, depth = 2):

        turn = self.turn
        turn_num = max(self.ply_info)
        #for piece, options in self.board_options[turn].items():
            #if self.square_pieces[piece] != None:
                #for move in options:
                #    move = self.ai_test_move(depth, self.square_pieces[piece], move)
                #moves.append(random.choice(options))
        #self.get_turn(turn_num)
        #pieces = list(self.board_options[turn].keys())
        #moves = []
        #while moves == [] and pieces != []:
        #    piece = random.choice(pieces)
        #    moves = self.board_options[turn][piece]
        #    if moves == []:
        #        pieces.remove(piece)
            #print(moves)
        #if pieces != []:
        #    self.move_piece(self.square_pieces[piece], random.choice(moves))
        pieces = list(self.board_options[turn].keys())
        moves = []
        best_l = []
        best_n = -10
        for p in self.board_options[turn]:
            for m in self.board_options[turn][p]:
                if m in self.square_pieces:
                    val = 0
                    if self.square_pieces[m] != None:
                        val = self.square_pieces[m].value
                    if val == best_n:
                        best_l.append((p, m))
                    elif val > best_n:
                        best_n = val
                        best_l = [(p, m)]
        if len(best_l) > 0:
            piece, move = random.choice(best_l)
            self.move_piece(self.square_pieces[piece], move)
                
    def ai_test_move(self, depth = 2):
        minimum = False
        turn = self.turn
        turn_num = max(self.ply_info)
        if depth == 0:
            return None, self.score
        pieces = list(self.board_options[turn].keys())
        moves = []
        best_l = {}
        for p in self.board_options[turn]:
            for m in self.board_options[turn][p]:
                if m in self.square_pieces:
                    self.move_piece(self.square_pieces[p], m, True)
                    if not minimum and turn == "white":
                        if self.score > minimum:
                            self.get_turn()
                            return None, self.score
                    #score = self.score
                    move, score = self.ai_test_move(depth - 1)
                    minimum = score
                    #score = self.score
                    self.get_turn()
                    best_l[score] = (p, m)

        if len(best_l) > 0:
            if turn == "white":
                score = max(list(best_l.keys()))
                piece, move = best_l[score]
            else:
                score = min(list(best_l.keys()))
                piece, move = best_l[score]
            return (piece, move), self.score # aaaaaaaaaaaaaaaah
        return None, self.score
        #self.move_piece(self.square_pieces[piece], move)
def get_square_pos(square):
        """Sets the piece's position to the center of square - INCOMPLETE"""
        let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        
        x = let.index(square[0]) * BOARD_rect.w//8
        y = (int(square[1]) - 9) * -1
        y = (y - 1) * BOARD_rect.h//8
        x += BOARD_rect.x
        y += BOARD_rect.y
        return (x + PIECE_ADJUST, y + PIECE_ADJUST)

#region Pieces
class Pieces():
    def __init__(self, square, colour):
        self.square = square
        self.colour = colour
        self.has_moved = False
        self.en_passant = False

        self.get_image()
        self.rect = pygame.Rect((get_square_pos(square), (PIECE_WIDTH, PIECE_HEIGHT)))
        self.pos = 0, 0
    def check_square(self, xy, take = None):
        let = ["A", "B", "C", "D", "E", "F", "G", "H"]

        add_let, add_num = xy
        current_pos = self.square

        current_let = let.index(current_pos[0]) #get value for letter
        current_num = int(current_pos[1]) #get number
        new_let, new_num = None, None

        #If the pos is within the board
        if current_let + add_let <= 7 and current_let + add_let >= 0:
            new_let = let[current_let + add_let] # set back to letter
        if current_num + add_num <= 8 and current_num + add_num >= 1:
            new_num = str(current_num + add_num)

        #If either pos not in board: return False
        if new_let == None or new_num == None:
            return None
        new_pos = new_let + new_num
        if BOARD.square_pieces[new_pos] == None: #if square is empty
            if take != True: #and if this move doesn't have to take
                return new_pos #return square as option
        elif BOARD.square_pieces[new_pos].colour != self.colour: #if the square's piece's colour is not equal to our colour
            if take != False:#and this move can take
                return new_pos #return square as option
        
    
class Pawn(Pieces):
    def get_image(self):
        self.name = "pawn"
        self.value = 1
        if self.colour == "white":
            self.image = WHITE_PAWN_IMAGE
        else:
            self.image = BLACK_PAWN_IMAGE
        self.alpha_image = self.image.copy()
        self.alpha_image.set_alpha(ALPHA)
    def movement(self):
        options = []

        i = 1
        if self.colour == "black":
            i = -1
        
        square = self.check_square((0,i), take = False) #one move forward and can't take
        if square != None:
            options.append(square)
            if self.has_moved == False:
                square = self.check_square((0, 2*i), take = False) #two moves forward and can't take
            if square != None:
                options.append(square)
        
        for x in [1,-1]: #check right and left
            square = self.check_square((x,i), take = True) #diagonally forward and must take
            if square != None:
                options.append(square)

        
        #if self.square[1] == str((4.5 + i/2 + 0.1)// 1):
        if self.square[1] in ["4","5"]:
            for x in [1, -1]:
                square = self.check_square((x, i), take = False)
                pawn_square = self.check_square((x, 0), take = True)
                if pawn_square != None and BOARD.square_pieces[pawn_square] != None:
                    prev_from, prev_to = BOARD.move
                    if prev_from[1] in ("2","7") and prev_to[1] in ("4","5") and BOARD.square_pieces[pawn_square].name == "pawn" and pawn_square == prev_to:
                        options.append(square)
        return options

class Knight(Pieces):
    def get_image(self):
        self.value = 3
        self.name = "knight"
        if self.colour == "white":
            self.image = WHITE_KNIGHT_IMAGE
        else:
            self.image = BLACK_KNIGHT_IMAGE
        self.alpha_image = self.image.copy()
        self.alpha_image.set_alpha(ALPHA)
    def movement(self):
        options = []

        for a in [1,-1]:
            for b in [2,-2]:
                square = self.check_square((a, b))
                if square != None:
                    options.append(square)
                square = self.check_square((b, a))
                if square != None:
                    options.append(square)
        return options


class Bishop(Pieces):
    def get_image(self):
        self.value = 3
        self.name = "bishop"
        if self.colour == "white":
            self.image = WHITE_BISHOP_IMAGE
        else:
            self.image = BLACK_BISHOP_IMAGE
        self.alpha_image = self.image.copy()
        self.alpha_image.set_alpha(ALPHA)
    def movement(self):
        options = []

        for a in [1,-1]:
            for b in [1,-1]:
                for i in range(1,8):
                    square = self.check_square((a*i, b*i))
                    if square == None:
                        break
                    options.append(square)
                    square = self.check_square((a*i, b*i), take = False)
                    if square == None:
                        break

        return options

class Rook(Pieces):
    def get_image(self):
        self.value = 5
        self.name = "rook"
        if self.colour == "white":
            self.image = WHITE_ROOK_IMAGE
        else:
            self.image = BLACK_ROOK_IMAGE
        self.alpha_image = self.image.copy()
        self.alpha_image.set_alpha(ALPHA)
    def movement(self):
        options = []
        for x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            a, b = x
            for i in range(1,8):
                square = self.check_square((i*a, i*b))
                if square == None:
                    break
                options.append(square)
                square = self.check_square((i*a, i*b), take = False)
                if square == None:
                    break
        return options

class Queen(Pieces):
    def get_image(self):
        self.value = 9
        self.name = "queen"
        if self.colour == "white":
            self.image = WHITE_QUEEN_IMAGE
        else:
            self.image = BLACK_QUEEN_IMAGE
        self.alpha_image = self.image.copy()
        self.alpha_image.set_alpha(ALPHA)
    def movement(self):
        options = []
        for a in [0, 1, -1]:
            for b in [0, 1, -1]:
                for i in range(1,8):
                    if a != 0 or b != 0:
                        square = self.check_square((i*a, i*b))
                        if square == None:
                            break
                        options.append(square)
                        square = self.check_square((i*a, i*b), take = False)
                        if square == None:
                            break
        return options

class King(Pieces):
    def get_image(self):
        self.value = 0
        self.name = "king"
        if self.colour == "white":
            self.image = WHITE_KING_IMAGE
        else:
            self.image = BLACK_KING_IMAGE
        self.alpha_image = self.image.copy()
        self.alpha_image.set_alpha(ALPHA)
    def movement(self):
        options = []
        for a in [0, 1, -1]:
            for b in [0, 1, -1]:
                if a != 0 or b != 0:
                    square = self.check_square((1*a, 1*b))
                    if square == None:
                        continue
                    options.append(square)
        #check to see if the king can castle
        for a in ["A", "H"]:
            square = valid_castle(self.square, a)
            if square != None and square != False:
                options.append(square)
        
        return options
#endregion
            

BOARD = Chess_Board()
def valid_castle(s, rook_square):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    rook = rook_square + s[1]
    if rook_square == "A":
        squares = ["D", "B", "C"]
        check_posis = ("C","D")
    elif rook_square == "H":
        squares = ["F","G"]
        check_posis = ("F","G")
    if rook not in BOARD.square_pieces:
        return False
    elif BOARD.square_pieces[rook] == None:
        return False
    elif BOARD.square_pieces[s].has_moved or BOARD.square_pieces[rook].has_moved:
        return False
    for sq in squares:
        if BOARD.square_pieces[sq + s[1]] != None:
            return False
    enemy_moves = []
    for p in BOARD.pieces:
        if p.colour != BOARD.turn and p.name != "king":
            enemy_moves += [p.movement()]
    for pos in check_posis:
        for moves in enemy_moves:
            if pos + s[1] in moves:
                return False
    return squares[-1] + s[1]
    
            
def draw_window():
    WIN.fill((255, 255, 255))
    pygame.draw.rect(WIN, (220, 220, 220),BOARD_rect) #board background
    WIN.blit(BOARD.image, (BOARD_rect.x, BOARD_rect.y)) #blit board
    if BOARD.selected_piece != None and BOARD.can_move == True and BOARD.selected_piece in BOARD.square_pieces:
         #blit selected_piece background
        temp = BOARD.selected_piece
        temp_piece = BOARD.square_pieces[temp]
        temp_rect = BOARD.square_positions[temp]
        img = temp_piece.alpha_image
        WIN.blit(img, (temp_rect.x, temp_rect.y))

        #blit piece options
        if temp_piece.square in BOARD.board_options[temp_piece.colour]:
            for temp_sq in BOARD.board_options[temp_piece.colour][temp_piece.square]:
                #pygame.draw.rect(WIN, (0,100,0, 60), BOARD.square_positions[temp_sq])
                if BOARD.square_pieces[temp].colour == BOARD.turn:
                    temp_rect = BOARD.square_positions[temp_sq]
                    WIN.blit(SQUARE_IMAGE, (temp_rect.x, temp_rect.y))
    for piece in BOARD.square_pieces.values(): #blit pieces
        if piece != None:
            WIN.blit(piece.image, (piece.rect.x, piece.rect.y))


    #pygame.draw.line(WIN, (0,0,0), (BOARD_rect.x - LINE_WIDTH, BOARD_rect.y - LINE_WIDTH), (BOARD_rect.x + BOARD_rect.w, BOARD_rect.y - LINE_WIDTH), LINE_WIDTH * 2) #top
    #pygame.draw.line(WIN, (0,0,0), (BOARD_rect.x - LINE_WIDTH, BOARD_rect.y + BOARD_rect.h), (BOARD_rect.x + BOARD_rect.w, BOARD_rect.y + BOARD_rect.h), LINE_WIDTH * 2) #bottom
    #pygame.draw.line(WIN, (0,0,0), (BOARD_rect.x - LINE_WIDTH, BOARD_rect.y - LINE_WIDTH), (BOARD_rect.x - LINE_WIDTH, BOARD_rect.y + BOARD_rect.h), LINE_WIDTH * 2) #left
    #pygame.draw.line(WIN, (0,0,0), (BOARD_rect.x  + BOARD_rect.w, BOARD_rect.y - LINE_WIDTH), (BOARD_rect.x + BOARD_rect.w, BOARD_rect.y + BOARD_rect.h), LINE_WIDTH * 2) #right

    #region text
    if BOARD.victory == False:
        turn = BOARD.turn.capitalize()
        if BOARD.score > 0:
            score = F"+{BOARD.score}"
        else:
            score = F"{BOARD.score}"
        txt = f"{turn}'s turn({score})"
    elif BOARD.victory == None:
        txt = "Draw!"
    else:
        txt = f"{BOARD.victory.capitalize()} Wins!"
    txt_width, txt_height = fonts["arial"].size(txt)
    label = fonts["arial"].render((txt), 1, (0, 0, 0))
    WIN.blit(label, (WIDTH//2 - txt_width // 2, 10))
    if BOARD.victory != False:
        WIN.blit(CHESS_BOARD_ALPHA_IMAGE, (BOARD_rect.x, BOARD_rect.y))
    if BOARD.promoting_piece != None:
        BOARD.get_promote()


    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    count = 0
    pressed = False
    BOARD.get_board_options()
    START_SOUND.play()
    #BOARD.store_ply()
    while run:
        count += 1
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_RETURN:
                    #return True
                    print(BOARD.board_options)
                    print(BOARD.turn_num)
                    print(len(BOARD.ply_info))
                elif event.key == pygame.K_f:
                    BOARD.flip()
                elif event.key == pygame.K_LEFT and BOARD.turn_num > 0 and BOARD.can_move and BOARD.selected_piece == None:
                    BOARD.get_turn()
                    BOARD.get_board_options()
                    break
                elif event.key == pygame.K_r:
                    return True
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #if the mouse was pressed down and is the left button
                for piece in BOARD.pieces:
                    if piece.rect.collidepoint(pos):
                        BOARD.selected_piece = piece.square
                        pressed = True
                        break
                if not pressed:
                    for pro_rect in BOARD.pro_rects:
                        if pro_rect.collidepoint(pos):
                            BOARD.promote(pro_rect)
            elif event.type == pygame.MOUSEBUTTONUP and pressed == True and event.button == 1: #if the mouse was released and is the right button
                pressed = False
                BOARD.selected_piece = None
                for spos, sq in BOARD.square_positions.items():
                    if BOARD.can_move and sq.collidepoint(pos) and piece.square in BOARD.board_options[BOARD.turn]:
                        if spos in BOARD.board_options[BOARD.turn][piece.square]:
                            BOARD.move_piece(piece, spos)
                            break
                    else: #return piece
                        sq_pos = BOARD.square_positions[piece.square]
                        piece.rect.x, piece.rect.y = sq_pos.x + PIECE_ADJUST, sq_pos.y + PIECE_ADJUST
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #return piece on right click
                pressed = False
                BOARD.selected_piece = None
                sq_pos = BOARD.square_positions[piece.square]
                piece.rect.x, piece.rect.y = sq_pos.x + PIECE_ADJUST, sq_pos.y + PIECE_ADJUST

        if pygame.mouse.get_pressed()[0] and pressed == True: #if left mouse button is being held and a piece has been pressed
            piece.rect.x, piece.rect.y = pos
            piece.rect.x -= PIECE_WIDTH//2
            piece.rect.y -= PIECE_HEIGHT//2
        draw_window()

while main():
    #print("reset")
    BOARD.__init__()