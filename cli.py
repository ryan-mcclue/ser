#! /usr/bin/env python3
# SPDX-License-Identifier: zlib-acknowledgement

# IMPORTANT(Ryan): Python handles network-byte-order translations
import socket

def DEBUGGER_BREAK():
    pass

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", 1234)

    try:
        sock.connect(addr)
    except Exception as e:
        DEBUGGER_BREAK()

    # TODO(Ryan): Could this throw an exception?
    sock.send(b"hello server")

    sock.close()

    return

if __name__ == "__main__":
    main()
