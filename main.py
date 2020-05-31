from shuaUI import Ui_shuaUI
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication
import sys
from requestium import Session
import time
import json
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import random


class Win(QWidget):
    currentDisplay = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_shuaUI()
        self.ui.setupUi(self)

        self.initUI()

    def initUI(self):
        self.ui.loadCookieBtn.clicked.connect(self.loadCookie)
        self.ui.loginBtn.clicked.connect(self.logIn)
        self.ui.playlistBtn.clicked.connect(self.playlistID)

    def initDriver(self):
        self.s = Session(webdriver_path=r'C:\Software\Cent\CentBrowser\Application\chromedriver.exe',
                         browser='chrome',
                         default_timeout=15,
                         webdriver_options={
                             'arguments': [
                                 # '-headless',
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

    def loadCookie(self):
        self.fileName, self.fileType = QFileDialog.getOpenFileName(self, "选取文件", "./", "Text Files (*.txt)")
        self.ui.cookieLable.setText(self.fileName)
        self.ui.cookiePic.setPixmap(QPixmap('2.png'))

    def logIn(self):
        self.initDriver()

        f = open(self.fileName)
        cookie = f.read()
        cookie = json.loads(cookie)
        for c in cookie:
            self.s.driver.add_cookie(c)
        self.s.driver.refresh()

        self.s.driver.get("https://music.163.com/#/user/update")
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))

        time.sleep(1)
        nickName = self.s.driver.find_element_by_xpath('//*[@id="nickname"]').get_attribute('value')
        self.ui.introLable.setText('你好呀(✿◠‿◠): ' + nickName)
        self.ui.loginPic.setPixmap(QPixmap('2.png'))
        self.s.driver.get("https://music.163.com")

    def playlistID(self):
        listID = self.ui.playlistEdit.text()
        self.s.driver.get("https://music.163.com/#/playlist?id=" + listID)
        self.track_handle = self.s.driver.current_window_handle
        self.ui.playlistPic.setPixmap(QPixmap('2.png'))

        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))

        trackCount = self.s.driver.find_element_by_xpath('//*[@id="m-playlist"]/div[1]/div/div/div[2]/div[1]/span').text
        self.ui.totalPlayLcd.display(trackCount[:-2])

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
        time.sleep(2)
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))

        reqnextLv1 = self.s.driver.find_element_by_xpath('//*[@id="m-level"]/div/div[3]/div[2]').text
        reqnextLv = (reqnextLv1.split("\n", 1))[1]
        reqnextLv = reqnextLv[4:-1]

        currentLv1 = self.s.driver.find_element_by_xpath('//*[@id="m-level"]/div/div[1]/div[1]').text
        currentLv = currentLv1.split("\n", 2)[1]

        self.ui.numLcd.display(reqnextLv)
        self.ui.lvLcd.display(currentLv)

        self.s.driver.switch_to.window(self.track_handle)
        self.startPlay()

    def startPlay(self):
        # #  播 放
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))
        element = self.s.driver.find_element_by_xpath("//*[@id='content-operation']/a[1]")
        element.click()
        self.timeNeeded()

    def timeNeeded(self):
        global currentDisplay
        self.timeDelay = random.randint(85, 135)
        self.ui.totalSongTimeLcd.display(self.timeDelay)

        currentDisplay = self.timeDelay

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeDisplay)
        self.timer.start(1000)

    def timeDisplay(self):
        global currentDisplay
        currentDisplay -= 1
        if currentDisplay == 0:
            self.timer.stop()

        self.ui.currentSongTimeLcd.display(currentDisplay)

    def nextSong(self):
        self.s.driver.switch_to.frame(self.s.driver.find_element_by_id("g_iframe"))
        ele = self.s.driver.find_element_by_xpath("//*[@id='g_player']/div[1]/a[3]")
        ele.click()
        self.timeNeeded()


def main():
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
