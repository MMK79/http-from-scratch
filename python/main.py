# os.Open() in golang open file in binary
# read the file in binary mode
with open("messages.txt", "rb") as f:
    data = f.read(8)
    while data:
        # convert the binary to str
        # errors="replace" tells if you can't decode properly don't crash, just replace them with replacement character
        # emoji's can cause problem, they are 4 byte, so when you decode them, it may cause incomplete byte sequence
        print("read:", data.decode("utf-8", errors="replace"))
        data = f.read(8)
