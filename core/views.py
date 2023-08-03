from django.shortcuts import render,HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Word</h1>')
def operação(request, operação, n1, n2):
    conta = 0,
    if operação == "soma":
        conta = n1 + n2,
    elif operação == "multiplicação":
        conta = n1 * n2,
    elif operação == "divisão":
        conta= n1 / n2,
    return HttpResponse('A {} dos números {} e {} é igual a: {}'.format(operação, n1, n2, conta))
