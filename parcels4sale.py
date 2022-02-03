from requests import Session

url = 'https://nft-api.decentraland.org/v1/nfts'

results_per_page = 24
page_count = 0 * results_per_page
parcel_num = 0

loop_exit = False

while loop_exit == False:

  parameters = {
  'first': results_per_page,
  'skip': page_count, 
  'sortBy': 'recently_listed', #sortBy: cheapest, recently_listed, recently_sold, newest, name
  'category': 'parcel',
  'isOnSale': 'true',
  } 

  session = Session()
  response = session.get(url, params=parameters)
  results = response.json()
  
  while parcel_num != 24:

    try:
      x_coord = results['data'][parcel_num]['nft']['data']['parcel']['x']
      y_coord = results['data'][parcel_num]['nft']['data']['parcel']['y']
      print('x: ' + x_coord + '\ny: ' + y_coord + '\n')
    
    except IndexError:
      print("List Complete!")
      loop_exit = True
      break

    parcel_num += 1

  page_count += results_per_page
  parcel_num = 0