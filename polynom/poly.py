import polynom.poly_logic as logic
s = '21x^6 + 50x^4 - 8x'
polynom = logic.reading(s)
logic.print_poly(logic.diff(polynom))
