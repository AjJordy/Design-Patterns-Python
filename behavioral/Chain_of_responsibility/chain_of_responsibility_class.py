from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['A', 'B', 'C']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'handler_ABC: conseguiu tratar o valor {letter}'
        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['D', 'E', 'F']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'handler_DEF: conseguiu tratar o valor {letter}'
        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'Nao tratou {letter}'


if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()    
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))

