class Character:
    def __init__(self, name: str, color: str):
        self.x = int(0)
        self.y = int(0)
        self.name = name
        self.color = color

    def stand(self):
        print("ready!")

    def sit(self):
        print("zzzzz!")

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        position = Move(self.x, self.y)
        return position

    def __str__(self):
        return f"Character name: {self.name}, Character color: {self.color}, Character position: ({self.x},{self.y})."


class Move:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Position: (x={self.x}, y={self.y})"


player1 = Character("spiderman", "red")
move1 = Move(1, 3)
position = player1 + move1
print(position)
move2 = Move(7, 2)
position = player1 + move2
print(position)
print(player1)
