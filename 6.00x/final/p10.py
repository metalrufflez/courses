def integrate(f, a, b, parts):
    spacing = float(b-a)/parts
    current = 0
    for i in range(parts):
        current += spacing * f(a+ i*spacing)
    return current

def successiveApproxIntegrate(f, a, b, epsilon):
    parts = 4
    while (integrate(f, a, b, parts) - integrate(f, a, b, parts/2) < epsilon):
        parts = parts + 2
        
    return integrate(f, a, b, parts)


