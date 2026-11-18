import hashlib

hash_obj = "e201994dca9320fc94336603b1cfc970"  # "secreto"
with open("diccionario.txt", "r") as f:
    for line in f:
        word = line.strip()
        if hashlib.md5(word.encode()).hexdigest() == hash_obj:
            print(f"Contraseña: {word}")
            break