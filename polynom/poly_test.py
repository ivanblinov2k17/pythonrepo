from unittest import TestCase, main
from polynom.poly_logic import read_poly, diff, poly2str


class Tester(TestCase):
    def test_true_poly_1(self):
        self.assertEqual(poly2str(diff(read_poly('10x^4+10x^6+6x'))),
                         '60x^5+40x^3+6')

    def test_true_poly_2(self):
        self.assertEqual(poly2str(diff(read_poly('x'))), '1')

    def test_true_poly_3(self):
        self.assertEqual(poly2str(diff(read_poly('x^2'))), '2x')

    def test_true_poly_4(self):
        self.assertEqual(poly2str(diff(read_poly('x^5-x^4-x^2'))),
                         '5x^4-4x^3-2x')

    def test_true_poly_5(self):
        self.assertEqual(poly2str(diff(read_poly('10x^155-x'))),
                         '1550x^154-1')

    def test_true_poly_6(self):
        self.assertEqual(poly2str(diff(read_poly('1+x^9+x^10'))),
                         '10x^9+9x^8')

    def test_true_poly_7(self):
        self.assertEqual(poly2str(diff(read_poly('1'))), '0')

    def test_true_poly_8(self):
        self.assertEqual(poly2str(diff(read_poly('-1-x^9+x^10'))),
                         '10x^9-9x^8')

    def test_true_poly_9(self):
        self.assertEqual(poly2str(diff(read_poly('-x^9-1+x^10'))),
                         '10x^9-9x^8')

    def test_true_poly_10(self):
        self.assertEqual(poly2str(diff(read_poly('-1-x^9+x^10-x'))),
                         '10x^9-9x^8-1')


if __name__ == '__main__':
    main()
