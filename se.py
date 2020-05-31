from requestium import Session
import time
import json
import random


def saveCookie(s):
    s.driver.switch_to.frame(s.driver.find_element_by_id("g_iframe"))

    term = s.driver.find_element_by_xpath('//*[@id="j-official-terms"]')
    term.click()

    a = s.driver.find_elements_by_xpath("//div[@class='u-alt']/ul/li/a")
    a[3].click()

    s.driver.switch_to.window(s.driver.current_window_handle)
    time.sleep(2)

    username = s.driver.find_element_by_xpath("//div[@class='f-pr']/input[@type='text']")
    username.send_keys("*******")
    passwd = s.driver.find_element_by_xpath("//input[@type='password']")
    passwd.send_keys("***********")
    s.driver.find_element_by_xpath("//a[@class='js-primary u-btn2 u-btn2-2']").click()

    time.sleep(5)

    cookies = s.driver.get_cookies()
    with open('cookie.txt', 'w') as f:
        f.write(json.dumps(cookies))


def logOut(s):
    s.driver.get('https://music.163.com/st/creator/#/')
    time.sleep(2)

    term = s.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[3]/a[2]')
    term.click()


def sendMsg(s):
    timeDelay = random.randint(85, 135)
    s.driver.switch_to.default_content()
    playingSong = s.driver.find_element_by_xpath("//*[@id='g_player']/div[3]").text
    msg = playingSong.split("\n", 2)
    return msg, timeDelay


def validNum(s, playerHandle):
    js = 'window.open("https://music.163.com/#/user/level");'
    s.driver.execute_script(js)

    # 获取当前窗口句柄集合（列表类型）
    handles = s.driver.window_handles

    # 获取 num 窗口
    num_handle = None
    for handle in handles:
        if handle != playerHandle:
            num_handle = handle

    s.driver.switch_to.window(num_handle)
    time.sleep(2)
    s.driver.switch_to.frame(s.driver.find_element_by_id("g_iframe"))

    Msg = s.driver.find_element_by_xpath('//*[@id="m-level"]/div/div[3]/div[2]').text
    validMsg = Msg.split("\n", 1)

    s.driver.close()
    s.driver.switch_to.window(playerHandle)
    return validMsg[1]


s = Session(webdriver_path=r'C:\Software\Cent\CentBrowser\Application\chromedriver.exe',
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

s.driver.get('http://music.163.com/#/login')
time.sleep(1)

s.driver.switch_to.default_content()
source_text = s.driver.page_source
autoId_st = source_text.find("visibility:") + 26
autoId_end = autoId_st + 24
autoId = source_text[autoId_st:autoId_end]
path = str("//*[@id='" + autoId + "']/div[1]/div[1]/a")

time.sleep(0.5)

lockBtn = s.driver.find_element_by_xpath(path)
lockBtn.click()

f1 = open('cookie.txt')
cookie = f1.read()
cookie = json.loads(cookie)
for c in cookie:
    s.driver.add_cookie(c)
s.driver.refresh()

s.driver.get("https://music.163.com/#/user/update")
s.driver.switch_to.frame(s.driver.find_element_by_id("g_iframe"))

print(s.driver.find_element_by_xpath('//*[@id="nickname"]').get_attribute('value'))
print(s.driver.find_element_by_xpath('//*[@id="avatar"]').get_attribute('src'))
