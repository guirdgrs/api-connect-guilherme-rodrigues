class UserRepository:
    def __init__(self):
        # Estrutura de persistência provisória em memória
        self._users = []
        # Mecanismo de geração de ID único incremental
        self._current_id = 0

    def _generate_id(self) -> int:
        """Incrementa e retorna o próximo ID único disponível."""
        self._current_id += 1
        return self._current_id

    def list_all(self):
        """Retorna todos os usuários cadastrados."""
        return self._users

    def find_by_id(self, user_id: int):
        """Busca e retorna um usuário específico pelo ID."""
        return next((user for user in self._users if user["id"] == user_id), None)

    def create(self, data: dict) -> dict:
        """Cria um novo registro associando um ID incremental único."""
        new_user = {
            "id": self._generate_id(),
            "nome": data["nome"],
            "email": data["email"]
        }
        self._users.append(new_user)
        return new_user

    def update(self, user_id: int, data: dict):
        """Atualiza os dados de um usuário existente pelo ID."""
        user = self.find_by_id(user_id)
        if not user:
            return None
        
        user["nome"] = data.get("nome", user["nome"])
        user["email"] = data.get("email", user["email"])
        return user

    def delete(self, user_id: int) -> bool:
        """Remove um usuário da lista pelo ID."""
        user = self.find_by_id(user_id)
        if not user:
            return False
        
        self._users.remove(user)
        return True

# Instância única do repositório para manter o estado dos dados em memória
user_repository = UserRepository()