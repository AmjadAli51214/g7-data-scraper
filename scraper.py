import asyncio
from playwright.async_api import async_playwright

async def run_scraper():
    async with async_playwright() as p:
        # Launch browser in 'headless' mode (no visible window)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("Navigating to test site...")
        await page.goto("https://books.toscrape.com/")
        
        # Get the title of the page
        title = await page.title()
        print(f"Successfully reached: {title}")
        
        # Take a screenshot to prove it worked
        await page.screenshot(path="screenshot.png")
        print("Screenshot saved as screenshot.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scraper())