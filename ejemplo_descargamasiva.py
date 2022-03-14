# -*- coding: utf-8 -*-
import pdb
from cfdiclient import DescargaMasiva
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

auth = Autenticacion(fiel)
token = auth.obtener_token()

descarga = DescargaMasiva(fiel)

rfc_solicitante = 'XAXX010101000'
id_paquete = '2d8bbdf1-c36d-4b51-a57c-c1744acdd89c_01'
result = descarga.descargar_paquete(token, rfc_solicitante, id_paquete)
print(result)