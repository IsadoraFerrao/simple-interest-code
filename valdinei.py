''' escrever um decorator chamado decorator_imprimir,
que será usado para a função chamada imprima os parâmetros:
capital, taxa e tempo, além do resultado da função.

Com isso, será criada uma função decoradora (decorator) chamada decorator_imprimir que,
ao ser usada com qualquer função parecida com a juros_simples (isto é,
uma função que receba 3 parâmetros — capital, taxa, tempo),
seja retornado um valor numérico correspondente ao juros.'''


def decorator_imprimir(function):
    def manda_pra_funcao_principal(*args,**kwargs):
        function(*args,**kwargs)
    return manda_pra_funcao_principal

@decorator_imprimir
def juros_simples():  
    capital,taxa, tempo = 1000, 5 ,6  
    print(f"Capital: {capital} Taxa: {taxa} %, tempo: {tempo}")
    print(capital * (taxa / 100) * tempo)
    
juros_simples() 