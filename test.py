from selenium import webdriver  #impoting
import time                         
driver = webdriver.Chrome(executable_path="chromedriver.exe") 
#path of the file which is downloaded from google driver for chrom version 108
# driver.get("https://pynative.com/python-classes-and-objects/") 


#webdriver commands 
#to open the window which url given in the url fuction.
#print(driver.title) # to print the title of the website whcih url mention above
#driver.maximize_window() #to maximize window automatically
#driver.minimize_window() #to minimize window automatically
# driver.quit()  #to quit or close the particulr website
#driver.refresh() #to refresh the website 
#print(driver.page_source) #to see page souce of particular website
#print(driver.get_window_size) #give the size of window of particular website
# driver.get_screenshot_as_file('ssofwebiste.png')  
# to take ss of website as file and it take one argumnet with file name and fine name should contain .png extention



#navigations command
# driver.get("https://pynative.com/python-classes-and-objects/") 
# print("it is in pynative website")
# driver.maximize_window()
# print("print title")
# print(driver.title)
# time.sleep(5)


# driver.get("https://google.com") 
# print("it is in google website")

# print(driver.title)     
# time.sleep(5)

# driver.back()
# print("back into pynative website")


# print(driver.title)
# driver.forward()


# driver.quit()

#conditional commands

