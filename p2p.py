import time, socket
from client import Client
from server import Server

def init_server(): Server().start()
def init_client(): Client(input("client: enter server hostname >> "), input("client: enter server port >> ")).start()

def init_p2p_default(
  server_use_crypto=False,
  server_port_for_server="25565",
  server_hostname_for_client=socket.gethostbyname(socket.gethostname()),
  server_port_for_client="25565",
):
  server = Server(server_port=server_port_for_server, use_crypt=server_use_crypto)
  client = Client(server_hostname_for_client, server_port_for_client)

  server.start()
  while server.server_started == False: time.sleep(0.2)
  input("p2p: server started, press any key to start client...")
  client.start()

def init_p2p_custom(): init_p2p_default(
  server_use_crypto=input("type (1) to encrypt server >> ") == "1",
  server_port_for_server=input("server: enter port >> "),
  server_hostname_for_client=input("client: enter server hostname >> "),
  server_port_for_client=input("client: enter server port >> "),
)

def init_p2p():
  user_input = input("(1) client mode, (2) server mode, (3) p2p default mode, (4) p2p custom mode >> ")[0]
  if   user_input == "1": init_client()
  elif user_input == "2": init_server()
  elif user_input == "3": init_p2p_default()
  elif user_input == "4": init_p2p_custom()

if __name__ == "__main__": init_p2p()