import random
from packet import Packet

def generate_packets(num_packets):
    packets = []
    for i in range(num_packets):
        packet_id = i + 1
        size = random.randint(1, 10)  # Taille du paquet entre 1 et 10
        arrival_time = random.randint(0, 10)  # Moment d'arrivée entre 0 et 10
        packets.append(Packet(packet_id, size, arrival_time))
    return packets
