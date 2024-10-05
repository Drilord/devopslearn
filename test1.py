path = "/home/ubuntu/devops/test.txt"

mydoc = open(path,'+a')
print("Que quieres escribir en el archivo?")
entrar=input()
mydoc.write(entrar)
print("quieres ver el archivo? y/n")
imprimir=input()
if imprimir is"y":
    read = mydoc.read()
    print(read)
else:
    print("chido barrio")
