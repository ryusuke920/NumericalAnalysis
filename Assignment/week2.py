from math import exp

def f(x):
    return x ** 2

def g(x):
    return exp(-x)

def h(x):
    return g(x) - f(x)

def h_prime(x):
    return -g(x) - 2 * x

def Newton(ini,err):
    x_n = ini
    x_n_scc = 0
    count = 0

    while True:
        count += 1
        x_n_scc = x_n - h(x_n) / h_prime(x_n)
        print(\
            count," Slolution:",x_n_scc, "\n")

        if abs(x_n_scc - x_n) < err:
            break
        x_n = x_n_scc
    print(\
        "Slolution:", x_n_scc, "\n"
        "Function Value:", h(x_n_scc), "\n"
        "Iteration:",count)
Newton(0.5, 0.00001)	    