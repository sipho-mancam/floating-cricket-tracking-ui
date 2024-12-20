import socket
import json

class UDPSender:
    def __init__(self, host, port):
        """Initialize the UDP sender with the target host and port."""
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket

    def send_message(self, message):
        """Send a message to the specified UDP address."""
        try:
            # Send the message (encoded as bytes) to the target address
            self.sock.sendto(message.encode('utf-8'), (self.host, self.port))
            print(f"Message sent to {self.host}:{self.port}")
        except Exception as e:
            print(f"Error sending message: {e}")

    def close(self):
        """Close the socket."""
        self.sock.close()

    def __del__(self)->None:
        self.close()


class VizEventSender:
    def __init__(self)->None:
        self.__udp_stream = UDPSender("10.0.100.90", 6101)
    

    def send_event(self, event:dict, viz_object)->None:
        to_send = f"SharedMemoryMap_SetValue|{viz_object}|{json.dumps(event)}\0"
        self.__udp_stream.send_message(to_send)
