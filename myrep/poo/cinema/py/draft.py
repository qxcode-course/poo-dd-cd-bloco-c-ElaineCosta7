class Client:
    def __init__(self, id: str, phone: int):
        self.__id: list[str] = []
        self.__phone: int = phone

    def getId(self) -> str:
        return self.__id
    def getPhone(self) -> int:
        return self.__id

    def setPhone(self, fone: int) -> int:
        self.__phone = fone
    def setId(self, id: str) -> str:
        self.__id = id

    def __str__(self) -> str:
        return f"{self.__id}"
    
class Theater:
    def __init__(self, capacity: int):
        self.__seats: list[Client | None] = [None] * capacity 
        self.__capacity: int = capacity

    #def __search(self, name: str) -> int:
    
    #def __verifyIndex(self, index: int) -> bool:

    #def reserve(self, id: str, phone: int, index: int) -> bool:

    #def cancel(self, id: str) -> None:

    #def getSeats(self) -> Client | None:

    def __str__(self) -> str:
        return f"[" + " ".join(x.getId() if x is not None else "-" for x in self.__seats) + "]"
    
def main():
    theater = Theater(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(theater)
        elif args[0] == "init":
            capacity = int(args[1])
            theater = Theater(capacity)
        else:
            print("comando invalido")
main()