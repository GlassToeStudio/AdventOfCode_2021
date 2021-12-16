"""
--- Day 16: Packet Decoder ---
As you leave the cave and reach open waters, you receive a transmission from
the Elves back on the ship.

The transmission was sent using the Buoyancy Interchange Transmission System
(BITS), a method of packing numeric expressions into a binary sequence. Your
submarine's computer has saved the transmission in hexadecimal (your puzzle
input).

The first step of decoding the message is to convert the hexadecimal
representation into binary. Each character of hexadecimal corresponds to four
bits of binary data:

0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111

The BITS transmission contains a single packet at its outermost layer which
itself contains many other packets. The hexadecimal representation of this
packet might encode a few extra 0 bits at the end; these are not part of the
transmission and should be ignored.

Every packet begins with a standard header: the first three bits encode the
packet version, and the next three bits encode the packet type ID. These two
values are numbers; all numbers encoded in any packet are represented as
binary with the most significant bit first. For example, a version encoded as
the binary sequence 100 represents the number 4.

Packets with type ID 4 represent a literal value. Literal value packets encode
a single binary number. To do this, the binary number is padded with leading
zeroes until its length is a multiple of four bits, and then it is broken into
groups of four bits. Each group is prefixed by a 1 bit except the last group,
which is prefixed by a 0 bit. These groups of five bits immediately follow the
packet header. For example, the hexadecimal string D2FE28 becomes:

110100101111111000101000
VVVTTTAAAAABBBBBCCCCC

Below each bit is a label indicating its purpose:

The three bits labeled V (110) are the packet version, 6.
The three bits labeled T (100) are the packet type ID, 4, which means the
packet is a literal value.

The five bits labeled A (10111) start with a 1 (not the last group, keep
reading) and contain the first four bits of the number, 0111.

The five bits labeled B (11110) start with a 1 (not the last group, keep
reading) and contain four more bits of the number, 1110.

The five bits labeled C (00101) start with a 0 (last group, end of packet) and
contain the last four bits of the number, 0101.

The three unlabeled 0 bits at the end are extra due to the hexadecimal
representation and should be ignored.


So, this packet represents a literal value with binary representation
011111100101, which is 2021 in decimal.

Every other type of packet (any packet with a type ID other than 4) represent
an operator that performs some calculation on one or more sub-packets
contained within. Right now, the specific operations aren't important; focus
on parsing the hierarchy of sub-packets.

An operator packet contains one or more packets. To indicate which subsequent
binary data represents its sub-packets, an operator packet can use one of two
modes indicated by the bit immediately after the packet header; this is called
the length type ID:


If the length type ID is 0, then the next 15 bits are a number that represents
the total length in bits of the sub-packets contained by this packet.

If the length type ID is 1, then the next 11 bits are a number that represents
the number of sub-packets immediately contained by this packet.


Finally, after the length type ID bit and the 15-bit or 11-bit field, the
sub-packets appear.

For example, here is an operator packet (hexadecimal string 38006F45291200)
with length type ID 0 that contains two sub-packets:

00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB


The three bits labeled V (001) are the packet version, 1.
The three bits labeled T (110) are the packet type ID, 6, which means the
packet is an operator.

The bit labeled I (0) is the length type ID, which indicates that the length is
a 15-bit number representing the number of bits in the sub-packets.

The 15 bits labeled L (000000000011011) contain the length of the sub-packets
in bits, 27.

The 11 bits labeled A contain the first sub-packet, a literal value
representing the number 10.

The 16 bits labeled B contain the second sub-packet, a literal value
representing the number 20.


After reading 11 and 16 bits of sub-packet data, the total length indicated in
L (27) is reached, and so parsing of this packet stops.

As another example, here is an operator packet (hexadecimal string
EE00D40C823060) with length type ID 1 that contains three sub-packets:

11101110000000001101010000001100100000100011000001100000
VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC


The three bits labeled V (111) are the packet version, 7.
The three bits labeled T (011) are the packet type ID, 3, which means the
packet is an operator.

The bit labeled I (1) is the length type ID, which indicates that the length is
a 11-bit number representing the number of sub-packets.

The 11 bits labeled L (00000000011) contain the number of sub-packets, 3.
The 11 bits labeled A contain the first sub-packet, a literal value
representing the number 1.

The 11 bits labeled B contain the second sub-packet, a literal value
representing the number 2.

The 11 bits labeled C contain the third sub-packet, a literal value
representing the number 3.


After reading 3 complete sub-packets, the number of sub-packets indicated in L
(3) is reached, and so parsing of this packet stops.

For now, parse the hierarchy of the packets throughout the transmission and add
up all of the version numbers.

Here are a few more examples of hexadecimal-encoded transmissions:

8A004A801A8002F478 represents an operator packet (version 4) which contains an
operator packet (version 1) which contains an operator packet (version 5)
which contains a literal value (version 6); this packet has a version sum of
16.

620080001611562C8802118E34 represents an operator packet (version 3) which
contains two sub-packets; each sub-packet is an operator packet that contains
two literal values. This packet has a version sum of 12.

C0015000016115A2E0802F182340 has the same structure as the previous example,
but the outermost packet uses a different length type ID. This packet has a
version sum of 23.

A0016C880162017C3686B18A3D4780 is an operator packet that contains an operator
packet that contains an operator packet that contains five literal values; it
has a version sum of 31.


Decode the structure of your hexadecimal-encoded BITS transmission; what do you
get if you add up the version numbers in all packets?



--- Part Two ---
Now that you have the structure of your transmission decoded, you can calculate
the value of the expression it represents.

Literal values (type ID 4) represent a single number as described above. The
remaining type IDs are more interesting:


Packets with type ID 0 are sum packets - their value is the sum of the values
of their sub-packets. If they only have a single sub-packet, their value is
the value of the sub-packet.

Packets with type ID 1 are product packets - their value is the result of
multiplying together the values of their sub-packets. If they only have a
single sub-packet, their value is the value of the sub-packet.

Packets with type ID 2 are minimum packets - their value is the minimum of the
values of their sub-packets.

Packets with type ID 3 are maximum packets - their value is the maximum of the
values of their sub-packets.

Packets with type ID 5 are greater than packets - their value is 1 if the value
of the first sub-packet is greater than the value of the second sub-packet;
otherwise, their value is 0. These packets always have exactly two
sub-packets.

Packets with type ID 6 are less than packets - their value is 1 if the value of
the first sub-packet is less than the value of the second sub-packet;
otherwise, their value is 0. These packets always have exactly two
sub-packets.

Packets with type ID 7 are equal to packets - their value is 1 if the value of
the first sub-packet is equal to the value of the second sub-packet;
otherwise, their value is 0. These packets always have exactly two
sub-packets.


Using these rules, you can now work out the value of the outermost packet in
your BITS transmission.

For example:

C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
04005AC33890 finds the product of 6 and 9, resulting in the value 54.
880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
D8005AC2A8F0 produces 1, because 5 is less than 15.
F600BC2D8F produces 0, because 5 is not greater than 15.
9C005AC2F8F0 produces 0, because 5 is not equal to 15.
9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.

What do you get if you evaluate the expression represented by your
hexadecimal-encoded BITS transmission?

"""


