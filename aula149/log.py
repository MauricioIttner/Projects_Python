# Abstração
# Log
from pathlib import Path
LOG_DIR = Path(__file__).parent / 'log.txt'


class Log:  # Mãe
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatted = f'{msg} ({self.__class__.__name__})'
        print('SALVANDO NO LOG...', msg_formatted)
        with open(LOG_DIR, 'a')as arquivo:
            arquivo.write(msg_formatted)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer')
    lp.log_success('qualquer')
    lf = LogFileMixin()
    lf.log_error('qualquer')
    lf.log_success('qualquer')
