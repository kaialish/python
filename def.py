def centerit(s, w):
    if len(s) >= w:
        return s
    else:
        probeli = (w - len(s)) // 2
        return ' ' * probeli + s

print(centerit("Я", 17))
print(centerit("Люблю", 17))
print(centerit("Свою маму", 17))
