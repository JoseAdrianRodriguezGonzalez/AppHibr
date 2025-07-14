def validar_entradas(n,l,m):
    """
    Recibe tres enteros n,l,m, captura los tres elementos
    dentro de la interfaz y valida si pueden ser calculados
    retorna en forma de tupla los valores n,l,m
    """
    if n <= 0 or l < 0 or l >= n or not (-l <= m <= l):
        raise ValueError("Debe cumplirse: n > 0, 0 ≤ l < n, y -l ≤ m ≤ l.")
    return n, l, m