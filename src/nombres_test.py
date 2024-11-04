from nombres import *

def test_leer_frecuencias_nombres():
    datos = leer_frecuencias_nombres("data/frecuencias_nombres.csv")
    print(f"Leidos {len(datos)} registros")
    print("Mostsrando los 3 primeros:", datos[0], datos[1], datos[2], sep = "\n")
    print("Mostrando los 3 últimos:",datos[-3], datos[-2], datos[-1], sep = "\n")
    
def test_filtrar_por_genero(datos):
    print("Número de registros para 'Hombre': ", len(filtrar_por_genero(datos, "Hombre")))
    print("Número de registros para 'Mujer': ", len(filtrar_por_genero(datos, "Mujer")))
    
def test_calcular_nombres(datos):
    print("- Ambos géneros:", calcular_nombres(datos, None)[:10])
    print("- Mujeres:", calcular_nombres(datos, "Mujer")[:10])
    print("- Hombres:", calcular_nombres(datos, "Hombre")[:10])
    
def test_calcular_top_nombres_de_año(datos):
    print("- Ambos géneros:", calcular_top_nombres_de_año(datos, None))
    print("- Mujeres:", calcular_top_nombres_de_año(datos, "Mujer"))
    print("- Hombres:", calcular_top_nombres_de_año(datos, "Hombre"))
    
def test_calcular_nombres_ambos_generos(datos):
    print("Nombres:", calcular_nombres_ambos_generos(datos))
    
def test_calcular_nombres_compuestos(datos):
    print("- Ambos géneros:", calcular_nombres_compuestos(datos, None))
    print("- Mujeres:", calcular_nombres_compuestos(datos, "Mujer"))
    print("- Hombres:", calcular_nombres_compuestos(datos, "Hombre"))

def test_calcular_frecuencia_media_nombre_años(datos):
    print(f"La frecuencia media del nombre Neres entre 2005 y 2010 es {calcular_frecuencia_media_nombre_años(datos, "NEREA",2005, 2010)}")
    
if __name__=="__main__":
    datos = leer_frecuencias_nombres("data/frecuencias_nombres.csv")

    test_leer_frecuencias_nombres()
    test_filtrar_por_genero(datos)
    test_calcular_nombres(datos)
    test_calcular_top_nombres_de_año(datos)
    test_calcular_nombres_ambos_generos(datos)
    test_calcular_nombres_compuestos(datos)
    test_calcular_frecuencia_media_nombre_años(datos)