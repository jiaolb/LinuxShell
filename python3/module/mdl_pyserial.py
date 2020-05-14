from serial import *
from serial.tools.list_ports import comports

def GetComPortList():
    '''获取当前所有端口的列表.'''
    com_list = []
    if sys.platform == 'win32':
        for com in list(comports()):
            com_list.append(com[0])
    else:
        com_list = range(10)
    return com_list

class SerialPort(Serial):
    def __init__(self):
        super(SerialPort, self).__init__()

    def OpenPort(self, com, baud=9600, parity='E', databit=8, stopbit=1):
        try:
            self.port = com
            self.portstr = com
            self.baudrate = baud
            self.parity = parity
            self.bytesize = databit
            self.stopbits = stopbit
            self.open()
            print('Open Serial Port Succed', self.portstr)
            return self.isOpen()
        except:
            print('Open Serial Port Faild', com)
            return False

    def ClosePort(self):
        try:
            self.close()
            print('Close Serial Port', self.portstr)
        except:
            pass

    def RecvData(self, RxList):
        if self.is_open == True:
            rlen = self.inWaiting()  # return the number of chars in the receive buffer
            if rlen > 0:
                RxList += self.read(rlen)
            return rlen
        else:
            return 0

    def SendData(self, TxList):
        if self.is_open == True:
            self.write(bytes(TxList))
            print('Serial Send data', end=' ')
            for i in TxList:
                print(format(i, '02x'), end='')
            print()

list = GetComPortList()
print (list)

list_send = [0x68, 0x32, 0x00, 0x32, 0x00, 0x68, 0x5B, 0x88, 0x88, 0xFE, 0xFF, 0x02, 0x0C, 0x61, 0x00, 0x00, 0x02, 0x00, 0xD9, 0x16]
list_recv = []

SerialCOM = SerialPort()
SerialCOM.OpenPort(list[0])

SerialCOM.SendData(list_send)
byte = 0
while True:
    rlen = SerialCOM.RecvData(list_recv)
    if(rlen > 0):
        byte += 1
    else:
        if byte >= 28:
            break

print (list_recv)
SerialCOM.ClosePort()

