# https://neps.academy/br/exercise/822

def main():

    distancia = int(input())
    
    resto = (distancia - 3) % 8
    
    if resto == 3:
        print(1)
    elif resto == 4:
        print(2)
    elif resto == 5:
        print(3)

if __name__ == "__main__":
    main()
