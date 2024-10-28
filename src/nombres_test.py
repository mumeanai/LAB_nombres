from nombres import *

def test_leer_frecuencias_nombres():
    datos = leer_frecuencias_nombres("data/frecuencias_nombres.csv")
    print("La primera persona es: ", datos[0])
    print("La última persona es: ", datos[-1])
    
def test_filtrar_por_genero(datos):
    print("Las personas filtradas son: ", len(filtrar_por_genero(datos, "Hombre")))
    print("Las personas filtradas son: ", len(filtrar_por_genero(datos, "Mujer")))
    
def test_calcular_nombres(datos):
    print("Los nombres de las personas de dicho género son:", calcular_nombres(datos, "Mujer"))
    print("Los nombres de las personas de dicho género son:", calcular_nombres(datos, "Hombre"))
    
def test_calcular_nombres_ambos_generos(datos):
    print("Los nomnbre usados para amnbos géneros son:", calcular_nombres_ambos_generos(datos))
    
def test_calcular_nombres_compuestos(datos):
    print("Los nombres de las mujeres con nombre compuesto son:", calcular_nombres_compuestos(datos, "Mujer"))
    print("Los nombres de los hombres con nombre compuesto son:", calcular_nombres_compuestos(datos, "Hombre"))
    
if __name__=="__main__":
    datos = leer_frecuencias_nombres("data/frecuencias_nombres.csv")

    test_leer_frecuencias_nombres()
    test_filtrar_por_genero(datos)
    test_calcular_nombres(datos)
    test_calcular_nombres_ambos_generos(datos)
    test_calcular_nombres_compuestos(datos)