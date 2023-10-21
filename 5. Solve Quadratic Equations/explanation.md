
## Concept
Use Roots of Quadratic Equation Formula (discriminant, coefficients, etc.)

![Quadratic Formula](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-3e0406efda06bbce611a5a1fadab709d_l3.svg)

discriminant = b^2 - 4ac

if d > 0:
root1 = (-b + discriminant) / 2a
root2 = (-b - discriminant) / 2a

if d = 0:
root1 = root2 = -b / 2a {because √dis = 0}

if d < 0:
complex roots/ not real roots/imaginary roots

## Modules Required
- ```import math```

## Variable(s) Required
- a, b, c [coefficients]
- discriminant
- square root of discriminant
- soln1, soln2 (or directly print)

## Function(s) Required
- findRoots(a,b,c)

## Check(s) Required
- if equation/coefficient is valid [a != 0]
- value of discriminant [< 0, > 0, = 0]
