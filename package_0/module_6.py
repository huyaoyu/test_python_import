
import inspect

from package_1.module_2 import p_0_p_1_m_2_f_0

def p_0_m_6_f_0():
    print(f'{inspect.stack()[0][3]} calls p_0_p_1_m_2_f_0')
    p_0_p_1_m_2_f_0()