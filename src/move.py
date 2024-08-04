
class Move:

    def __init__(
            self,
            initial,
            final
    ):
        # initial and final are squares (not tuple)
        self.initial = initial
        self.final = final