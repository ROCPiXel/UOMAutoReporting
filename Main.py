from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import datetime
import Definitions

timeNow = datetime.datetime.now()
#defaultStartTime = timeNow.day+1

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
        print('[WARN] 元素' + str(xpath) + '未找到，重试' + str(i) +'次')
        time.sleep(waitTime)
    return drive.find_element(by.XPATH, xpath)

def TryInputPhoneNum():
    FindElementIfExists(driver, Definitions.PhoneNumInput_XPATH, waitTime=1).send_keys(Definitions.PhoneNum)

def TryGetTabButton():
    FindElementIfExists(driver, Definitions.TabButton_XPATH, waitTime=1).click()

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

# 以下：操作方法，负责模拟用户状态
def OpenMenu():
    FindElementIfExists(driver, Definitions.Menu1_XPATH, 1).click() # 飞行活动申请
    FindElementIfExists(driver, Definitions.Menu2_XPATH, 1).click() # 一般飞行活动
    print(f'[INFO] {str(datetime.datetime.now())} ----------完成目录展开----------')

def CopyTask():
    FindElementIfExists(driver, Definitions.CopyTaskButton_XPATH, 1).click() # 仅适配单一模板，等待后期更新.
    print(f'[INFO] {str(datetime.datetime.now())} ----------已完成复制飞行任务，准备自动填写信息----------')

def CreateNewTask():
   # for _ in range(3): 
        #driver.find_element(by.XPATH, Definitions.TabButton_XPATH).click()
    time.sleep(3)
    FindElementIfExists(driver, Definitions.CreateNewTaskButton_XPATH, 1).click() # 仅适配单一模板，等待后期更新.
    print(f'[INFO] {str(datetime.datetime.now())} ----------已完成新建飞行任务，准备自动填写信息----------')

def AutoFillContent():
    CleanWithSend(FindElementIfExists(driver, Definitions.StartTimeBox_XPATH, 1), Definitions.StartTime)
    CleanWithSend(FindElementIfExists(driver, Definitions.FinishTimeBox_XPATH, 1), Definitions.FinishTime)
    print(f'[INFO] {str(datetime.datetime.now())} 完成时间更改')
    driver.find_element(by.XPATH, Definitions.ChangeTypeBox_XPATH).click()
    FindElementIfExists(driver, Definitions.ChangeTypeButton_XPATH, 0.5).click()
    print(f'[INFO] {str(datetime.datetime.now())} 完成 任务性质 更改')
    CleanWithSend(FindElementIfExists(driver, Definitions.HeightInput_XPATH, 1), Definitions.Height)
    print(f'[INFO] {str(datetime.datetime.now())} 完成高度更改')

    CleanWithSend(driver.find_element(by.XPATH, Definitions.LocationInput_XPATH), Definitions.Location); print(f'[INFO] {str(datetime.datetime.now())} 完成 起降备降场地 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.EmergencyProcessInput_XPATH), Definitions.EmergencyProcess); print(f'[INFO] {str(datetime.datetime.now())} 完成 应急处置程序 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.SpecialReqInput_XPATH), Definitions.SpecialReq); print(f'[INFO] {str(datetime.datetime.now())} 完成 特殊飞行保障需求 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.AbilitiesInput_XPATH), Definitions.Abilities); print(f'[INFO] {str(datetime.datetime.now())} 完成 通信、导航和被监视能力 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.SpeedInput_XPATH), Definitions.Speed); print(f'[INFO] {str(datetime.datetime.now())} 完成 飞行速度和进出空域方法 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.ControlInput_XPATH), Definitions.ControlAbilities); print(f'[INFO] {str(datetime.datetime.now())} 完成 指挥控制链路无线电频率以及占用带宽 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.RadarInput_XPATH), Definitions.Radar); print(f'[INFO] {str(datetime.datetime.now())} 完成 二次雷达应答机或有关自动监视设备代码 更改')
    CleanWithSend(driver.find_element(by.XPATH, Definitions.OtherInfoInput_XPATH), Definitions.Other); print(f'[INFO] {str(datetime.datetime.now())} 完成 其他必要信息 更改')

    FindElementIfExists(driver, Definitions.AddDeviceButton_XPATH, 1).click()
    FindElementIfExists(driver, Definitions.DeviceChooseCheckBox_XPATH, 0.5).click()
    FindElementIfExists(driver, Definitions.DeviceDoneButton_XPATH, 0.5).click()
    print(f'[INFO] {str(datetime.datetime.now())} 完成 航空器信息 点选')
    FindElementIfExists(driver, Definitions.AddControllerButton_XPATH, 1).click()
    FindElementIfExists(driver, Definitions.ControllerChooseCheckBox_XPATH, 0.5).click()
    FindElementIfExists(driver, Definitions.ControllerDoneButton_XPATH, 0.5).click()
    print(f'[INFO] {str(datetime.datetime.now())} 完成 操控员信息 点选')

    driver.find_element(by.XPATH, Definitions.NullCheckBox_XPATH).click()
    print(f'[INFO] {str(datetime.datetime.now())} 完成复选框点选')
    driver.find_element(by.XPATH, Definitions.ChangeAirspaceButton_XPATH).click()

# 以下：主程序
print(timeNow)
Definitions.GetProfilePath()
Definitions.GetConfigures(Definitions.FilePath)
print(f'[REDY] {str(datetime.datetime.now())} 已从{Definitions.FilePath}获取配置' )
try:
    driver = webdriver.Edge()
    driver.get("https://uom.caac.gov.cn/")
except:
    print(f'[ERR] {str(datetime.datetime.now())}无法初始化网页，请重试')

TryInputPhoneNum()
print('[INFO] ----------在接下来的页面中进行登录----------')
TryGetTabButton()
OpenMenu()

driver.switch_to.frame(FindElementIfExists(driver, Definitions.IFrame1_XPATH, 1))
#CopyTask()
CreateNewTask()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame(FindElementIfExists(driver, Definitions.IFrameNewPage_XPATH, 1))
AutoFillContent()
print(f"[DONE] {str(datetime.datetime.now())} 自动填表已结束，点击下方按钮提交/保存/放弃")

time.sleep(1000) # 新版本Edge/Chrome通病，主线程增加等待防止闪退