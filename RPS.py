# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


import ipdb
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
            my_history=['R'], 
            counter_history = ['P'], 
            player_type = [PlayerType.UNKNOWN]
           ):

    #ipdb.set_trace()
    if not prev_play:
        prev_play = 'R'
    
    ## DETECTION PHASE 
    # Training phase to detect the type of the opponent player
    if len(opponent_history) < 300:
        move = random.choice(['R', 'P', 'S'])
        #move = 'P'
        my_history.append(move)
        counter_history.append(counter(move))

    # Predict the opponent type 
    elif len(opponent_history) == 300:
        player_type[0] = PlayerType.KRIS

        print('opponent_moves')

        print(len(opponent_history))
        print(opponent_history[:20])

        print('your moves')

        print(len(my_history))

        print(my_history[:20])

        print('counter_history moves')

        print(len(counter_history))

        print(counter_history[:20])
        if is_quincy(opponent_history):
            print('QUINCY ZA')

        elif is_Kris(counter_history, opponent_history):
            print('KRIIIIS')
            print('KRIIIIS')
            print('KRIIIIS')
            print('KRIIIIS')

            player_type[0] = PlayerType.QUINCY

        elif(is_abbey(opponent_history, my_history)):
            print('ABBEY')
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

def is_Kris(counter_history, opponent_history):
    # - 2 to handle the offset between the array

    return counter_history[:len(counter_history) - 2] == opponent_history[1:]

def is_abbey(opponent_moves, your_moves):


    # Initialize Abbey's play_order dictionary
    play_order = {
        "RR": 0, "RP": 0, "RS": 0,
        "PR": 0, "PP": 0, "PS": 0,
        "SR": 0, "SP": 0, "SS": 0,
    }

    # Simulate Abbey's behavior based on your moves
    abbey_predictions = []
    for i in range(0, len(your_moves)):
        #ipdb.set_trace()

        if i == 0 :
            # For the first line we add RFirst round
            prediction = 'R'
            abbey_predictions.append(prediction)


        elif i == 1:
            prediction = 'R'
            abbey_predictions.append(counter(prediction))

        else:
            last_two = your_moves[i - 2] + your_moves[i - 1]
            if last_two in play_order:
                play_order[last_two] += 1
            
            potential_plays = [
                your_moves[i - 1] + "R",
                your_moves[i - 1] + "P",
                your_moves[i - 1] + "S",
            ]
            sub_order = {
                k: play_order[k]
                for k in potential_plays if k in play_order
            }

            if sub_order:
                prediction = max(sub_order, key=sub_order.get)[-1]
            else:
                prediction = 'R'

            abbey_predictions.append(counter(prediction))
    

    matches = sum(1 for p, o in zip(abbey_predictions, opponent_moves) if p == o)

    # print('opponent_moves')

    # print(len(opponent_moves))
    # print(opponent_moves[:20])

    # print('abbey_predictions')

    # print(len(abbey_predictions))
    # print(abbey_predictions[:20])

    # print('your moves')

    # print(len(your_moves))

    # print(your_moves[:20])




    # If the opponent's moves match abbey's predictions more than a threshold, detect abbey
    threshold = 0.9  
    return matches / len(opponent_moves) >= threshold 



def counter(move):
    match move:
        case 'R':
            return 'P'
        case 'P':
            return 'S'
        case 'S':
            return 'R'
        case _:
            ipdb.set_trace()
            return 'R'
    