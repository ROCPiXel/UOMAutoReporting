from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import datetime
import Definitions
import Logger
import re
import base64
import Captcha

# 以下：基础方法
def ElementIsExists(drive, xpath):
    try:
        drive.find_element(by.XPATH, xpath)
        return True
    except:
        return False
    
def FindElementIfExists(drive, xpath, waitTime=1):
    i = 0
    while ElementIsExists(drive=drive, xpath=xpath) != True:
        i += 1
        logger.pwl(tag='[WARN]',usingDatetime=False, content=f'元素 {str(xpath)} 未找到，重试 {str(i)}次')
        time.sleep(waitTime)
    return drive.find_element(by.XPATH, xpath)

def BackspaceClean(element, deviation = 10): # From: https://blog.csdn.net/xianzhe_/article/details/119697764
    lens = len(element.get_attribute("value")) + deviation
    for i in range(lens):
        element.send_keys(keys.BACKSPACE)
    if len(element.get_attribute("value")) != 0:
        element.send_keys(keys.CONTROL, 'a')
        element.sned_keys(keys.BACKSPACE)

def CleanWithSend(element, text:str, **kwargs):
    BackspaceClean(element, **kwargs)
    element.send_keys(text)

# 以下：登录界面
def FillCaptcha(isFirstTime=False):
    global CaptchaIsSuccess
    try:
        time.sleep(0.5)
        driver.find_element(by.XPATH, Definitions.CloseBox_XPATH).click()
        CaptchaIsSuccess = False
    except:
        CaptchaIsSuccess = False if isFirstTime else True

    try:
        image = FindElementIfExists(driver, Definitions.CaptchaImage_XPATH)
    except:
        driver.find_element(by.XPATH, Definitions.CloseBox_XPATH).click()
        time.sleep(1)
        image = FindElementIfExists(driver, Definitions.CaptchaImage_XPATH)
    imagePath = f'CaptchaPic\\{str(timeNow.strftime("%Y-%m-%d-%H%M%S.%f"))}.jpg'
    with open(imagePath, 'wb') as f:
        f.write(base64.b64decode(image.get_attribute('src').split('jpeg;base64,')[-1]))
    captcha = Captcha.Captcha(imagePath)

    CleanWithSend(driver.find_element(by.XPATH, Definitions.CaptchaInput_XPATH), keys.BACKSPACE)
    CleanWithSend(driver.find_element(by.XPATH, Definitions.CaptchaInput_XPATH), Captcha.GetCalcResult(captcha.OCR()))
    try: 
        driver.find_element(by.XPATH, Definitions.CloseBox_XPATH).click() 
    except:
        pass

def TryInputPhoneNum():
    FindElementIfExists(driver, Definitions.PhoneNumInput_XPATH, waitTime=1).send_keys(profile.PhoneNum)

# 以下：操作方法，负责模拟用户状态
def TryGetTabButton():
    FindElementIfExists(driver, Definitions.TabButton_XPATH, waitTime=1).click()

def OpenMenu():
    FindElementIfExists(driver, Definitions.Menu1_XPATH, 1).click() # 飞行活动申请
    FindElementIfExists(driver, Definitions.Menu2_XPATH, 1).click() # 一般飞行活动
    try:
        for _ in range(3): 
            driver.find_element(by.XPATH,  Definitions.Menu2_XPATH).click()
            time.sleep(0.3)
    except:
        pass
    logger.pwl(content='----------完成目录展开----------')

def CopyTask():
    FindElementIfExists(driver, Definitions.CopyTaskButton_XPATH, 1).click() # 仅适配单一模板，等待后期更新.
    logger.pwl(content='----------已完成复制飞行任务，准备自动填写信息----------')

def CreateNewTask():
    time.sleep(1)
    FindElementIfExists(driver, Definitions.CreateNewTaskButton_XPATH, 1).click()
    logger.pwl(content='----------已完成新建飞行任务，准备自动填写信息----------')

