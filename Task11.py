from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Set up the WebDriver (Ensure ChromeDriver is installed)
driver = webdriver.Chrome()

# Open the target website
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe that contains the draggable and droppable elements
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Locate the draggable (White Rectangle) and droppable (Yellow Rectangle) elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Perform the drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Print confirmation
print("Drag and Drop operation completed successfully!")

# Close the browser
driver.quit()
