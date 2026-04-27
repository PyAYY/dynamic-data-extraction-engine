import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Open a new, automated Google Chrome browser
driver = webdriver.Chrome()

# 2. Go to a website
driver.get("https://www.wikipedia.org/")

# 3. FIND the search bar (Wikipedia's search bar has the name="search")
search_box = driver.find_element(By.NAME, "search")

# 4. ACT: Type our text into the box
search_box.send_keys("Software Engineering")

# 5. ACT: Press the "Enter" key
search_box.send_keys(Keys.RETURN)

# Keep the browser open for a few seconds so you can see the result!
time.sleep(5)

# 6. Close the browser
driver.quit()