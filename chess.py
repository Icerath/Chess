import pygame
import os
import random
import time
import sys

pygame.init()

display_info = pygame.display.Info()
WIDTH, HEIGHT = display_info.current_w, display_info.current_h
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME, pygame.FULLSCREEN)
FPS = 60
AI_MODE = True
FULL_AI_MODE = False
DEPTH = 3
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

START_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Sound', 'START.wav'))
MOVE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Sound','MOVE.wav'))
CAPTURE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Sound', 'CAPTURE.wav'))
CASTLE_SOUND = MOVE_SOUND
CHECK_SOUND = pygame.mixer.Sound(os.path.join('Assets','Sound','SILENCE.wav'))
CHECKMATE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Sound','GENERIC_NOTIFY.wav'))
DRAW_SOUND = pygame.mixer.Sound(os.path.join('Assets','Sound','GENERIC_NOTIFY.wav'))
#endregion
#Classes
class Chess_Board():
    pawn_time = bishop_time = knight_time = rook_time = queen_time = king_time = 0
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
        
        self.score = self.get_score()
        if bot and self.no_valid_moves():
            self.score += 20000 * self.score_direction[self.alt_turn]
        if not bot:
            sound = self.check_state(sound)
            if sound != None:
                sound.play()
                #if not bot:
                #    draw_window()
        
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
                    #self.botless_turn = self.turn
                    #move, val = self.ai_test_move()
                    start_time = time.time()
                    #move, val = self.my_alpha_beta(50000)
                    #score, move = self.alpha_beta_black(-float("inf"), float("inf"), DEPTH)
                    move = self.start_alpha_beta()
                    if move != None:
                        p, m = move
                        self.move_piece(self.square_pieces[p], m)
                    do_time = True
                    if do_time:
                        print("function calls:", self.test_count)
                        print("store turn:", self.store_time)
                        print("get turn time:", self.get_turn_time)
                        print("gbo time:", self.gbo_time)
                        print("  pawn time", self.pawn_time)
                        print("  knight time", self.knight_time)
                        print("  bishop time", self.bishop_time)
                        print("  rook time", self.rook_time)
                        print("  queen time", self.queen_time)
                        print("  king time", self.king_time)
                        print("test move time:", self.test_move_time)
                        print("get threats time:", self.get_threats_time)
                        print("check square time:", self.check_square_time)
                        print("total time:", time.time() - start_time)
                        print()
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
            ply_pieces, self.turn, square_pieces.copy(), self.move,
            placement, self.promoting_piece, self.can_move, self.pawn_or_cap_count,
            self.captured_pieces.copy())
    def get_turn(self, turn_num = None):
        start_time = time.time()
        if turn_num == None:
            self.turn_num -= 1
        else:
            self.turn_num = turn_num
        self.pro_rects = []
        self.pieces, self.turn, self.square_pieces, self.move, placement, self.promoting_piece, self.can_move, self.pawn_or_cap_count, self.captured_pieces = self.ply_info[self.turn_num]
        if self.turn == "white":
            self.alt_turn = "black"
        else:
            self.alt_turn = "white"
        self.score = self.get_score()
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
        to_piece = self.square_pieces[spos]
        #if type(to_piece) == King:
        #    print(self.board_options)
        #    while True:
        #        pygame.display.update()
        #        draw_window()
        self.square_pieces[piece.square] = None
        if piece.name == "pawn": #reset pocc
            self.pawn_or_cap_count = 0
        if to_piece != None:
    
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


        piece.has_moved = True
        #queening
        did_promote = False
        if type(piece) == Pawn and piece.square[1] in ("1", "8"):
            if not bot:
                #print(2)
                self.promoting_piece = piece
            else:
                #self.promoting_piece = piece
                #self.promote(Queen, bot)   
                print(piece.name, piece.square)
                new_piece = Queen(piece.square, piece.colour)
                new_piece.has_moved = True
                self.pieces[self.pieces.index(piece)] = new_piece
                self.square_pieces[new_piece.square] = new_piece
        if self.promoting_piece == None:
            self.change_turn(bot, sound)
    def test_move(self, piece, spos):
        attackers = 0
        start_time = time.time()
        piece_square = piece.square
        to_piece = self.square_pieces[spos]
        #move pieces
        self.square_pieces[piece.square] = None
        self.square_pieces[spos] = piece
        piece.square = spos

        #pieces = [i for i in self.square_pieces.values() if i != None and i.colour == self.turn]# get pieces
        pieces = self.pieces

        valid = True
        for p in pieces:
            if type(p) == King and p.colour == self.turn:
                attackers = p.get_threats(initial = False)
                break
        piece.square = piece_square
        self.square_pieces[piece.square] = piece #from prev pos
        self.square_pieces[spos] = to_piece
        self.test_move_time += time.time() - start_time
        return attackers
    def get_board_options(self):
        self.test_count += 1
        start_time = time.time()
        board_options = {}
        pieces = [p for p in self.pieces if p.colour == self.turn]
        temp_bool = False
        for k in pieces:
            if type(k) == King:
                king = k
                temp_bool = True
                break
        attackers, protectors = king.get_threats(initial = True)
        for p in pieces:
            if p not in protectors and type(p) != King:
                board_options[p.square] = p.movement()
        if attackers == 0:
            for piece in protectors + [king]:
                board_options[piece.square] = []
                for move in piece.movement():
                    test_attackers = self.test_move(piece, move)
                    if test_attackers == 0:
                        board_options[piece.square].append(move)
        else:
            for piece in pieces:
                board_options[piece.square] = []
                for move in piece.movement():
                    attackers = self.test_move(piece, move)
                    if attackers == 0:
                        board_options[piece.square].append(move)
        self.board_options = board_options
        #for piece in pieces:
        #    if piece.colour != self.turn:
        #        continue
        #    sq = piece.square
        #    board_options[sq] = []
        #    for move in piece.movement():
        #        attackers = self.test_move(piece, move)
        #        if attackers == 0:
        #            board_options[sq].append(move)
        #self.board_options = board_options
        self.gbo_time += time.time() - start_time
    def get_check(self):
        """return True if turn's team is giving check"""
        start_time = time.time()
        board_options = self.board_options
        for piece in self.pieces:
            if type(piece) == King and piece.colour == self.turn:
                if piece.get_threats(initial = False) > 0:
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
            pieces, turn, square_pieces, move, placement, promoting_piece, can_move, pawn_or_cap_count, captured_pieces = self.ply_info[t]
            placementS += [placement]
        
        for p in placementS:
            if placementS.count(p) >= 3:
                return True
    def get_promote(self):
        #print("get_promote")
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
    def promote(self, cl_type, bot = False):
        self.can_move = True
        piece = self.promoting_piece
        self.square_pieces[piece.square] = cl_type(piece.square, piece.colour)
        new_piece = self.square_pieces[piece.square]
        new_piece.has_moved = True
        self.pieces.remove(self.promoting_piece)
        self.pieces.append(new_piece)
        self.promoting_piece = None
        self.pro_rects == []
        self.change_turn(bot)
    def update_clocks(self, amount = 1/FPS, bot = False):
        WIN.fill((255, 255, 255), self.clock1[2])
        WIN.fill((255, 255, 255), self.clock2[2])

        #if not bot:
        if self.turn_num > 0:
            if self.botless_turn == "black":
                self.clock1[1] -= amount
            else:
                self.clock2[1] -= amount
        #else:
        #    self.clock2[1] -= 1/FPS
        
        for clock in [self.clock1, self.clock2]:
            pygame.draw.rect(WIN, (0, 0, 0), clock[2], 1)
            seconds = round(clock[1])
            minutes = seconds // 60
            seconds = seconds - minutes * 60
            hours = minutes // 60
            minutes = minutes - hours * 60
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
                WIN.blit(image[colour], (x, y))
                if colour == "white":
                    w_x += 40
                else:
                    b_x += 40
  
    def alpha_beta_max(self, alpha, beta, depth, initial = False):
        if depth == 0:
            if DEPTH % 2 == 0:
                return -self.get_score()
            return self.get_score()
        board_options = self.board_options
        for p in board_options:
            for m in board_options[p]:
                self.move_piece(self.square_pieces[p], m, bot = True)
                score = self.alpha_beta_min(alpha, beta, depth - 1)
                self.get_turn()
                if score >= beta:
                    if initial:
                        return beta, (p, m)
                    return beta
                if score > alpha:
                    alpha = score
                    alpha_move = p, m
        if initial:
            return alpha, alpha_move
        return alpha
    def alpha_beta_min(self, alpha, beta, depth, initial = False):
        if depth == 0: 
            if DEPTH % 2 == 0:
                return self.get_score()
            return -self.get_score()
        board_options = self.board_options
        for p in board_options:
            for m in board_options[p]:
                self.move_piece(self.square_pieces[p], m, bot = True)
                score = self.alpha_beta_max(alpha, beta, depth - 1)
                self.get_turn()
                if score <= alpha:
                    if initial:
                        return alpha, (p, m)
                    return alpha
                if score < beta:
                    beta = score
                    beta_move = p, m
        if initial:
            return beta, beta_move
        return beta
    def start_alpha_beta(self, depth = DEPTH):
        start_time = time.time()
        board_options = self.board_options.copy()
        scores = {}
        for p in board_options:
            for m in board_options[p]:
                self.move_piece(self.square_pieces[p], m, bot = True)
                if self.turn == "white":
                    ab_func = self.alpha_beta_white
                else:
                    ab_func = self.alpha_beta_black
                score = ab_func(-float("inf"), float("inf"), depth-1)
                self.get_turn()
                if score not in scores:
                    scores[score] = []
                scores[score].append((p, m))
        if depth % 2 == 0:
            m_func = max
        else:
            m_func = min
        if len(scores) == None:
            return None
        print(scores, m_func)
        score = m_func(list(scores.keys()))
        self.update_clocks(time.time() - start_time, bot = False)
        return random.choice(scores[score])
    def start_alpha_beta(self, depth = DEPTH):
        start_time = time.time()
        board_options = self.board_options
        score, move = self.alpha_beta_max(-float("inf"), float("inf"), depth, initial = True)
        self.update_clocks(time.time() - start_time, bot = True)
        return move
    def get_score(self):
        score = 0
        let = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for p in self.pieces:
            x, y = p.square[0], p.square[1]
            x = let.index(x)
            y = int(y) - 1
            if p.colour == "white":
                score += p.value
                score += p.score_map[7-y][7-x]
            else:
                score -= p.value
                score -= p.score_map[y][x]
        return score
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
    has_moved = False
    en_passant = False
    pos = 0, 0
    def __init__(self, square, colour):
        self.square = square
        self.colour = colour
        self.rect = pygame.Rect((get_square_pos(square), (PIECE_WIDTH, PIECE_HEIGHT)))
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
    name = "pawn"
    image = {"white": WHITE_PAWN_IMAGE, "black": BLACK_PAWN_IMAGE}
    alpha_image = {"white": WHITE_PAWN_ALPHA, "black": BLACK_PAWN_ALPHA}
    small_image = {"white": WHITE_PAWN_SMALL, "black": BLACK_PAWN_SMALL}
    value = 100
    score_map =  [[0,  0,  0,  0,  0,  0,  0,  0],
		         [50, 50, 50, 50, 50, 50, 50, 50],
		         [10, 10, 20, 30, 30, 20, 10, 10],
 		         [5,  5, 10, 25, 25, 10,  5,  5],
 		         [0,  0,  0, 20, 20,  0,  0,  0],
 		         [5, -5,-10,  0,  0,-10, -5,  5],
 		         [5, 10, 10,-20,-20, 10, 10,  5],
 		         [0,  0,  0,  0,  0,  0,  0,  0]]
    def movement(self):
        start_time = time.time()
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
                        if square != None:
                            options.append(square)
        BOARD.pawn_time += time.time() - start_time
        return options

