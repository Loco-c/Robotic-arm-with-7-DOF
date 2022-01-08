# Creating a connection
import sim

def connect(port):
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID != -1: print("Connected to remote API server",port)
    else: print('Failed connecting to remote API server')
    
    return clientID

   
# intialization of connection port
clientID = connect(19999)


if __name__ == '__main__':
     connect(19999)

     