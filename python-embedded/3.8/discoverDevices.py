#pip3 install pyserial --pre --force
import serial.tools.list_ports

def get_ports():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        print(port.manufacturer, port.device)
        
get_ports()