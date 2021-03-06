
# This file was *autogenerated* from the file 422.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_43 = Integer(43); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_61 = Integer(61); _sage_const_1e9 = RealNumber('1e9'); _sage_const_13 = Integer(13); _sage_const_10 = Integer(10); _sage_const_24 = Integer(24)
Qx, Qy = _sage_const_7 , _sage_const_1 
Px1, Py1 = _sage_const_13 , _sage_const_61  / _sage_const_4 
Px2, Py2 = -_sage_const_43  / _sage_const_6 , -_sage_const_4  / _sage_const_1 

def M(x1, y1, x2, y2):
    return _sage_const_24  * x1 * x2 + _sage_const_7  * (x1 * y2 + x2 * y1) - _sage_const_24  * y1 * y2

MOD = int(_sage_const_1e9 ) + _sage_const_7 

last = _sage_const_1 
for i in range(_sage_const_10 ):
    Dx, Dy = Px1 - Qx, Py1 - Qy
    mu = M(Dx, Dy, Px2, Py2) / M(Dx, Dy, Qx, Qy) # (625 - M(Px1, Py1, Qx, Qy))
    Px3, Py3 = Px2 + mu * Dx, Py2 + mu * Dy

    print (Px3.numerator() + Px3.denominator() + Py3.numerator() + Py3.denominator()) % MOD, Px3 - Qx, Py3 - Qy
    cur = gcd(Px3.denominator(), Py3.denominator())
    # print cur / last, last
    last = cur

    Px1, Py1 = Px2, Py2
    Px2, Py2 = Px3, Py3

