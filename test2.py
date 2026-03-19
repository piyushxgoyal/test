from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time, os

driver = webdriver.Chrome()
driver.maximize_window()

# ---------------- Q1 ----------------
driver.get("https://demowebshop.tricentis.com")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Books").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Shopping cart").click()
product = driver.find_element(By.XPATH, "//td[@class='product']/a")
print("Q1:", "Product present" if product.is_displayed() else "Not found")

# ---------------- Q2 ----------------
driver.get("https://demowebshop.tricentis.com")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Electronics").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='sub-category-item']//a[contains(text(),'Cell phones')]").click()
print("Q2 done")

# ---------------- Q3 ----------------
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element(By.XPATH, "//button").click()
text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "finish")))
print("Q3:", text.text)

# ---------------- Q4 ----------------
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.find_element(By.XPATH, "//button[text()='Remove']").click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']"))
).click()
print("Q4 done")

# ---------------- Q5 ----------------
driver.get("https://demoqa.com/select-menu")
time.sleep(3)
driver.find_element(By.ID, "withOptGroup").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text()='Group 2, option 1']").click()
value = driver.find_element(
    By.XPATH, "//div[@id='withOptGroup']//div[contains(@class,'singleValue')]"
).text
print("Q5:", value)

# ---------------- Q6 ----------------
multi = Select(driver.find_element(By.ID, "cars"))
multi.select_by_visible_text("Volvo")
multi.select_by_visible_text("Saab")
multi.select_by_visible_text("Opel")
print("Q6:")
for option in multi.all_selected_options:
    print(option.text)

# ---------------- Q7 ----------------
driver.get("https://demoqa.com/menu/")
time.sleep(3)
actions = ActionChains(driver)
main = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
actions.move_to_element(main).perform()
time.sleep(2)
sub = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
actions.move_to_element(sub).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 1']").click()
print("Q7 done")

# ---------------- Q8 ----------------
driver.get("https://demoqa.com/droppable")
time.sleep(3)
drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop(drag, drop).perform()
time.sleep(2)
print("Q8:", drop.text)

# ---------------- Q9 ----------------
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
driver.switch_to.alert.accept()
print("Q9:", driver.find_element(By.ID, "result").text)

# ---------------- Q10 ----------------
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)
file_path = os.path.abspath("test.txt")
with open(file_path, "w") as f:
    f.write("test")
driver.find_element(By.ID, "file-upload").send_keys(file_path)
driver.find_element(By.ID, "file-submit").click()
print("Q10:", driver.find_element(By.ID, "uploaded-files").text)

# ---------------- Q11 ----------------
driver.get("https://the-internet.herokuapp.com/download")
path = os.path.expanduser("./downloads")
before = set(os.listdir(path))
file = driver.find_element(By.XPATH, "//div[@class='example']//a[1]")
name = file.text
file.click()
time.sleep(5)
after = set(os.listdir(path))
print("Q11:", "Downloaded" if name in after else "Not Downloaded")

# ---------------- Q12 ----------------
driver.get("https://demowebshop.tricentis.com")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Books").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()
driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[2]").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Shopping cart").click()
products = driver.find_elements(By.XPATH, "//td[@class='product']/a")
print("Q12:", "2 products added" if len(products) == 2 else "Wrong count")

# ---------------- Q13 ----------------
driver.get("https://demowebshop.tricentis.com")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Books").click()
time.sleep(3)

books = driver.find_elements(By.XPATH, "//div[@class='product-item']")
for b in books:
    price = float(b.find_element(By.CLASS_NAME, "price").text.replace("$", ""))
    if price < 20:
        b.find_element(By.XPATH, ".//input[@value='Add to cart']").click()
        time.sleep(1)

print("Q13 done")

driver.quit()
