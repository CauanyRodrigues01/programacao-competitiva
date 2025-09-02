# https://neps.academy/br/exercise/976

def main():

    moedas = int(input())
    marinheiros = int(input())

    capitao = (moedas/(marinheiros+2))*2

    print(f"{capitao:.0f}")

if __name__ == "__main__":
    main()
