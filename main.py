from selenium import webdriver
from urllib.request import urlretrieve
import os
import distutils.dir_util
import requests
from selenium.webdriver.chrome.options import Options
def download_img(url,title,filename):
    file_dir = "./download_images/"+title+"/"
    if not os.path.isdir(file_dir):
        print("다운로드 디렉토리 생성")
        # os.mkdir(file_dir)
        distutils.dir_util.mkpath(file_dir)

    sess =requests.session()
    for cookie in driver.get_cookies():
        c = {cookie['name']: cookie['value']}
        sess.cookies.update(c)
    r = sess.get(img,allow_redirects=True)
    open(file_dir+filename,'wb').write(r.content)
    # urlretrieve(url,file_dir+filename)
    print(filename+"다운로드 완료")
driver = webdriver.Chrome("../chromedriver")

driver.get("https://page.kakao.com/main")



print("먼저 첫장을 열어주세요.")
input("열었으면 엔터")
title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/p').text
cnt=0
while True:
    try:
        # print(driver.page_source)
        img = driver.find_element_by_class_name('viewImg').get_attribute('src')
        # print(img)
        print(img)
        download_img(img,title,title+"_"+str(cnt)+".png")

        driver.find_element_by_class_name('btnNext').click()
        cnt +=1
    except Exception as exc:
        if "iconWrap" in driver.page_source:
            print("[불필요 메시지 넘김]")
            driver.find_element_by_class_name('iconWrap').click()
            continue
        if "마지막 페이지입니다" in driver.page_source:
            print("마지막 페이지")
            # input("다음장은 엔터")
            # next_page_btn = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/img[2]')
            next_page_btn = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/span[4]')
            next_page_btn.click()
            while True:
                try:
                    title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/p').text
                    if len(title)>1:
                        break
                except:
                    continue
            print(title)
            cnt = 0
            continue
        if "해당 콘텐츠를 열람하시려면 로그인" in driver.page_source:
            print("로그인이 필요")
        # print(driver.page_source)
        # print(exc)
        # break