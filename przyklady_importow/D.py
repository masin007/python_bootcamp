# from A import foo as foo_z_A
# from B import foo as foo_z_B
#
#
# foo_z_A()
# foo_z_B()

import C
C.A.foo()
C.B.foo()
print(dir(C))
