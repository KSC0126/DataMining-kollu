'''libraries importing'''
import requests
from bs4 import BeautifulSoup
import csv

place_details = []

''' printing url of website that have different search letters'''
for i in range(9,10):
    letter = chr(i+88)
    url = "http://www.visitsingapore.com/search.html?q="+letter
    print(url)
    

    ''' Beautiful soup way parsing html '''
    html = requests.get(url).text
    ''' storing in varaible. '''
    soup = BeautifulSoup(html,'html.parser')
    ''' taking the contents of same class name
        then take the text from the h6,h4 tags
        category and name '''
    place = soup.findAll('img',{'class',"search-listing--img"})
    for visit in place:
        visited = visit.findNext('div',{'class':'search-listing--content'})
        category = visit.findNext('h6').text
        name = visit.findNext('h4').text
       
        ''' dictionary for details defined. '''
        place_dict = {}
        place_dict['Category'] = category
        place_dict['Place name'] = name
        ''' All the details are appended to the list'''
        place_details.append(place_dict)

print(place_details)


''' output file returned as csv '''
with open('names.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    #writer.writerow(place_details)
    for each in place_details:
        for key, value in each.items():
            writer.writerow([key, value])    
            
