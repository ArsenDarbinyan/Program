import selenium
from pip._vendor import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os


class InstBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("chromedriver.exe")

    def like(self, url):

        self.browser.get(url)
        time.sleep(1.5)
        self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
        time.sleep(1.5)
        self.browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
        # time.sleep(random.randint(80, 100))

    def clos(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        try:

            self.browser.get("https://www.instagram.com")
            time.sleep(1)
            u, p = self.browser.find_element_by_name("username"), self.browser.find_element_by_name("password")
            time.sleep(1)
            u.clear()
            u.send_keys(self.username)
            p.clear()
            p.send_keys(self.password + "\ue007")
        except Exception as ex:
            print(ex)
            self.clos()

    def tag(self, h, n):
        try:
            tags = self.browser.find_element_by_class_name("XTCLo.x3qfX")
            tags.send_keys("#" + h)
            time.sleep(2)
            tags.send_keys("\ue007")
            tags.send_keys("\ue007")
            # "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a"
            time.sleep(3)
            for x in range(1, n):
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            heshtag = [x.get_attribute("href") for x in self.browser.find_elements_by_tag_name("a") if
                       "/p/" in x.get_attribute("href")]
            for x in heshtag:
                self.like(x)
        except Exception as ex:
            print(ex)
            self.clos()

    def exsist(self, Xpath):
        try:
            self.browser.find_element_by_xpath(Xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    #
    def mark1(self, user):
        try:
            self.browser.get(user)
            time.sleep(2)
            if self.exsist("/html/body/div[1]/section/main/div/h2"):
                print("plan1")
                self.clos()
            else:
                print("plan2")
                self.like(user)
                print(f"plan 2{user} finish")
        except Exception as ex:
            print(ex)
            self.clos()

    def mark2(self, user):
        try:
            self.browser.get(user)
            time.sleep(2)
            if self.exsist("/html/body/div[1]/section/main/div/h2"):
                print("plan1")
                self.clos()
            else:
                u = int(self.browser.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text) // 12
                ulrs = []
                for x in range(u):
                    href = [x.get_attribute("href") for x in self.browser.find_elements_by_tag_name("a") if
                            "/p/" in x.get_attribute("href")]
                    for x in href:
                        ulrs.append(x)
                    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                file = [x for x in user.split("/") if "" != x][-1]

                # with open(f"{file}.txt","a") as f:
                #     for x in list(set(ulrs)):
                #         f.write(x+"\n")
                for x in range(len(list(set(ulrs)))):
                    self.like(list(set(ulrs))[x])


        except Exception as e:
            print(e)
            self.clos()

    def install(self, url):

        try:

            self.browser.get(url)
            u = int(self.browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text) // 12
            ulrs = []
            for x in range(u):
                href = [x.get_attribute("href") for x in self.browser.find_elements_by_tag_name("a") if
                        "/p/" in x.get_attribute("href")]
                for x in href:
                    ulrs.append(x)
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            file = [x for x in url.split("/") if "" != x][-1]
            fil = []

            # with open(f"{file}.txt", "a") as f:
            #     for x in list(set(ulrs)):
            #         f.write(x + "\n")
            if os.path.exists(f"{file}"):
                pass
            else:
                os.mkdir(file)
            intn = 0
            for x in list(set(ulrs)):
                try:
                    intn += 1
                    self.browser.get(x)
                    time.sleep(3)
                    img1 = "/html/body/div[1]/section/main/div/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/img"
                    img = "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img"
                    video = "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/div/div/video"
                    post_id = [x1 for x1 in x.split("/") if "" != x1][-1]

                    if self.exsist(img):
                        imgS = self.browser.find_element_by_xpath(img).get_attribute("src")
                        fil.append(imgS)
                        with open(f"{file}/{intn}_{post_id}.jpg", "wb") as img_file:
                            img_file.write(requests.get(imgS).content)

                    elif self.exsist(video):
                        fil.append(self.browser.find_element_by_xpath(video).get_attribute("src"))

                        # сохраняем видео
                        get_video = requests.get(self.browser.find_element_by_xpath(video).get_attribute("src"),
                                                 stream=True)
                        with open(f"{file}/{intn}_{post_id}video.mp4", "wb") as video_file:
                            for x2 in get_video.iter_content(chunk_size=1024 * 1024):
                                if x2:
                                    video_file.write(x2)
                    elif self.exsist(img1):
                        imgS = self.browser.find_element_by_xpath(img1).get_attribute("src")
                        fil.append(imgS)
                        with open(f"{file}/{intn}_{post_id}.jpg", "wb") as img_file:
                            img_file.write(requests.get(imgS).content)
                    else:
                        # print("Упс! Что-то пошло не так!")
                        fil.append(f"{post_id}, нет ссылки!")
                    print(f"Контент из поста {post_id} успешно скачан!")


                except Exception as ex:
                    print(ex)
                    self.clos()
        except Exception as ex:
            print(ex)
            self.clos()


login = ""  # your password
password = ""  # your password
username = ""  # username
a = InstBot()
a.login()
time.sleep(20)
a.install(f"https://www.instagram.com/{username}/")
time.sleep(2)

a.clos()
