import socket, os
from cryptography.fernet import Fernet

class Client():
  def __init__(self, server_url=socket.gethostbyname(socket.gethostname()), server_port="25565"):
    self.server_url = server_url
    self.server_port = int(server_port)
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connected = False
    self.fernet = None

  def send_message(self):
    client_message = input("enter a message >> ")
    self.client_socket.send(self.encode_message(client_message))

  def exit(self):
    self.client_socket.send(self.encode_message("3"))
    self.client_socket.close()
    self.connected = False

  def init_crypt_service(self):
    fernet_key = bytes(input("enter fernet key >> "), "utf-8")
    self.fernet =Fernet(fernet_key)
    self.client_socket.send(bytes("4", "utf-8"))

  def start(self):
    self.client_socket.connect((self.server_url, self.server_port))
    self.connected = True
    while self.connected:
      print("esperando mensagem...")
      server_message = self.decode_message(self.client_socket.recv(4096))
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f"{server_message}")
      user_input = input(f"(1) send message, (2) refresh chat, (3) exit{', (4) start crypt service ' if self.fernet == None else ' '}>> ")[0]
      if user_input == "1": self.send_message()
      elif user_input == "2": self.client_socket.send(self.encode_message("2"))
      elif user_input == "3": self.exit()
      elif user_input == "4": self.init_crypt_service()
      else: self.exit()
  
  def encode_message(self, message: str):
    bytes_message = bytes(message, "utf-8")
    coded_message = bytes_message if self.fernet == None else self.fernet.encrypt(bytes_message)
    return coded_message

  def decode_message(self, bytes_message: bytes):
    print(f"message: {bytes_message.decode()}")
    decoded_message = (bytes_message if self.fernet == None else self.fernet.decrypt(bytes_message)).decode()
    return decoded_message

if __name__ == "__main__":
  custom_config = input("custom config? (s/n) >> ")[0] == "s"
  client = Client() if custom_config == False else Client(input("enter server hostname >> "), input("enter server port >> "))
  client.start()