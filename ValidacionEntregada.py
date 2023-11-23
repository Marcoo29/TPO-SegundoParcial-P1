def validacion(usuario_ingresado, contraseña_ingresada):
    usuario = "Coding_Ninja"
    contraseña = "Minecraft123"
    resultado = False
    if usuario == usuario_ingresado and contraseña == contraseña_ingresada:
        resultado = True
    return resultado