import math
from io import TextIOWrapper

hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

binary_to_hex = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return [y.strip() for x in in_file.readlines() for y in x.strip()]


def convert_hex_to_bin(packet):
    b = hex_to_binary[packet]
    # print(f"- {packet}: {b}")
    return b


def get_packet_version(bit):
    h = binary_to_hex[bit.zfill(4)]
    return h


def get_packet_type(bit):
    """ 4 is literal anything else is operator"""
    h = binary_to_hex[bit.zfill(4)]
    return h


def convert_to_number(bit):
    if bit[0] == "1":
        n = bit[1:]
        return n, False
    else:
        n = bit[1:5]
        return n, True


def decode_packet(packet, versions, values):
    version = get_packet_version(packet[:3])
    packet_type = get_packet_type(packet[3:6])
    versions.append(int(version))
    # print(" -- ************************************* --")
    # print(f" -- {packet=}")
    # print(f" -- {version=}")
    print(f" -- {packet_type=}")
    packet, values = read_packet(packet[6:], packet_type, versions, values)
    return packet, values


def check_type_id_and_values(type_id, values, i):
    print(i)
    i = -i
    if type_id == '0':
        print(type_id, values)
        if len(values) == 2:
            values = [sum(values)]
        if len(values) > 2:
            values = [*values[:i], sum(values[i:])]
        print(type_id, values)

        pass
    if type_id == '1':
        print(type_id, values)
        if len(values) == 2:
            values = [math.prod(values)]
        if len(values) > 2:
            values = [*values[:i], math.prod(values[i:])]
        print(type_id, values)
        pass
    if type_id == '2':
        print(type_id, values)

        if len(values) == 2:
            values = [min(values)]
        if len(values) > 2:
            values = [*values[:i], min(values[i:])]
        print(type_id, values)
        pass
    if type_id == '3':
        print(type_id, values)
        if len(values) == 2:
            values = [max(values)]
        if len(values) > 2:
            values = [*values[:i], max(values[i:])]
        print(type_id, values)
        pass
    if type_id == '5':
        print(type_id, values)
        a = values.pop()
        b = values.pop()
        values.append(1 if b > a else 0)
        print(type_id, values)
        pass
    if type_id == '6':
        print(type_id, values)
        a = values.pop()
        b = values.pop()
        values.append(1 if b < a else 0)
        print(type_id, values)
        pass
    if type_id == '7':
        print(type_id, values)
        a = values.pop()
        b = values.pop()
        values.append(1 if b == a else 0)
        print(type_id, values)
        pass
    return values


