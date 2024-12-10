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
            counter_history = [], 
            player_type = [PlayerType.UNKNOWN]
           ):

    if not prev_play:
        prev_play = 'R'
    
    ## DETECTION PHASE 
    # Training phase to detect the type of the opponent player
    if len(opponent_history) < 300:
        move = random.choice(['R', 'P', 'S'])
        my_history.append(move)
        counter_history.append(counter(move))

    # Predict the opponent type 
    elif len(opponent_history) == 300:
        if is_quincy(opponent_history):
            print('QUINCY ZA')
            player_type[0] = PlayerType.QUINCY
        elif is_Kris(counter_history, opponent_history, my_history):
            print('KRIIIIS')
            player_type[0] = PlayerType.KRIS
        else:
            print('UNKNOWW')

        move = 'R'

    # Counter depending on the opponent type 
    else:
        move = 'R'
    opponent_history.append(prev_play)

    if(len(opponent_history) == 1000):
        opponent_history.clear()
        my_history.clear()
        counter_history.clear()
        player_type[0] = PlayerType.UNKNOWN

    return move
        



def is_quincy(opponent_history):
    if len(opponent_history) < 10:
        return False
    quincy_cycle = ["R", "R", "P", "P", "S"]
    double_cycle = quincy_cycle + quincy_cycle  # ["R", "R", "P", "P", "S", "R", "R", "P", "P", "S"]

    # Compare the first 10 elements of opponent history with double cycle
    return opponent_history[:10] == double_cycle

def is_Kris(counter_history, opponent_history, my_history):
    # - 2 to handle the offset between the array

    return counter_history[0: len(counter_history) -2] == opponent_history[2:]

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
    