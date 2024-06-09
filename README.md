# Falabella Job Scraper and Email Notifier

This project is a Python script that uses Selenium to scrape job listings from the Falabella website and sends the results via email.

## Features

- Headless web scraping using Selenium
- Searches for data-related jobs on the Falabella website
- Sends job listings via email using SMTP

## Prerequisites

- Python 3.7+
- Google Chrome
- ChromeDriver
- Gmail account for sending emails (with App Password if 2FA is enabled)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/falabella-job-scraper.git
   cd falabella-job-scraper
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Download and install ChromeDriver if you haven't already. Make sure the ChromeDriver version matches your installed version of Google Chrome.

## Configuration

Update the following details in the `main()` function of the script:

- `to_email`: The recipient email address.
- `from_email`: The sender email address.
- `password`: The sender email's app password (if 2FA is enabled) or regular password.

## Usage

Run the script:

```bash
python main.py
```

The script will:
- Open the Falabella website.
- Search for data-related jobs.
- Collect job listings.
- Send the job listings to the specified email address.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [Webdriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager)
