Esse programa em Python calcula a sequência de Fibonacci e retorna uma mensagem avisando se o número informado pertence ou não a sequência.

A função fibonacci_sequence(n) recebe um número n como argumento e retorna uma lista com a sequência de Fibonacci até o número n. A função inicia a sequência com 0 e 1, adiciona o próximo número à sequência enquanto ele for menor que n, e retorna a sequência completa. A função inclui uma docstring explicando o que a função faz, quais são os argumentos e o que ela retorna.

A função is_fibonacci_number(n) recebe um número n como argumento e verifica se ele pertence à sequência de Fibonacci. A função verifica se o número é negativo, pois a sequência de Fibonacci começa com 0 e 1. A função usa a função fibonacci_sequence(n) para obter a sequência de Fibonacci até o número n e verifica se o número n está presente na sequência. A função retorna True se o número pertence à sequência de Fibonacci, e False caso contrário. A função também inclui uma docstring explicando o que ela faz e quais são os argumentos e o que ela retorna.

O programa solicita ao usuário um número para verificar se ele pertence à sequência de Fibonacci.

O programa usa a função is_fibonacci_number(n) para verificar se o número informado pertence à sequência de Fibonacci e imprime uma mensagem informando se o número pertence ou não à sequência.
