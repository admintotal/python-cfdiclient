# -*- coding: utf-8 -*-
from cfdiclient import VerificaSolicitudDescarga
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

v_descarga = VerificaSolicitudDescarga(fiel)

auth = Autenticacion(fiel)
token = auth.obtener_token()

id_solicitud = '8b109c9c-8918-4382-ad9e-5ba904e301ec'
result = v_descarga.verificar_descarga(token, RFC, id_solicitud)
print(result)
