import math

def eval_f(t, y):
    return (
        y - 
        0.5 * math.exp(t/2) * math.sin(5*t) + 
        5 * math.exp(t/2) * math.cos(5*t)
    )

N = 16

t0 = 0
t_max = 9
h = (t_max - t0) / N

t = t0
y = 0
print('{},{}'.format(t, y))

for i in range(N):
    k1 = eval_f(t, y)
    k2 = eval_f(t + h/2, y + h*k1/2)
    k3 = eval_f(t + h/2, y + h*k2/2)
    k4 = eval_f(t + h, y + h*k3)

    y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
    t += h
    print('{},{}'.format(t, y))