'''
Logger.py: 
日志类
author: ROCPiXel, last change:2024/12/6
'''
import datetime

class Logger:
    def __init__(self, logFilePath:str, usingLogger:bool):
        if usingLogger:
            self.logFilePath = logFilePath
            self.logFile = open(logFilePath, mode='w+', encoding='utf-8')
        else:
            return
    '''
    写日志（行）
    '''
    def wl(self, tag='[INFO]', usingDatetime:bool=True, content:str=''):
        try: 
            self.logFile.write(f'{tag} {datetime.datetime.now()} {content}\n') if usingDatetime else self.logFile.write(f'{tag} {content} \n')
        except: 
            pass
    '''
    在调用端输出日志并写入日志
    '''
    def pwl(self, tag='[INFO]', usingDatetime:bool=True, content:str=''):
        try: 
            self.wl(tag=tag, usingDatetime=usingDatetime, content=content) 
        except: 
            pass
        print(f'{tag} {datetime.datetime.now()} {content}') if usingDatetime else print(f'{tag} {content}')

    def close(self):
        self.logFile.close()