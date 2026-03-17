# import serial
# import time
# import websocket

# class ESP32Comms:
    # Use below for raspberry pi
    # def __init__(self, port="/dev/ttyUSB0", baudrate=115200):
    #     self.ser = serial.Serial(port, baudrate, timeout=1)
    #     time.sleep(2)
          # allow ESP32 reset
    
    # Use below for websocket wokwi simulation
    # def __init__(self, url="ws://localhost:9010"):
    #     self.ws = websocket.create_connection(url)

    # def send_move(self, move):
    #     # move = [3, 6, 3, 4]
    #     msg = f"MOVE {move[0]} {move[1]} {move[2]} {move[3]}\n"
    #     # Use below for raspberry pi
    #     # self.ser.write(msg.encode())
    #     # print(f"[SENT] {msg.strip()}")

    #     # Use below for websocket wokwi simulation
    #     self.ws.send(msg)
    #     print(f"[SENT] {msg.strip()}")
    # def read_response(self):
        # Use below for raspberry pi
        # if self.ser.in_waiting:
        #     return self.ser.readline().decode().strip()
        # return None

        #Use below code for websocket wokwi simulatio
        # try:
        #     return self.ws.recv()
        # except:
        #     return None

import subprocess

class ESP32Comms:
    def __init__(self):
        self.proc = subprocess.Popen(
            ["wokwi-cli", "."],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def send_move(self, move):
        msg = f"MOVE {move[0]} {move[1]} {move[2]} {move[3]}\n"
        self.proc.stdin.write(msg)
        self.proc.stdin.flush()
        print(f"[SENT] {msg.strip()}")

    def read_response(self):
        return self.proc.stdout.readline().strip()