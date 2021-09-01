import math

def angle1_a(g, m1, m2, t1, t2, L1, L2, v1, v2):

    num1 = -g * (2 * m1 + m2) * math.sin(t1)
    num2 = -m2 * g * math.sin(t1 - 2 * t2)
    num3 = -2 * math.sin(t1 - t2)
    num4 = v2 * v2 * L2 + v1 * v1 * L1 * math.cos(t1 - t2)
    num5 = L1 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

    return (num1 + num2 + num3 * num4)/num5

def angle2_a(g, m1, m2, t1, t2, L1, L2, v1, v2):
    num1 = 2 * math.sin(t1 - t2)
    num2 = v1 * v1 * L1 * (m1 + m2) 
    num3 = g * (m1 + m2) * math.cos(t1)
    num4 = v2 * v2 * L2 * m2 * math.cos(t1 - t2)
    num5 = L2 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

    return (num1 * (num2 + num3 + num4))/num5 

