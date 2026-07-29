# CLI Painter 🎨

Uma biblioteca simples em Python para colorir mensagens no terminal, ideal para alertas, sucessos e erros em mini apps.

## Como importar usando Git Submodules

Execute o comando abaixo na raiz do seu projeto principal:

`git submodule add <LINK_DO_SEU_GITHUB/cli-painter.git>`

## Como utilizar

No seu arquivo Python principal, importe a biblioteca e chame as funções:

```python
import sys
sys.path.append('./cli-painter')
from clipainter import print_success, print_error, print_warning, print_info

print_success("Operação realizada com sucesso!")
print_error("Falha ao conectar no banco.")
print_warning("Atenção ao uso de memória.")
print_info("Iniciando o sistema...")