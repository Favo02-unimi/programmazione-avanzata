# def magic(classto):
#     print("magic", classto)

#     class wrapped:
#         def __init__(self, classfrom):
#             print("init", classfrom)
#             self.classto = classto
#             self.classfrom = classfrom

#         def __call__(self, *args):
#             print("call", args)
#             for k, v in self.classfrom.__dict__.items():
#                 if callable(v) and not k.startswith("__"):
#                     print("method", k)
#             return self.classfrom(*args)

#         def __getattr__(self, name):
#             # On attribute fetch
#             print(f"I'm fetching {self.wrapped}.{name} ...")
#             return getattr(self.classfrom, name)

#     return wrapped

# class magic:
#     def __init__(self, classto):
#         print("init", classto)
#         self.classto = classto

#     def __call__(self, classfrom):
#         print("call", classfrom)
#         self.classfrom = classfrom
#         print(classfrom.__dict__)
#         return classfrom

def magic(classto):

    def wrapped(classfrom):

        class MagicFrom:
            def __init__(self, *args):
                print("init", args)
                self.classfrominstance = classfrom(*args)

            def __call__(self, *args):
                print("call", args)

            def __getattr__(self, name):
                print("fetch", name)
                if callable(self.classfrominstance.__class__.__dict__[name]):
                    method = self.classfrominstance.__class__.__dict__[name]
                    print("fetching callable", name)
                    setattr(classto, name, method)
                return getattr(self.classfrominstance, name)

        return MagicFrom

    return wrapped

class Empty: pass

@magic(Empty)
class Person:
    def __init__(self, name, gross, netp):
        self.gross_salary = gross
        self.netpercentage = netp
        self.name = name
    def who(self): return self.name
    def salary(self): return self.gross_salary*self.netpercentage/12

@magic(Empty)
class Exam:
    def __init__(self, title, n, ne):
        self.title = title
        self.students = n
        self.exams = ne
    def todo(self): return "still {} students should pass the {} exam".format(self.students-self.exams, self.title)

if __name__ == "__main__":
    m = Empty()
    x = Exam("PA", 100, 15)
    y = Exam("TSP", 50, 45)
    p = Person("Bob", 100000, .6)
    try: print("m salary :- ",m.salary())
    except Exception as e: print("*** {0}: {1}".format(type(e).__name__, e))
    print("p salary :- ", p.salary())
    print("m salary :- ", m.salary())
    try: print("m todo :- ", m.todo())
    except Exception as e: print("*** {0}: {1}".format(type(e).__name__, e))
    print("x todo :- ", x.todo())
    print("m todo :- ", m.todo())
    p.netpercentage=.45
    print("m salary :- ", m.salary())
    print("y todo :- ", y.todo())
    print("m todo :- ", m.todo())
    print("m students :- ",m.students)
    print("x todo :- ", x.todo())
    print("m students :- ",m.students)
    try: print("m who :- ",m.who)
    except Exception as e: print("*** {0}: {1}".format(type(e).__name__, e))
