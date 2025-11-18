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

    def inserir(self, criança: Criança) -> None:
        self.__espera.append(criança)

    def moverFila(self):
        if len(self.__espera) > 0:
            aux: Criança = self.__espera.pop(0)
            self.__brincando.append(aux)
        return
        
    def moverBrincando(self) -> None:
        if len(self.__brincando) > 0:
            aux = self.__brincando.pop(0)
            self.__espera.append(aux)
        return
        
    def removerCriança(self, criança: Criança, nome: str, idade: int) -> None:
        for i, criança in enumerate(self.__espera):
            if criança.getNome() == nome and criança.getIdade() == idade:
                del self.__espera[i]
                return
            
        for i, criança in enumerate(self.__brincando):
            if criança.getNome() == nome and criança.getIdade() == idade:
               del self.__espera[i]
               return
            
    def removerLista(self, nome: str) -> None:
        
        for i, criança in enumerate(self.__espera):
            if criança.getNome() == nome:
                del self.__espera[i]
                return

        for i, criança in enumerate(self.__brincando):
            if criança.getNome() == nome:
                del self.__brincando[i]
                return

        print(f"fail: {nome} nao esta no pula-pula")

    def __str__(self) -> str:
        espera = ", ".join(str(criança) for criança in reversed (self.__espera))
        brincando = ", ".join(str(criança) for criança in reversed (self.__brincando))
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
            trampolim.inserir(criança)
        elif args[0] == "enter":
            trampolim.moverFila()
        elif args[0] == "leave":
            trampolim.moverBrincando()
        elif args[0] == "remove":
            nome = args[1]
            trampolim.removerLista(nome)
        else:
            print("comando invalido")

main()

    

