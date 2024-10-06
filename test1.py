path = "/home/ubuntu/devops/test.txt"

mydoc = open(path,'a')
print("Que quieres escribir en el archivo?")
entrar=input()
mydoc.write(entrar)
mydoc.close()
print("quieres ver el archivo? y/n")
imprimir=input()
if imprimir is"y":
    mydoc = open(path,'r')
    print(mydoc.read())
else:
    print("chido barrio")
