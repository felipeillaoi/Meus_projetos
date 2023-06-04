import hashlib

def encryptar(texto):
    global hash_texto
    hash_texto = hashlib.sha256(texto.encode("utf8"))
    hash_texto = hash_texto.hexdigest()
    return hash_texto
