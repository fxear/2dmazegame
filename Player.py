from Vector import Vec2
 
class Player:
    lives = 3
    score = 0
    position = Vec2(0, 0) #position of thet player
 
    dead = False
 
    def to_string(self):
        ret = f"Lives: {self.lives} / Score: {self.score} / Pos: {self.position.to_string()}"
        if self.dead: ret = "(dead) " + ret
 
        return ret
 
    def lose_life(self):#defines that the player has lost a life
        self.lives -= 1
        if self.lives <= 0: self.dead = True
 
    def gain_score(self, points): #if the player has gained points
        self.points += points
 
    def move_xy(self, x, y): 
        if self.dead: return False
 
        self.position.x += x
        self.position.y += y
 
    def move_vec(self, vec):
        self.move_xy(vec.x, vec.y)