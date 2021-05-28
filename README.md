# automating-job-application
## Problem: Applying jobs on LinkedIn automatically!
## Solutions
1.Exit a job application if it doesn't have "Easy Apply" function with only click of a button
```
def exit_application():
    exit = driver.find_element_by_css_selector("button[aria-label='Dismiss']").click()
    discard_application = driver.find_element_by_css_selector("button[data-control-name='discard_application_confirm_btn']").click()
```
2. Apply for a job
```
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
```
3. Looping through the jobs to apply each job
```
def keep_applying_for_a_job():
    jobs = driver.find_elements_by_css_selector(
        "a[class='disabled ember-view job-card-container__link job-card-list__title']")
    for job in jobs:
        job.click()
        time.sleep(5)
        apply_for_a_job()
```
## Lessons
1. Keep learning
2. Dirty code is fine because I'm here to learn and having fun
