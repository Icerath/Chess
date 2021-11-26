import pygame
import os
import random
import time
import sys
#import datetime
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
#WIN = pygame.display.set_mode((1920, 1080))
FPS = 45
AI_MODE = True
FULL_AI_MODE = True
AI_COLOUR = "black"
ALPHA = 64
pygame.display.set_caption("Chess")
MIN_WH = min(WIDTH, HEIGHT)
DIV = 2
wh = MIN_WH * 0.75
SMALL_IS = 60
#BOARD_rect = pygame.Rect(WIDTH // div -  wh // 2, (HEIGHT // div - wh // 2) + WIDTH // 25, wh, wh)
BOARD_rect = pygame.Rect(WIDTH // DIV -  wh // 2, (HEIGHT // DIV - wh // 2) + WIDTH // 50, wh, wh)
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
WHITE_PAWN_ALPHA = WHITE_PAWN_IMAGE.copy()
WHITE_PAWN_ALPHA = WHITE_PAWN_ALPHA.convert_alpha()
WHITE_PAWN_ALPHA.set_alpha(ALPHA)
WHITE_PAWN_SMALL = pygame.transform.smoothscale(WHITE_PAWN_IMAGE.copy(), (SMALL_IS, SMALL_IS))

WHITE_BISHOP_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_BISHOP.png"))
WHITE_BISHOP_IMAGE = pygame.transform.smoothscale(WHITE_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
WHITE_BISHOP_ALPHA = WHITE_BISHOP_IMAGE.copy()
WHITE_BISHOP_ALPHA = WHITE_BISHOP_ALPHA.convert_alpha()
WHITE_BISHOP_ALPHA.set_alpha(ALPHA)
WHITE_BISHOP_SMALL = pygame.transform.smoothscale(WHITE_BISHOP_IMAGE.copy(), (SMALL_IS, SMALL_IS))

WHITE_KNIGHT_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_KNIGHT.png"))
WHITE_KNIGHT_IMAGE = pygame.transform.smoothscale(WHITE_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
WHITE_KNIGHT_ALPHA = WHITE_KNIGHT_IMAGE.copy()
WHITE_KNIGHT_ALPHA = WHITE_KNIGHT_ALPHA.convert_alpha()
WHITE_KNIGHT_ALPHA.set_alpha(ALPHA)
WHITE_KNIGHT_SMALL = pygame.transform.smoothscale(WHITE_KNIGHT_IMAGE.copy(), (SMALL_IS, SMALL_IS))

WHITE_ROOK_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_ROOK.png"))
WHITE_ROOK_IMAGE = pygame.transform.smoothscale(WHITE_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
WHITE_ROOK_ALPHA = WHITE_ROOK_IMAGE.copy()
WHITE_ROOK_ALPHA = WHITE_ROOK_ALPHA.convert_alpha()
WHITE_ROOK_ALPHA.set_alpha(ALPHA)
WHITE_ROOK_SMALL = pygame.transform.smoothscale(WHITE_ROOK_IMAGE.copy(), (SMALL_IS, SMALL_IS))

WHITE_KING_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_KING.png"))
WHITE_KING_IMAGE = pygame.transform.smoothscale(WHITE_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
WHITE_KING_ALPHA = WHITE_KING_IMAGE.copy()
WHITE_KING_ALPHA = WHITE_KING_ALPHA.convert_alpha()
WHITE_KING_ALPHA.set_alpha(ALPHA)
WHITE_KING_SMALL = pygame.transform.smoothscale(WHITE_KING_IMAGE.copy(), (SMALL_IS, SMALL_IS))

WHITE_QUEEN_IMAGE = pygame.image.load(os.path.join("Assets", "WHITE_QUEEN.png"))
WHITE_QUEEN_IMAGE = pygame.transform.smoothscale(WHITE_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
WHITE_QUEEN_ALPHA = WHITE_QUEEN_IMAGE.copy()
WHITE_QUEEN_ALPHA = WHITE_QUEEN_ALPHA.convert_alpha()
WHITE_QUEEN_ALPHA.set_alpha(ALPHA)
WHITE_QUEEN_SMALL = pygame.transform.smoothscale(WHITE_QUEEN_IMAGE.copy(), (SMALL_IS, SMALL_IS))


BLACK_PAWN_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_PAWN.png"))
BLACK_PAWN_IMAGE = pygame.transform.smoothscale(BLACK_PAWN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
BLACK_PAWN_ALPHA = BLACK_PAWN_IMAGE.copy()
BLACK_PAWN_ALPHA = BLACK_PAWN_ALPHA.convert_alpha()
BLACK_PAWN_ALPHA.set_alpha(ALPHA)
BLACK_PAWN_SMALL = pygame.transform.smoothscale(BLACK_PAWN_IMAGE.copy(), (SMALL_IS, SMALL_IS))

BLACK_BISHOP_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_BISHOP.png"))
BLACK_BISHOP_IMAGE = pygame.transform.smoothscale(BLACK_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
BLACK_BISHOP_ALPHA = BLACK_BISHOP_IMAGE.copy()
BLACK_BISHOP_ALPHA = BLACK_BISHOP_ALPHA.convert_alpha()
BLACK_BISHOP_ALPHA.set_alpha(ALPHA)
BLACK_BISHOP_SMALL = pygame.transform.smoothscale(BLACK_BISHOP_IMAGE.copy(), (SMALL_IS, SMALL_IS))

BLACK_KNIGHT_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_KNIGHT.png"))
BLACK_KNIGHT_IMAGE = pygame.transform.smoothscale(BLACK_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
BLACK_KNIGHT_ALPHA = BLACK_KNIGHT_IMAGE.copy()
BLACK_KNIGHT_ALPHA = BLACK_KNIGHT_ALPHA.convert_alpha()
BLACK_KNIGHT_ALPHA.set_alpha(ALPHA)
BLACK_KNIGHT_SMALL = pygame.transform.smoothscale(BLACK_KNIGHT_IMAGE.copy(), (SMALL_IS, SMALL_IS))

BLACK_ROOK_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_ROOK.png"))
BLACK_ROOK_IMAGE = pygame.transform.smoothscale(BLACK_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
BLACK_ROOK_ALPHA = BLACK_ROOK_IMAGE.copy()
BLACK_ROOK_ALPHA = BLACK_ROOK_ALPHA.convert_alpha()
BLACK_ROOK_ALPHA.set_alpha(ALPHA)
BLACK_ROOK_SMALL = pygame.transform.smoothscale(BLACK_ROOK_IMAGE.copy(), (SMALL_IS, SMALL_IS))

BLACK_KING_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_KING.png"))
BLACK_KING_IMAGE = pygame.transform.smoothscale(BLACK_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
BLACK_KING_ALPHA = BLACK_KING_IMAGE.copy()
BLACK_KING_ALPHA = BLACK_KING_ALPHA.convert_alpha()
BLACK_KING_ALPHA.set_alpha(ALPHA)
BLACK_KING_SMALL = pygame.transform.smoothscale(BLACK_KING_IMAGE.copy(), (SMALL_IS, SMALL_IS))

BLACK_QUEEN_IMAGE = pygame.image.load(os.path.join("Assets", "BLACK_QUEEN.png"))
BLACK_QUEEN_IMAGE = pygame.transform.smoothscale(BLACK_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)).convert_alpha()
BLACK_QUEEN_ALPHA = BLACK_QUEEN_IMAGE.copy()
BLACK_QUEEN_ALPHA = BLACK_QUEEN_ALPHA.convert_alpha()
BLACK_QUEEN_ALPHA.set_alpha(ALPHA)
BLACK_QUEEN_SMALL = pygame.transform.smoothscale(BLACK_QUEEN_IMAGE.copy(), (SMALL_IS, SMALL_IS))

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
        self.botless_turn = "white"
        self.prev_time = None
        self.captured_pieces = []
        self.test_count = 0
        self.check_square_time = 0
        self.get_check_time = 0
        self.check_state_time = 0
        self.get_threats_time = 0
        self.get_turn_time = 0
        self.store_time = 0
        self.gbo_time = 0
        self.test_move_time = 0
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
        self.board_options = {}
        self.turn = "white"
        self.alt_turn = "black"
        self.turn_num = 0
        self.ply_info = {}
        self.ply_pieces = {}
        self.ply_turn = {}
        self.store_ply()
        self.score_direction = {"white": 1, "black": -1}
        #promoting rects
        self.white_pro_rects = [WHITE_QUEEN_IMAGE, WHITE_ROOK_IMAGE, WHITE_KNIGHT_IMAGE, WHITE_BISHOP_IMAGE]
        self.black_pro_rects = [BLACK_QUEEN_IMAGE, BLACK_ROOK_IMAGE, BLACK_KNIGHT_IMAGE, BLACK_BISHOP_IMAGE]

        self.selected_piece = None
        self.victory = False
        offset = 80
        #clock1 = pygame.Rect(offset, HEIGHT//2 - 60, 240, 120)
        #clock2 = pygame.Rect(WIDTH - offset - 240, HEIGHT//2 - 60, 240, 120)
        #clock1 = pygame.Rect(offset, HEIGHT//2 - 240, 240, 120)
        #clock2 = pygame.Rect(offset, HEIGHT//2 + 120, 240, 120)
        clock1 = pygame.Rect(WIDTH - offset - 240, HEIGHT//2 + 60, 240, 120)
        clock2 = pygame.Rect(WIDTH - offset - 240, HEIGHT//2 - 180, 240, 120)
        self.clock1 = ["white", 30 * 60, clock1]
        self.clock2 = ["black", 30 * 60, clock2]
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
    def change_turn(self, bot = False, sound = MOVE_SOUND):
        if not bot:
            self.botless_turn = self.turn
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
        #get_check = self.get_check(self.alt_turn)
        #valid_moves = self.valid_moves(self.turn)
        if bot and self.no_valid_moves():
            self.score += 1000 * self.score_direction[self.alt_turn]
        if not bot:
            sound = self.check_state(sound)
            if sound != None:
                sound.play()
                if not bot:
                    draw_window()
        
            #for piece in self.pieces:
                #square_positions = self.square_positions
                #piece.rect.x, piece.rect.y = square_positions[piece.square].x + PIECE_ADJUST, square_positions[piece.square].y + PIECE_ADJUST
            if self.victory != False:
                self.can_move = False
            if AI_MODE:
                if FULL_AI_MODE or self.turn == AI_COLOUR:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                    draw_window()
                    self.og_score = self.score
                    self.botless_turn = self.turn
                    #move, val = self.ai_test_move()
                    move, val = self.my_alpha_beta(1000)
                    if move != None:
                        p, m = move
                        self.move_piece(self.square_pieces[p], m)
                    print("function calls:", self.test_count)
                    print("store time:", self.store_time)
                    print("get turn time:", self.get_turn_time)
                    print("gbo time:", self.gbo_time)
                    print("test move time:", self.test_move_time)
                    print("get threats time:", self.get_threats_time)
                    print("check square time:", self.check_square_time)
    def flip(self):
        """flips the board arround so that the squares match up to the flipped positions"""
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
        #for piece in pieces:
        #    pos = self.square_positions[piece.square]
        #    piece.rect.x, piece.rect.y = pos.x + PIECE_ADJUST, pos.y + PIECE_ADJUST
        self.clock1[2].y, self.clock2[2].y = self.clock2[2].y, self.clock1[2].y
        self.pieces = pieces
    def store_ply(self):
        ply_pieces = []
        start_time = time.time()
        for piece in self.pieces:
            ply_pieces.append(type(piece)(piece.square, piece.colour))
            ply_pieces[-1].has_moved = piece.has_moved
        self.store_time += time.time() - start_time
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
        
        self.ply_info[self.turn_num] = (
            ply_pieces, self.turn, square_pieces.copy(), self.score, self.move,
            placement, self.promoting_piece, self.can_move, self.pawn_or_cap_count,
            self.captured_pieces)
    def get_turn(self, turn_num = None):
        start_time = time.time()
        if turn_num == None:
            self.turn_num -= 1
        else:
            self.turn_num = turn_num
        self.pro_rects = []
        self.pieces, self.turn, self.square_pieces, self.score, self.move, placement, self.promoting_piece, self.can_move, self.pawn_or_cap_count, self.captured_pieces = self.ply_info[self.turn_num]
        if self.turn == "white":
            self.alt_turn = "black"
        else:
            self.alt_turn = "white"
        self.store_ply()
        self.ply_info.pop(max(self.ply_info))
        #for piece in self.pieces:
        #    square_positions = self.square_positions
        #    piece.rect.x, piece.rect.y = square_positions[piece.square].x + PIECE_ADJUST, square_positions[piece.square].y + PIECE_ADJUST
        self.get_turn_time += time.time() - start_time
    def check_state(self, sound = MOVE_SOUND):
        start_time = time.time()
        get_check = self.get_check()
        valid_moves = self.no_valid_moves()
        if not get_check and valid_moves:
            sound = DRAW_SOUND
            self.victory = None
        elif valid_moves:
            sound = CHECKMATE_SOUND
            self.victory = self.alt_turn
            self.score = 1000 * (self.score_direction[self.alt_turn])
        elif get_check:
            sound = CHECK_SOUND
        if self.is_repeating():
            sound = DRAW_SOUND
            self.victory = None
        if self.pawn_or_cap_count >= 50:
            sound = DRAW_SOUND
            self.victory = None
        self.check_state_time += time.time() - start_time
        return sound
    def move_piece(self, piece, spos, bot = False):
        sq = self.square_positions[spos]
        sound = MOVE_SOUND
        #piece.rect.x, piece.rect.y = sq.x + PIECE_ADJUST, sq.y + PIECE_ADJUST
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
            if not bot:
                self.captured_pieces.append((to_piece.small_image, to_piece.colour))
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
            self.change_turn(bot, sound)
    def test_move(self, piece, spos, turn):
        attackers = 0
        start_time = time.time()
        piece_square = piece.square
        to_piece = self.square_pieces[spos]
        #move pieces
        self.square_pieces[piece.square] = None
        self.square_pieces[spos] = piece
        piece.square = spos

        pieces = [i for i in self.square_pieces.values() if i != None]# get pieces

        valid = True
        for p in pieces:
            if p.name == "king" and p.colour == self.turn:  
                attackers = p.get_threats()
                break
        piece.square = piece_square
        self.square_pieces[piece.square] = piece #from prev pos
        self.square_pieces[spos] = to_piece
        self.test_move_time += time.time() - start_time
        return attackers
    def get_board_options(self, pieces = None):
        self.test_count += 1
        start_time = time.time()
        if pieces == None:
            pieces = self.pieces
        board_options = {}
        #for pot_king in pieces:
        #    if pot_king.name == "king" and pot_king.colour == self.turn:
        #        attkers = pot_king.get_threats()
        #        break
        for piece in pieces:
            if piece.colour != self.turn:
                continue
            #if piece.name != "king" and attkers >= 2:
            #    print("shortened")
            #    continue
            sq = piece.square
            board_options[sq] = []
            for move in piece.movement():
                attackers = self.test_move(piece, move, piece.colour)
                if attackers == 0:
                    board_options[sq].append(move)
        self.board_options = board_options
        self.gbo_time += time.time() - start_time
    def get_check(self):
        """return True if turn's team is giving check"""
        start_time = time.time()
        board_options = self.board_options
        for piece in self.pieces:
            if piece.name == "king" and piece.colour == self.turn:
                if piece.get_threats() > 0:
                    self.get_check_time += time.time() - start_time
                    return True
        self.get_check_time += time.time() - start_time
        return False
    def no_valid_moves(self):
        """returns True if turn is in checkmate"""
        for moves in self.board_options.values():
            if moves != []:
                return False
        return True 
    def is_repeating(self):
        placementS = []
        for t in self.ply_info:
            pieces, turn, square_pieces, score, move, placement, promoting_piece, can_move, pawn_or_cap_count, captured_pieces = self.ply_info[t]
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
        n_sign = 1
        if piece.colour == "white":
            n_sign = -1
        if self.pro_rects == []:
            q_x, q_y = (piece.rect.x - piece.rect.w - half, piece.rect.y + (n_sign * piece.rect.h))
            r_x, r_y = (piece.rect.x - half, piece.rect.y + (n_sign * piece.rect.h))
            n_x, n_y = (piece.rect.x + piece.rect.w - half, piece.rect.y + (n_sign * piece.rect.h))
            b_x, b_y = (piece.rect.x + piece.rect.w*2 - half, piece.rect.y + (n_sign * piece.rect.h))

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
    def update_clocks(self, bot = False):
        WIN.fill((255, 255, 255), self.clock1[2])
        WIN.fill((255, 255, 255), self.clock2[2])

        #if not bot:
        if self.turn_num > 0:
            if self.botless_turn == "white":
                self.clock1[1] -= 1/FPS
            else:
                self.clock2[1] -= 1/FPS
        #else:
        #    self.clock2[1] -= 1/FPS
        
        for clock in [self.clock1, self.clock2]:
            pygame.draw.rect(WIN, (0, 0, 0), clock[2], 1)
            hours, minutes, seconds = seconds_to_time(round(clock[1]))
            txt = f"{hours:02}:{minutes:02}:{seconds:02}"
            txt_width, txt_height = fonts["arial"].size(txt)
            label = fonts["arial"].render((txt), 1, (0, 0, 0))
            WIN.blit(label, (clock[2].x + clock[2].w / 2 - txt_width / 2, clock[2].y + clock[2].h / 2 - txt_height / 2  ))
        if not bot:
            w_x = self.clock1[2].x
            b_x = w_x
            w_y = self.clock2[2].y - 60
            b_y = self.clock1[2].y - 60
            for piece in self.captured_pieces:
                image, colour = piece
                x, y = w_x, w_y
                if colour == "black":
                    x, y = b_x, b_y
                WIN.blit(image, (x, y))
                if colour == "white":
                    w_x += 40
                else:
                    b_x += 40
    def ai_test_move(self, depth = 2):
        my_time = round(time.time() * FPS)
        if my_time != self.prev_time and my_time % 1 == 0:
            self.prev_time = my_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.update_clocks(True)
            pygame.display.update()
        turn = self.turn
        if depth == 0:
            return None, self.score
        best_l = {}
        board_options = self.board_options.copy()
        for p in board_options:
            for m in board_options[p]:
                if p in self.square_pieces:
                    self.move_piece(self.square_pieces[p], m, True)
                    score = self.score
                    if self.victory == None:
                        score = 0
                    else:
                        move, score = self.ai_test_move(depth - 1)
                    self.get_turn()
                    if score not in best_l:
                        best_l[score] = []
                    best_l[score].append((p, m))
        if len(best_l) > 0:
            temp_func = max
            if turn == "black":
                temp_func = min
            score = temp_func(list(best_l.keys()))
            piece, move = random.choice(best_l[score])
            return (piece, move), score
        return None, self.score
        #self.move_piece(self.square_pieces[piece], move)
    def my_alpha_beta(self, best_scoree, depth = 2):
        my_time = round(time.time() * FPS)
        if my_time != self.prev_time and my_time % 1 == 0:
            self.prev_time = my_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.update_clocks(True)
            pygame.display.update()
        turn = self.turn
        if depth == 0:
            return None, self.score
        best_l = {}
        board_options = self.board_options.copy()
        for p in board_options:
            for m in board_options[p]:
                if p in self.square_pieces:
                    abandon = False
                    self.move_piece(self.square_pieces[p], m, True)
                    if self.turn == "white":
                        if self.score > best_scoree:
                            self.get_turn()
                            abandon = True
                    score = self.score
                    if self.victory == None:
                        score = 0
                    elif not abandon:
                        move, score = self.my_alpha_beta(best_scoree, depth - 1)
                    else:
                        continue
                    self.get_turn()
                    if score not in best_l:
                        best_l[score] = []
                    best_l[score].append((p, m))
                    if self.turn == "black":
                        best_scoree = min(best_scoree, score)
                    
        if len(best_l) > 0:
            temp_func = max
            if turn == "black":
                temp_func = min
            score = temp_func(list(best_l.keys()))
            piece, move = random.choice(best_l[score])
            return (piece, move), score
        return None, self.score
        #self.move_piece(self.square_pieces[piece], move)
def seconds_to_time(seconds):
    minutes = seconds // 60
    seconds = seconds - minutes * 60

    hours = minutes // 60
    minutes = minutes - hours * 60

    return (hours, minutes, seconds)
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
        start_time = time.time()
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
                BOARD.check_square_time += time.time() - start_time
                return new_pos #return square as option
        elif BOARD.square_pieces[new_pos].colour != self.colour: #if the square's piece's colour is not equal to our colour
            if take != False:#and this move can take
                BOARD.check_square_time += time.time() - start_time
                return new_pos #return square as option
        
    
class Pawn(Pieces):
    def get_image(self):
        self.name = "pawn"
        self.value = 1
        if self.colour == "white":
            self.image = WHITE_PAWN_IMAGE
            self.alpha_image = WHITE_PAWN_ALPHA
            self.small_image = WHITE_PAWN_SMALL
        else:
            self.image = BLACK_PAWN_IMAGE
            self.alpha_image = BLACK_PAWN_ALPHA
            self.small_image = BLACK_PAWN_SMALL
    def movement(self):
        options = []

        i = 1
        if self.colour == "black":
            i = -1
        
        square = self.check_square((0,i), take = False) #one move forward and can't take
        if square != None:
            options.append(square)
            if not self.has_moved:
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
            self.alpha_image = WHITE_KNIGHT_ALPHA
            self.small_image = WHITE_KNIGHT_SMALL
        else:
            self.image = BLACK_KNIGHT_IMAGE
            self.alpha_image = BLACK_KNIGHT_ALPHA
            self.small_image = BLACK_KNIGHT_SMALL
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
            self.alpha_image = WHITE_BISHOP_ALPHA
            self.small_image = WHITE_BISHOP_SMALL
        else:
            self.image = BLACK_BISHOP_IMAGE
            self.alpha_image = BLACK_BISHOP_ALPHA
            self.small_image = BLACK_BISHOP_SMALL
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
            self.alpha_image = WHITE_ROOK_ALPHA
            self.small_image = WHITE_ROOK_SMALL
        else:
            self.image = BLACK_ROOK_IMAGE
            self.alpha_image = BLACK_ROOK_ALPHA
            self.small_image = BLACK_ROOK_SMALL
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
            self.alpha_image = WHITE_QUEEN_ALPHA
            self.small_image = WHITE_QUEEN_SMALL
        else:
            self.image = BLACK_QUEEN_IMAGE
            self.alpha_image = BLACK_QUEEN_ALPHA
            self.small_image = BLACK_QUEEN_SMALL
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
            self.alpha_image = WHITE_KING_ALPHA
            self.small_image = WHITE_KING_SMALL
        else:
            self.image = BLACK_KING_IMAGE
            self.alpha_image = BLACK_KING_ALPHA
            self.small_image = BLACK_KING_SMALL
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
    def get_threats(self):
        attackers = 0
        start_time = time.time()
        i = 1
        if self.colour == "black":
            i = -1
        operations = []
        #pawns
        coords = [(1, 1*i), (-1, 1*i)]
        operations.append([Pawn, coords, True])
        #knights
        coords = [(1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]
        operations.append([Knight, coords, None])
        #bishops
        lcoords = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],
                  [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)],
                  [(-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)],
                  [(-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7)]]
        for coords in lcoords:
            operations.append([Bishop, coords, None])
        #rooks
        lcoords = [[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
                  [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
                  [(-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)],
                  [(0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)]]
        for coords in lcoords:
            operations.append([Rook, coords, None])
        let = ["A", "B", "C", "D", "E", "F", "G", "H"]
        a, b = self.square[0], int(self.square[1])
        a = let.index(a) + 1
        for op in operations:
            for coords in op[1]:
                na, nb = coords
                if not a + na <= 8 or not a + na >= 1:
                    break
                if not b + nb <= 8 or not b + nb >= 1:
                    break
                new_let = let[a + na - 1]
                new_num = str(b + nb)
                new_pos = new_let + new_num
                if type(BOARD.square_pieces[new_pos]) == op[0]:
                    if BOARD.square_pieces[new_pos].colour != self.colour:
                        attackers += 1
                #elif BOARD.square_pieces[new_pos] != None:
                #    if BOARD.square_pieces[new_pos].colour != self.colour:
                #        print(type(BOARD.square_pieces[new_pos]))
                if op[0] == Rook or op[0] == Bishop:
                    if type(BOARD.square_pieces[new_pos]) == Queen:
                        if BOARD.square_pieces[new_pos].colour != self.colour:
                            attackers += 1
                    if BOARD.square_pieces[new_pos] != None:
                        break
        BOARD.get_threats_time += time.time() - start_time
        return attackers

            

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
    if BOARD.selected_piece == None:
        for piece in BOARD.pieces:
            square_positions = BOARD.square_positions
            piece.rect.x, piece.rect.y = square_positions[piece.square].x + PIECE_ADJUST, square_positions[piece.square].y + PIECE_ADJUST
    WIN.fill((255,255,255))
    WIN.fill((40, 50, 60))
    BOARD.update_clocks()
    pygame.draw.rect(WIN, (220, 220, 220),BOARD_rect) #board background
    WIN.blit(BOARD.image, (BOARD_rect.x, BOARD_rect.y)) #blit board
    if BOARD.move != ("",""):
            for sq in BOARD.move:
                pos = BOARD.square_positions[sq]
                WIN.blit(SQUARE_IMAGE, (pos.x, pos.y))
    if BOARD.selected_piece != None and BOARD.can_move == True and BOARD.selected_piece in BOARD.square_pieces:
         #blit selected_piece background
        temp = BOARD.selected_piece
        temp_piece = BOARD.square_pieces[temp]
        temp_rect = BOARD.square_positions[temp]
        img = temp_piece.alpha_image
        WIN.blit(img, (temp_rect.x, temp_rect.y))
        #blit last move
        #blit piece options
        if temp_piece.square in BOARD.board_options:
            for temp_sq in BOARD.board_options[temp_piece.square]:
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
    label = fonts["arial"].render((txt), 1, (180, 190, 200))
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
    #time = [hour, min, sec]
    #clock1 = (colour, time)
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
                    #print(BOARD.board_options)
                    print(BOARD.square_pieces)
                    #print(BOARD.turn_num)
                    print(len(BOARD.ply_info))
                elif event.key == pygame.K_f:
                    BOARD.flip()
                elif event.key == pygame.K_s:
                    move, val = BOARD.my_alpha_beta(1000)
                    if move != None:
                        p, m = move
                        BOARD.move_piece(BOARD.square_pieces[p], m)
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
                    if BOARD.can_move and sq.collidepoint(pos) and piece.square in BOARD.board_options:
                        if spos in BOARD.board_options[piece.square]:
                            #piece.rect.x, piece.rect.y = BOARD.square_positions[spos].x + PIECE_ADJUST, BOARD.square_positions[spos].y + PIECE_ADJUST
                            #draw_window()
                            BOARD.move_piece(piece, spos)
                            break
                    #else: #return piece
                        #sq_pos = BOARD.square_positions[piece.square]
                        #piece.rect.x, piece.rect.y = sq_pos.x + PIECE_ADJUST, sq_pos.y + PIECE_ADJUST
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #return piece on right click
                pressed = False
                BOARD.selected_piece = None
                #sq_pos = BOARD.square_positions[piece.square]
                #piece.rect.x, piece.rect.y = sq_pos.x + PIECE_ADJUST, sq_pos.y + PIECE_ADJUST

        if pygame.mouse.get_pressed()[0] and pressed == True: #if left mouse button is being held and a piece has been pressed
            piece.rect.x, piece.rect.y = pos
            piece.rect.x -= PIECE_WIDTH//2
            piece.rect.y -= PIECE_HEIGHT//2
        draw_window()

if __name__ == "__main__":
    while main():
        BOARD.__init__()
