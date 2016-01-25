import os
from selenium import webdriver
from urllib.request import urlretrieve

driver = webdriver.Chrome()

def LogInMessenger(email,password):
	driver.get('https://www.messenger.com/login.php')
	driver.find_element_by_id('email').send_keys(email)
	driver.find_element_by_id('pass').send_keys(password)
	driver.find_element_by_id('loginbutton').click()

def GetImages():
	driver.implicitly_wait(10)
	imageList=driver.find_elements_by_css_selector('._3m31')

	count=1
	for i in imageList:
		imageUrl=str(i.get_attribute('style').split('(')[1].split(')')[0].split('"')[1])
		print('Downloading Image : '+str(count))
		urlretrieve(imageUrl,'FBPhotos/'+str(count)+'.jpg')
		count+=1

def showUsers():
	driver.implicitly_wait(10)
	userList=driver.find_elements_by_class_name('_1ht6')
	count = 0
	option=0
	for i in userList:
		userName=i.text
		print(str(count+1)+'. '+userName)
		count+=1

	print('\n')
	while True:	
		option=int(input('Choose User (Enter Number) : '))
		if(option > 0 and option < count):
			break
	print('\n')
	driver.find_elements_by_xpath("//a[@class='_1ht5 _5l-3']")[option-1].click()

if __name__ == '__main__':
	email=input("Enter Email : ")
	password=input("Enter Password : ")
	LogInMessenger(email,password)
	showUsers()
	if not os.path.exists('FBPhotos'): os.makedirs('FBPhotos')
	GetImages()
	driver.implicitly_wait(4)
	driver.quit()