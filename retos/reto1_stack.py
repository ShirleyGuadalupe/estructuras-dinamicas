"""
Reto 1: Validador de expresión usando Stack.
Paréntesis válidos: (), {}, []

Función a implementar:
    validate_expression(expression: str) -> bool

Reglas:
- Recorre la cadena; apila aperturas; ante un cierre, desapila y compara.
- Si al final la pila queda vacía y nunca hubo desajuste -> True.

Tips:
- Usa Stack de estructuras/stack.py
"""

from estructuras.stack import Stack

PARES = {')': '(', '}': '{', ']': '['}

def validate_expression(expression: str) -> bool:
    # TODO: Implementar con Stack siguiendo las reglas de arriba.
    # Debe ser O(n) en tiempo; O(n) espacio peor caso.
    pila = Stack()
    for elemento in expression :
        if elemento in PARES.values() :
            pila.push(elemento)
        elif elemento in PARES.keys() :
            if pila.is_empty() or pila.pop() != PARES[elemento] :
                return False
    return pila.is_empty()