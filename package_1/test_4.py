import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

from package_0.module_6_2 import p_0_m_6_2_f_0

if __name__ == '__main__':
    print(f'{os.path.abspath(__file__)} calls p_0_m_6_2_f_0')
    p_0_m_6_2_f_0()
    