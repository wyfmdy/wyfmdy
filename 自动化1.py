from selenium import webdriver
from selenium.webdriver.common.by import By
import time, selenium

# 创建谷歌对象
option = webdriver.ChromeOptions
option.binary_location = r'D:\Google\Chrome\Application\chrome.exe'
chromeDriver = webdriver.Chrome()


# 窗口最大化
chromeDriver.maximize_window()

# 京东
chromeDriver.get("http://www.jd.com")
chromeDriver.find_element(By.XPATH, "//*[@id='key']").send_keys("iphone 13")
chromeDriver.find_element(By.XPATH, "//*[@clstag='h|keycount|head|search_a' and @class='button']").click()
chromeDriver.implicitly_wait(4)
chromeDriver.find_element(By.XPATH, "//*[@data-sku='100026667884' and @data-spu='100026667884']").click()
chromeDriver.implicitly_wait(3)
handle = chromeDriver.window_handles
chromeDriver.switch_to.window(handle[1])
chromeDriver.find_element(By.XPATH, "//*[@id='InitCartUrl']").click()
chromeDriver.implicitly_wait(3)
time.sleep(2)
chromeDriver.close()
chromeDriver.switch_to.window((handle[0]))
chromeDriver.implicitly_wait(3)

# # 苏宁
# chromeDriver.get("http://www.suning.com")
# chromeDriver.find_element(By.ID, "searchKeywords").click()
# chromeDriver.implicitly_wait(3)
# chromeDriver.find_element(By.ID, "public0_zzrs_华为Mate40_0-0").click()
# handles = chromeDriver.window_handles
# chromeDriver.switch_to.window((handles[1]))
# chromeDriver.implicitly_wait(3)
# chromeDriver.find_element(By.XPATH, "//*[@class='product-box']").click()
# handles = chromeDriver.window_handles
# chromeDriver.switch_to.window((handles[2]))
# chromeDriver.implicitly_wait(3)
# chromeDriver.find_element(By.ID, "addCart").click()
# chromeDriver.implicitly_wait(3)
# time.sleep(2)
# for i in range(len(handles)-1):
#     chromeDriver.close()
#     chromeDriver.switch_to.window(handles[i])
# chromeDriver.implicitly_wait(3)

# # b站
#
#
# chromeDriver.get("http://www.bilibili.com")
# chromeDriver.find_element(By.XPATH, "//*[@class='nav-search-input' or @x-webkit-grammar='builtin:translate']").send_keys("鬼畜")
# chromeDriver.implicitly_wait(3)
# chromeDriver.find_element(By.XPATH, "//*[@class='nav-search-btn-text' or @class='nav-search-btn']").click()
# handles = chromeDriver.window_handles
# chromeDriver.switch_to.window(handles[1])
# chromeDriver.implicitly_wait(3)
# chromeDriver.find_element(By.XPATH, "//*[@class='video-item matrix']").click()
# handles = chromeDriver.window_handles
# chromeDriver.switch_to.window(handles[2])
# chromeDriver.implicitly_wait(3)
# chromeDriver.find_element(By.XPATH, "//*[@class='van-icon-videodetails_like']").click()
# chromeDriver.implicitly_wait(3)
# time.sleep(2)
#
#
# chromeDriver.quit()


