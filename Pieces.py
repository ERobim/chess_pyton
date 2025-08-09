from enum import Enum

class PieceType(Enum):
    NONE = 0
    ROOK = 1
    HORSE = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5
    PAWN = 6

class PieceColor(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    def __init__(self, piece_type: PieceType, color: PieceColor, square):
        self.type = piece_type
        self.color = color
        self.pos = square #(varia entre 0-63)

    def set_position(self, new_square):
        self.pos = new_square

    def __str__(self):
        return f"{self.color.name.capitalize()} {self.type.name.capitalize()} at ({Piece.square_to_notation(self.pos)})"

    @staticmethod
    def square_to_notation(square: int) -> str:
        return ("abcdefgh"[square % 8]) + str(square // 8 + 1)

    @staticmethod
    def notation_to_square(notation: str) -> int:
        rows = "abcdefgh"
        col_int = rows.index(notation[0].lower())
        row_int = int(notation[1]) - 1
        return col_int * 8 + row_int


rook = Piece(PieceType.ROOK, PieceColor.WHITE, Piece.notation_to_square("a1"))
print(rook)  # White Rook at a1

rook.set_position(Piece.notation_to_square("h8"))
print(rook)  # White Rook at h8

print(Piece.square_to_notation(0))   # a1
print(Piece.square_to_notation(63))  # h8