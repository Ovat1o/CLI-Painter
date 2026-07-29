class Colors:
    # Códigos ANSI para as cores no terminal
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    
    # Reseta a cor para o padrão do terminal
    RESET = '\033[0m' 
    
    # Deixa o texto em negrito
    BOLD = '\033[1m'  

def print_success(message):
    # Imprime mensagem de sucesso em verde e negrito
    print(f"{Colors.GREEN}{Colors.BOLD}✓ {message}{Colors.RESET}")

def print_error(message):
    # Imprime mensagem de erro em vermelho
    print(f"{Colors.RED}✗ {message}{Colors.RESET}")

def print_warning(message):
    # Imprime aviso em amarelo
    print(f"{Colors.YELLOW}⚠ {message}{Colors.RESET}")
    
def print_info(message):
    # Imprime informação em azul
    print(f"{Colors.BLUE}ℹ {message}{Colors.RESET}")