import hashlib
import itertools
import string

hash_obj = "8e41b8197a1e94d06214743e740314b2"  # "a4f"
chars = string.ascii_lowercase + string.digits

for length in range(1, 5):
    for combo in itertools.product(chars, repeat=length):
        word = "".join(combo)
        if hashlib.md5(word.encode()).hexdigest() == hash_obj:
            print(f"Contraseña: {word}")
            exit()