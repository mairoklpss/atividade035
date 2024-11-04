#Ler uma lista de 10 números reais e mostre-os na ordem inversa.

list = []

print('digite 10 números.')

#receber os 10 numeros.
for i in range(1, 11):
    n = input(f"digite o {i} número: ")
    list.append(n)

print("a lista normal:", list)

#reverter a lista.
list.reverse()
print("a lista reversa:", list)