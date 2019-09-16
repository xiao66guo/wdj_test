# -*- coding:utf-8 -*-
__author__ = 'xiaoguo'

from appium import webdriver
import yaml, logging, logging.config, os

log_file = '../config/log.conf'
logging.config.fileConfig(log_file)
logging = logging.getLogger()

def appium_caps():

    with open('../config/wdj_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    xg_caps = {}
    xg_caps['platformName'] = data['platformName']
    xg_caps['platformVersion'] = data['platformVersion']
    xg_caps['deviceName'] = data['deviceName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    xg_caps['app'] = app_path
    xg_caps['appPackage'] = data['appPackage']
    xg_caps['appActivity'] = data['appActivity']

    xg_caps['noReset'] = data['noReset']
    xg_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    xg_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('start app ......')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', xg_caps)

    driver.implicitly_wait(6)
    return driver

if __name__ == '__main__':
    appium_caps()


