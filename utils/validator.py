def validar_entradas(entry_n,entry_l,entry_m):
    """
    Recibe tres objetos de la clase entry, captura los tres elementos
    dentro de la interfaz y valida si pueden ser calculados
    retorna en forma de tupla los valores n,l,m
    """
    n = int(entry_n.get())
    l = int(entry_l.get())
    m = int(entry_m.get())
    if n <= 0 or l < 0 or l >= n or not (-l <= m <= l):
        raise ValueError("Debe cumplirse: n > 0, 0 ≤ l < n, y -l ≤ m ≤ l.")
    return n, l, m