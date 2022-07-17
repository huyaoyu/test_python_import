import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

from package_0.module_5 import p_0_m_5_f_0

if __name__ == '__main__':
    print(f'{os.path.abspath(__file__)} calls p_0_m_5_f_0')
    p_0_m_5_f_0()
    