
from interface.util.service import Service
from interface.util.utility import Utility


class Login:
    def __init__(self,driver):
        self.driver=driver
    def input_name(self,username):
        uname=self.driver.find_element_by_name('userName')
        Service.send_input(uname,username)
    def input_upass(self,password):
        upass=self.driver.find_element_by_name('userPass')
        Service.send_input(upass,password)
    def input_vfcode(self,verifycode):
        vfcode=self.driver.find_element_by_name('checkcode')
        Service.send_input(vfcode,verifycode)
    def click_button(self):
        self.driver.find_element_by_css_selector('.btn').click()

    def do_login(self,base_config_path,login_data):
        Service.open_page(self.driver,base_config_path)
        self.input_name(login_data['username'])
        self.input_upass(login_data['password'])
        self.input_vfcode(login_data['verfifycode'])
        self.click_button()
    def do_login_admin(self,base_config_path):
        Service.open_page(self.driver, base_config_path)
        info=Utility.get_json(base_config_path)
        print(info)



if __name__ == '__main__':
    from selenium import webdriver
    driver=webdriver.Firefox()
    Login(driver).do_login_admin('..\\config\\base.conf')
    # from selenium import webdriver
    #
    # driver = webdriver.Firefox()
    # driver.implicitly_wait(10)
    # Service.open_page(driver,'..\\config\\base.conf')
    # a=driver.find_element_by_xpath('//div[@class="modal-body"]/div[1]/input')
    # a.click()
    # a.send_keys('wncd000')
    #
    # b=driver.find_element_by_xpath('//div[@class="modal-body"]/div[2]/input')
    # b.click()
    # b.send_keys('woniu123')
    # c=driver.find_element_by_xpath('//div[@class="modal-body"]/div[3]/input')
    # c.click()
    # c.clear()
    # c.send_keys('0000')
    # driver.find_element_by_xpath('//div[@class="modal-footer"]/button').click()
    # import time
    # time.sleep(2)
    # driver.find_element_by_link_text('注销').click()
