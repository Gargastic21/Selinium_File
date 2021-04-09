from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/amish/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.voxi.co.uk/')
#driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button').click()
file_name="req.txt"
f=open(file_name,"r")

def convert(str):
    l1=list(str.split())
    return l1

#def click(l):
 #   return ("{0}('{1}').click()".format(l[0],l[2]))

#def send(l):
#    return ("{0}.send({1})".format(l[0],l[2]))

time.sleep(5)

for i in f:
    #print("{0}".format(i.strip()))
    str = i.strip()
    l=convert(str)
    if l[1] == "click":
        print("{0}('{1}').click()".format(l[0],l[2]))
        "{0}('{1}').click()".format(l[0],l[2])
        
    elif l[1] == "send":
        print("{0}.send({1})".format(l[0],l[2]))
        "{0}.send({1})".format(l[0],l[2])


 

#driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button').click()
#------------------------------------------
