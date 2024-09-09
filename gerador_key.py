import secrets

# Gera uma chave de 16 bytes e converte para hexadecimal
key = secrets.token_hex(16)

print(key)
