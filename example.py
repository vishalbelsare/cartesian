import numpy as np
from sklearn.utils.validation import check_random_state

from cgp.algorithm import oneplus
from cgp.cgp import create_pset, Terminal, Primitive, to_polish

primitives = [
    Primitive("add", np.add, 2),
    Primitive("mul", np.multiply, 2),
    Terminal("x_0"),
    Terminal("x_1")
]

pset = create_pset(primitives)
rng = check_random_state(None)

x = rng.normal(size=(100, 2))
y = x[:, 1] * x[:, 1] + x[:, 0]
y += 0.05 * rng.normal(size=y.shape)

def func(individual):
    yhat = individual.fit_transform(x)
    return np.sqrt(np.mean((y - yhat)**2))

res = oneplus(func, pset, 2, 2, 2, 1, f_tol=0.1, random_state=rng, max_iter=10000)
print(res)
print(to_polish(res, return_args=False))
