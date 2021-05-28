import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def exit_application():
    exit = driver.find_element_by_css_selector("button[aria-label='Dismiss']").click()
    discard_application = driver.find_element_by_css_selector("button[data-control-name='discard_application_confirm_btn']").click()

def apply_for_a_job():
    try:
        easy_apply = driver.find_element_by_css_selector("button[data-control-name='jobdetails_topcard_inapply']")
        time.sleep(5)
        easy_apply.click()

        easy_apply_submit = driver.find_element_by_css_selector("button[aria-label='Submit application']")
        time.sleep(5)
        easy_apply_submit.click()

    except NoSuchElementException:
        exit_application()

def keep_applying_for_a_job():
    jobs = driver.find_elements_by_css_selector(
        "a[class='disabled ember-view job-card-container__link job-card-list__title']")
    for job in jobs:
        job.click()
        time.sleep(5)
        apply_for_a_job()

# Open LinkedIn
chrome_driver_path = "/Users/ByoungjunJo/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&geoId=90000084&keywords=sales%20engineer&location=San%20Francisco%20Bay%20Area")

# Login to LinkedIn
login = driver.find_element_by_xpath("/html/body/div[3]/a[1]")
time.sleep(5)
login.click()

# LinkedIn Login
linkedin_id = os.getenv("LINKEDIN_USERNAME")
linkedin_pwd = os.getenv("LINKEDIN_PWD")

id_input = driver.find_element_by_id("username")
id_input.send_keys(linkedin_id)

pwd_input = driver.find_element_by_id("password")
pwd_input.send_keys(linkedin_pwd)

submit = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()

# Apply for all the jobs
# Automatically apply to the first job that only requires you to enter your phone number
try:
    apply_for_a_job()

except NoSuchElementException:
    exit_application()

finally:
    while True:
        keep_applying_for_a_job()




