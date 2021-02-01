from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def driver_wait_until(self, resource, expected_conditions_func=EC.visibility_of_element_located, timeout=10):
        '''
        self.driver_wait_until(By.XPATH, '(//div[@id="chatroomTextarea"])[2]').click()
        '''
        return WebDriverWait(self.driver, timeout).until(expected_conditions_func(resource))

    def is_element_existed(self, resource, expected_text=None, expected_conditions_func=EC.visibility_of_all_elements_located):
        '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回True
        resource =(By.CSS_SELECTOR,'#swfEveryCookieWrap')
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(resource))
        '''
        self.driver_wait_until(resource, EC.invisibility_of_element_located)

        '''
        self.is_element_existed(resource=self.resource.conponent.CHATROOM_MESSAGES,
            expected_text=text, expected_conditions_func=EC.presence_of_all_elements_located)
        self.is_element_existed(self.resource.conponent.CHATROOM_LINK_TITLE,
            title)
        '''
        # elements = self.driver_wait_until(resource, expected_conditions_func)
        # elements.reverse()
        # for e in elements:
        #     if e.text == expected_text:
        #         return True
        # else:
        #     return False

    def find_element_to_click(self, resource, expected_text, expected_conditions_func=EC.visibility_of_all_elements_located):
        '''
        self.find_element_to_click(self.resource.conponent.CONTACTS_MAN, contact_name)
        '''
        elements = self.driver_wait_until(resource, expected_conditions_func)
        for e in elements:
            if e.text == expected_text:
                e.click()
                break
        else:
            assert False, 'Can not find the element by text: {}'.format(expected_text)

