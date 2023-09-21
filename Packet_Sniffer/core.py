import itertools
import time
from socket import socket, PF_PACKET, SOCK_RAW, ntohs
from typing import Iterator
import netprotocols

class Decoder:
    def __init__(self, interface: str):
        self.interface = interface
        self.data = None
        self.protocol_queue = ["Ethernet"]
        self.packet_num = 0
        self.frame_length = 0
        self.epoch_time = 0

    def bind_interface(self, sock):
        if self.interface:
            sock.bind((self.interface, 0))

    def attach_protocols(self, frame):
        start = end = 0
        for proto in self.protocol_queue:
            proto_class = getattr(netprotocols, proto, None)
            if proto_class:
                end = start + proto_class.header_len
                protocol = proto_class.decode(frame[start:end])
                setattr(self, proto.lower(), protocol)
                if protocol.encapsulated_proto in (None, "undefined"):
                    break
                self.protocol_queue.append(protocol.encapsulated_proto)
                start = end
        self.data = frame[end:]

    def execute(self) -> Iterator:
        with socket(PF_PACKET, SOCK_RAW, ntohs(0x0003)) as sock:
            self.bind_interface(sock)
            for self.packet_num in itertools.count(1):
                frame = sock.recv(9000)
                self.frame_length = len(frame)
                self.epoch_time = time.time_ns() / (10 ** 9)
                self.attach_protocols(frame)
                yield self

class PacketSniffer:
    def __init__(self):
        self.observers = []

    def register(self, observer) -> None:
        self.observers.append(observer)

    def notify_all(self, *args, **kwargs) -> None:
        for observer in self.observers:
            observer.update(*args, **kwargs)

    def listen(self, interface: str) -> Iterator:
        for frame in Decoder(interface).execute():
            self.notify_all(frame)
            yield frame
