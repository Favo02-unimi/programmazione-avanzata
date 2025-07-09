class UpDownFile:
    BREAK = "!@#$%^&*()_+=[]{};:'\",<>./?\\| \n\t"

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        # si potrebbe leggere tutto il file con read qua dentro,
        # splittare le parole e tenere semplicemente un indice
        # però si perde il senso dell'iteratore
        # dato che file grossi verrebbero caricati tutti direttamente
        # in memoria
        self.file = open(self.filename)
        self.read = []
        self.stepsback = 0
        return self

    def __next__(self):

        # quindi tocca scrivere sta porcata (che si può scrivere 1000 volte meglio)
        # che legge un carattere alla volta
        def _read_word():
            acc = []
            while True:
                r = self.file.read(1)
                if r == "":
                    raise StopIteration
                if r in UpDownFile.BREAK and len(acc) > 0:
                    return "".join(acc)
                if r not in UpDownFile.BREAK:
                    acc.append(r)

        assert self.stepsback >= 0
        if self.stepsback > 0:
            res = self.read[-self.stepsback]
            self.stepsback -= 1
            return res

        self.read.append(_read_word())
        return self.read[-1]

    def ungetw(self):
        self.stepsback += 1

if __name__ == "__main__":
    fiter = UpDownFile('up_down_file.txt')
    iter(fiter)
    print('### Let\'s go up and down for a little')
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    print('### Let\'s finish the iteration')
    try:
        while True:
            print(next(fiter))
    except StopIteration: pass
    print('### Let\'s restart the iteration')
    iter(fiter)
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    print(next(fiter))
