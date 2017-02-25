import argparse
import serial
from OSC import OSCClient, OSCMessage, OSCClientError
import settings


def get_client(ip, port):
    print 'OSC: Connecting to {}:{}'.format(ip, port)
    client = OSCClient()
    client.connect((ip, port))
    return client


def send_message(client):
    print 'OSC: ding dong!!'
    try:
        client.send(OSCMessage("/doorbell"))
    except OSCClientError:
        print 'OSC: error connecting'


def main(ip, port, serial_file):
    ser = serial.Serial(serial_file, 9600)
    client = get_client(ip, port)

    while True:
        line = ser.readline()
        print 'Serial: {}'.format(line)
        send_message(client)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--osc-ip', default=settings.MATTS_IP)
    parser.add_argument('--osc-port', default=settings.MATTS_PORT)
    parser.add_argument('--serial', default=settings.SERIAL_PORT)
    args = parser.parse_args()

    if args.test:
        client = get_client(args.osc_ip, args.osc_port)
        send_message(client)
    else:
        main(args.osc_ip, args.osc_port, args.serial)
