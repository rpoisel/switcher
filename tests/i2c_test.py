import smbus

# UDEV rule (put into /etc/udev/rules.d/99-i2c.rules)
# KERNEL=="i2c-[0-9]*", MODE="660", OWNER="rpoisel", GROUP="users"


def main():
    bus = smbus.SMBus(2)
    address = 0x50

    cnt = 0
    for curChar in "LTD121EWVB":
    #for curChar in "AAAAAAAAAA":
        letter = bus.read_byte_data(address, 0xf1 + cnt)
        #bus.write_byte_data(address, 0xf1 + cnt, ord(curChar))

        print("Current character: " + chr(letter))

        cnt += 1


if __name__ == "__main__":
    main()