def read_packet(packet, type_id, versions, values):
    if type_id == '4':
        # print("********** Literal")
        # print(f"{packet=}")
        nums = ''
        for i in range(0, len(packet), 5):
            # print(i)
            num = packet[i:i+5]
            # print(f"{num=}")
            n, end_of_packet = convert_to_number(num)
            # print(f"{n=}")
            nums += n
            if end_of_packet:
                # print(f"{nums=}")
                values.append(int(nums, 2))
                to_return = packet[i+5:]
                break

        # print(int(nums, 2))
    else:
        to_return = None
        # print(" ********** Operator")
        # print(f"{packet=}")
        if packet[0] == '0':
            # print(f"{packet[0]=} Type : length of each subpacket")
            # the next 15 bits are a number that represents the
            # total length in bits of the sub-packets
            # contained by this packet

            length_in_bits = int(packet[1:16], 2)
            # print(f"{length_in_bits=}")
            packet = packet[16:]
            sub_packet = packet
            i = 0
            while len(sub_packet) > 7:
                sub_packet, values = decode_packet(sub_packet[:length_in_bits], versions, values)
                i += 1
            values = check_type_id_and_values(type_id, values, i)
            to_return = packet[length_in_bits:]
        else:
            # the next 11 bits are a number that represents
            # the number of sub-packets immediately contained
            # by this packet.
            # print(f"{packet[0]=} Type = number of subpacket")
            number_of_subpackets = int(packet[1:12], 2)
            # print(f"{number_of_subpackets=}")
            sub_packet = packet[12:]

            for _ in range(number_of_subpackets):
                sub_packet, values = decode_packet(sub_packet, versions, values)

            values = check_type_id_and_values(type_id, values, number_of_subpackets)
            packet = sub_packet
            to_return = packet

    return to_return, values


if __name__ == "__main__":
    with open("Day_16/input.txt", "r", encoding='utf-8') as f:
        data = format_data(f)
        # print(data)
        versions = []
        values = []
        packet = ''
        for char in data:
            packet += (convert_hex_to_bin(char))
        packet, values = decode_packet(packet, versions, values)
        print(f"{values=}")
        print(sum(versions))
