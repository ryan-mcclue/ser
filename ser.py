#! /usr/bin/env python3
# SPDX-License-Identifier: zlib-acknowledgement

# hosts send or recieve data over a network
# client requests, server responds
# ip address identifies host, 32 bits divided into 4 octets. they are hierarchical in nature
# subnetting (setting a ip address range) is typically done to create a hierarchy of ip addresses
# hosts on a network share the same address space

# a host will reside in a network (any connected computers with some logical grouping. prefixed with medium, e.g. wifi network)
# network within another network is a subnet, i.e will be a subnet of particular ip address space

# data crossing a wire decays? use a repeater to overcome distance limits
# a hub is a multi-port repeater, however it will send data to everyone, even if it is only intended for one particular host
# a bridge connects two hubs, and can learn what hosts are on each side, so can contain signal to one side if packet is to be sent to that side only
# a switch is like a bridge and a hub that can learn what host is on each port. a switch facilitates communication within a network

# a router facilitates communication between networks. ultimatley this will be needed if want to connect our network to the internet
# a router is the logical place to employ security policies
# routers learn which networks they are attached to. knowledge of each of these networks is known as a route, stored in a routing table
# a router has an ip address for each network it is attached to. this ip address is going to serve as the gateway, i.e. each host's way out of their local network
# for a host this will be its default gateway ip address.
# routers create the hierarchy of the internet.
# routing is the process of moving data between networks. a router performs routing.
# switching is the process of moving data within networks.
# there are many other network devices, e.g. access points, load balancers, virtual routers (in the cloud). they all peform both or one of switching or routing.

# fundamental purpose of networking is to allow hosts to share data
# hosts must follow a set of rules, which are divided into the 7 layers of the OSI model
# these rules are to satisfy the fundamental goal of networking
# layer 1 (goal: transportation of bits), i.e. physical, e.g. twisted pair (ethernet), coaxial, fibre, wireless, repeater, hub
# layer 2 (goal: hop to hop) is retreiving and putting bits on wire, e.g switches, NIC uses mac address, (12 hex digits). this layer only concerned with hop to hop, i.e. not necessarily the endpoint but just the next MAC address
# a hop is going from one network to another. many times require multiple hops. each router has it's own NIC, which will have its own MAC address
# the layer 2 header, i.e. mac addresses are removed and added between hops, i.e. between routers
# layer 3 (goal: end-to-end) utilising IP, e.g. routers, hosts (anything with an IP)
# ARP links IP with a MAC address
# is it the computer that has a MAC address or the NIC?
# layer 4 (goal: service to service --> distinguish data streams). like other layers, has addressing scheme, namely ports. TCP and UDP are different strategies to distinguish data streams 
# additional information will be 'layered' onto the packet


# ping uses ICMP defined in RFC? doesn't use ports? 
# traceroute uses UDP with invalid port, manipulating ttl field to traverse routers? understand output?
# ifconfig displays/configures interfaces. what is lo?
# netstat command? kernel has routing table also? how different to routers? what is broadcast address?
# netperf can measure one-way and round-trip latency. how to use?
# the inverse dns lookup of dig and nslookup don't give the actual website name just server?

# promiscuous mode will pass on packets that are not intended for the host
# wireshark is to get a good overview
# usermod -aG wireshark $(whoami); reboot
# to isolate web traffic, search for 'dns' add look for website name. 'frame contains twitter'
# may see multiple tcp sessions, i.e. syn packets for efficiency. the longer the length of conversation more likely bulk of data rather than just security key exchanges
# conversation filter on syn packet.
# useful for tcp.port filtering, protocol filtering and ip.addr
# isolate particular tcp stream? can this be from different addresses?
# statistics->conversations is great to isolate who is consuming data


# issues with threads is synchronisation and memory
# as GIL, can run concurrently not in parallel, i.e if waiting for another, e.g I/O bound, can switch to another
# import _thread

# if having to read buffers of unknown size, e.g. video streaming, perhaps use select syscall?

# can assign anything to a variable with no error: l = sadsad?
# can pass in more parameters to function than accpeted with no error?
# using things from un-imported modules no error
import socket
import struct
import select
import typing
import enum 
import dataclass

# NOTE(Ryan): struct module format string in standard size
# TODO(Ryan): use a namedtuple?
stdint = {
    "u8": "B",
    "u16": "H",
    "u32": "I"
}

@dataclasses.dataclass
class Connection:
    self.sock = typing.Any = 0
    self.addr = typing.Any = 0
    
class ClientMsgID(enum.Enum):
    JOIN
    LEAVE
    INPUT
class ServerMsgID(enum.Enum):
    JOIN_RESULT
    STATE

MAX_CONNECTIONS = 32
connections = [Connection() for i in range(0, MAX_CONNECTIONS)]

#def msg():
#    # maybe just check is within range of type when preparing byte array to send?
#    msg_header_id = stdint["u8"]
#    msg_header_size = stdint["u32"]
#    msg_header = f"={msg_header_id}{msg_header_size}"
#    msg = struct.Struct(msg_header)
#    msg_body = bytes([])

def DEBUGGER_BREAK():
    pass

def loop(client_sock, client_addr):
    while True:
        try:
            # this can read up to 1024 bytes
            # this data may be chunked, i.e. require multiple calls of recv()
            data = client_sock.recv(1024)
            # will get this on any call to recv or send if disconnected
        except socket.error as err:
            if err.errno == errno.ECONNRESET:
                client_sock.close()
                return
            else
                DEBUGGER_BREAK()

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setblocking(False)
    addr = ("127.0.01", 1234)
    try:
        server_sock.bind(addr)
    except Exception as e:
        DEBUGGER_BREAK()

    # TODO(Ryan): What creates an unaccepted connection?
    # TODO(Ryan): Could this throw an exception?
    server_sock.listen(1)
    
    inputs = [server_sock]
    outputs = []

    while True:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for sock in readable:
            if sock is server_sock:
                client_sock, client_address = sock.accept()
                client_sock.setblocking(False)
                inputs.append(client_sock)
            else:
                message = sock.recv(1024)
                if message:
                    # process messasge and store response message to be handled when writable
                    if sock not in outputs:
                        outputs.append(sock)
                else:
                    if sock in outputs:
                        outputs.remove(sock)
                    inputs.remove(sock)
                    sock.close()
                    del messages[sock]
        
        for sock in writable:
            message = messages[sock]
            sock.send(message)

        for sock in exceptional:
            inputs.remove(sock)
            if sock in outputs:
                outputs.remove(sock)
            sock.close()
            del messages[sock]

    # NOTE(Ryan): So debugger can step over all previous statements
    return

if __name__ == "__main__":
    main()
