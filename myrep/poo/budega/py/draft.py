class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"{self.__nome}"

class Budega:
    def __init__(self, num_caixas: int):
        self.__caixas: list[Pessoa | None] = []
        for _ in range(num_caixas):
            self.__caixas.append(None)
        self.__espera: list[Pessoa] = []

    def arrive(self, pessoa: Pessoa) -> None:
        self.__espera.append(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.__caixas):
            print("fail: indice inesxistente")
            return
        if self.__caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.__espera) == 0:
            print("fail: sem clientes")
            return
        self.__caixas[index] = self.__espera[0]
        del self.__espera[0]

    def finish(self, index: int) -> Pessoa | None:
        if index < 0 or index >= len(self.__caixas):
            print("fail: caixa inexistente")
            return
        if self.__caixas[index] is None:
            print("fail: caixa vazio")
            return
        self.__caixas[index] = None

    def __str__(self) -> str:
        caixas = ", ".join(["-----" if x is None else str(x) for x in self.__caixas])
        espera = ", ".join([str(x) for x in self.__espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

def main():
    budega = Budega
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(budega)
        elif args[0] == "init":
            caixas = int(args[1])
            budega = Budega(caixas)
        elif args[0] == "arrive":
            nome = args[1]
            pessoa = Pessoa(nome)
            budega.arrive(pessoa)
        elif args[0] == "call":
            index = int(args[1])
            budega.call(index)
        elif args[0] == "finish":
            index = int(args[1])
            budega.finish(index)
        else:
            print("fail: comando invalido")

main()