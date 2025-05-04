# Scrapy Job Scraper

A simple Scrapy spider to scrape job listings from the Greenhouse job board.

## Prerequisites

Before running the project, make sure you have Python 3.8+ and **Scrapy** installed on your machine.

- **Python**: [Download Python](https://www.python.org/downloads/)
- **Scrapy**: To install Scrapy, you can run the following command:

    ```bash
    pip install scrapy
    ```

## Install Dependencies

1. Clone the repository (if applicable):

    ```bash
    git clone https://github.com/yourusername/scrapy-job-scraper.git
    cd scrapy-job-scraper
    ```

2. If you haven't installed Scrapy yet, do so by running:

    ```bash
    pip install scrapy
    ```
## Spider Structure

- `spiders/behavox_spider.py`: The Scrapy spider for scraping job listings from Greenhouse job boards.
- `job_list.json`: Sample output file for job listings (can be replaced by any custom file name).

## How to Use
### 1. Run the Spider

To run the spider, simply execute the following command in the project directory:

```bash
scrapy crawl behavox_spider -o output/job_list.json
