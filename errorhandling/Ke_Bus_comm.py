## @package Ke_Bus_comm
#Kommunikation per SOcket zum Busmaster
#
#Enthält alle Funktionen zur KOmmunikation mit der Sensor-Aktor-Hardware

import sys
import struct
import time
import logging

from socket_client import Socket_Sender, KeSocketError
import config
#Adressen der Slaves und deren Befehlscodes
import config_Slaves as adr
#import Wetter_logging

logger = logging.getLogger('Raspi_GH')

class KeBusError(Exception):
    def __init__(self, typ, wert):
        super().__init__()
        self.typ = typ
        self.wert = wert

def call_for_sensorvalue(address, command, timeout_in_s=1):
    '''Sendet Befehl ohne Parameter'''
    return send_command(adr.TYP_CMD, address, command, wert=0, timeout_in_s=timeout_in_s)

## Sende Befehl an Busmaster
# Versucht mehrmals Socket zum Busmaster zu schicken
# und liefert Ergebnis der dreistufigen Kommunikation Raspi->Busmaster->Busslave->Sensor/Aktor
# In jeder Ebene können Fehler entstehen, die zurückgemeldet werden
# Die Rückgabe besteht aus: # Typ-ID, Typname, Kommunikations-Ergebnis
# Bei einem fehlerfreien Kommunikationsergebnis, wird Typname TYP_RESI oder TYP_REST zurückgegeben liegt
def send_command(msgtyp, address, command, wert=0, timeout_in_s=1):
    #Hier noch testen ob wert<= 0xFFFF
    #Hier noch testen ob timout<= 255

    try:
        #Verpacke Daten in Byte-Feld
        msg = struct.pack('<BBBBhB', 7, msgtyp, address, command, wert, timeout_in_s)
        logger.debug("Sende an Slave %s: <%s> .", address, msg)
    except:
        logger.error('Packen des Byte-Feldes fehlgeschlagen', exc_info=True)
        raise KeBusError(adr.TYP_PACK_ERR, "")

    #Socket-Sender anlegen
    Sender = Socket_Sender(config.bus_master_ip, config.bus_master_port)

    buserr = None
    socketerr = None

    #Versuche Socket-Kommunikation bis max retries erreicht
    for socket_retries in range(0, config.max_socket_retries):

        try:
            #Sende Socket wirft Fehler wenn keine Kommunikation möglich
            result = Sender.send(msg)
        except KeSocketError as myerr:
            #Fehlversuch loggen und erneut versuchen
            socketerr = myerr
            logger.error("Fehler beim Socket senden:%s", sys.exc_info())
        else:
            #Socket-Kommunikation erfolgreich
            #Trotzdem kann untergeordnete Bus- oder Sensor-Kommunikation fehlgeschlagen sein
            #Analysiere Ergebnis

            # 2 Bytes der Antwort (Len der Antwort und Typ) aus Byte-Feld auspacken
            msglen, typ = struct.unpack_from('BB', result)
            logger.debug("Antwort len: %s typ: %s .", msglen, typ)

            #Antwort mit Int-Wert
            if typ == adr.TYP_RESI:
                erg = struct.unpack_from('<h', result, 2)
                logger.debug("TYP_RESI mit Wert <%s>", erg[0])
                answer = (typ, erg[0])
                break #Abbruch, da gueltige Antowrt

            #Anwort mit Text
            elif typ == adr.TYP_REST:
                erg = str(result[2:], "ascii")
                logger.debug("TYP_REST mit Wert <%s>", erg)
                answer = (typ, erg)
                break #Abbruch, da gueltige Antowrt

            #Keine Antwort ueber Bus vom slave erhalten
            elif typ == adr.TYP_NORESPONSE:
                #erg enthaelt BUS-Fehlerkenner
                erg = struct.unpack_from('B', result, 2)
                logger.error("TYP_NORESPONSE  <%s>", erg[0])
                #Fehler zum raise weiter unten erzeugen
                buserr = KeBusError(typ, erg[0])

            #Sensorfehler
            elif typ == adr.TYP_SLAVE_ERR:
                #erg enthaelt Slave-Fehlerkenner
                erg = struct.unpack_from('B', result, 2)
                logger.error("TYP_SLAVE_ERR  <%s>", erg[0])
                buserr = KeBusError(typ, erg[0])

        finally:
            #warten und noch mal versuchen
            time.sleep(1)
        print(socket_retries, config.max_socket_retries)

    #kein gültiger Versuch
    if socket_retries == config.max_socket_retries-1:

        if buserr is not None:
            #Falls letzter Versuch mit Busfehler endete
            raise buserr
        if socketerr is not None:
            #Falls letzter Versuch mit socketfehler endete
            raise socketerr
        #Falls keine Verbindung zum Busmastwer möglich
        raise KeBusError(adr.TYP_SOCKET_ERR, "Keine Socketverbindung")

    # Typ-ID, Typname, Kommunikations-Ergebnis
    return answer

################################################ Tests ab hier
def check_int_answer():
    #In der Simulation kommt auf diesen Befehl die Antwort 999
    typ, value = send_command(adr.TYP_CMD, adr.ADR_ATTINY_HYGBOD, adr.CMD_HYGBOD_GETVAL, 0, 3)
    print("-----\n answertype {} Bodenfeuchte in V: {}".format(typ, value))

def check_text_answer():
    #In der Simulation kommt auf diesen Befehl die Antwort 'Ich messe Bodenfeuchte'
    typ, value = send_command(adr.TYP_CMD, adr.ADR_ATTINY_HYGBOD, adr.CMD_HYGBOD_TEXTTEST, 0, 3)
    print("-----\n answertype {} 'Ich messe Bodenfeuchte': <{}>".format(typ, value))

def check_slave_err_answer():
    try:
        #simuliert kommt Antwort TYP_SLAVE_ERR 111
        typ, value = send_command(adr.TYP_CMD, adr.ADR_ATTINY_433, adr.CMD_433_A_OFF, 0, 3)
        print("-----\n Erwarte Slave-Error 111 bekam answertype {} {}".format(typ, value))
    except KeSocketError as kerr:
        print('Fehler erkannt:', kerr, sys.exc_info())
    except KeBusError as berr:
        print('Fehler erkannt:', berr.typ, berr.wert, sys.exc_info())

def check_noresponse_err_answer():
    try:
        #simuliert kommt Antwort TYP_NORESPONSE 222
        typ, value = send_command(adr.TYP_CMD, adr.ADR_ATTINY_433, adr.CMD_433_A_ON, 0, 3)
        print("-----\n Erwarte Noresponse-Error 222 bekam answertype {} {}".format(typ, value))
    except (KeBusError, KeSocketError):
        print(sys.exc_info())

if __name__ == '__main__':
    #check_int_answer()
    #check_text_answer()
    check_slave_err_answer()
    #check_noresponse_err_answer()
