import time
from abc import ABC, abstractmethod

class Output(ABC):
    def __init__(self, subject):
        subject.register(self)

    @abstractmethod
    def update(self, frame):
        pass

class OutputToScreen(Output):
    def __init__(self, subject, display_data: bool):
        super().__init__(subject)
        self.display_data = display_data

    def update(self, frame):
        self.display_output_header(frame)
        self.display_protocol_info(frame)
        self.display_packet_contents(frame)

    def display_output_header(self, frame):
        local_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"[>] Frame #{frame.packet_num} at {local_time}:")

    def display_protocol_info(self, frame):
        for proto in frame.protocol_queue:
            display_method = getattr(self, f"display_{proto.lower()}_data", None)
            if display_method:
                display_method(frame)
            else:
                print(f"{'':>4}[+] Unknown Protocol")

    def display_ethernet_data(self, frame):
        ethernet = frame.ethernet
        interface = frame.interface if frame.interface else "all"
        frame_length = frame.frame_length
        epoch_time = frame.epoch_time
