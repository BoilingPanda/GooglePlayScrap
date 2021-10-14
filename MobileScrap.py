from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = None


def get_release_date(game_name, device_name):
    print("0")
    global driver
    APPIUM = "http://localhost:4723/wd/hub"
    #APP = "com.android.vending"
    print("11")
    desired_caps = {
        "deviceName": device_name,
        "platformName": "Android",
        "platformVersion": "7.0",
        'automationName': 'UIAutomator2',
        #"browserName": "Chrome",
        #"chromedriverExecutable":"E:\IdeaProjects\GooglePlayScrap\chromedriver.exe",
        #"headspin:autoDownloadChromedriver": True
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main"
        # "appPackage": APP,
        # "appActivity": ".AssetBrowserActivity"
    }
    try:
        print("1")
        driver = webdriver.Remote(APPIUM, desired_caps)
        print(game_name)
        driver.get(game_name)
        time.sleep(5)
        driver.start_activity('com.android.vending', 'com.google.android.finsky.activities.MainActivity')
        # WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable(MobileBy.ACCESSIBILITY_ID, "PLAY STORE UYGULAMASINDA AÇ")).click()

        # WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
        #                                                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget."
        #                                                 "FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget."
        #                                                 "FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/"
        #                                                 "android.view.ViewGroup/android.widget.FrameLayout/android.view."
        #                                                 "ViewGroup/android.widget.TextView"))
        # ).click()
        #
        # search_input = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText"))
        # )
        # search_input = driver.find_element(MobileBy.XPATH,
        #                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText")
        # search_input.click()
        # search_input.send_keys(game_name)
        # driver.press_keycode(66)

        # time.sleep(10)
        # game_substr = game_string[5:10]
        # print("game substr: {}".format(game_substr))
        # if check_element("//android.widget.CompoundButton[@content-desc=\"4,0 yıldız ve üzeri\"]/android.widget.TextView"):
        #     print("Listeden oyun seçimi yapılıyor.")
        #     driver.find_element_by_android_uiautomator(
        #         'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("' + game_string + '").instance(0));').click()
        #     # for i in range(10):
        #     #     try:
        #     #         xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[{}]/android.view.ViewGroup/android.view.View".format(
        #     #             i)
        #     #         the_game = driver.find_element(MobileBy.XPATH, xpath)
        #     #         if game_substr.lower() in the_game.get_attribute("content-desc").lower():
        #     #             the_game.click()
        #     #             break
        #     #     except NoSuchElementException:
        #     #         print("Element not found")
        # elif check_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]"):
        #     if game_substr in driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]").get_attribute("content-desc"):
        #         print("promo ekranından oyuna ulaşılıyor. {} - {}". format(game_string, driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]").get_attribute("content-desc")))
        #         WebDriverWait(driver, 30).until(
        #             EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]"))
        #         ).click()
        #         #driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]").click()
        # else:
        #     print("herhangi bir koşula girmedi 1")
        #     print(driver.find_element(MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]").get_attribute("content-desc"))
        # print("1")
        time.sleep(10)
        # more = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Bu oyun hakkında için diğer sonuçlar"))
        # )
        driver.find_element(MobileBy.ACCESSIBILITY_ID, "Bu oyun hakkında için diğer sonuçlar").click()
        print("2")
        # WebDriverWait(driver, 30).until(
        #     EC.visibility_of(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
        # )
        time.sleep(10)
        print("3")
        element = driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("' + "Çıkış tarihi" + '").instance(0));')
        date_label = driver.find_element(MobileBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.TextView[1]")
        date = driver.find_element(MobileBy.XPATH,
                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.TextView[2]")
        if date_label.get_attribute("text") == "Çıkış tarihi":
            return date.get_attribute("text")
        else:
            return driver.find_element(MobileBy.XPATH,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[2]").get_attribute("text")
    except:
        print("Tarih bulunamadı")
        return "Yok"


# def check_element(selector_string):
#     time.sleep(5)
#     try:
#         driver.find_element(MobileBy.XPATH, selector_string)
#         return True
#     except NoSuchElementException:
#         return False
