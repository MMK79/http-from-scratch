f = open("messages.txt")
with open("messages.txt", "rb"):
    data = f.read(8)
    while data:
        print("read:", data)
        data = f.read(8)

with open("messages.txt", "r", encoding="utf-8") as f:
    print(type(f))
    bytes = f.read(8)
    while bytes:
        print("read:", bytes)
        bytes = f.read(8)
