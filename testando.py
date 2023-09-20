def composicao(f, g):

    def resultado_gof(x):
        return g(f(x))

    def resultado_gog(x):
        return g(g(x))

    def resultado_fof(x):
        return f(f(x))

    def resultado_fog(x):
        return f(g(x))

    return resultado_gof, resultado_gog, resultado_fof, resultado_fog


definicao_f = input("Digite a definição da função f(x): ")
exec("def f(x): return " + definicao_f)

definicao_g = input("Digite a definição da função g(x): ")
exec("def g(x): return " + definicao_g)

x = float(input("Digite o valor de x: "))

resultado_gof, resultado_gog, resultado_fof, resultado_fog = composicao(f, g)

print("(g ° f)(", x, ") =", resultado_gof(x))
print("(g ° g)(", x, ") =", resultado_gog(x))
print("(f ° f)(", x, ") =", resultado_fof(x))
print("(f ° g)(", x, ") =", resultado_fog(x))
