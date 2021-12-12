class Unknown:
    def __init__(self, name: str, shift=0, scalar=1):
        self.name = name
        self.shift = shift
        self.scalar = scalar

    def __str__(self):
        return f"{self.scalar if self.scalar != 1 else ''}{self.name}{'+ '+ str(self.shift) if self.shift != 0 else ''}"

