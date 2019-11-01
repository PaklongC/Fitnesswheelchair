with open("t.properties") as properties:
    l = [line.split("=") for line in properties.readlines()]
    d = {key.strip(): value.strip() for key, value in l}
    print(d)
    print(l)
    properties.close()
    print(d['a'])
