# Ejecutar con permisos de admin

import scapy.all as scapy 


def scan(ip):

	scapy.arping(ip)


scan("172.16.144.1/24")