from polynom.poly_logic import read_poly
from polynom.poly_logic import diff
from polynom.poly_logic import poly2str
s = '4x^1+0x'
polynom = read_poly(s)
print(polynom)
print(diff(polynom))
print(poly2str(diff(polynom)))
