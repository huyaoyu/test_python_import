import inspect
import os

def p_0_p_1_m_0_f_0():
    print(inspect.stack()[0][3])

if __name__ == '__main__':
    print(os.path.abspath(__file__))
    print(f'calls p_0_p_1_m_0_f_0')
    p_0_p_1_m_0_f_0()