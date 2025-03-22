from functools import wraps
def mi_decorador(func):
    @wraps(func)  # <- Copia la metadata de 'func' a 'envoltura'
    def envoltura(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return envoltura

@mi_decorador
def saludar():
    """Esta función dice hola"""
    print("¡Hola!")

print(saludar.__name__)  # 'saludar'
print(saludar.__doc__)   # 'Esta función dice hola'
saludar()
