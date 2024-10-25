path = "/home/ubuntu/devops/read.txt"

#mydoc = open(path,'r')
#print("Que quieres escribir en el archivo?")
#entrar=input()
#mydoc.write(entrar)
#mydoc.close()
#print("quieres ver el archivo? y/n")
#imprimir=input()
#if imprimir is"y":     //=mydoc.readline(20)
mydoc = open(path,'r', newline="")
list=[line.strip() for line in mydoc.readlines()]
print(list)
#else:
 #   print("chido barrio")
