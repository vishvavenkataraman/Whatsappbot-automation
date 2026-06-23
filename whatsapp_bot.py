from playwright.sync_api import sync_playwright
import pandas as pd
import time
from datetime import datetime

contacts = pd.read_excel("contacts.xlsx")

received_data = []

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=1000
    )

    context = browser.new_context()

    page = context.new_page()

    print("Opening WhatsApp Web...")

    page.goto("https://web.whatsapp.com")

    print("Please scan QR Code...")
    input("Press ENTER after login...")

    for index, row in contacts.iterrows():

        name = row["Name"]
        phone = str(row["Phone"])
        message = row["Message"]

        print(f"Sending message to {name}")

        whatsapp_url = (
            f"https://web.whatsapp.com/send?phone={phone}"
            f"&text={message}"
        )

        page.goto(whatsapp_url)

        time.sleep(5)

        try:

            message_box = page.locator('div[contenteditable="true"]').last
            message_box.click()
            message_box.fill(message)
            page.keyboard.press("Enter")
            print(f"Message sent to {name}")

            time.sleep(3)

            messages = page.locator(
                "div.message-in"
            )

            count = messages.count()

            latest_msg = "No incoming message"

            if count > 0:
                latest_msg = messages.nth(
                    count - 1
                ).inner_text()

            received_data.append({
                "Name": name,
                "Phone": phone,
                "Latest Reply": latest_msg,
                "Timestamp":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

            time.sleep(2)

        except Exception as e:

            print(
                f"Failed for {name}: {e}"
            )

    report_name = (
        f"extracted_messages_"
        f"{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    )

    pd.DataFrame(
        received_data
    ).to_excel(
        report_name,
        index=False
    )

    page.screenshot(
        path=f"whatsapp_report_"
             f"{datetime.now().strftime('%Y-%m-%d')}.png",
        full_page=True
    )

    print(
        f"Report saved as {report_name}"
    )

    browser.close()
