xA, yA = map(int, input('Введите координаты точки А через пробел: ').split())
xB, yB = map(int, input('Введите координаты точки B через пробел: ').split())
xC, yC = map(int, input('Введите координаты точки C через пробел: ').split())

len_AB = ((xA - xB)**2 + (yA - yB)**2)**0.5
len_BC = ((xC - xB)**2 + (yC - yB)**2)**0.5
len_AC = ((xA - xC)**2 + (yA - yC)**2)**0.5

if len_AB > len_BC:
    len_AB, len_BC = len_BC, len_AB
    xA, yA, xC, yC = xC, yC, xA, yA
if len_BC > len_AC:
    len_AC, len_BC = len_BC, len_AC
    xA, yA, xB, yB = xB, yB, xA, yA
if len_AB > len_BC:
    len_AB, len_BC = len_BC, len_AB
    xA, yA, xC, yC = xC, yC, xA, yA
    
M_k_min = 0.5 * (2 * len_AC**2 + 2 * len_BC**2 - len_AB**2)**0.5
M_k_max = 0.5 * (2 * len_AB**2 + 2 * len_BC**2 - len_AC**2)**0.5
M_k_med = 0.5 * (2 * len_AC**2 + 2 * len_AB**2 - len_BC**2)**0.5

B_k_min = (len_BC * len_AC * (len_BC + len_AC + len_AB) * (len_BC + len_AC - len_AB))**0.5 / (len_BC + len_AC)
B_k_max = (len_BC * len_AB * (len_BC + len_AC + len_AB) * (len_BC + len_AB - len_AC))**0.5 / (len_BC + len_AB)
B_k_med = (len_AB * len_AC * (len_BC + len_AC + len_AB) * (len_AC + len_AB - len_BC))**0.5 / (len_AB + len_AC)

P = (len_AB + len_BC + len_AC) / 2
S = (P * (P - len_AB) * (P - len_BC) * (P - len_AC))**0.5

H_k_min = 2 / len_AB * S
H_k_max = 2 / len_AC * S
H_k_med = 2 / len_BC * S

R = len_AB * len_BC * len_AC / (4 * S)
r = S / P

from math import degrees, asin

angle_min = degrees(asin(2 * S / (len_BC * len_AC)))
angle_max = degrees(asin(2 * S / (len_BC * len_AB)))
angle_med = degrees(asin(2 * S / (len_AB * len_AC)))
