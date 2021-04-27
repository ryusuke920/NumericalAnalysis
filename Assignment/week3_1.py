from math import exp, log

c, g, W, B = 0.08, 32.2, 527.436, 470.327

a = (W - B) / c
d = 300.0 * c * g / W

def f(v):
    return v + d + a * log(1 - (v / a))

def f_prime(v):
    return 1 - a / (a - v)

def Newton(ini, err):
    x_n = ini
    x_n_scc = 0
    count = 0
    while True:
        count += 1
        x_n_scc = x_n - f(x_n) / f_prime(x_n)
        print(\
            count, " Slolution:", x_n_scc, "\n")

        if abs(x_n_scc-x_n) / x_n_scc < err:
            break
        x_n = x_n_scc
    print(\
        "Slolution:",x_n_scc,"\n"
        "Function Value:",f(x_n_scc),"\n"
        "Iteration:", count)

if __name__ == '__main__':
    Newton(40.0, 0.0001)