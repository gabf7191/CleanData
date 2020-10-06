x= 0
List = []
file = open("RESULTADO.csv")

with file as f:
    for line in f:
        for char in line:
            x = x +1
            if x == 22:
                List.append(char)
                x= 0
        print(List)
