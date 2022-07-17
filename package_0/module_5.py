
import inspect
import os

from .module_0 import p_0_m_0_f_0

def p_0_m_5_f_0():
    print(f'{inspect.stack()[0][3]} calls p_0_m_0_f_0')
    p_0_m_0_f_0()

if __name__ == '__main__':
    print(f'{os.path.abspath(__file__)} calls p_0_m_5_f_0()')
    p_0_m_5_f_0()