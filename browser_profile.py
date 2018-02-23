from selenium import webdriver

def browser_file_download_profile(browser):
    if browser == 1:
        profile = webdriver.FirefoxProfile()
        #设置成0表示下载到桌面;设置成1表示下载到默认路径;设置成2则可以保存到指定目录
        profile.set_preference('browser.download.folderList',2)
        #设置一个本地电脑路径
        profile.set_preference('browser.download.dir','d:\\')
        #对所给出文件类型不再弹出框进行询问
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',"application/octet-stream")
        driver  =webdriver.Firefox(firefox_profile = profile)
        driver.get("http://note.youdao.com/")
        driver.find_element_by_id("download-btn").click()
    elif browser == 2:
        profile = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups':0,'download.default_directory':'d:\\'}
        profile.add_experimental_option('prefs',prefs)
        #这个是chromedriver的路径 如果设置过环境变量，此参数可以省略
        #chromedriver_path = "D:\\path\\chromedriver.exe"
        driver = webdriver.Chrome(chrome_options=profile)
        driver.get("http://note.youdao.com/")
        driver.find_element_by_id("download-btn").click()
    else:
        print("浏览器类型不正确，请重新选择！")



browser_file_download_profile(1)
