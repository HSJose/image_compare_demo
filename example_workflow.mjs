import { remote } from 'webdriverio';
import fetch from 'node-fetch';
import dotenv from 'dotenv';

dotenv.config();

const auth_token = process.env.API_TOKEN;
const APPIUM = `https://dev-us-sny-8.headspin.io:7001/v0/${auth_token}/wd/hub`;
const HEADER = { 'Authorization': `Bearer ${auth_token}` };

const CAPS = {
    deviceName: 'SM-S911U',
    udid: 'RFCR115W4ND',
    autoAcceptAlerts: true,
    automationName: 'UiAutomator2',
    platformName: 'Android',
    appPackage: 'com.android.settings',
    appActivity: 'com.android.settings.Settings',
    'headspin:testName': 'Demo_Insurance_App',
    'headspin:capture': true,
    adbExecTimeout: 100000,
};

let driver;

try {
    driver = await remote({
        capabilities: CAPS,
        path: '/wd/hub',
        port: 7001,
        hostname: 'dev-us-sny-8.headspin.io',
        protocol: 'https',
        headers: HEADER
    });

    await driver.terminateApp('com.android.settings');
    await driver.pressKeyCode(3);

    const insuranceCalcIcon = await driver.$('~Insurance Calculator');
    const startTime = Date.now();
    await insuranceCalcIcon.click();

    const carButton = await driver.$('id=com.tricentis.insuranceCalculatorApp:id/Car');
    const endTime = Date.now();
    await carButton.click();

    const ocrEndTime = Date.now();

    await driver.$('id=com.tricentis.insuranceCalculatorApp:id/Make').click();
    await driver.$('id=android:id/button1').click();
    await driver.$('id=com.tricentis.insuranceCalculatorApp:id/YearOfConstruction').click();
    await driver.$('~valuePicker').click();
    await driver.$('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.CheckedTextView[2]').click();
    await driver.$('id=android:id/button1').click();
    await driver.$('~Listprice').click();
    await driver.$('~Listprice').setValue('12000');
    await driver.$('~MileagePerYear').click();
    await driver.$('~MileagePerYear').setValue('2000');
    await driver.$('id=com.tricentis.insuranceCalculatorApp:id/Performance').setValue('20');
    await driver.hideKeyboard();
    await driver.$('id=com.tricentis.insuranceCalculatorApp:id/Fuel').click();
    await driver.$('id=android:id/button1').click();
    await driver.hideKeyboard();
    await driver.$('id=com.tricentis.insuranceCalculatorApp:id/Usage').click();
    await driver.$('id=android:id/button1').click();


    await driver.$('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[3]/android.widget.TextView').click();

    const firstName = await driver.$('~FirstName');

    await firstName.setValue('Head');
    await driver.$('~LastName').setValue('Spin');
    await driver.$('~DayOfBirth').click();
    await driver.$('~Decrease month').click();
    await driver.$('~Decrease month').click();
    await driver.$('id=android:id/button1').click();
    await driver.$('~GenderMale').click();
    await driver.$('~Occupation').click();
    await driver.$('id=android:id/button1').click();
    await driver.$('~Product Details').click();
    await driver.$('~PreferredStartDate').click();
    await driver.$('~Increase month').click();
    await driver.$('~Increase month').click();
    await driver.$('id=android:id/button1').click();
    await driver.$('~PaymentOption').click();
    await driver.$('id=android:id/button1').click();
    await driver.$('~EuroProtection').click();
    await driver.$('~LegalProtection').click();
    await driver.$('~DamageInsurance').click();
    await driver.$('~valuePicker').click();
    await driver.$('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.CheckedTextView[2]').click();
    await driver.$('id=android:id/button1').click();
    await driver.$('~Quote').click();
    await driver.$('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[1]/android.widget.TextView').click();


    const sessionEndTime = Date.now();
    const videoEndTime = sessionEndTime.toString();

    // Function to perform a POST request
    async function postRequest(url, headers, body) {
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(body),
            });
            const data = await response.json();
            console.log('Response:', data);
            return data;
        } catch (error) {
            console.error('Error:', error);
        }
    }

    const session_id = await driver.getSessionId();
    const stringSearchStart = startTime.toString();
    const stringSearchStop = endTime.toString();
    const endOcrTime = ocrEndTime.toString();

    const api_endpoint = `https://api-dev.headspin.io/v0/sessions/${session_id}/label/add`;

    // Cold Start Time
    const session_data = {
        "name": "Insurance Calculator Cold Start",
        "label_type": "page-load-request",
        "category": "an optional category for the label",
        "ts_start": stringSearchStart,
        "ts_end": stringSearchStop,
        "data": {"optional": "data"},
        "pinned": true
    };
    await postRequest(api_endpoint, HEADER, session_data);

    // Image Match Information
    const image_data = {
        "name": "Car Image Match",
        "label_type": "image-match-request",
        "category": "Image Match",
        "ts_start": stringSearchStart,
        "ts_end": stringSearchStop,
        "data": {"method": "template", "image_id": "acd42572-9383-11ee-a112-0271dce7b5c3", "threshold": 0.9},
        "pinned": true
    };
    await postRequest(api_endpoint, HEADER, image_data);

    // Video MOS Below 4.0 Information
