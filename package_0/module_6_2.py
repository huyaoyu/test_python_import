
import inspect
import os

# if __name__ == '__main__':
#     import sys
#     sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import package_0
from .package_2.module_9 import p_0_p_2_m_9_f_0

def p_0_m_6_2_f_0():
    print(f'{inspect.stack()[0][3]} calls p_0_p_2_m_9_f_0')
    p_0_p_2_m_9_f_0()
    
if __name__ == '__main__':
    print(f'{os.path.abspath(__file__)} calls p_0_m_6_2_f_0')
    p_0_m_6_2_f_0()