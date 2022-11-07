from bs4 import BeautifulSoup
import requests
import csv


# Webpage that we are trying to scrape
page = requests.get('https://www.autoblog.com/utica-ny-gas-prices/')

# HTML parser var, this gathers the HTML as text and allows us to parse it as HTML and store
soup = BeautifulSoup(page.content, 'html.parser')

# Accessing the HTML class that contains all the info we are looking for. (PRICE, STATION NAME, ADDRESS, DISTANCE)
shops = soup.find_all('ul', class_='details')

# Defining the name for our csv file to where we will write our scraped data to 
filename = 'GasPriceInfo.csv'

# Opening the file with writting permissons ('w')
f = open(filename,'w')

# Defining our headers for data within our csv file
headers = "PRICE, STATION NAME, ADDRESS, DISTANCE\n" #csv are delimited by newlines

# Writting the headers
f.write(headers)

# looping through the HTML on the webpage
# shops var gathers all the details about each gas station 
for shop in shops:
    
    # since we cannot reach the price class directly we 
    # navigate through the tree to get the required class > looking in the next class > setting the price to variable "price"
    get_price_class = shop.find('li',class_='slab price') 
    get_price = get_price_class.find('data', class_='price')
    price = get_price.text.strip()

    # navigating through the tree to get the required class > looking in the next class > setting the stations name to variable "station"
    get_station_name = shop.find('li', class_='name')
    get_station = get_station_name.find('h4')
    station = get_station.text.strip()

    # navigating through the tree to get the required class > looking in the next class > setting the address to variable "address"
    get_address_class = shop.find('li', class_='name')
    get_address = get_address_class.find('address')
    address = get_address.text.strip()
    
    # navigating through the tree to get the required class > looking in the next class > setting the distance to variable "distance"
    get_distance_class = shop.find('li', class_='dist')
    get_distance = get_distance_class.find('data', class_='distance')
    distance = get_distance.text.strip()


    # Printing the information we scraped to check and see if it is 
    print('Price of Gas: ', price + ' ,','Station Name: ', station + ' ,','Location: ', address + ' ,', 'Distance: ', distance)

    # write to csv file: the product names/prices have commas in them which must be replaced, otherwise they'll be a new column in csv
    f.write(price + "," + station.replace(",", "|") + "," + address.replace(",", "") + "," + distance + "\n")

# close the file
f.close()
print('Gas price info has succesfully been written to csv file!')