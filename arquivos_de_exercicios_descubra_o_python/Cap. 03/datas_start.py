#
# Arquivo com exemplos de manipulação de  datas
#

from datetime import date
from datetime import datetime
from datetime import time

def ManipulaDataEHora():
    hoje = date.today()
    print("hoje é : " , hoje)
    print("Partes da data: ", hoje.day, hoje.month, hoje.year)

ManipulaDataEHora()
