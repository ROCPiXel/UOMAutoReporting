'''
Captcha.py: 
验证码相关操作，使用ddddocr
'''
import ddddocr

class Captcha:
    def __init__(self, path:str):
        self.captchaFile = path
        self.ocr = ddddocr.DdddOcr()
    def OCR(self) -> str:
        with open(self.captchaFile, 'rb') as f:
            imgBytes = f.read()
        self.result = self.ocr.classification(imgBytes)
        return self.result
    def GetResult(self) -> str :
        return self.result
    
def GetCalcResult(string:str):
    characterList = list(string)
    if characterList[1] == '+':
        return int(characterList[0]) + int(characterList[2])
    elif characterList[1] == '-':
        return int(characterList[0]) - int(characterList[2])
    elif characterList[1] == '*' or characterList[1] == '×':
        return int(characterList[0]) * int(characterList[2])
    elif characterList[1] == '+' or characterList[1] == '÷':
        return int(characterList[0]) / int(characterList[2])
    else:
        return 'Err'
    
if __name__ == "__main__":
    testStr = Captcha('CaptchaPic\\2024-12-07-182200.229262.jpg').OCR()
    print(GetCalcResult(testStr))
