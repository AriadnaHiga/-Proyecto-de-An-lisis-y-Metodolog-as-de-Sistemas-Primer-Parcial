import string

def contiene_caracteres_invalidos(texto):
    # Devuelve True si el texto contiene caracteres que no son letras ni espacios
    return any(c not in string.ascii_letters + "áéíóúÁÉÍÓÚñÑ " for c in texto)

def validar_datos(nombre, apellido, puesto, pedido):
    # Validación de nombre, apellido y puesto: solo letras (y espacios)
    if contiene_caracteres_invalidos(nombre) or contiene_caracteres_invalidos(apellido) or contiene_caracteres_invalidos(puesto):
        return False
    # Validar que el pedido no esté vacío
    if pedido.strip() == "":
        return False
    return True

def sistema_envios():
    print("===================================")
    print("BIENVENIDOS A Barc.Co")
    print("SISTEMA DE ADMINISTRACIÓN DE ENVÍOS")
    print("===================================\n")

    while True:
        # Solicita los datos
        nombre = input("Ingresa tu nombre: ").strip()
        apellido = input("Ingresa tu apellido: ").strip()
        puesto = input("Ingresa tu puesto: ").strip()
        pedido = input("Ingresa el pedido: ").strip()

        # Validación
        if validar_datos(nombre, apellido, puesto, pedido):
            print("\n✅ Tu pedido está en el contenedor.")
            break  # termina el sistema
        else:
            print("\n❌ ERROR: No se permiten símbolos o campos vacíos. Vuelve a intentarlo.\n")

    print("\nFIN DEL PROCESO.")

# Ejecutar el sistema
sistema_envios()
