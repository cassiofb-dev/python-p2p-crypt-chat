import socket, threading, requests, time, os
from cryptography.fernet import Fernet

class ClientThread(threading.Thread):
  def __init__(self, client_socket: socket.socket, client_address: tuple[str, int], server: "Server"):
    threading.Thread.__init__(self)
    self.client_socket = client_socket
    self.client_address = client_address
    self.server = server
    self.username = "no_username"
    self.has_to_start_crypt_service = self.server.server_use_crypt
    self.has_to_send_username = True

  def run(self):
    client_message = None
    while True:
      if self.has_to_start_crypt_service:
        self.client_socket.send(bytes("server: fernet enabled, please start crypt service\n", "utf-8"))
        client_message = self.client_socket.recv(4096).decode()
        if client_message == "4": self.has_to_start_crypt_service = False
      elif self.has_to_send_username:
        self.client_socket.send(self.encode_message("server: connected to server, enter a username or send '1'\n"))
        client_message = self.decode_message(self.client_socket.recv(4096))
        if client_message != "1": self.username = client_message
        if client_message != "2":
          self.server.usernames.append(self.username)
          self.server.messages.append(f"server: ({self.username}) joined the chat")
          self.has_to_send_username = False
      else:
        self.send_server_chat()
        client_message = self.decode_message(self.client_socket.recv(4096))
        if client_message == "3": break
        client_username_message = f"({self.username}): {client_message}"
        if client_message != "2": self.server.messages.append(client_username_message)
    self.server.usernames.remove(self.username)
    self.server.messages.append(f"server: ({self.username}) left the chat")
  
  def send_server_chat(self):
    server_message = ""
    server_message += f"server: your username is ({self.username}), have a nice chat\n"
    server_message += "\n".join(self.server.messages)
    server_message += f"\n\nserver: your username is: ({self.username}), there are ({len(self.server.usernames)}) online users"
    self.client_socket.send(self.encode_message(server_message))


  def encode_message(self, message: str):
    bytes_message = bytes(message, "utf-8")
    coded_message = bytes_message if self.server.server_fernet == None else self.server.server_fernet.encrypt(bytes_message)
    return coded_message

  def decode_message(self, bytes_message: bytes):
    decoded_message = (bytes_message if self.server.server_fernet == None else self.server.server_fernet.decrypt(bytes_message)).decode()
    return decoded_message

class Server(threading.Thread):
  def __init__(self, server_url=socket.gethostbyname(socket.gethostname()), server_port="25565", use_crypt=False):
    threading.Thread.__init__(self)
    self.server_url = server_url
    self.server_port = int(server_port)
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_started = False
    self.usernames = []
    self.messages = []
    self.server_use_crypt = use_crypt
    if self.server_use_crypt == False:
      self.server_fernet_key = None
      self.server_fernet = None
    else:
      self.server_fernet_key = Fernet.generate_key()
      self.server_fernet = Fernet(self.server_fernet_key)
      print(f"server starting on crypto mode, paste key for clients: {self.server_fernet_key.decode()}\n5 seconds to clear key and start server...")
      time.sleep(5)
      os.system('cls' if os.name == 'nt' else 'clear')

  def run(self):
    self.server_socket.bind((self.server_url, self.server_port))
    print(f"server started on ({self.server_url}:{self.server_port})")
    print(f"server public ip: {requests.get('https://api.ipify.org').text}")
    self.server_started = True
    while True:
      self.server_socket.listen(1)
      client_socket, client_address = self.server_socket.accept()
      client_thread = ClientThread(client_socket, client_address, self)
      client_thread.start()

if __name__ == "__main__":
  custom_config = input("custom config? (s/n) >> ")[0] == "s"
  server = Server() if custom_config == False else Server(
    server_url=input("enter server hostname >> "),
    server_port=input("enter server port >> "),
    use_crypt=input("use encryption? (s/n) >> ")[0] == "s",
  )
  server.start()