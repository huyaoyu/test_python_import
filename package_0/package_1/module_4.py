import inspect
import os

from module_5 import p_0_m_5_f_0

def p_0_p_1_m_4_f_0():
    print(f'{inspect.stack()[0][3]} calls p_0_m_5_f_0')
    p_0_m_5_f_0()

if __name__ == '__main__':
    print(os.path.abspath(__file__))
    print(f'calls p_0_m_5_f_0')
    p_0_m_5_f_0()