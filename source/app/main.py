import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from validate_email import validate_email
from webdriver_manager.chrome import ChromeDriverManager
from linkedineasyapply import LinkedinEasyApply
import sys

def init_browser():
    browser_options = Options()
    options = ['--disable-blink-features',
               '--no-sandbox',
               '--start-maximized',
               '--disable-extensions',
               '--ignore-certificate-errors',
               '--disable-blink-features=AutomationControlled',
               '--remote-debugging-port=9222']

    for option in options:
        browser_options.add_argument(option)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=browser_options)
    driver.implicitly_wait(1) # wait time in seconds to allow loading of elements
    driver.set_window_position(0, 0)
    driver.maximize_window()
    return driver


def validate_yaml():
    with open("C:/Users/kenne/Desktop/EasyApplyBot/config.yaml", 'r') as stream:
        try:
            parameters = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise Exception(f"Error while parsing YAML file: {exc}")

    mandatory_params = ['email',
                        'password',
                        'disableAntiLock',
                        'remote',
                        'lessthanTenApplicants',
                        'experienceLevel',
                        'jobTypes',
                        'date',
                        'positions',
                        'locations',
                        'residentStatus',
                        'distance',
                        'outputFileDirectory',
                        'checkboxes',
                        'universityGpa',
                        'languages',
                        'experience',
                        'personalInfo',
                        'eeo',
                        'uploads']

    for mandatory_param in mandatory_params:
        if mandatory_param not in parameters:
            raise Exception(f"Missing mandatory parameter: {mandatory_param}")

    try:
        assert validate_email(parameters['email'])
    except AssertionError:
        raise Exception("Invalid email address")

    try:
        assert len(str(parameters['password'])) > 0
    except AssertionError:
        raise Exception("Password cannot be empty")

    boolean_params = ['disableAntiLock', 'remote', 'lessthanTenApplicants', 'residentStatus']
    for param in boolean_params:
        try:
            assert isinstance(parameters[param], bool)
        except AssertionError:
            raise Exception(f"Parameter '{param}' must be a boolean value")

    experience_level = parameters.get('experienceLevel', [])
    if not any(experience_level.values()):
        raise Exception("At least one experience level must be set to True")

    job_types = parameters.get('jobTypes', [])
    if not any(job_types.values()):
        raise Exception("At least one job type must be set to True")

    date = parameters.get('date', [])
    if sum(date.values()) != 1:
        raise Exception("Exactly one date option must be set to True")

    approved_distances = {0, 5, 10, 25, 50, 100}
    if parameters['distance'] not in approved_distances:
        raise Exception(f"Invalid distance value: {parameters['distance']}. Allowed values are {approved_distances}")

    if len(parameters['positions']) == 0:
        raise Exception("At least one position must be specified")

    if len(parameters['locations']) == 0:
        raise Exception("At least one location must be specified")

    if 'resume' not in parameters['uploads']:
        raise Exception("Resume file path must be provided in the 'uploads' section")

    assert validate_email(parameters['email'])
    assert len(str(parameters['password'])) > 0
    assert isinstance(parameters['disableAntiLock'], bool)
    assert isinstance(parameters['remote'], bool)
    assert isinstance(parameters['lessthanTenApplicants'], bool)
    assert isinstance(parameters['residentStatus'], bool)
    assert len(parameters['experienceLevel']) > 0
    experience_level = parameters.get('experienceLevel', [])
    at_least_one_experience = False

    for key in experience_level.keys():
        if experience_level[key]:
            at_least_one_experience = True
    assert at_least_one_experience

    assert len(parameters['jobTypes']) > 0
    job_types = parameters.get('jobTypes', [])
    at_least_one_job_type = False
    for key in job_types.keys():
        if job_types[key]:
            at_least_one_job_type = True

    assert at_least_one_job_type
    assert len(parameters['date']) > 0
    date = parameters.get('date', [])
    at_least_one_date = False

    for key in date.keys():
        if date[key]:
            at_least_one_date = True
    assert at_least_one_date

    approved_distances = {0, 5, 10, 25, 50, 100}
    assert parameters['distance'] in approved_distances
    assert len(parameters['positions']) > 0
    assert len(parameters['locations']) > 0
    assert len(parameters['uploads']) >= 1 and 'resume' in parameters['uploads']
    assert len(parameters['checkboxes']) > 0

    checkboxes = parameters.get('checkboxes', [])
    assert isinstance(checkboxes['driversLicence'], bool)
    assert isinstance(checkboxes['requireVisa'], bool)
    assert isinstance(checkboxes['legallyAuthorized'], bool)
    assert isinstance(checkboxes['certifiedProfessional'], bool)
    assert isinstance(checkboxes['urgentFill'], bool)
    assert isinstance(checkboxes['commute'], bool)
    assert isinstance(checkboxes['backgroundCheck'], bool)
    assert isinstance(checkboxes['securityClearance'], bool)
    assert 'degreeCompleted' in checkboxes
    assert isinstance(parameters['universityGpa'], (int, float))

    languages = parameters.get('languages', [])
    language_types = {'none', 'conversational', 'professional', 'native or bilingual'}
    for language in languages:
        assert languages[language].lower() in language_types

    experience = parameters.get('experience', [])
    for tech in experience:
        assert isinstance(experience[tech], int)
    assert 'default' in experience

    assert len(parameters['personalInfo'])
    personal_info = parameters.get('personalInfo', [])
    for info in personal_info:
        assert personal_info[info] != ''

    assert len(parameters['eeo'])
    eeo = parameters.get('eeo', [])
    for survey_question in eeo:
        assert eeo[survey_question] != ''

    return parameters

if __name__ == '__main__':
    try:
        parameters = validate_yaml()
    except Exception as e:
        print(f"Validation failed: {str(e)}")
        sys.exit(1)

    try:
        browser = init_browser()
    except Exception as e:
        print(f"Failed to initialize browser: {str(e)}")
        sys.exit(1)

    bot = LinkedinEasyApply(parameters, browser)

    try:
        bot.login()
        bot.security_check()
        bot.start_applying()
    except Exception as e:
        print(f"An error occurred during execution: {str(e)}")
        sys.exit(1)
    finally:
        browser.quit()
