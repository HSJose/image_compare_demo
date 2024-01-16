import json

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy as MobileBy
from appium.common import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from os import path, getenv 
import time
import requests
from dotenv import load_dotenv

# Load the .env file
load_dotenv()


auth_token = getenv('AUTH_TOKEN')
APPIUM = f'https://dev-us-sny-8.headspin.io:7001/v0/{auth_token}/wd/hub'
HEADER={'Authorization': f'Bearer {auth_token}'}

CAPS = {
    'deviceName': 'SM-S911U',
    'udid': 'RFCR115W4ND',
    'autoAcceptAlerts': True,
    'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': 'com.android.settings.Settings',
    'headspin:testName': 'Demo_Insurance_App',
    'headspin:capture': 'True',
    'adbExecTimeout': '100000'
}

OPTIONS = UiAutomator2Options().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)

wait = WebDriverWait(driver, 20)
startTime = 0
endTime = 0

driver.terminate_app('com.android.settings')

driver.press_keycode(3)

insuranceCalc_icon = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,
                                                                'Insurance Calculator')))

startTime = time.time()
insuranceCalc_icon.click()


carButton = wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.tricentis.insuranceCalculatorApp:id/Car')))

endTime = time.time()

carButton.click()

ocr_endtime = time.time()

driver.find_element(MobileBy.ID, 'com.tricentis.insuranceCalculatorApp:id/Make').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.find_element(MobileBy.ID, 'com.tricentis.insuranceCalculatorApp:id/YearOfConstruction').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'valuePicker').click()

driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.CheckedTextView[2]').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Listprice').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Listprice').send_keys('12000')

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'MileagePerYear').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'MileagePerYear').send_keys('2000')

driver.find_element(MobileBy.ID, 'com.tricentis.insuranceCalculatorApp:id/Performance').send_keys('20')

driver.hide_keyboard()

driver.find_element(MobileBy.ID, 'com.tricentis.insuranceCalculatorApp:id/Fuel').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.hide_keyboard()

driver.find_element(MobileBy.ID, 'com.tricentis.insuranceCalculatorApp:id/Usage').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

user_startTime = time.time()

driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[3]/android.widget.TextView').click()

first_name = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'FirstName')))

user_endTime = time.time()

first_name.send_keys('Head')

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'LastName').send_keys('Spin')

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'DayOfBirth').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Decrease month').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Decrease month').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'GenderMale').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Occupation').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Product Details').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'PreferredStartDate').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Increase month').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Increase month').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'PaymentOption').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'EuroProtection').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'LegalProtection').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'DamageInsurance').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'valuePicker').click()

driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.CheckedTextView[2]').click()

driver.find_element(MobileBy.ID, 'android:id/button1').click()

driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Quote').click()

driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[1]/android.widget.TextView').click()

perf_data = {
        "session_id": driver.session_id,
        "status": "passed"
    }

session_id = driver.session_id

sessionEndTime = time.time()
videoEndTime = str(sessionEndTime)

driver.execute_script('headspin:quitSession', {'status': 'passed'})

stringSearchStart = str(startTime)
stringSearchStop = str(endTime)
endOcrTime = str(ocr_endtime)

api_endpoint = f'https://api-dev.headspin.io/v0/sessions/' + session_id + '/label/add'
print(api_endpoint)

#cold start time
session_data = {
    "name": "Insurance Calculator Cold Start",
    "label_type": "page-load-request",
    "category": "an optional category for the label",
    "ts_start": stringSearchStart,
    "ts_end": stringSearchStop,
    "data": {"optional": "data"},
    "pinned": True
    }

output = requests.post(api_endpoint, headers=HEADER, json=session_data)
print("This is the output: ", output)

#Image Match Information
image_data = {
    "name": "Car Image Match",
    "label_type": "image-match-request",
    "category": "Image Match",
    "ts_start": stringSearchStart,
    "ts_end": stringSearchStop,
    "data": {"method": "template", "image_id": "acd42572-9383-11ee-a112-0271dce7b5c3", "threshold": 0.9},
    "pinned": True
}

