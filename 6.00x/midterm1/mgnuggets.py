def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for a in range(n/6+1):
        for b in range(n/9+1):
            for c in range(n/20+1):
                if 6*a + 9*b + 20*c == n:
                    return True

    return False

print McNuggets(12)
