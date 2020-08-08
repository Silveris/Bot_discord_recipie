# binging scraper
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import dont_add


def scrape_binging():
    # returns a list of dicts for the binging with babish website
    # does not load into db. makes the variable for you to load
    
    print('scraping Binging With Babish for current recipes')
    # base recipe page scraper
    # geiing the urls of all the recipies

    # gets html from binging recipe page using a chrome browser
    # makes soup using the html
    print('getting the base list of urs')
    
    url = 'https://www.bingingwithbabish.com/recipes'
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # using the soup to get the urls list
    recipe_url_raw_info_soup = soup.find('div', class_='site-wrapper').find('div', class_='recipe-row').find_all('div', class_='recipe-col')
    recipe_urls = []

    # loops through and appends the urls to a list
    for recipe in recipe_url_raw_info_soup:
        recipe_url = recipe.a['href']
        recipe_urls.append(recipe_url)

    # makes the empty recipe list
    list_of_recipes = []
    url_base = 'https://www.bingingwithbabish.com'
    
    print('looping through the urls and getting recipes')

    for url_end in recipe_urls:
        # makes the target url
        url = url_base + url_end
        print(f'getting html from {url}')

        # opens the browser to get the html
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        
        print('attempting to find data')

        # the bits we want
        recipe_title = soup.find('div', class_='site-wrapper').find('div', class_='page-title-wrapper').text.replace('\n', '').strip()
        recipe_description = soup.find('div', class_='site-wrapper').find('div', class_='entry-content').h2.text
        ingredents_list_html = soup.find('div', class_='site-wrapper').find('div', class_='entry-content').ul.find_all('li')
        instructions_list_html = soup.find('div', class_='site-wrapper').find('div', class_='entry-content').ol.find_all('li')

        # gets the specific ingredents in the format we want
        ingredents = []
        for item in ingredents_list_html:
            ingredents.append(item.text.replace('\xa0', ''))

        # gets the specific steps in the format we want while indexing them
        steps = []
        i = 1
        for step in instructions_list_html:
            trimmed = step.text.replace('\xa0', '')
            instruction = f'{i}. {trimmed}'
            steps.append(instruction)
            i += 1
            
        print('making recipe dict')

        # loads the recipe dict
        recipe = {
            'Title' : recipe_title
            ,'Author' : 'Babish'
            ,'Url' : url
            ,'Description' : recipe_description
            ,'Ingredents' : ingredents
            ,'Steps' : steps
        }
        print('appending recipe to the list')

        list_of_recipes.append(recipe)
    print('Binging Scraping Complete')
    
    return list_of_recipes


