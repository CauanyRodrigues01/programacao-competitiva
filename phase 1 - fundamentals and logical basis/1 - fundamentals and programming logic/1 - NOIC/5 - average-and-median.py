# https://neps.academy/br/exercise/1656

def main():

    a, b = map(int, input().split())
    
    opcoes = []
    
    # c < a = mediana = a
    c1 = 2 * a - b
    if c1 <= a: 
        opcoes.append(c1)
    
    # a < c < b = mediana = C
    if (a + b) % 2 == 0:
        c2 = (a + b) // 2
        if a <= c2 <= b: 
            opcoes.append(c2)
    
    # c > b = mediana = b
    c3 = 2 * b - a
    if c3 >= b:
        opcoes.append(c3)
    
    print(min(opcoes))

if __name__ == "__main__":
    main()
