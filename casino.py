from game import Game
from player import Player
from randomplayer import RandomPlayer
from student import StudentPlayer

def main(n_games=1000, pocket=100):
    #players = [StudentPlayer("Diogo Martins", pocket)]
    players = [Player("Pedro", 100)]
    for i in range(n_games):
        #print(players)
        g = Game(players, min_bet=1, max_bet=5, verbose=True) 
        #g = Game(players, debug=True)
        g.run()
    
    print("OVERALL: ", players)

if __name__ == '__main__':
    main()
