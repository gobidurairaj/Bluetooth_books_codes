import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.bind(("50:76:af:3d:63:7c",4))
# Bluetooth Address - 50.76.af.3d.63.7c
# client.listen(1)

# server, addr = client.accept()

try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
        print (f"Message: {data.decode('utf-8')}")

except OSError as e:
    pass

client.close()

