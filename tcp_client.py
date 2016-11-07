#-*- coding: UTF-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Beim Client muss die richitge IP stehen
    # -> hier localhost
s.connect(("localhost", 8080))

# Anfrage formulieren

anfrage = raw_input("> Bitte Anfrage eingeben: ")

s.send(anfrage)

data = s.recv(1024)

print "Ergebnis empfangen: ==>    {}".format(data)

s.close()
