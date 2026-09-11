def calificaciones (nota1, nota2, nota3):
    promedio =(nota1+nota2+nota3)/3
    return promedio

#Uso de la función
nota1=10
nota2=9
nota3=8
resultado = calificaciones (nota1,nota2,nota3)

print("-----NOTAS----- ")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("El promedio de las notas es: ", resultado)
