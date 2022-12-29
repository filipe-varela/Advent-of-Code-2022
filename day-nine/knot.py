class Knot(object):
    def __init__(self, desc: str = '') -> None:
        self.pos = [0,0]
        self.desc = desc
        self.history = [self.pos.copy()]

    def add_to_history(self) -> None:
        if self.pos not in self.history:
            self.history.append(self.pos.copy())

    def move(self, direction: str = "", delta: int = 1) -> None:
        match(direction):
            case 'R': 
                self.pos[0] += delta
            case 'L': 
                self.pos[0] -= delta
            case 'U': 
                self.pos[1] += delta
            case 'D': 
                self.pos[1] -= delta
            case other: 
                return
        
        self.add_to_history()

    def passing_by(self) -> int:
        return len(set([(x,y) for x,y in self.history]))


def distance_vector(start: list[int], end: list[int]) -> list[int]:
    return [b-a for a,b in zip(start, end)]

def norm(vec: list[int]) -> float: return sum(x**2 for x in vec)**.5

def absv(v: list[int]) -> list[int]: return [abs(i) for i in v]

class Tail(Knot):
    def __init__(self, head: Knot, desc: str) -> None:
        super().__init__(desc=desc)
        self.head = head

    def move(self, direction: str = "", delta: int = 0) -> None:
        # while norm(dist_vec := distance_vector(self.pos, self.head.pos)) > 2**.5:
        dist_vec = distance_vector(self.pos, self.head.pos)
        match(dist_vec):
            case [2,0]:
                self.pos[0] += 1
            case [0,2]:
                self.pos[1] += 1
            case [-2,0]:
                self.pos[0] -= 1
            case [0,-2]:
                self.pos[1] -= 1
            case [2,1] | [1,2] | [2,2]: 
                self.pos[0] += 1
                self.pos[1] += 1
            case [2,-1] | [1,-2] | [2,-2]: 
                self.pos[0] += 1
                self.pos[1] -= 1
            case [-2,1] | [-1,2] | [-2,2]: 
                self.pos[0] -= 1
                self.pos[1] += 1
            case [-2,-1] | [-1,-2] | [-2,-2]:
                self.pos[0] -= 1
                self.pos[1] -= 1
            case other: pass

        self.add_to_history()