# -*- coding:utf-8 -*-
__author__ = 'xiaoguo'

from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from general.xg_caps import appium_caps
from selenium.webdriver.common.by import By
import logging, time, os

class general_view(BaseView):
    cancelBtn = (By.ID, 'com.wandoujia.phoenix2:id/s5')
    jumpBtn = (By.ID, 'com.wandoujia.phoenix2:id/v8')

    # 取消更新操作
    def click_cancelBtn(self):
        logging.info('*' * 10 + 'cancelBtn' + '*' * 10)
        try:
            cancel_element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('cancelBtn is not found !')
        else:
            logging.info('click cancelBtn')
            cancel_element.click()

    # 点击跳过操作
    def click_jumpBtn(self):
        logging.info('——' * 10 + 'jumpBtn' + '——' * 10)
        try:
            jump_element = self.driver.find_element(*self.jumpBtn)
        except NoSuchElementException:
            logging.info('jumpBtn is not fond !')
        else:
            logging.info('click jumpBtn')
            jump_element.click()

    # 获取屏幕尺寸
    def get_size(self):
        x = self.get_screen_size()['width']
        y = self.get_screen_size()['height']
        return x, y

    # 向上滑动操作
    def swipe_up(self):
        up = self.get_size()
        x1 = int(up[0] * 0.5)
        y1 = int(up[1] * 0.9)
        y2 = int(up[0] * 0.3)
        self.swipe(x1, y1, x1, y2, 3000)
        logging.info('向上滑动操作')

    # 向下滑动操作
    def swipe_down(self):
        down = self.get_size()
        x1 = int(down[0] * 0.5)
        y1 = int(down[0] * 0.3)
        y2 = int(down[1] * 0.9)
        self.swipe(x1, y1, x1, y2, 3000)
        logging.info('向下滑动操作')

    # 获取当前时间
    def getTime(self):
        self.currentTime = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.currentTime

    # 屏幕截图
    def getScreenIcon(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screen_icons/%s_%s.png' % (module, time)

        logging.info('get %s screenicon' % module)
        self.driver.get_screenshot_as_file(image_file)

if __name__ == '__main__':
    driver = appium_caps()
    general = general_view(driver)
    general.click_jumpBtn()
    general.click_cancelBtn()
    general.getScreenIcon('startApp')
    general.swipe_down()
    general.swipe_up()

