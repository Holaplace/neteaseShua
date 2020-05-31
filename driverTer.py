from requestium import Session
import time
import json


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

s.driver.get("https://music.163.com/#/playlist?id=2482231841")
s.driver.switch_to.frame(s.driver.find_element_by_id("g_iframe"))
sumCount = s.driver.find_element_by_xpath('//*[@id="m-playlist"]/div[1]/div/div/div[2]/div[1]/span').text
print(sumCount[:-2])


# s.driver.get("https://music.163.com/#/user/level")
# s.driver.switch_to.frame(s.driver.find_element_by_id("g_iframe"))
# trackCount = s.driver.find_element_by_xpath('//*[@id="m-level"]/div/div[1]/div[1]').text

# s.driver.get("https://music.163.com/#/playlist?id=2482231841")
player_handle = s.driver.current_window_handle
time.sleep(2)

# #  播 放
# s.driver.switch_to.frame(s.driver.find_element_by_id("g_iframe"))
element = s.driver.find_element_by_xpath("//*[@id='content-operation']/a[1]")
element.click()

trackCount = s.driver.find_element_by_css_selector('[class="ply ply-z-slt"] + [class="num"]').text

print(trackCount)
