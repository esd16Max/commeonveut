from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import re

def callback(packet):
	if packet[TCP].payload:
		pkt = str(packet[TCP].payload)
		if packet[IP].dport == 80 and "POST" in str(packet[TCP].payload):
			print "-" * 60
			print("\n{} to {}:{}:\n".format(packet[IP].src, packet[IP].dst, packet[IP].dport))
			print "-" * 60
			print str(bytes(packet[TCP].payload))
			print "-" * 60
sniff(filter="tcp", prn=callback, store=0)
