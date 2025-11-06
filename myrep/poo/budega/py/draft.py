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
        self.espera: list[Pessoa] = []

    def arrive(self, pessoa: Pessoa) -> None:
        self.espera.append(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.__caixas):
            print("indice inexistente")
            return
        if self.__caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        self.__caixas[index] = self.espera[0]
        del self.espera[0]
 
    def finish(self, index: int) -> Pessoa | None:
        if index < 0 or index >= len(self.__caixas):
            print("fail: caixa inexistente")
            return
        if self.__caixas[index] is None:
            print("fail: caixa vazio")
            return
        self.__caixas[index] = None

    def give_up(self, nome: str) -> Pessoa | None:
        for i, pessoas in enumerate(self.espera):
            if pessoas.getNome() == nome:
                aux = self.espera[i]
                del self.espera[i]
                return aux
            return None
        
    def __str__(self):
        caixas = ", ".join(["-----" if x is None else str(x) for x in self.__caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

def main():
    budega = Budega
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
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
        elif args[0] == "show":
            print(budega)
        else:
            print("comando inválido")


main()