class Knight(Pieces):
    name = "knight"
    image = {"white": WHITE_KNIGHT_IMAGE, "black": BLACK_KNIGHT_IMAGE}
    alpha_image = {"white": WHITE_KNIGHT_ALPHA, "black": BLACK_KNIGHT_ALPHA}
    small_image = {"white": WHITE_KNIGHT_SMALL, "black": BLACK_KNIGHT_SMALL}
    value = 320
    score_map = [[50,-40,-30,-30,-30,-30,-40,-50],
                [-40,-20,  0,  0,  0,  0,-20,-40],
                [-30,  0, 10, 15, 15, 10,  0,-30],
                [-30,  5, 15, 20, 20, 15,  5,-30],
                [-30,  0, 15, 20, 20, 15,  0,-30],
                [-30,  5, 10, 15, 15, 10,  5,-30],
                [-40,-20,  0,  5,  5,  0,-20,-40],
                [-50,-40,-30,-30,-30,-30,-40,-50]]
    def movement(self):
        start_time = time.time()
        options = []

        for a in [1,-1]:
            for b in [2,-2]:
                square = self.check_square((a, b))
                if square != None:
                    options.append(square)
                square = self.check_square((b, a))
                if square != None:
                    options.append(square)
        BOARD.knight_time += time.time() - start_time
        return options


