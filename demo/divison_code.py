from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class A:
    driver = WebDriver()

    def page_contains(self, text, timeout=5):
        try:
            wait = WebDriverWait(driver=self.driver, timeout=timeout)
            flag = wait.until(lambda d: text in d.page_source)
            # self.Logger.info(f'判断页面包[{text}]，结果是True')return flag
            return flag
        except:
            # self.Logger.info(f'判断页面包含[text子]，结果是FaLse')return False
            return False

    def b(self, c):
        # wait = WebDriverWait(driver=self.driver, timeout=3)
        flag = c.page_source

# page_contains()
