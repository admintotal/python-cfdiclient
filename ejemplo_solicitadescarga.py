# -*- coding: utf-8 -*-
import datetime
from cfdiclient import SolicitaDescarga
from cfdiclient import Fiel
import os
from cfdiclient.autenticacion import Autenticacion

##
## Constantes de Loggin
##
RFC = os.environ.get('RFC', 'ESI920427886')
FIEL_CER = os.environ.get('FIEL_CER', 'certificados/ejemploCer.cer')
FIEL_KEY = os.environ.get('FIEL_KEY', 'certificados/ejemploKey.key')
FIEL_PAS = os.environ.get('FIEL_PASS', '12345678a')

print("*" * 15)
print(f"FIEL_CER = {FIEL_CER}")
print(f"FIEL_KEY = {FIEL_KEY}")
print(f"FIEL_PAS = {FIEL_PAS}")
print("*" * 15)

cer_der = open(FIEL_CER, 'rb').read()
key_der = open(FIEL_KEY, 'rb').read()

fiel = Fiel(cer_der, key_der, FIEL_PAS)

descarga = SolicitaDescarga(fiel)

auth = Autenticacion(fiel)
token = auth.obtener_token()

fecha_inicial = datetime.datetime(2021, 11, 1)
fecha_final = datetime.datetime(2021, 11, 2)

# Emitidos
result = descarga.solicitar_descarga(token, RFC, fecha_inicial, fecha_final, rfc_emisor=RFC)
print(result)

# # Recibidos
# result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final)
# print(result)
