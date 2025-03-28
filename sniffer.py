import os
import time
import pyshark
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Load the file to store information
file_name = os.getenv("FILE_NAME")

# Store a list of authorized devices mac address 
str_records = os.getenv("ADDRESS_LIST")
records = str_records.split(",") if str_records else []

# Write to the file
def unknown_device(address, time):
    file = open(file_name,"a")
    file.write("{" + "\"time\":\"" + time + "\"," )
    file.write("\"source\":\"" + address + "\""+ "}" + '\n')
    file.close()

# Run continuously
# If new device sleep for a second to prevent overload
def capture_packets(interface):
    capture = pyshark.LiveCapture(interface=interface)
    for packet in capture.sniff_continuously():
        if 'ETH' in packet:
            if packet.eth.src not in records:
                unknown_device(packet.eth.src, datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                time.sleep(1)
                print(f"Captured Packet: {packet.eth.src} -> {packet.eth.dst}")


# Change interfaces according to your needs
# Run ipconfig on windows to find adapter names
capture_packets("Wi-Fi")




