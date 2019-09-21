## @package socket_client
# Senden von Befehlen an den Bus-Master per socket
import logging
import socket
import struct
import traceback

import config

logger = logging.getLogger('Raspi_GH')

class KeSocketError(Exception):
    def __init__(self, typ, descript):
        super().__init__()
        self.typ = typ
        self.descript = descript

    def __str__(self):
        desc = "Ke-Typ: {} Klasse: {}\nKurzbesch:{}"\
            .format(self.typ, self.__class__, self.descript)
        desc += "\ncontext:\n{}".format(self.__context__)
        desc += "\ntraceback:\n"
        for line in traceback.format_tb(self.__traceback__):
            desc += line
        return desc

class Socket_Sender:
    def __init__(self, myhost, myport):
        self.port = myport
        self.host = myhost
        self.timeout = config.socket_timeout
        self.sock = None

    # Veraltet kann weg ?????
    def is_connectable(self):
        # Create a TCP/IP socket
        socket.setdefaulttimeout(self.timeout)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.host, self.port)
        #print ( 'connecting to %s port %s' % server_address)
        try:
            self.sock.connect(server_address)
            logger.info('Connect: Socket-Verbindung zu %s', self.host)
            return True
        except:
            logger.error('Connect: keine Socket-Verbindung zu %s', self.host, exc_info=True)
            return False

    def send(self, text2send):
        # Create a TCP/IP socket
        socket.setdefaulttimeout(self.timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.host, self.port)
        #print ( 'connecting to %s port %s' % server_address)
        try:
            sock.connect(server_address)
        except (TimeoutError, ConnectionResetError, ConnectionRefusedError) as ori_except:
            msg = 'Socket-Connect: keine Socket-Verbindung zu {}'.format(self.host)
            logger.error(msg, exc_info=True)
            myerr = KeSocketError('ConnectErr', msg).with_traceback(ori_except.__traceback__)
            raise myerr #from ori_except
        except (BaseException, Exception) as err:
            msg = 'Unerwarteter Fehler bei Socket-Connect: keine Socket-Verbindung zu {}\n'\
                .format(self.host)
            logger.error(msg, exc_info=True)
            myerr = KeSocketError('UnexpectedConnectErr', msg).with_traceback(err.__traceback__)
            raise myerr

        try:

            # Send data
            sock.sendall(text2send)
            # Look for the response
            amount_received = 1

            heard = b''
            while  amount_received > 0:
                data = sock.recv(64)
                amount_received = len(data)
                heard += data #str(data, 'ascii')
                logger.debug('received "%s"', heard)
            if len(heard) > 0:
                return heard

            msg = 'leere Socket-Antwort von host {}'.format(self.host)
            logger.error(msg, exc_info=True)
            myerr = KeSocketError('EmptyAnswerErr', msg)
            raise myerr
        except KeSocketError as myerr:
            raise myerr
        except (BaseException, Exception) as ori_err:
            msg = 'Unerwarteter Fehler beim Senden zum Host: {}'.format(self.host)
            logger.error(msg, exc_info=True)
            myerr = KeSocketError('UnexpectedSendErr', msg).with_traceback(ori_err.__traceback__)
            raise myerr

        finally:
            #print ( 'closing socket')
            sock.close()

if __name__ == '__main__':
    #host = "192.168.1.17" #ESP32 IP in local network
    #port = 8888             #ESP32 Server Port
    host = config.bus_master_ip
    port = config.bus_master_port

    Sender = Socket_Sender(host, port)
    #Sender.connect()
    slen = 7
    msgtyp = 0x11
    address = 1
    command = 0
    wert = 0
    timeout_in_s = 1
    message = struct.pack('<BBBBhB', slen, msgtyp, address, command, wert, timeout_in_s)
    try:
        res = Sender.send(message)
    except KeSocketError as err:
        print(err)
    else:
        print(res)
