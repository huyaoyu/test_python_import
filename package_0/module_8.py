import inspect

from module_7 import p_0_m_7_f_0

def p_0_m_7_f_0():
    print(f'{inspect.stack()[0][3]} calls p_0_m_7_f_0')
    p_0_m_7_f_0()
