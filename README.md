# Webb app UI testing
Example testing harness around a mock ecommerce webapp.  

### Getting Started
- install Python3.8+
- install [ChromeDriver](https://chromedriver.chromium.org/downloads) 
corresponding to your version of Chrome
  - add chromedriver to your PATH
- install dependencies `pip install -r requirements.txt`

### Framework
**driver/** chrome webdriver generator.  
**my_store/** classes which implement a page object model pattern.  
**tests/** sample tests to demonstrate a pattern in working towards better coverage.  
**.env** config file to keep the browser from closing (used for debug purposes / post test run inspections)

### Notes
`test_search_by_category` tests currently fail due to faulty search results when searching by category.  
Resource limitations stop testing from a multi-processed approach.   

### Enhancements
Flush out test cases in the current framework to cover more search, view, and cart functionality.  
Add coverage for:  
 - filter options
 - wishlist feature
 - compare feature
 - product sorting
 - footer links
 - breadcrumb feature
 - contact us form
 - product configuration
 - checkout
 - create account
 - load testing