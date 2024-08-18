from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def automate_purchase(url, selected_size):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the provided URL
    driver.get(url)
    time.sleep(5)  # Wait for the page to load (you may need to adjust this)

    try:
        # Select the desired size
        size_select = driver.find_element(By.ID, 'size')  # Assuming size selection dropdown has id='size'
        size_select.select_by_visible_text(selected_size)

        # Click on the 'Add to Cart' button (assuming the button has class='btn-add-to-cart')
        add_to_cart_button = driver.find_element(By.CLASS_NAME, 'btn-add-to-cart')
        add_to_cart_button.click()
        time.sleep(3)  # Wait for the item to be added to the cart

        # Navigate to the cart page
        driver.get('https://shop.palaceskateboards.com/cart')
        time.sleep(3)  # Wait for the cart page to load

        # Proceed to checkout (assuming the button has class='checkout')
        checkout_button = driver.find_element(By.CLASS_NAME, 'checkout')
        checkout_button.click()

        # Optionally, automate filling out the checkout form (name, address, etc.)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    url = input("Enter the URL of the Shopify product you want to purchase: ")
    selected_size = input("Enter the size of the product you want to purchase: ")
    automate_purchase(url, selected_size)
