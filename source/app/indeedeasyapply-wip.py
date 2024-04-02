import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class IndeedEasyApply:
    def __init__(self, parameters, driver):
        self.browser = driver
        self.email = parameters['email']
        self.password = parameters['password']
        self.phone = parameters['phone']
        self.resume_dir = parameters['uploads']['resume']
        self.cover_letter_dir = parameters['uploads'].get('coverLetter', '')
        self.positions = parameters.get('positions', [])
        self.locations = parameters.get('locations', [])
        self.base_search_url = self.get_base_search_url(parameters)
        self.output_file_directory = parameters['outputFileDirectory']
        self.seen_jobs = []
        self.technology = parameters.get('technology', [])  
        self.infrastructure = parameters.get('infrastructure', [])
        self.operations = parameters.get('operations', [])
        self.industry_experience = parameters.get('industryExperience', [])
        self.travel = parameters['travel']
        self.certifications = parameters.get('certifications', [])

    def get_base_search_url(self, parameters):
        # Construct the base search URL based on the provided parameters
        base_url = "https://www.indeed.com/jobs?"
        location = parameters.get('location', '')
        position = parameters.get('position', '')
        base_search_url = f"{base_url}q={position}&l={location}"
        return base_search_url

    def start_applying(self):
        self.browser.get(self.base_search_url)
        # Wait for the page to load
        time.sleep(random.uniform(3, 5))

        # Find the sign-in button and click it
        sign_in_button = self.browser.find_element(By.LINK_TEXT, 'Sign in')
        sign_in_button.click()
        time.sleep(random.uniform(2, 4))

        # Prompt the user to manually sign in
        print("Please sign in to your Indeed account in the browser window.")
        print("Once you have successfully signed in, press Enter in the console to continue.")
        input()

        # Verify if the user is signed in
        is_signed_in = False
        try:
            # Check for the presence of the user's inbox link
            inbox_link = self.browser.find_element(By.CSS_SELECTOR, 'a[data-gnav-element-name="Inbox"]')
            is_signed_in = True
            print("Sign-in successful. Continuing with job application process.")
        except:
            print("Sign-in not detected. Please make sure you are signed in before continuing.")

        if is_signed_in:
            # Click the "Skip" button three times if present
            skip_count = 0
            while skip_count < 3:
                try:
                    skip_button = self.browser.find_element(By.CSS_SELECTOR, 'button[data-tn-element="skip-section"]')
                    skip_button.click()
                    print(f"Skipped additional prompt {skip_count + 1} after sign-in.")
                    skip_count += 1
                    
                    # Pause for 2 seconds before the next skip attempt
                    time.sleep(2)
                except:
                    print(f"No more skip buttons found after {skip_count} skips.")
                    break

            # Start the job application process
            self.apply_jobs()
        else:
            print("Sign-in verification failed. Exiting the program.")
            return

    def apply_jobs(self, location):
        no_jobs_text = ""
        try:
            no_jobs_element = self.browser.find_element(By.CLASS_NAME, 'jobsearch-NoResult-messageContainer')
            no_jobs_text = no_jobs_element.text
        except:
            pass
        if 'did not match any jobs' in no_jobs_text:
            raise Exception("No more jobs on this page.")

        job_results = self.browser.find_elements(By.CLASS_NAME, 'jobsearch-ResultsList')
        if len(job_results) == 0:
            raise Exception("No job results found on this page.")

        job_list = job_results[0].find_elements(By.CLASS_NAME, 'jobsearch-SerpJobCard')
        if len(job_list) == 0:
            raise Exception("No job cards found on this page.")

        for job_card in job_list:
            job_title, company, location, apply_method, link = "", "", "", "", ""

            try:
                job_title_element = job_card.find_element(By.CLASS_NAME, 'jobTitle')
                job_title = job_title_element.find_element(By.TAG_NAME, 'span').text.strip()
                link = job_title_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            except:
                pass
            try:
                company = job_card.find_element(By.CLASS_NAME, 'companyName').text.strip()
            except:
                pass
            try:
                location = job_card.find_element(By.XPATH, './/div[@data-testid="job-location"]').text.strip()
            except:
                pass
            try:
                apply_method = job_card.find_element(By.CLASS_NAME, 'jobsearch-IndeedApplyButton-newDesign').text.strip()
            except:
                pass

            if apply_method.lower() == 'apply now':
                if link not in self.seen_jobs:
                    self.seen_jobs.append(link)
                    try:
                        job_card.click()
                        time.sleep(random.uniform(2, 4))
                        self.handle_application()
                        print(f"Application submitted for {job_title} at {company}.")
                    except:
                        print(f"Failed to apply to job: {job_title} at {company}.")
                        pass
                else:
                    print(f"Already applied to job: {job_title} at {company}. Skipping...")
            else:
                print(f"Job does not have 'Apply now' option: {job_title} at {company}. Skipping...")

    def handle_application(self):
        # Implement the logic to handle the job application process
        # This includes filling out the application form, uploading the resume, and submitting the application
        pass

    def fill_form(self):
        # Implement the logic to fill out the application form
        pass

    def upload_resume(self):
        # Implement the logic to upload the resume
        pass

    def submit_application(self):
        # Implement the logic to submit the application
        pass

    def write_to_file(self, company, job_title, link, location, search_location):
        # Implement the logic to write the job application details to a file
        pass

    def scroll_slow(self, scrollable_element, start=0, end=3600, step=100, reverse=False):
        # Implement the logic to slowly scroll through a scrollable element
        pass

    def avoid_lock(self):
        # Implement the logic to prevent the computer from locking
        pass

    def next_job_page(self, position, location, job_page):
        # Implement the logic to navigate to the next page of job listings
        pass