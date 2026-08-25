import re

def validate_user_payload(data: dict, is_update: bool = False) -> tuple[bool, str | None]:
    """
    Valida a integridade do payload de usuário.
    - is_update=False (POST): Exige nome e email obrigatórios.
    - is_update=True (PUT): Valida apenas os campos fornecidos.
    """
    if not isinstance(data, dict):
        return False, "O corpo da requisicao deve ser um objeto JSON valido."

    if not is_update:
        if "nome" not in data or not str(data.get("nome", "")).strip():
            return False, "O campo 'nome' é obrigatorio e nao pode estar vazio."
        if "email" not in data or not str(data.get("email", "")).strip():
            return False, "O campo 'email' é obrigatorio e nao pode estar vazio."

    # Validação do tipo e conteúdo de 'nome' (se fornecido)
    if "nome" in data:
        nome = data["nome"]
        if not isinstance(nome, str) or len(nome.strip()) < 3:
            return False, "O campo 'nome' deve ser um texto com no minimo 3 caracteres."

    # Validação de formato regex de 'email' (se fornecido)
    if "email" in data:
        email = data["email"]
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not isinstance(email, str) or not re.match(email_regex, email.strip()):
            return False, "O campo 'email' possui um formato invalido."

    return True, None