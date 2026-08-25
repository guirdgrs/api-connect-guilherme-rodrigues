# API Connect - Gerenciamento de Usuários

## Objetivo da API
API RESTful desenvolvida como Produto Mínimo Viável (MVP) para uma startup de tecnologia. O sistema provê endpoints para gerenciamento completo de usuários (CRUD), servindo de base estável para integração com aplicações front-end.

---

## Tecnologias Utilizadas
* **Python 3.10**
* **Flask** (Microframework web)
* **Flask-CORS** (Gerenciamento de requisições Cross-Origin)
* **python-dotenv** (Gerenciamento de variáveis de ambiente)

---

## Passo a Passo para Execução Local

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/guirdgrs/api-connect-guilherme-rodrigues.git
   cd api-connect-nome-sobrenome
   ```

2. **Criar e ativar o ambiente virtual:**
   ```bash
   python -m venv venv

   #Windows (PowerShell):
   .\venv\Scripts\Activate.ps1

   #Linux/macOS
   source venv/bin/activate
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ``` 
4. **Executar a aplicação:**
   ```bash
   python app.py
   ```
## Endpoints da API
| Método | Endpoint | Descrição | Status Sucesso |
| :--- | :--- | :--- | :--- |
| GET | / | Health Check do servidor | 200 OK |
| GET | /users | Listagem geral de usuários | 200 OK |
| GET | /users/\<id\> | Busca específica de usuário por ID | 200 OK / 404 Not Found |
| POST | /users | Cadastro de novo usuário | 201 Created / 400 Bad Request |
| PUT | /users/\<id\> | Atualização de usuário existente | 200 OK / 404 Not Found |
| DELETE | /users/\<id\> | Remoção de usuário por ID | 200 OK / 404 Not Found |

### Exemplo de Payload
   ```json
   {
    "nome": "Guilherme Rodrigues",
    "email": "guilhermerodrigues@gmail.com" 
   }
