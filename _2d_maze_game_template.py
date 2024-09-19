from Player import Player
 
def main():
    player = Player()
 
    print(player.to_string())
 
    player.lose_life()
    player.move_xy(5, 6)
    print(player.to_string())
    player.lose_life()
    player.move_xy(-2, -10)
    print(player.to_string())
 
    player.lose_life()
    player.move_xy(2, 2) # should do nothing; player is dead
    print(player.to_string())
 
if __name__ == "__main__":
    main()
