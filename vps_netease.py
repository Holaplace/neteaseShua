from requestium import Session
import time
import json
import random


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

        try:
            f = open('cookie.txt')
            cookie = f.read()
            cookie = json.loads(cookie)
            for c in cookie:
                self.s.driver.add_cookie(c)
            self.s.driver.refresh()
        except:
            with open('cookie.txt', 'w'):
                pass

        try:
            self.s.driver.get('https://music.163.com/#/user/level')
            self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))
            self.s.driver.find_element_by_xpath('//*[@id="m-level"]')
        except:
            self.s.driver.get('http://music.163.com/#/login')
            time.sleep(1)
            self.saveCookie()

    def playlistID(self):
        self.listID = input('\nPlease input playlist ID: ')
        self.s.driver.get("https://music.163.com/#/playlist?id=" + self.listID)
        self.track_handle = self.s.driver.current_window_handle
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))

        sumCount = self.s.driver.find_element_by_xpath('//*[@id="m-playlist"]/div[1]/div/div/div[2]/div[1]/span').text
        self.totalSongs = sumCount[:-2]

        time.sleep(2)
        self.reqSongs()

    def reqSongs(self):
        js = 'window.open("https://music.163.com/#/user/level");'
        self.s.driver.execute_script(js)

        # 获取当前窗口句柄集合（列表类型）
        handles = self.s.driver.window_handles

        # 获取 num 窗口
        self.reqsongs_handle = None
        for handle in handles:
            if handle != self.track_handle:
                self.reqsongs_handle = handle

        self.s.driver.switch_to.window(self.reqsongs_handle)
        time.sleep(1)
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))

        reqnextLv1 = self.s.driver.find_element_by_xpath('//*[@id="m-level"]/div/div[3]/div[2]').text
        reqnextLv = (reqnextLv1.split("\n", 1))[1]
        self.reqnextLv = reqnextLv[4:-1]

        currentLv1 = self.s.driver.find_element_by_xpath('//*[@id="m-level"]/div/div[1]/div[1]').text
        self.currentLv = currentLv1.split("\n", 2)[1]

        self.s.driver.close()
        self.s.driver.switch_to.window(self.track_handle)

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
        self.timeDelay = random.randint(105, 135)

        time.sleep(1)
        self.trackCount = self.s.driver.find_element_by_css_selector('[class="ply ply-z-slt"] + [class="num"]').text

        self.s.driver.switch_to.default_content()
        playingSong = self.s.driver.find_element_by_xpath("//*[@id='g_player']/div[3]").text
        self.msg = playingSong.split("\n", 2)

        while self.timeDelay > 0:
            print("\r{} <-> {} <-> {} <-> {}s; Require {} <-> to Lv{}".format(self.trackCount,
                                                                              self.msg[0],
                                                                              self.msg[1],
                                                                              self.timeDelay,
                                                                              self.reqnextLv,
                                                                              str(int(self.currentLv) + 1)), end="")
            time.sleep(1)
            self.timeDelay -= 1

        if int(self.trackCount) <= int(self.totalSongs):
            self.reqSongs()
            self.nextSong()
        else:
            self.playlistID()
            self.startPlay()

    def saveCookie(self):
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))

        term = self.s.driver.find_element_by_xpath('//*[@id="j-official-terms"]')
        term.click()

        a = self.s.driver.find_elements_by_xpath("//div[@class='u-alt']/ul/li/a")
        a[3].click()

        self.s.driver.switch_to.window(self.s.driver.current_window_handle)
        time.sleep(2)

        username = self.s.driver.find_element_by_xpath("//div[@class='f-pr']/input[@type='text']")
        username.send_keys("xuzhencang@163.com")
        passwd = self.s.driver.find_element_by_xpath("//input[@type='password']")
        passwd.send_keys("210071Xzc12145")
        self.s.driver.find_element_by_xpath("//a[@class='js-primary u-btn2 u-btn2-2']").click()

        time.sleep(2)

        cookies = self.s.driver.get_cookies()
        with open('cookie.txt', 'w') as f:
            f.write(json.dumps(cookies))

        self.s.driver.get('http://music.163.com')

    # def logOut(self):
    #     self.s.driver.get('https://music.163.com/st/creator/#/')
    #     time.sleep(2)
    #
    #     term = self.s.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[3]/a[2]')
    #     term.click()
    #     self.saveCookie()


def main():
    one_instance = shuaNetease()
    one_instance.logIn()
    one_instance.playlistID()
    one_instance.startPlay()


if __name__ == '__main__':
    main()
