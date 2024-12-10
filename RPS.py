# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
class PlayerType:
    QUINCY = "quincy"
    MRUGESH = "mrugesh"
    KRIS = "kris"
    ABBEY = "abbey"
    UNKNOWN = "unknown"


def player(prev_play, opponent_history=[], 
           play_order=[{
                "RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0
            }], 
            my_history=[], 
            counter_history = [], player_type = [PlayerType.UNKNOWN]
           ):

    if not prev_play:
        prev_play = 'R'
    
    ## DETECTION PHASE 
    # First move will be R to allow kris detection
    if len(opponent_history) == 0 :
 
        move = 'R'
        my_history.append(move)
        # Hard code the first value for Kris
        counter_history.append('R')
        opponent_history.append(prev_play)
        return 'R'
    
    # Training phase to detect the type of the opponent player
    elif len(opponent_history) < 300:
        move = random.choice(['R', 'P', 'S'])
        my_history.append(move)
        counter_history.append(counter(move))
        opponent_history.append(prev_play)

        # print(player_type)
        # print('my_history')
        # print(my_history[0:12])

        # print('counter')
        # print(counter_history[0:10])
        # print('opponent')
        # print(opponent_history[0:10])
        return move

    # Predict the opponent type 
    elif len(opponent_history) == 300:
        print(my_history[0])
        if is_quincy(opponent_history):
            player_type = PlayerType.QUINCY
        elif is_kris(counter_history, opponent_history):
            player_type = PlayerType.KRIS

        opponent_history.append(prev_play)

        print(player_type)
        print('my_history')
        print(my_history[0:12])
        print('counter')
        print(counter_history[0:10])
        print('opponent')
        print(opponent_history[0:10])
        
        
        return counter(det_nxt_move(player_type, opponent_history))

    # Counter depending on the opponent type 
    else:
        return 'R'
           




def is_quincy(opponent_history):
    if len(opponent_history) < 10:
        return False
    quincy_cycle = ["R", "R", "P", "P", "S"]
    double_cycle = quincy_cycle + quincy_cycle  # ["R", "R", "P", "P", "S", "R", "R", "P", "P", "S"]

    # Compare the first 10 elements of opponent history with double cycle
    return opponent_history[:10] == double_cycle



def is_kris(counter_history, opponent_history):


    return counter_history == opponent_history


def det_quincy_nxt_move(opponent_history):
    quincy_cycle = ["R", "R", "P", "P", "S"]
    current_position = len(opponent_history)% len(quincy_cycle)
    return quincy_cycle[current_position]

def det_nxt_move(playerType, opponent_history):
      match playerType:
        case PlayerType.QUINCY:
            return det_quincy_nxt_move( opponent_history)
        case PlayerType.KRIS:
            return 'S'
        case _:
            return 'R'
          

def counter(move):
    match move:
        case 'R':
            return 'P'
        case 'P':
            return 'S'
        case 'S':
            return 'R'
        case _:
            return 'R'
    