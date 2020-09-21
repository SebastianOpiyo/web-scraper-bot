from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
url_path = "https://www.ezpassnj.com/vector/violations/violationList.do"
driver.get(url_path)

pay_value = "P00042720203866464"
email_val = "clients@innovativetoll.com"

pay_plan = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/div/form/div/'
                                        'div[2]/div[3]/div[1]/div/div[1]/input')

driver.execute_script("arguments[0].click();", pay_plan)
print(pay_value)
pay_plan.send_keys(pay_value.strip())

time.sleep(3)

email = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[3]/div/'
                                     'div/form/div/div[2]/div[3]/div[2]/div/div[1]/input')
driver.execute_script("arguments[0].click();", email)
print(email_val)
email.send_keys(email_val.strip())

time.sleep(3)

submit_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/'
                                             'div[3]/div/div/form/div/div[3]/div[2]/button')
driver.execute_script("arguments[0].click();", submit_button)
submit_button.submit()

# email.submit()
