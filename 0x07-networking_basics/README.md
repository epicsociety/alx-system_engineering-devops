============================
Network 
------------------------------
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

---------------------------------
TYPES OF NETWORKS
----------------------------------
LAN, WAN, WLAN, MAN, SAN, CAN, PAN

====================================
MAC AND IP ADDRESS
====================================

A MAC address is responsible for local identification and an IP address for global identification. This is the primary difference between a MAC address and IP address, and it affects how they differ in their number of bits, address assignment and interactions. The MAC address is only significant on the LAN to which a device is connected, and it is not used or retained in the data stream once packets leave that network.
Internet routers move the packets from the source network to the destination network and then to the LAN on which the destination device is connected. That local network translates the IP address to a MAC address, adds the MAC address to the data stream and sends the data to the right device.

=============================
TRANSPORT LAYER
=============================
TCP - reliable, three handshakes, no data loss
UDP - no error checking, faster, possible data loss

======================================
> MOST USED PORTS
======================================
22 for SSH
80 for HTTP
443 for HTTPS


-----------------------------------------
ping is a hack == ping -c packets target
------------------------------------------


