from polynom.poly_logic import read_poly
from polynom.poly_logic import diff
from polynom.poly_logic import poly2str
s = '10x^4+10x^6+6x'
polynom = read_poly(s)
print(poly2str(diff(polynom)))
