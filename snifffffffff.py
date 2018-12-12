from scapy.all import *

def callback(packet):
	if packet[TCP].payload:
		pkt = str(packet[TCP].payload)
		if packet[IP].dport == 80 and "POST" == str(packet[TCP].payload)[:4]:
			print "-" * 60
			print("\n{} to {}:{}:\n".format(packet[IP].src, packet[IP].dst, packet[IP].dport))
			print "-" * 60
			print str(bytes(packet[TCP].payload))
			print "-" * 60
sniff(filter="tcp", prn=callback, store=0)
