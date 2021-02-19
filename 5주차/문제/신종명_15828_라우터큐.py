buffer_size = int(input())
packets = []

while True:
    packet = int(input())

    if packet == -1:
        break

    if packet == 0:
        packets.pop(0)
        continue

    if len(packets) >= buffer_size:
        continue

    packets.append(packet)

if not packets:
    print('empty')
    exit()

for packet in packets:
    print(packet, end=" ")
