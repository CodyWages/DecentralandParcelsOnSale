from requests import Session

# API URL for NFT's
url = 'https://nft-api.decentraland.org/v1/nfts'

# A max of 24 results can be retrieved per api query.
results_per_page = 24

# Replace 0 with number of pages you would like to skip, or replace all with an exact integer if needed.
page_count = 0 * results_per_page 

# Index variable for the nested loop.
parcel_num = 0

# Loop condition
loop_exit = False

# Loop to iterate page numbers
while loop_exit == False:

  parameters = {
  'first': results_per_page,
  'skip': page_count, 
  'sortBy': 'recently_listed', # sortBy: cheapest, recently_listed, recently_sold, newest, name
  'category': 'parcel',
  'isOnSale': 'true',
  } 

  # Request info from API, and stores as JSON.
  session = Session()
  response = session.get(url, params=parameters)
  results = response.json()
  
  # Loop to iterate parcels in a page.
  while parcel_num != 24:

    # Indexes parcel coordinates and prints them.
    try:
      x_coord = results['data'][parcel_num]['nft']['data']['parcel']['x']
      y_coord = results['data'][parcel_num]['nft']['data']['parcel']['y']
      print('x: ' + x_coord + '\ny: ' + y_coord + '\n')
    
    # A print statement that indicates the parcel list has been completed.
    except IndexError:
      print("List Complete!")
      loop_exit = True # Exit main loop
      break

    # Increments loop.
    parcel_num += 1
  
  # Increments loop.
  page_count += results_per_page
  parcel_num = 0