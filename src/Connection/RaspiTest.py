from smbus import SMBus

addr = 0x8  # bus address
bus = SMBus(1)  # indicates /dev/ic2-1

numb = 1

print("Enter 1 to 4 to control the Controller")
while numb == 1:
    # input data
    ledstate = input(">>>>   ")

    if ledstate == "1":
        bus.write_byte(addr, 0x1)  # Press A
    elif ledstate == "2":
        bus.write_byte(addr, 0x2)  # Press X
    elif ledstate == "3":
        bus.write_byte(addr, 0x3)  # Press HOME
    elif ledstate == "4":
        bus.write_byte(addr, 0x4)  # Press DPad UP
    else:
        numb = 0
