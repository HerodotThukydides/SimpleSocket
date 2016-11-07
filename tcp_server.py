#-*- coding: UTF-8 -*-
import socket

    # 1. Adress Familie -> IPv4; AF_INET6 ist IPv6
    # 2. Welches Protokoll? TCP; SOCK_DGRAM wäre UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # An den Port binden; IP nicht notwending
s.bind( ("", 8080) )

    # nur eine Verbindung parallel verarbeiten
s.listen(1)

    # Verbindung mit Client erstellen
conn, addr = s.accept()

print "Verbidnung von Host: {}, port {}".format(addr[0], addr[1])

    #Buffergröße
data = conn.recv(1024)

    # Die Daten an "*" splitten und unter jeweiligen Variablen Speichern
operator, zahl1, zahl2 = data.split("*")

# Bekannte Operatoren?
UNKOWN_OP = operator == "ADD" or operator == "SUB" or operator == "MUL" or operator == "DIV"

# 1. Wurden Zahlen geschickt?
if zahl1.isdigit() and zahl2.isdigit():
    # 2. Operatoren bekannt?
    if UNKOWN_OP: # Siehe OBEN
        # 3. Berechnen
        if operator == "ADD":
            ergebnis = str( int(zahl1) + int(zahl2) )
        elif operator == "SUB":
            ergebnis = str( int(zahl1) - int(zahl2) )
        elif operator == "MUL":
            ergebnis = str( int(zahl1) * int(zahl2) )
        else: # 4. Sonderfall Division
            if int(zahl2) == 0:
                ergebnis = "Bitte nicht durch 0 teilen!"
            else:
                ergebnis = str( int(zahl1) / int(zahl2) )
    else:
        ergebnis = "Unbekannte Operation!"

else:
    ergebnis = "Bitte Zahlen verwenden.\nFormat ==> Operator*Zahl1*Zahl2"

    # Das gesendete muss entweder String oder Buffer sein
conn.send(ergebnis)

conn.close()
s.close()
