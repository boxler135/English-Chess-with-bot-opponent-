
class Piece:

    def __init__(
            self,
            name,
            color,
            value,
            texture = None,
            teture_rect = None
    ):
        pass

class Pawn(Piece):

    def __init__(
            self,
            color
    ):
        self.dir = -1 if color == 'white' else 1
        super().__init__(
            'pawn',
            color,
            1.0 # for AI to know value of piece
        )

class Knight(Piece):

    def __init__(
            self,
            color
    ):
        super().__init__(
            'knight',
            color,
            3.0
        )

class Bishop(Piece):

    def __init__(
            self,
            color
    ):
        super().__init__(
            'bishop',
            color,
            3.001 # so AI will know bishops are more impt than knights
        )

class Rook(Piece):

    def __init__(
            self,
            color
    ):
        super().__init__(
            'rook',
            color,
            5.0
        )

class Queen(Piece):

    def __init__(
            self,
            color
    ):
        super().__init__(
            'queen',
            color,
            9.0
        )

class King(Piece):

    def __init__(
            self,
            color
    ):
        super().__init__(
            'king',
            color,
            10000.0 # most important piece in board
        )