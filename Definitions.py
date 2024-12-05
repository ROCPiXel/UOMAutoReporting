'''
Definitions.py: 
存储相关设置方法与固定路径，以便随时修改
author: ROCPiXel lastUpdate: 20241205
isMainApp: False
'''
import datetime
import json

# 以下：网页元素路径
PhoneNumInput_XPATH = '//*[@id="portal"]/section/div[2]/div/div/div[2]/div[1]/div/div/div/form/div[1]/div/div/input'
TabButton_XPATH = '//*[@id="app"]/div/div/div[1]/div[3]/span/strong[9]'
Menu1_XPATH = '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/div/div/ul/div[2]/li/div/span'
Menu2_XPATH = '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/div/div/ul/div[2]/li/ul/div/li/span/div/div'
CopyTaskButton_XPATH = '//*[@id="app"]/div/section/div/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[12]/div/button[1]/span'
CreateNewTaskButton_XPATH = '//*[@id="app"]/div/section/div/div[1]/div[1]/button/span'

IFrame1_XPATH = '//*[@id="main-body-content"]/div[3]/div/div/div[2]/iframe'
IFrameNewPage_XPATH = '//*[@id="main-body-content"]/div[3]/div/div/div[2]/iframe'
IFrameCopyPage_XPATH = '//*[@id="main-body-content"]/div[3]/div/div/div[3]/iframe'

ChangeTypeBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/div/input'
ChangeTypeButton_XPATH = '/html/body/div[2]/div[1]/div[1]/ul/li/span'
StartTimeBox_SELECTOR = '#app > div > section > div > form > div:nth-child(1) > div.fromDiv > span > div:nth-child(1) > div > div > div.ivu-date-picker-rel > div > div > input'
FinishTImeBox_SELECTOR = '#app > div > section > div > form > div:nth-child(1) > div.fromDiv > span > div:nth-child(2) > div > div > div.ivu-date-picker-rel > div > div > input'
StartTimeBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/span/div[1]/div/div/div[1]/div/div/input'
FinishTimeBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/span/div[2]/div/div/div[1]/div/div/input'

HeightInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[5]/div/div/input'
ContactInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[6]/div/div/textarea'
LocationInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[7]/div/div/textarea'
EmergencyProcessInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[8]/div/div/textarea'
SpecialReqInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[9]/div/div/textarea'
AbilitiesInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[10]/div/div/textarea'
SpeedInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[11]/div/div/textarea'
ControlInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[12]/div/div/textarea'
RadarInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[13]/div/div/textarea'
OtherInfoInput_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[14]/div/div/textarea'

AddDeviceButton_XPATH = '//*[@id="app"]/div/section/div/form/div[2]/div[1]/div/div/button/span'
DeviceChooseCheckBox_rPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span'
DeviceChooseCheckBox_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"
DeviceDoneButton_rPATH = '/html/body/div[2]/div/div/div[1]/div[3]/button[1]'
DeviceDoneButton_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[3]/button[1]/span"
AddControllerButton_XPATH = '//*[@id="app"]/div/section/div/form/div[2]/div[4]/div/div/button/span'
ControllerChooseCheckBox_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span"
ControllerDoneButton_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[3]/button[1]/span"
ChangeAirspaceButton_XPATH = '//*[@id="app"]/div/section/div/form/div[5]/div[1]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span'
NullCheckBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[15]/div/label[6]/span[2]'

InnerFrame1_XPATH = "//*[starts-with(@id, 'notification_')]"
InnerFrame2_XPATH = "//div[starts-with(@id, 'notification_')]"

SaveFileButton_XPATH = '//*[@id="app"]/div/section/div/form/div[6]/div/button[2]'
FinishButton_XPATH = '//*[@id="app"]/div/section/div/form/div[6]/div/button[3]'
CancelButton_XPATH = '//*[@id="app"]/div/section/div/form/div[6]/div/button[1]'

# 以下：默认配置/读取设置
FilePath = ''

PhoneNum = ''
StartTime = '2024-12-06 11:45'
FinishTime = '2024-12-06 17:54'
UsingDefaultTime = "True"
ExpectStartHour = '12'
ExpectFinishHour = '15'
Height = ''
Location = ''
EmergencyProcess = '紧急情况立即检查并降落'
SpecialReq = '无'
Abilities = 'Remote ID，导航定位，遥控器信号等可被监视'
Speed = '垂直起降；水平最大10m/s，垂直最大3m/s'
ControlAbilities = '无'
Radar = '无'
Other = '将使用辅助飞行并最大程度保证飞行安全，将绕开敏感并避开敏感区域，做到安全飞行。希望批准，谢谢！'

def GetProfilePath():
    global FilePath
    with open('Configures.json', 'r') as cfg:
        FilePath = json.load(cfg)['usingProfilePath']

def GetConfigures(path):
    global StartTime, FinishTime, Location, PhoneNum, ExpectStartHour, ExpectFinishHour
    global Height, Location, EmergencyProcess, SpecialReq, Abilities, Speed, ControlAbilities, Radar, Other
    with open(path, 'r', encoding='utf-8') as profile:
        profileCfg = json.load(profile)
        UsingDefaultTime = profileCfg['app']['usingDefaultTime']
        PhoneNum = profileCfg['login']['phoneNum']
        StartTime = profileCfg['content']['startTime']
        FinishTime = profileCfg['content']['finishTime']
        ExpectStartHour = profileCfg['content']['expectStartHour']
        ExpectFinishHour = profileCfg['content']['expectFinishHour']

        Height = profileCfg['content']['height']
        Location = profileCfg['content']['location']
        EmergencyProcess = profileCfg['content']['emergencyProcess']
        SpecialReq = profileCfg['content']['specialReq']
        Abilities = profileCfg['content']['abilities']
        Speed = profileCfg['content']['speed']
        ControlAbilities = profileCfg['content']['controlAbilities']
        Radar = profileCfg['content']['radar']
        Other = profileCfg['content']['other']

    if UsingDefaultTime == "True":
        StartTime = DefaultStartTime()
        FinishTime = DefaultFinishTime()

'''
DefaultTime：返回str
判断时间是否会被拦截，并给出可以申请的时间
'''
def DefaultStartTime():
    now = datetime.datetime.now()
    expectStartTime = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=int(ExpectStartHour))
    print(expectStartTime)
    if now.hour < 12:
        return (expectStartTime + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    else:
        return (expectStartTime + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M")
    
def DefaultFinishTime():
    now = datetime.datetime.now()
    expectFinishTime = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=int(ExpectFinishHour))
    if now.hour < 12:
        return (expectFinishTime + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    else:
        return (expectFinishTime + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M")

if __name__ == "__module__":
    GetProfilePath()
    GetConfigures(FilePath)

if __name__ == "__main__":
    GetProfilePath()
    print(FilePath)
    print(DefaultStartTime())
    print(DefaultFinishTime())
    GetConfigures(FilePath)
    print(f'\n{StartTime},{FinishTime},{ExpectStartHour},{ExpectFinishHour}\n{Height}')