class Bishop(Pieces):
    name = "bishop"
    image = {"white": WHITE_BISHOP_IMAGE, "black": BLACK_BISHOP_IMAGE}
    alpha_image = {"white": WHITE_BISHOP_ALPHA, "black": BLACK_BISHOP_ALPHA}
    small_image = {"white": WHITE_BISHOP_SMALL, "black": BLACK_BISHOP_SMALL}
    value = 330
    score_map = [[-20,-10,-10,-10,-10,-10,-10,-20],
                [-10,  0,  0,  0,  0,  0,  0,-10],
                [-10,  0,  5, 10, 10,  5,  0,-10],
                [-10,  5,  5, 10, 10,  5,  5,-10],
                [-10,  0, 10, 10, 10, 10,  0,-10],
                [-10, 10, 10, 10, 10, 10, 10,-10],
                [-10,  5,  0,  0,  0,  0,  5,-10],
                [-20,-10,-10,-10,-10,-10,-10,-20]]
    def movement(self):
        start_time = time.time()
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
        BOARD.bishop_time += time.time() - start_time
        return options

class Rook(Pieces):
    name = "rook"
    image = {"white": WHITE_ROOK_IMAGE, "black": BLACK_ROOK_IMAGE}
    alpha_image = {"white": WHITE_ROOK_ALPHA, "black": BLACK_ROOK_ALPHA}
    small_image = {"white": WHITE_ROOK_SMALL, "black": BLACK_ROOK_SMALL}
    value = 500
    score_map = [[0,  0,  0,  0,  0,  0,  0,  0],
                [5, 10, 10, 10, 10, 10, 10,  5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [-5,  0,  0,  0,  0,  0,  0, -5],
                [0,  0,  0,  5,  5,  0,  0,  0]]
    def movement(self):
        start_time = time.time()
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
        BOARD.rook_time += time.time() - start_time
        return options

class Queen(Pieces):
    name = "queen"
    image = {"white": WHITE_QUEEN_IMAGE, "black": BLACK_QUEEN_IMAGE}
    alpha_image = {"white": WHITE_QUEEN_ALPHA, "black": BLACK_QUEEN_ALPHA}
    small_image = {"white": WHITE_QUEEN_SMALL, "black": BLACK_QUEEN_SMALL}
    value = 900
    score_map = [[-20,-10,-10, -5, -5,-10,-10,-20],
                [-10,  0,  0,  0,  0,  0,  0,-10],
                [-10,  0,  5,  5,  5,  5,  0,-10],
                [-5,  0,  5,  5,  5,  5,  0, -5],
                [0,  0,  5,  5,  5,  5,  0, -5],
                [-10,  5,  5,  5,  5,  5,  0,-10],
                [-10,  0,  5,  0,  0,  0,  0,-10],
                [-20,-10,-10, -5, -5,-10,-10,-20]]
    def movement(self):
        start_time = time.time()
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
        BOARD.queen_time += time.time() - start_time
        return options

class King(Pieces):
    name = "king"
    image = {"white": WHITE_KING_IMAGE, "black": BLACK_KING_IMAGE}
    alpha_image = {"white": WHITE_KING_ALPHA, "black": BLACK_KING_ALPHA}
    small_image = {"white": WHITE_KING_SMALL, "black": BLACK_KING_SMALL}
    value = 20000
    score_map = [[-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-30,-40,-40,-50,-50,-40,-40,-30],
                [-20,-30,-30,-40,-40,-30,-30,-20],
                [-10,-20,-20,-20,-20,-20,-20,-10],
                [20, 20,  0,  0,  0,  0, 20, 20],
                [20, 30, 10,  0,  0, 10, 30, 20]]
    def movement(self):
        start_time = time.time()
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
        BOARD.king_time += time.time() - start_time
        return options
    def get_threats(self, initial = False):
        start_time = time.time()
        i = 1
        if self.colour == "black":
            i = -1
        operations = []
        #pawns
        coords = [(1, 1*i), (-1, 1*i)]
        operations.append([Pawn, coords])
        #knights
        coords = [(1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]
        operations.append([Knight, coords])
        #bishops
        coords = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
        operations.append([King, coords])
        lcoords = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],
                  [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)],
                  [(-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)],
                  [(-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7)]]
        for coords in lcoords:
            operations.append([Bishop, coords])
        #rooks
        lcoords = [[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
                  [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
                  [(-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)],
                  [(0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)]]
        for coords in lcoords:
            operations.append([Rook, coords])
        let = ["A", "B", "C", "D", "E", "F", "G", "H"]
        a, b = self.square[0], int(self.square[1])
        a = let.index(a) + 1
        attackers = 0
        #if BOARD.get_threats_time == 0:
            #for op in operations:
                #print(op)
        protectors = []
        for op in operations:
            blocked = 0
            temp_protector = None
            for coords in op[1]:
                na, nb = coords
                if not a + na <= 8 or not a + na >= 1:
                    continue
                if not b + nb <= 8 or not b + nb >= 1:
                    continue
                new_pos = let[a + na - 1] + str(b + nb)
                c_piece = BOARD.square_pieces[new_pos]
                if blocked == 0:
                    if type(c_piece) == op[0] and c_piece.colour != self.colour:
                        attackers += 1
                    elif op[0] == Rook or op[0] == Bishop:
                        if type(c_piece) == Queen and c_piece.colour != self.colour:
                            attackers += 1 
                if op[0] == Rook or op[0] == Bishop:
                    if initial and c_piece != None and c_piece.colour == self.colour:
                        blocked += 1
                        temp_protector = c_piece
                    if blocked == 1:
                        if type(c_piece) == op[0] and c_piece.colour != self.colour:
                            protectors.append(temp_protector)
                        elif op[0] == Rook or op[0] == Bishop:
                            if type(c_piece) == Queen and c_piece.colour != self.colour:
                                protectors.append(temp_protector)
                    if c_piece != None and (c_piece.colour != self.colour or not initial):
                        break
                    elif blocked == 2:
                        break
        #print(protectors)
        #for p in protectors:
        #    print(p.square)


        BOARD.get_threats_time += time.time() - start_time
        if initial:
            return attackers, protectors
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
        img = temp_piece.alpha_image[temp_piece.colour]
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
            WIN.blit(piece.image[piece.colour], (piece.rect.x, piece.rect.y))
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
        #pass


    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    count = 0
    pressed = False
    BOARD.get_board_options()
    START_SOUND.play()
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
                elif event.key == pygame.K_a:
                    print(BOARD.board_options)
                elif event.key == pygame.K_s and FULL_AI_MODE:
                    BOARD.turn, BOARD.alt_turn = BOARD.alt_turn, BOARD.turn
                    BOARD.turn_num -= 1
                    BOARD.change_turn()
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
                if BOARD.pro_rects != [] and not pressed:
                    for index, pro_rect in enumerate(BOARD.pro_rects):
                        if pro_rect.collidepoint(pos):
                            if index == 0:
                                cl_type = Queen
                            elif index == 1:
                                cl_type = Rook
                            elif index == 2:
                                cl_type = Knight
                            else:
                                cly_type = Bishop
                            BOARD.promote(cl_type)
            elif event.type == pygame.MOUSEBUTTONUP and pressed == True and event.button == 1: #if the mouse was released and is the right button
                pressed = False
                BOARD.selected_piece = None
                for spos, sq in BOARD.square_positions.items():
                    if BOARD.can_move and sq.collidepoint(pos) and piece.square in BOARD.board_options:
                        if spos in BOARD.board_options[piece.square]:
                            BOARD.move_piece(piece, spos)
                            break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #return piece on right click
                pressed = False
                BOARD.selected_piece = None

        if pygame.mouse.get_pressed()[0] and pressed == True: #if left mouse button is being held and a piece has been pressed
            piece.rect.x, piece.rect.y = pos
            piece.rect.x -= PIECE_WIDTH//2
            piece.rect.y -= PIECE_HEIGHT//2
        draw_window()

if __name__ == "__main__":
    while main():
        BOARD.__init__()
