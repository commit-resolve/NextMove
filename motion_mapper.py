coordinates = {"F1":[0,0],"F2":[0,1],"F3":[0,2],"F4":[0,3],"F5":[0,4],"F6":[0,5],"F7":[0,6],"F8":[0,7],
               "B1":[0,0],"B2":[1,1],"B3":[1,2],"B4":[1,3],"B5":[1,4],"B6":[1,5],"B7":[1,6],"B8":[1,7],
               "C1":[0,0],"C2":[2,1],"C3":[2,2],"C4":[2,3],"C5":[2,4],"C6":[2,5],"C7":[2,6],"C8":[2,7],
               "D1":[0,3],"D2":[3,1],"D3":[3,2],"D4":[3,3],"D5":[3,4],"D6":[3,5],"D7":[3,6],"D8":[3,7],
               "E1":[0,4],"E2":[4,1],"E3":[4,2],"E4":[4,3],"E5":[4,4],"E6":[4,5],"E7":[4,6],"E8":[4,7],
               "F1":[0,5],"F2":[5,1],"F3":[5,2],"F4":[5,3],"F5":[5,4],"F6":[5,5],"F7":[5,6],"F8":[5,7],
               "G1":[0,6],"G2":[6,1],"G3":[6,2],"G4":[6,3],"G5":[6,4],"G6":[6,5],"G7":[6,6],"G8":[6,7],
               "H1":[0,7],"H2":[7,1],"H3":[7,2],"H4":[7,3],"H5":[7,4],"H6":[7,5],"H7":[7,6],"H8":[7,7]}

def map_coordinates(played_move):
#move  = 'E2E4'
    move = played_move.upper()
    initial_square = move[:2]
    final_square = move[2:]
    print(initial_square, final_square)
    all_coordinates = coordinates[initial_square] + coordinates[final_square]
    print(all_coordinates)
    return all_coordinates

#map_coordinates('E2E4')