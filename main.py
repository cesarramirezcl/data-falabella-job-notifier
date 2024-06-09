from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, to_email, from_email, password):
    # Create the email headers
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)

    # Quit the SMTP server
    server.quit()


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Add headless mode
    chrome_options.add_argument("--no-sandbox")  # Add no-sandbox option
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Specify the Chrome binary location

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the website
        driver.get("https://muevete.falabella.com/explorar")

        # Wait for the page to fully load
        time.sleep(5)

        # Locate and interact with elements
        input_element = driver.find_element(By.ID, "formSearch")
        input_element.clear()
        input_element.send_keys("data")

        pais_element = driver.find_element(By.ID, "react-select-6-input")
        pais_element.click()
        pais_element.send_keys("c")
        pais_element.send_keys(Keys.RETURN)

        input_element.submit()

        time.sleep(5)

        # Collect job elements
        job_elements = driver.find_elements(By.CLASS_NAME, "card-body")
        body = ""

        for i, element in enumerate(job_elements, start=1):
            try:
                lines = element.text.split('\n')
                job_title = lines[0]
                job_link = driver.find_element(
                    By.XPATH, f'//*[@id="root"]/div/div[3]/div/div/div[2]/div[{i}]/a').get_attribute("href")
                job_date = lines[-1]
                body += f"{job_title} {job_link}\n{job_date}\n\n"
            except Exception as e:
                print(f"Error processing job element {i}: {e}")

        # Email details
        subject = "Falabella Data Jobs"
        to_email = "@gmail.com"
        from_email = "@gmail.com"
        password = "************"  # Use an App Password if you have 2FA enabled

        # Send the email
        send_email(subject, body, to_email, from_email, password)
    finally:
        # Ensure the driver quits even if an error occurs
        driver.quit()


if __name__ == '__main__':
    main()
