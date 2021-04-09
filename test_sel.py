from selenium import webdriver
from flask import Flask

import time

test_sel = Flask(__name__)

driver = webdriver.Chrome('C:/Users/amish/Downloads/chromedriver_win32/chromedriver.exe')

result = []

try:
  driver.get('https://www.voxi.co.uk/')
  result.append(['step1', 'true'])
except:
  result.append(['step1', 'false'])
  print("please check the code")
finally:
  print("step1 testing completed")

#------------------------------------------

try:
  accept_cookie = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button')
  accept_cookie.click()
  result.append(['step2', 'true'])
except:
  result.append(['step2', 'false'])
  print("please check the code")
finally:
  print("step2 testing completed")

#------------------------------------------

try:
  phone_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[3]/div/div/div/div[1]/div/a/div[3]')
  phone_button.click()
  result.append(['step3', 'true'])
except:
  result.append(['step3', 'false'])
  print("please check the code")
finally:
  print("step3 testing completed")

#------------------------------------------

try:
  view_phone = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div[3]/a/div/div')
  view_phone.click()
  time.sleep(5)
  result.append(['step4', 'true'])
except:
  result.append(['step4', 'false'])
  print("please check the code")
finally:
  print("step4 testing completed")

#------------------------------------------

try:
  choose_plan = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[3]/div/form/div/div[4]/div[3]/div/button')
  driver.execute_script("arguments[0].click();", choose_plan)
  result.append(['step5', 'true'])
except:
  result.append(['step5', 'false'])
  print("please check the code")
finally:
  print("step5 testing completed")

#------------------------------------------

try:
  get_this_plan = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[4]/div/div/div/div[1]/div/div/div/div[3]/footer/div[2]/button')
  driver.execute_script("arguments[0].click();", get_this_plan)
  time.sleep(5)
  result.append(['step6', 'true'])
except:
  result.append(['step6', 'false'])
  print("please check the code")
finally:
  print("step6 testing completed")

#------------------------------------------

try:
  not_want_extras = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[4]/div/div/div/div[2]/div/div/button')
  driver.execute_script("arguments[0].click();", not_want_extras)
  time.sleep(5)
  result.append(['step7', 'true'])
except:
  result.append(['step7', 'false'])
  print("please check the code")
finally:
  print("step7 testing completed")

#------------------------------------------

try:
  checkout = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[4]/div/div/div[3]/button')
  driver.execute_script("arguments[0].click();", checkout)
  time.sleep(5)
  result.append(['step8', 'true'])
except:
  result.append(['step8', 'false'])
  print("please check the code")
finally:
  print("step8 testing completed")

#------------------------------------------

try:
  driver.find_element_by_id("first-name").send_keys('test')
  driver.find_element_by_id("last-name").send_keys('jindal')
  driver.find_element_by_id("dob").click()
  driver.find_element_by_id("dob").send_keys('12 / 11 / 1990')
  time.sleep(1)
  driver.find_element_by_id("username").send_keys('testjindal2021')
  driver.find_element_by_id("email").send_keys('designcreative1811@gmail.com')
  # click enter address manually option and putting values
  Enter_adress_manually = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div/div[2]/div/div/form/div/div[1]/div/div/div[4]/div[1]/div/div[2]/small/button')
  driver.execute_script("arguments[0].click();", Enter_adress_manually)
  time.sleep(5)
  driver.find_element_by_id("input-address-flat-number").send_keys('1102')
  driver.find_element_by_id("input-address-house-name").send_keys('testjindal')
  driver.find_element_by_id("input-address-house-number").send_keys('1105')
  driver.find_element_by_id("input-address-street-name").send_keys('abcd bazar')
  driver.find_element_by_id("input-address-city").send_keys('london')
  driver.find_element_by_id("input-address-county").send_keys('england')
  driver.find_element_by_id("input-address-postcode").send_keys('RG142FB')
  driver.find_element_by_id("pin").send_keys('1102')
  driver.find_element_by_id("memorableWord").send_keys('maggie')
  driver.find_element_by_id("password").send_keys('12Testjindal@')
  driver.find_element_by_id("confirm-password").send_keys('12Testjindal@')
  result.append(['step9', 'true'])
except:
  result.append(['step9', 'false'])
  print("please check the code")
finally:
  print("step9 testing completed")

#------------------------------------------

try:
  #clicking continue option
  continue_output = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div/div[2]/div/div/form/div/div[3]/div/div/button')
  driver.execute_script("arguments[0].click();", continue_output)
  result.append(['step10', 'true'])
except:
  result.append(['step10', 'false'])
  print("please check the code")
finally:
  print("step10 testing completed")

#------------------------------------------

print(result)
driver.close()
#-------------------------


f = open("result.html", "w")
text = ''' 
<!DOCTYPE html>
<html>
<style>
h1{
  font-size: 30px;
  color: #fff;
  text-transform: uppercase;
  font-weight: 300;
  text-align: center;
  margin-bottom: 15px;
}
table{
  width:100%;
  table-layout: fixed;
}
.tbl-header{
  background-color: rgba(255,255,255,0.3);
 }
.tbl-content{
  margin-top: 0px;
  border: 1px solid rgba(255,255,255,0.3);
}
th{
  padding: 20px;
  text-align: center;
  font-weight: 500;
  font-size: 20px;
  color: #000;
  text-transform: uppercase;
  border: 1px solid rgba(255,255,255,0.3)
}
td{
  padding: 25px;
  text-align: center;
  vertical-align:middle;
  font-weight: 300;
  font-size: 18px;
  color: #000;
  text-transform: uppercase;
  border-bottom: solid 1px rgba(255,255,255,0.1);
}

@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
body{
  background: -webkit-linear-gradient(left, #25c481, #25b7c4);
  background: linear-gradient(to right, #25c481, #25b7c4);
  font-family: 'Roboto', sans-serif;
}
section{
  margin: 50px;
}
</style>
<section>
  <h1>VOXI Synthetic Test</h1>
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>Step</th>
          <th>Status</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
'''
f.write(text)
for i in range(len(result)):
    s0=result[i][0]
    s1=result[i][1]
    if s1=="true":
        s2="green"
    else:
        s2="red"
    text= '''
    <tr>
    <td >{0}</td>
    <td bgcolor="{2}">{1}</td>
    </tr>
    '''
    print(text.format(s0,s1,s2),file=f)

text = '''
      </tbody>
    </table>
  </div>
</section>
'''
f.write(text)
f.close()

