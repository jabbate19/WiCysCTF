from scapy.all import *
import random

def main():
    packets = []
    # 41.039094, -71.960738

    # 41.032390, -71.946419

    for i in range(0, 100):
        p = scapy.layers.dot11.RadioTap(pad=181,len=17, present=0x0000182e, Rate=2, ChannelFrequency=2437, ChannelFlags=0x00a0, dBm_AntSignal=-33, Antenna=1) / b'\x04'
        # 48:1C:B9
        p = p / b'\x80\x00\x00\x00' / (b'\xff'*6) / b'\x48\x1c\xb9\xc3\x74\xa2' / b'\x48\x1c\xb9\xc3\x74\xa2' / b'\x00\x0d'
        p = p / (b'\x00' * 8) / b'\xb8\x0b\x21\x04' #scapy.layers.dot11.Dot11Beacon(timestamp=0, interval=3.072, cap=0x421)
        ssid = b'USA-OP-NOTFLAG'
        p = p / b'\x03\x01\x06' / b'\x00\x0e' / ssid
        p = p / b'\xdd'
        odid_data = b'\xfa\x0b\xbc' + b'\x0d'
        # Count is here
        odid_data += i.to_bytes(1, 'little') + b'\xf0\x19\x03'
        odid_data += b'\x00\x00' + b'BINGUSDRONE' + (b'\x00' * 9) + b'\x00\x50\xf6'
        odid_data += b'\x10\x00' + b'\x00\x00\x00' # Dir Speed vert
        lat = random.uniform(41.032390, 41.039094)
        lat = (int) (lat*1e7)
        lon = random.uniform(-71.960738, -71.946419)
        lon = (int) (lon*1e7)
        pressure = 0
        geodetic = 2474
        height = 2200
        odid_data += lat.to_bytes(4, 'little', signed=True)  # UA Lat
        odid_data += lon.to_bytes(4, 'little', signed=True) # UA Long
        odid_data += pressure.to_bytes(2, 'little') # Pressure
        odid_data += geodetic.to_bytes(2, 'little') # Geodetic
        odid_data += height.to_bytes(2, 'little') # Height
        odid_data += b'\x39\x41\x00\x00\x0a\x00'
        odid_data += b'\x50\x00' + ssid + (b'\x00' * 6) + b'\x00\x00\x00' # Operator
        odid_len = len(odid_data)
        p = p / odid_len.to_bytes(1, 'big') / odid_data # LEN
        packets.append(p)

    wrpcap('dronebrrr.pcap', packets)

if __name__ == '__main__':
    main()

