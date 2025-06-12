import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
def login(driver, username_value, password_value):
    driver.get("https://www.saucedemo.com/")
    id_input = "user-name"
    id_password = "password"
    id_btn = "login-button"
    element_input = driver.find_element(By.ID, id_input)
    driver.find_element(By.ID, "user-name").clear()
    element_input.send_keys(username_value)
    element_password = driver.find_element(By.ID, id_password)
    driver.find_element(By.ID, "password").clear()
    element_password.send_keys(password_value)
    element_btn=driver.find_element(By.ID, id_btn)
    element_btn.click()
    return True
def get_products(driver):
    try:
        class_name_value = "inventory_item_name"
        class_price_value = "inventory_item_price"
        name_elements = driver.find_elements(By.CLASS_NAME, class_name_value)
        price_elements = driver.find_elements(By.CLASS_NAME, class_price_value)
        return [(name_product.text, price_product.text) for name_product, price_product in zip(name_elements, price_elements)]
    except Exception as error:
        print("Không thể lấy sản phẩm:", error)
        return []
def main():
    usernames_array = [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user"
    ]
    password = "secret_sauce"
    all_products = []
    for username in usernames_array:
        print(f"Đang đăng nhập với tài khoản: {username}")
        driver = webdriver.Firefox()
        try:
            login(driver, username, password)
            products = get_products(driver)
            for name, price in products:
                all_products.append({
                    "Tên người dùng": username,
                    "Tên sản phẩm": name,
                    "Giá": price
                })
        except Exception as error:
            print(f"Lỗi với tài khoản {username}: {error}")
        finally:
            driver.quit()
    if all_products:
        df_all_product = pd.DataFrame(all_products)
        df_all_product.to_excel("Products_All.xlsx", index=False)
        print("Đã lưu file: Products_All.xlsx")
    else:
        print("Không có sản phẩm nào được lưu.")
if __name__ == "__main__":
    main()
