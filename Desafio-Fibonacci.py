def fibonacci_sequence(n):    
#Essa função retorna uma lista com a sequência de Fibonacci até o número informado 'n'.

    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# O 'n' é o número máximo para a sequência, ele retorna uma lista com a sequência até 'n'.

def is_fibonacci_number(n):
# Essa função que verifica se um número pertence à sequência de Fibonacci.
# O 'n' é o número para verificar, e resulta true se o número pertence a sequência de Fibonacci
# E false se não pertence
    if n < 0:
        return False
    fib_sequence = fibonacci_sequence(n)
    if n in fib_sequence:
        return True
    else:
        return False

# Você entre com um número para verificar se pertence à sequência
num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número informado pertence à sequência de Fibonacci ou não
if is_fibonacci_number(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} nao pertence a sequência de Fibonacci.")
