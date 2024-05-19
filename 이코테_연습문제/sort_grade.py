n = 2

d = {'홍길동':95, '이순신':77}

print(dict(sorted(d.items(), key=lambda x: x[1])).keys())