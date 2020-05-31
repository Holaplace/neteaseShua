from requestium import Session
import time
import json
import random
from twilio.rest import Client


numTag = 1


account_sid = 'AC42a0cd6e0266090f4d58340d9ebf6932'
auth_token = '2be41969718c99732244ed18f9c7aa0b'
# myNumber='+8618019156817'
myNumber='+8617750669561'
twilioNumber = '+12055263797'


def textmyself(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(to=myNumber, from_=twilioNumber, body=message)


class shuaNetease:
    def __init__(self):
        pass

    def initDriver(self):
        self.s = Session(webdriver_path=r'C:\Software\Cent\CentBrowser\Application\chromedriver.exe',
                         browser='chrome',
                         default_timeout=35,
                         webdriver_options={
                             'arguments': [
                                 '-headless',
                                 '-mute-audio',
                                 '-window-size=1920,1080',
                                 '-start-maximized',
                                 '-no-sandbox']}
                         )

        self.s.driver.get('http://music.163.com/#/login')
        time.sleep(1)

        self.s.driver.switch_to.default_content()
        source_text = self.s.driver.page_source
        autoId_st = source_text.find("visibility:") + 26
        autoId_end = autoId_st + 24
        autoId = source_text[autoId_st:autoId_end]
        path = str("//*[@id='" + autoId + "']/div[1]/div[1]/a")

        time.sleep(0.5)

        lockBtn = self.s.driver.find_element_by_xpath(path)
        lockBtn.click()

    def logIn(self):
        self.initDriver()

        f = open('cookie.txt')
        cookie = f.read()
        cookie = json.loads(cookie)
        for c in cookie:
            if 'expiry' in c:
                del c['expiry']
        
            self.s.driver.add_cookie(c)
        self.s.driver.refresh()

    def playlistID(self):
        self.listID = input('Please input playlist ID: ')
        self.totalNum = int(input('Total playlist number: '))
        
        global numTag
        numTag = 1
        
        self.s.driver.get("https://music.163.com/#/playlist?id=" + self.listID)
        time.sleep(3)
        self.startPlay()
        
    def startPlay(self):
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))
        element = self.s.driver.find_element_by_xpath("//*[@id='content-operation']/a[1]")
        element.click() 
        self.currentPlay()

    def nextSong(self):
        self.s.driver.switch_to.default_content()
        ele = self.s.driver.find_element_by_xpath("//*[@id='g_player']/div[1]/a[3]")
        ele.click()

        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))
        self.currentPlay()

    def currentPlay(self):
        global numTag
        
        self.timeDelay = random.randint(65, 75)

        time.sleep(1)
        self.trackCount = self.s.driver.find_element_by_css_selector('[class="ply ply-z-slt"] + [class="num"]').text

        self.s.driver.switch_to.default_content()
        playingSong = self.s.driver.find_element_by_xpath("//*[@id='g_player']/div[3]").text
        self.msg = playingSong.split("\n", 2)
        
        if numTag == int(self.trackCount):
            pass
        elif numTag < int(self.trackCount):
            numTag = int(self.trackCount)
        else:
            textmyself('Plz reinput... from shua')
            self.playlistID()
        
        while self.timeDelay > 0:
            print("\r{}/{} <-> {} <-> {} <-> {}s.".format(self.trackCount, str(self.totalNum),
                                                          self.msg[0],
                                                          self.msg[1],
                                                          self.timeDelay, ), end="")
            time.sleep(1)
            self.timeDelay -= 1
            
        numTag += 1
        self.nextSong()
  

def main():
    one_instance = shuaNetease()
    try:
        one_instance.logIn()
        one_instance.playlistID()
    except:
        textmyself('Plz reinput... from shua')
        one_instance.logIn()
        one_instance.playlistID()


if __name__ == '__main__':
    main()
