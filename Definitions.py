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
CreateNewTaskButton_XPATH = '//*[@id="app"]/div/section/div/div[1]/div[1]/button'
CaptchaImage_XPATH = '//*[@id="lastLine"]/div/span/img'
CaptchaInput_XPATH = '//*[@id="lastLine"]/div/div/input'
GetSmscodeButton_XPATH = '//*[@id="portal"]/section/div[2]/div/div/div[2]/div[1]/div/div/div/form/div[3]/div/span[1]/span'
MsgBoxInfo_XPATH = '/html/body/div[6]/div[2]/div/div/div/div/div[2]/div'
MsgBoxInfo_CLASS = 'ivu-modal-confirm-body'
CloseBox_XPATH = '/html/body/div[7]/div[2]/div/div/div/div/div[3]/button'
CloseBox_CLASS = 'ivu-btn ivu-btn-primary'

IFrame1_XPATH = '//*[@id="main-body-content"]/div[3]/div/div/div[2]/iframe'
IFrame2_XPATH = '//*[@id="main-body-content"]/div[3]/div/div/div[3]/iframe'
IFrameNewPage_XPATH = '//*[@id="main-body-content"]/div[3]/div/div/div[2]/iframe'
IFrameCopyPage_XPATH = '//*[@id="main-body-content"]/div[3]/div/div/div[3]/iframe'

ChangeTypeBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[2]/div/div/div/input'
ChangeTypeButton_XPATH = '/html/body/div[2]/div[1]/div[1]/ul/li/span'
StartTimeBox_SELECTOR = '#app > div > section > div > form > div:nth-child(1) > div.fromDiv > span > div:nth-child(1) > div > div > div.ivu-date-picker-rel > div > div > input'
FinishTImeBox_SELECTOR = '#app > div > section > div > form > div:nth-child(1) > div.fromDiv > span > div:nth-child(2) > div > div > div.ivu-date-picker-rel > div > div > input'
StartTimeBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/span/div[1]/div/div/div[1]/div/div/input'
FinishTimeBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/span/div[2]/div/div[1]/div[1]/div/div/input'

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
DeviceChooseCheckBox_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"
DeviceChooseCheckBox2_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span"
DeviceDoneButton_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[3]/button[1]/span"
#
AddControllerButton_XPATH = '//*[@id="app"]/div/section/div/form/div[2]/div[4]/div/div/button/span'
ControllerChooseCheckBox_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span"
# ControllerChooseCheckBox2_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span"
ControllerDoneButton_XPATH = "//*[starts-with(@id, 'vlip')]/div/div[1]/div[3]/button[1]/span"
ChangeAirspaceButton_XPATH = '//*[@id="app"]/div/section/div/form/div[5]/div[1]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span'
NullCheckBox_XPATH = '//*[@id="app"]/div/section/div/form/div[1]/div[3]/div[15]/div/label[6]/span[2]'

InnerFrame1_XPATH = "//*[starts-with(@id, 'notification_')]"
InnerFrame2_XPATH = "//div[starts-with(@id, 'notification_')]"

SaveFileButton_XPATH = '//*[@id="app"]/div/section/div/form/div[6]/div/button[2]'
FinishButton_XPATH = '//*[@id="app"]/div/section/div/form/div[6]/div/button[3]'
SubmitButton_XPATH = "/html/body/div[3]/div/div[3]/button[2]"
SubmitButton_SECTOR = "body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary"
CancelButton_XPATH = '//*[@id="app"]/div/section/div/form/div[6]/div/button[1]'

IDText_XPATH = '//*[@id="app"]/div/section/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div'

# 以下：默认配置/读取设置

class Configures:
    def __init__(self):
        self.GetProfilePath()
        with open(self.FilePath, 'r', encoding='utf-8') as profile:
            profileCfg = json.load(profile)
            self.UsingDefaultTime = profileCfg['app']['usingDefaultTime']
            self.UsingAutoReport = profileCfg['app']['autoReport']
            self.UsingLogger = True if profileCfg['app']['usingLogger']=='True' else False
            self.AutoCaptcha = True if profileCfg['app']['autoCaptcha']=='True' else False
    
            self.PhoneNum = profileCfg['login']['phoneNum']
            self.StartTime = profileCfg['content']['startTime']
            self.FinishTime = profileCfg['content']['finishTime']
            self.ExpectStartHour = profileCfg['content']['expectStartHour']
            self.ExpectFinishHour = profileCfg['content']['expectFinishHour']
   
            self.Height = profileCfg['content']['height']
            self.Location = profileCfg['content']['location']
            self.EmergencyProcess = profileCfg['content']['emergencyProcess']
            self.SpecialReq = profileCfg['content']['specialReq']
            self.Abilities = profileCfg['content']['abilities']
            self.Speed = profileCfg['content']['speed']
            self.ControlAbilities = profileCfg['content']['controlAbilities']
            self.Radar = profileCfg['content']['radar']
            self.Other = profileCfg['content']['other']

        if self.UsingDefaultTime == "True":
            self.StartTime = self.DefaultStartTime()
            self.FinishTime = self.DefaultFinishTime()

    def GetProfilePath(self):
        with open('Configures.json', 'r') as cfg:
            self.FilePath = json.load(cfg)['usingProfilePath']
        return self.FilePath
    '''
    DefaultTime：返回str
    判断时间是否会被拦截，并给出可以申请的时间
    '''
    def DefaultStartTime(self):
        now = datetime.datetime.now()
        self.expectStartTime = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=int(self.ExpectStartHour))
        if now.hour < 12:
            return (self.expectStartTime + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        else:
            return (self.expectStartTime + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M")
    def DefaultFinishTime(self):
        now = datetime.datetime.now()
        self.expectFinishTime = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=int(self.ExpectFinishHour))
        if now.hour < 12:
            return (self.expectFinishTime + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        else:
            return (self.expectFinishTime + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M")

if __name__ == "__module__":
    init = Configures()
    init.GetConfigures(init.GetProfilePath())

if __name__ == "__main__":
    init = Configures()
    print(init.GetProfilePath())
    print(init.DefaultStartTime())
    print(init.DefaultFinishTime())
    print(f'\n{init.StartTime},{init.FinishTime},{init.ExpectStartHour},{init.ExpectFinishHour}\n{init.Height}')