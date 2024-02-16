## @package socket_client
# Senden von Befehlen an den Bus-Master per socket
import logging
import traceback
import sys


logger = logging.getLogger('Raspi_GH')


class KeError2(Exception):
    def __init__(self, typ, wert):
        super().__init__()
        self.typ = typ
        self.wert = wert

class KeError1(Exception):
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

class AClass:

    def make_err(self):
        y = 0
        try:
            x = 100 / y
        except (BaseException, Exception) as err:
            msg = 'Meine Meldung\n'
            logger.error(msg, exc_info=True)
            myerr = KeError1('KlausErr1', msg).with_traceback(err.__traceback__)
            raise myerr

    def just_raise(self):
        raise KeError2('KlausErr2', 'Meldung 2')

    def raise_n_catch(self):
        try:
            raise KeError2('KlausErr3', 'Meldung 3')
        except KeError2 as myerr:
            print (sys.exc_info())
            print (myerr.typ)
            print (type(myerr))

if __name__ == '__main__':
    # AClass().make_err()
    # AClass().just_raise()
    AClass().raise_n_catch()
