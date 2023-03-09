import serial.tools.list_ports

def get_ports():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if port.manufacturer.startswith("STM"):
            port_number = port.device
    return port_number

def receive_data():
    try:
        value = iot_device.readline()
        print(value)
    except:
        print("Nothing to print")

def send_data(data):
    try:
        iot_device.write(data.encode())
    except:
        print("Nothing to send")

#iot_device = serial.Serial(port=get_ports(),baudrate=115200, bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,timeout=1)
#while True:
#   try:
#        value = iot_device.readline()
#        print(value)
#    except:
#        print("Nothing to print")

while True:
    receive_data()
    send_data('A45')
    