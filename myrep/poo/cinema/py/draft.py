class Client:
    def __init__(self, id: str, phone: int):
        self.__id: str = id
        self.__phone: int = phone

    def getId(self) -> str:
        return self.__id
    def getPhone(self) -> int:
        return self.__phone

    def setPhone(self, fone: int) -> None:
        self.__phone = fone
    def setId(self, id: str) -> None:
        self.__id = id

    def __str__(self) -> str:
        return f"{self.__id}:{self.__phone}"
    
class Theater:
    def __init__(self, capacity: int):
        self.__seats: list[Client | None] = [None] * capacity 
        self.__capacity: int = capacity

    #def __search(self, name: str) -> int:
    
    #def __verifyIndex(self, index: int) -> bool:

    def reserve(self, id: str, phone: int, index: int) -> bool:
        if index < 0 or index >= len(self.__seats):
            print("fail: cadeira nao existe")
            return False
        if self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        for c in self.__seats:
            if c is not None and c.getId() == id:
                print("fail: cliente ja esta no cinema")
                return False
        self.__seats[index] = Client(id, phone)
        
    def cancel(self, id: str) -> None:
        for i in range(len(self.__seats)):
            client = self.__seats[i]
            if client is not None and client.getId() == id:
                self.__seats[i] = None
                return
        print("fail: cliente nao esta no cinema")

    #def getSeats(self) -> Client | None:

    def __str__(self) -> str:
        return f"[" + " ".join(str(x) if x is not None else "-" for x in self.__seats) + "]"
    
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
        elif args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            theater.reserve(id, phone, index)
        elif args[0] == "cancel":
            id = args[1]
            theater.cancel(id)
        else:
            print("comando invalido")
main()