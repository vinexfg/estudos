


class Log:
    def log(self, msg):
        raise NotImplementedError('Implementar o metodo log')
    

class LogFileMixin(Log):
    ...

if __name__ == '__main__':
    l = Log()
    l.Log()
