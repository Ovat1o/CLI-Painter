# CLI Painter 🎨: O Fim do Monocromatismo Depressivo!

Experimente o **CLI Painter**! Uma biblioteca construída com uma arquitetura tão formidável (meia dúzia de variáveis com códigos ANSI) que vai transformar o seu modesto mini app de terminal em uma verdadeira obra de arte. 

## Funcionalidades de Ponta

*  🟢 **Dopamina Visual Technology (`print_success`):** Utilizamos ondas de luz na frequência exata do verde para injetar satisfação instantânea no seu cérebro toda vez que seu código rodar sem quebrar. 

*  🔴 **Protocolo de Pânico (`print_error`):** Por que falhar em silêncio quando você pode sangrar na tela? Esta função não apenas avisa que algo deu errado, mas grita visualmente na cara do usuário, garantindo o desespero apropriado diante de uma falha de sistema.

*  🟡 **Amarelo Ansiedade (`print_warning`):** Alerte os usuários de que algo terrível *pode* acontecer a qualquer momento. Perfeito para manter a tensão e o engajamento no seu sistema.

*  🔵 **Engenharia de Ícones Avançada:** Insere manualmente caracteres complexos (`✓`, `✗`, `⚠`, `ℹ`) na frente das suas strings, poupando incríveis 2 segundos da sua vida. 

## Como integrar esta revolução gráfica

Se você decidiu, em um momento de clareza, que seu sistema merece sair da era das trevas, o complexo ritual de invocação via submódulos Git, é o seguinte:

```bash
git submodule add <COLOQUE_O_SEU_LINK_AQUI>
```

## Guia de Sobrevivência (Como usar)

A curva de aprendizado é quase vertical de tão fácil. Observe:

```python
import sys

sys.path.append('./cli-painter') 

from clipainter import print_success, print_error, print_warning, print_info

# Injetando vida no seu terminal
print_info("Iniciando o sistema com uma interface altamente gráfica.")

print_warning("Cuidado: Nível crítico de gambiarra detectado na linha 42.")

print_error("Falha catastrófica: O dev esqueceu de rodar o git push na sexta-feira.")

print_success("Apesar de tudo, rodou. A nota está garantida!")
```