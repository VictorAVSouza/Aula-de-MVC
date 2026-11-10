def validar_aluno(nome, email, curso):
    if len(nome) < 3:
        return "O nome precisa ter pelo menos 3 letras."
    if "@" not in email or "." not in email:
        return "Digite um e-mail válido."
    if curso == "":
        return "Informe o curso."
    return None