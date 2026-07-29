#Faça o teste do CLI Painter aqui:

import sys
sys.path.append('./cli-painter') 

from clipainter import print_success, print_error

# Simulando uma ação do sistema
senha_digitada = "123"

if senha_digitada == "admin123":
    print_success("Acesso liberado!")
else:
    print_error("Acesso negado. Senha incorreta.")