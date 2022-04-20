import pathlib
class dir():
    def __init__(self,dir):
        self.path=pathlib.Path(dir)
    def isconten(self,subdir):
        for i in self.path.iterdir():
            _,sub=str(i).split('/',maxsplit=2)
            if sub==subdir:
                return True
        return False
    def mksubdir(self,subdir):
        if not self.isconten(subdir):
            self.path.mkdir()

d=dir('data')
print(d.isconten('sound'))