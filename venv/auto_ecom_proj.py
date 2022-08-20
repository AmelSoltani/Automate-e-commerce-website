from selenium import webdriver
import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
#initial webdriver
driver = webdriver.Edge('C:/edgedriver_win64 (1)/msedgedriver.exe')
#open the website to automate tasks on 
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

#select phone
phones = driver.find_element('xpath','//*[@id="menu"]/div[2]/ul/li[6]/a')

#phones = driver.find_element('xpath','//a[text()="Phones & PDAs"]')
phones.click()
#select iphone
iphone = driver.find_element('xpath','//a[text()="iPhone"]')
iphone.click()
time.sleep(2)

#click on picture
pic=driver.find_element('xpath','//ul[@class="thumbnails"]/li[1]')
pic.click()
time.sleep(2)

#see all the position of the phone
next= driver.find_element('xpath','//button[@title="Next (Right arrow key)"]')
for i in range(0,5):
    next.click()
    time.sleep(1)
driver.save_screenshot("screenshot"+str(random.randint(0, 20))+'.png')
exit=driver.find_element('xpath','/html/body/div[2]/div/div[1]/div/button')
exit.click()
time.sleep(1)

#enter the quantity of the phone
qte=driver.find_element('id','input-quantity')
qte.click()
time.sleep(2)
qte.clear()
time.sleep(2)
qte.send_keys(3)
time.sleep(1)

#add thee phone to the product to buy
buy_button=driver.find_element('id','button-cart')
buy_button.click()
time.sleep(1)

#click on the button to see the laptop category
laptop=driver.find_element('xpath','//*[@id="menu"]/div[2]/ul/li[2]/a')
action=ActionChains(driver)
action.move_to_element(laptop).perform()
time.sleep(2)

#go to laptop shop
laptop_1=driver.find_element('xpath','//*[@id="menu"]/div[2]/ul/li[2]/div/a')
laptop_1.click()
time.sleep(2)

#choose laptop
choose_laptp=driver.find_element('xpath','//*[@id="content"]/div[4]/div[1]/div/div[1]/a/img')
choose_laptp.click()
time.sleep(2)

#scroll
add_button=driver.find_element('xpath','//*[@id="button-cart"]')
add_button.location_once_scrolled_into_view
time.sleep(1)
#choose date
choose_date=driver.find_element('xpath','//*[@id="product"]/div[1]/div/span/button')
choose_date.click()
time.sleep(2)

choose_year=driver.find_element('xpath','/html/body/div[4]/div/div[1]/table/thead/tr[1]/th[2]')

#search for the year date we want
next_click=driver.find_element('xpath','/html/body/div[4]/div/div[1]/table/thead/tr[1]/th[3]')
while choose_year.text != 'December 2022':
    next_click.click()

#choose date
calender_day=driver.find_element('xpath','/html/body/div[4]/div/div[1]/table/tbody/tr[5]/td[6]')
calender_day.click()
time.sleep(2)

#dd the product
add_button.click()
time.sleep(2)

#click on panier button_icon
panier=driver.find_element("xpath",'//*[@id="cart"]/button')
panier.click()
time.sleep(2)

#checkout
check_button=driver.find_element("xpath",'//*[@id="cart"]/ul/li[2]/div/p/a[2]/strong')
check_button.click()
time.sleep(2)

#check if the quantity of the product is in stock
url=driver.current_url
error_url="http://tutorialsninja.com/demo/index.php?route=checkout/cart"
if(url==error_url):
    error_msg=driver.find_element("xpath",'//*[@id="checkout-cart"]/div[1]').text
    print(error_msg)
while (url==error_url):
    product_qte=driver.find_element("xpath",'//*[@id="content"]/form/div/table/tbody/tr[1]/td[4]/div/input')
    refresh=driver.find_element("xpath",'//*[@id="content"]/form/div/table/tbody/tr[1]/td[4]/div/span/button[1]/i')
    qte=str(int(product_qte.get_attribute('value'))-1)
    product_qte.clear()
    product_qte.send_keys(qte)
    refresh.click()
    time.sleep(1)
    check_stock=driver.find_element("xpath",'//*[@id="content"]/div[3]/div[2]/a')
    check_stock.click()
    time.sleep(4)
    url=driver.current_url

#choose_guest_checkout
guest_checkout=driver.find_element("xpath",'//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
guest_checkout.click()
time.sleep(2)
    
#continu
continu=driver.find_element("xpath",'//*[@id="button-account"]')
continu.click()
time.sleep(2)
    
#second_step
sec_step=driver.find_element('xpath','//*[@id="accordion"]/div[2]/div[1]/h4/a')
sec_step.location_once_scrolled_into_view
time.sleep(2)
    
#first_name
first_name=driver.find_element('id','input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test name')
    
    
#last_name
last_name=driver.find_element('id','input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test last name')
    
#email
email=driver.find_element('id','input-payment-email')
email.click()
time.sleep(1)
email.send_keys('hello@gmail.com')
    
#telephone
telephone=driver.find_element('id','input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys(50470201)
    
#address1
address1=driver.find_element('id','input-payment-address-1')
address1.click()
time.sleep(1)
address1.send_keys('test name')
    
#city
city=driver.find_element('id','input-payment-city')
city.click()
time.sleep(1)
city.send_keys('sousse')
    
#post_code
postcode=driver.find_element('id','input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys(4060)
    
#select a country
country= driver.find_element('xpath','//*[@id="input-payment-country"]')
drop_down= Select(country)
time.sleep(2)
drop_down.select_by_index(230)
time.sleep(2)
    
#select a cregion
region= driver.find_element('id',"input-payment-zone")
drop_down1= Select(region)
time.sleep(2)
drop_down1.select_by_visible_text("Sousse")
time.sleep(2)
    
#continue to 3rd step
continu1=driver.find_element("xpath",'//*[@id="button-guest"]')
continu1.click()
time.sleep(2)
       
#continue to 4rd step
continu1=driver.find_element("id",'button-shipping-method')
continu1.click()
time.sleep(2)
    
    
#check agreement
check_agreement=driver.find_element('xpath','//*[@id="collapse-payment-method"]/div/div[2]/div/input[1]')
check_agreement.click()
time.sleep(1)
    
#continu to the 5th step
continu5= driver.find_element('id','button-payment-method')
continu5.click()
time.sleep(2)
    
price=driver.find_element("xpath",'//*[@id="collapse-checkout-confirm"]/div/div[1]/table/tfoot/tr[3]/td[2]')
Price=price.text
print("The total price of the products is :" + Price) 

#finish the whole process
pay_button=driver.find_element('id','button-confirm')
pay_button.click()
time.sleep(1)

#msg after finishing the whole process
succes_msg=driver.find_element("xpath",'//*[@id="content"]/h1')
print(succes_msg.text)
