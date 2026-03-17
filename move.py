from tokenize import String
import chess
import chess.engine
from comms import ESP32Comms
from motion_mapper import map_coordinates

# Create board
board = chess.Board()

# Connect to Stockfish
engine = chess.engine.SimpleEngine.popen_uci("../stockfish/stockfish-macos-m1-apple-silicon")
print(engine.id)
print(board)

while not board.is_game_over():

    user_move = input("Your move (e2e4): ")

    try:
        move = chess.Move.from_uci(user_move)

        if move in board.legal_moves:
            board.push(move)
            print("\nYou played:", user_move)
            print(board)

            # Engine move
            result = engine.play(board, chess.engine.Limit(time=0.5))
            board.push(result.move)
            
            print("\nStockfish played:", result.move)
            print(board)
            #print(result.move.uci())
            mapped_coordinates = map_coordinates(result.move.uci())
            comms = ESP32Comms(port="/dev/ttyUSB0")  # adjust if needed
            comms.send_move(mapped_coordinates)
            #print(mapped_coordinates)
        else:
            print("Illegal move!")

    except:
        print("Invalid format!")

engine.quit()