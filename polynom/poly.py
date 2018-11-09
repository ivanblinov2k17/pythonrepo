from polynom.poly_logic import read_poly
from polynom.poly_logic import diff
from polynom.poly_logic import poly2str
s = '-x^2-x-1'
polynom = read_poly(s)
print(polynom)
print(diff(polynom))
print(poly2str(diff(polynom)))
