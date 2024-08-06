
class Move:

    def __init__(
            self,
            initial,
            final
    ):
        # initial and final are squares (not tuple)
        self.initial = initial
        self.final = final

    # if a move is equal to another move
    def __eq__(
            self,
            other
    ):
        return self.initial == other.initial and self.final == other.final