const video_mos_data = {
    "name": "Video MOS Below 4.0",
    "label_type": "time-series-request",
    "category": "Video MOS check",
    "ts_start": stringSearchStart,
    "ts_end": videoEndTime,
    "data": {"method": "range", "time_series_key": "video_quality_mos", "parameters": {"upper_limit": 4.0}},
    "pinned": true
};
await postRequest(api_endpoint, HEADER, video_mos_data);

// Video MOS Summary Stats: mean, 50th & 90th Percentiles
const video_summary_data = {
    "name": "Video MOS Summary Stats",
    "label_type": "time-series-request",
    "category": "Video MOS check",
    "ts_start": stringSearchStart,
    "ts_end": videoEndTime,
    "data": {"method": "stats", "time_series_key": "video_quality_mos", "parameters": {"metrics": ["mean", "percentile 50", "percentile 90"]}},
    "pinned": true
};
await postRequest(api_endpoint, HEADER, video_summary_data);

// Loading Animation
const loading_animation_data = {
    "name": "Loading Animation",
    "label_type": "loading-animation-request",
    "category": "an optional category for the label",
    "ts_start": stringSearchStart,
    "ts_end": stringSearchStop,
    "data": {"min_radius": 10, "max_radius": 20},
    "pinned": true
};
await postRequest(api_endpoint, HEADER, loading_animation_data);

// OCR Request for Car Information
const ocr_car_data = {
    "name": "Car Text",
    "label_type": "ocr-request",
    "category": "OCR Car check",
    "ts_start": stringSearchStop,
    "ts_end": endOcrTime,
    "video_box": [[160, 160, 200, 195]],
    "pinned": true
};
const ocr_car_output = await postRequest(api_endpoint, HEADER, ocr_car_data);

let ocr_request_label = '';
if (ocr_car_output && ocr_car_output.label_id) {
    ocr_request_label = ocr_car_output.label_id;
}

const ocr_endpoint = `https://api-dev.headspin.io/v0/sessions/label/${ocr_request_label}`;

const ocr_label_group = await fetch(ocr_endpoint, { headers: HEADER });
const ocr_label_group_text = await ocr_label_group.json();
const ocr_label_group_id = ocr_label_group_text.label_group_id;
console.log(ocr_label_group_id);
const ocr_analysis_endpoint = `https://api-dev.headspin.io/v0/sessions/analysis/status/${session_id}?track=ocr&timeout=40`;
const ocr_analysis_status = await fetch(ocr_analysis_endpoint, { headers: {'Authorization': `Bearer ${auth_token}`} });
const ocr_analysis_status_result = await ocr_analysis_status.json();
const status = ocr_analysis_status_result.status;

if (status === 'done') {
    const ocr_group_endpoint = `https://api-dev.headspin.io/v0/sessions/label/group/${ocr_label_group_id}`;
    const ocr_result = await fetch(ocr_group_endpoint, { headers: {'Authorization': `Bearer ${auth_token}`} });
    const ocr_result_text = await ocr_result.json();
    console.log(ocr_result_text);
    ocr_result_text.labels.forEach(label => {
        console.log(label.name);
    });
} else {
    console.log('status timed out');
}

const session_waterfall_url = `https://ui.headspin.io/sessions/${session_id}/waterfall`;
console.log('The session waterfall URL: ' + session_waterfall_url);

// At the end of your script
await driver.deleteSession();
} catch (e) {
    console.error(e);
    if (driver) {
    await driver.deleteSession();
    }
}
