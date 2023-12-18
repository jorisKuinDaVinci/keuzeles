PINNEN = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

def Pin(id, inOut):
    return (id, inOut)

pin []

for id in PINNEN:
    pin.append(Pin(id, 42))
