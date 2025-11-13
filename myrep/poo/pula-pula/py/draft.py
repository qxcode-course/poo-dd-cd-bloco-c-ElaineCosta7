class Criança:
    def __init__(self, nome: str, idade: int):
        self.__nome: str = nome
        self.__idade: int = idade

    def getNome(self) -> str:
        return self.__nome
    def getIdade(self) -> int:
        return self.__idade

    def setNome(self, nome: str) -> str:
        self.__nome = nome
    def setIdade(self, idade: int) -> int:
        self.__idade = idade

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__idade}"
    
class Trampolim:
    def __init__(self):
        self.__brincando: list[Criança] = []
        self.__espera: list[Criança] = []

    def arrive(self, criança: Criança) -> None:
        self.__espera.append(criança)
        self.__espera.sort(key=lambda c: c.getIdade())

    def enter(self):
        if len(self.__espera) == 0:
            return
        criança = self.__espera.pop(-1)
        self.__brincando.append(criança)


    def __str__(self) -> str:
        brincando = ", ".join([str(x) for x in self.__brincando])
        espera = ", ".join([str(x) for x in self.__espera])
        return f"[{espera}] => [{brincando}]"

def main():
    trampolim = Trampolim()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(trampolim)
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            criança = Criança(nome, idade)
            trampolim.arrive(criança)
        elif args[0] == "enter":
            trampolim.enter()
        else:
            print("comando invalido")

main()

    

