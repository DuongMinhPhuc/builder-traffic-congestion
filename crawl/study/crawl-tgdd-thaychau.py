from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException   

header = ['Name', 'Rating', 'Comment']
df = pd.DataFrame(columns=header)
driver = webdriver.Chrome()
url = 'https://www.thegioididong.com/dtdd'

def crawlPaperFromTheGioiDiDong(url):
    driver.get(url)
    while True:
        try:
            element = driver.find_element_by_class_name('viewmore')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        except:
            break;
    listOfProduct = driver.find_elements_by_tag_name("li")
    i = 2
    listOfHyperlink = []
    index = 1
    try:
        while listOfProduct:
            ele = listOfProduct.pop()
            xpath = "/html/body/section/ul[2]/li[" + str(i) + "]/a "
            hyperlink = ele.find_element(By.XPATH, xpath).get_attribute('href')
            i = i + 1
            listOfHyperlink.append(hyperlink)
    except:
        pass
    while listOfHyperlink:
        ele = listOfHyperlink.pop()
        driver.get(ele)
        time.sleep(1)
        # get all comments of the product
        try:
            nameProduct = driver.find_element(By.XPATH, '/html/body/section/div[1]/h1').text
            tmp = driver.find_element(By.XPATH, '//*[@id="boxRatingCmt"]/div[3]/div[2]/div')
            
            idx = 1
            while True:
                try:
                    driver.execute_script('ratingCmtList(' + str(idx) + ')')
                    time.sleep(1)
                    listComment = driver.find_element(By.XPATH, '//*[@id="boxRatingCmt"]/div[3]/ul')
                    comments = listComment.find_elements(By.CLASS_NAME, "par")
                    for comment in comments:
                        textComment = comment.find_element(By.XPATH, 'div[2]/p/i').text
                        print(textComment)
                        tmp = comment.find_element(By.XPATH, 'div[2]/p/span')
                        rating = len(tmp.find_elements(By.CLASS_NAME, 'iconcom-txtstar'))
                        
                        # to create dataframe
                        df.set_value(index, "Name", nameProduct)
                        df.set_value(index, "Comment", textComment)
                        df.set_value(index, "Rating", rating)
                        index = index + 1
                        print(nameProduct, textComment, rating)
                    idx = idx + 1
                except:
                    # for button in buttoms:
                    break
        except NoSuchElementException:
            try:
                listComment = driver.find_element(By.XPATH, '//*[@id="boxRatingCmt"]/div[3]/ul')
                comments = listComment.find_elements(By.CLASS_NAME, "par")
                for comment in comments:
                    textComment = comment.find_element(By.XPATH, 'div[2]/p/i').text
                    print(textComment)
                    tmp = comment.find_element(By.XPATH, 'div[2]/p/span')
                    rating = len(tmp.find_elements(By.CLASS_NAME, 'iconcom-txtstar'))
                    
                    df.set_value(index, "Name", nameProduct)
                    df.set_value(index, "Comment", textComment)
                    df.set_value(index, "Rating", rating)
                    index = index + 1
                    print(nameProduct, textComment, rating)
            except:
                pass
        except:
            pass
    return df
crawlPaperFromTheGioiDiDong(url).to_csv('result.csv',encoding='utf-8')
driver.close()
driver.quit()