def AutoFillContent():
    CleanWithSend(FindElementIfExists(driver, Definitions.StartTimeBox_XPATH, 1), profile.StartTime)
    CleanWithSend(FindElementIfExists(driver, Definitions.FinishTimeBox_XPATH, 1), profile.FinishTime)
    logger.pwl(content='完成时间更改')
    driver.find_element(by.XPATH, Definitions.ChangeTypeBox_XPATH).click()
    FindElementIfExists(driver, Definitions.ChangeTypeButton_XPATH, 0.5).click()
    logger.pwl(content='完成 任务性质 更改')
    CleanWithSend(FindElementIfExists(driver, Definitions.HeightInput_XPATH, 1), profile.Height)
    logger.pwl(content='完成高度更改')

    CleanWithSend(driver.find_element(by.XPATH, Definitions.LocationInput_XPATH), profile.Location); logger.pwl(content='完成 起降备降场地 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.EmergencyProcessInput_XPATH), profile.EmergencyProcess); logger.pwl(content='完成 应急处置程序 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.SpecialReqInput_XPATH), profile.SpecialReq); logger.pwl(content='完成 特殊飞行保障需求 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.AbilitiesInput_XPATH), profile.Abilities); logger.pwl(content='完成 通信、导航和被监视能力 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.SpeedInput_XPATH), profile.Speed); logger.pwl(content='完成 飞行速度和进出空域方法 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.ControlInput_XPATH), profile.ControlAbilities); logger.pwl(content='完成 指挥控制链路无线电频率以及占用带宽 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.RadarInput_XPATH), profile.Radar); logger.pwl(content='完成 二次雷达应答机或有关自动监视设备代码 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.OtherInfoInput_XPATH), profile.Other); logger.pwl(content='完成 其他必要信息 更改')

    FindElementIfExists(driver, Definitions.AddDeviceButton_XPATH, 1).click()
    FindElementIfExists(driver, Definitions.DeviceChooseCheckBox_XPATH, 0.5).click()
    FindElementIfExists(driver, Definitions.DeviceDoneButton_XPATH, 0.5).click()
    logger.pwl(content='完成 航空器信息 点选')
    FindElementIfExists(driver, Definitions.AddControllerButton_XPATH, 1).click()
    FindElementIfExists(driver, Definitions.ControllerChooseCheckBox_XPATH, 0.5).click()
    FindElementIfExists(driver, Definitions.ControllerDoneButton_XPATH, 0.5).click()
    logger.pwl(content='完成 操控员信息 点选')

    driver.find_element(by.XPATH, Definitions.NullCheckBox_XPATH).click()
    logger.pwl(content='完成复选框点选')
    driver.find_element(by.XPATH, Definitions.ChangeAirspaceButton_XPATH).click()
    logger.pwl(content="----------自动填表已结束，点击下方按钮提交/保存/放弃----------")

    if profile.UsingAutoReport == 'Submit':
        driver.find_element(by.XPATH, Definitions.FinishButton_XPATH).click()
        FindElementIfExists(driver, Definitions.SubmitButton_XPATH, 2).click()
        logger.pwl(tag='[DONE]', content='----------已完成自动提交申请----------')
    elif profile.UsingAutoReport == 'Save':
        driver.find_element(by.XPATH, Definitions.SaveFileButton_XPATH).click()
        logger.pwl(tag='[DONE]', content='----------已完成保存提交申请----------')

# 以下：主程序
# 初始化方法
CaptchaIsSuccess = False
timeNow = datetime.datetime.now()
profile = Definitions.Configures()
logger = Logger.Logger(f'Log\\{str(timeNow.strftime("%Y-%m-%d-%H%M%S.%f"))}.log', usingLogger=profile.UsingLogger)

logger.wl(tag='[START]', usingDatetime=False, content=str(timeNow))
logger.pwl(tag='[REDY]', content=f'已从{profile.FilePath}获取配置' )
try:
    driver = webdriver.Edge()
    driver.get("https://uom.caac.gov.cn/")
except:
    logger.pwl(tag='[ERR]', content='无法初始化网页，请重试')

TryInputPhoneNum()
if profile.AutoCaptcha:
    FillCaptcha(True)
    driver.find_element(by.XPATH, Definitions.GetSmscodeButton_XPATH).click()
    i = 0
    while CaptchaIsSuccess != True:
        i += 1
        #time.sleep(0.1)
        FillCaptcha(False)
        driver.find_element(by.XPATH, Definitions.GetSmscodeButton_XPATH).click()
        logger.pwl('[WARN]', content=f'验证码出现错误，重试{i}次')
logger.pwl(content='----------在接下来的页面中进行登录----------')

TryGetTabButton()
OpenMenu()

try:
    driver.switch_to.frame(FindElementIfExists(driver, Definitions.IFrame2_XPATH, 1))
except:
    driver.switch_to.frame(FindElementIfExists(driver, Definitions.IFrame1_XPATH, 1))
#CopyTask()
CreateNewTask()
time.sleep(3)

driver.switch_to.default_content()
try:
    driver.switch_to.frame(FindElementIfExists(driver, Definitions.IFrame2_XPATH, 1))
except:
    driver.switch_to.frame(FindElementIfExists(driver, Definitions.IFrameNewPage_XPATH, 1))
AutoFillContent()
logger.close()

time.sleep(1000) # 新版本Edge/Chrome通病，主线程增加等待防止闪退