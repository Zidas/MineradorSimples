from hashlib import sha256
import time

#linha de comando criptografia
def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()

#linha de comando mineração
def minerar(num_bloco, transacoes, hash_anterior, quantos_zeros):
    nonce = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        Hashe = aplicar_sha256(texto)
        if Hashe.startswith("0" * quantos_zeros):
            return nonce, Hashe
        nonce += 1
        
        
#inserção de dados
if __name__ == "__main__":
    num_bloco = #numero do bloco
    transacoes = """ insira as transacoes"""
    quantos_zeros = #quantidade de zeros
    hash_anterior = "insira o hash"

    resultado = minerar(num_bloco, transacoes, hash_anterior, quantos_zeros)
    print(resultado)
    
    #timer
    inicio = time.time()
    print(time.time() - inicio)