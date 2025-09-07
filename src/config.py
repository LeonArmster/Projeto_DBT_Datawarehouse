#biblioteca
from pathlib import Path

# Caminho para base do projeto
base_dir = Path(__file__).resolve().parent.parent

# Diretorios
env = base_dir / '.env'



print(env)