image_output = requests.post(api_endpoint, headers=HEADER, json=image_data)
print("This is the image output: ", image_output)

#Video MOS Below 4.0 Information
video_mos_data = {
    "name": "Video MOS Below 4.0",
    "label_type": "time-series-request",
    "category": "Video MOS check",
    "ts_start": stringSearchStart,
    "ts_end": videoEndTime,
    "data": {"method": "range", "time_series_key": "video_quality_mos", "parameters": {"upper_limit": 4.0}},
    "pinned": True
}

video_mos_output = requests.post(api_endpoint, headers=HEADER, json=video_mos_data)
print("This is the video mos output: ", video_mos_output)

#Video MOS Summary Stats: mean, 50th & 90th Percentiles
video_summary_data = {
    "name": "Video MOS Summary Stats",
    "label_type": "time-series-request",
    "category": "Video MOS check",
    "ts_start": stringSearchStart,
    "ts_end": videoEndTime,
    "data": {"method": "stats", "time_series_key": "video_quality_mos", "parameters": {"metrics": ["mean", "percentile 50", "percentile 90"]}},
    "pinned": True
}

video_summary_output = requests.post(api_endpoint, headers=HEADER, json=video_summary_data)
print("This is the video summary output: ", video_mos_output)

#Loading Animation
loading_animation_data = {
    "name": "Loading Animation",
    "label_type": "loading-animation-request",
    "category": "an optional category for the label",
    "ts_start": stringSearchStart,
    "ts_end": stringSearchStop,
    "data": {"min_radius": 10, "max_radius": 20},
    "pinned": True
}
loading_animation_output = requests.post(api_endpoint, headers=HEADER, json=loading_animation_data)
print("This is the loading animation output: ", loading_animation_output)

#OCR Request for Car Information
ocr_car_data = {
    "name": "Car Text",
    "label_type": "ocr-request",
    "category": "OCR Car check",
    "ts_start": stringSearchStop,
    "ts_end": endOcrTime,
    "video_box": [[160, 160, 200, 195]],
    "pinned": True
}

ocr_car_output = requests.post(api_endpoint, headers=HEADER, json=ocr_car_data)
print("This is the ocr car output: ", ocr_car_output)

ocr_car_data_output = json.loads(ocr_car_output.text)
ocr_request_label = ocr_car_data_output['label_id']

ocr_endpoint = 'https://api-dev.headspin.io/v0/sessions/label/' + ocr_request_label


ocr_label_group = requests.get(ocr_endpoint, headers=HEADER)
ocr_label_group_text = json.loads(ocr_label_group.text)
ocr_label_group_id = ocr_label_group_text['label_group_id']
print(ocr_label_group_id)

ocr_analysis_endpoint = f'https://api-dev.headspin.io/v0/sessions/analysis/status/' + session_id + '?track=ocr&timeout=40'
ocr_analysis_status = requests.get(ocr_analysis_endpoint, headers={'Authorization': 'Bearer {}'.format(auth_token)})

ocr_analysis_status_result = json.loads(ocr_analysis_status.text)
status = ocr_analysis_status_result['status']
if status == 'done':
    print('status is done')
    ocr_group_endpoint = 'https://api-dev.headspin.io/v0/sessions/label/group/' + ocr_label_group_id
    ocr_result = requests.get(ocr_group_endpoint, headers={'Authorization': 'Bearer {}'.format(auth_token)})
    ocr_result_text = json.loads(ocr_result.text)
    print(ocr_result_text)
    for each in ocr_result_text['labels']:
        print (each['name'])
else:
    print('status timed out')

session_waterfall_url = f'https://ui.headspin.io/sessions/' + session_id + '/waterfall'
print('The session waterfall URL: ' + session_waterfall_url)

