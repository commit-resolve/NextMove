import websocket

ws = websocket.create_connection("ws://localhost:9010")
ws.send("TEST\n")
print(ws.recv())