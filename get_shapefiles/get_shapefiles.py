import requests
import zipfile
import os
import us


"""
returns a list of all the urls from the census webiste to
downlaod shapefiles
"""
def get_shapefile_urls():
    states = us.states.mapping('fips','name')

    for fips,name in states.items():
        print(name)
        if fips:
            url ='https://www2.census.gov/geo/tiger/TIGER2010/STATE/2010/tl_2010_'+fips +'_state10.zip'

            target_path = name + ".zip"

            response = requests.get(url, stream=True)
            handle = open(target_path, "wb")
            for chunk in response.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunks
                    handle.write(chunk)
            handle.close()

            with zipfile.ZipFile(target_path, 'r') as zip_ref:
                zip_ref.extractall("../data/"+name)
            os.remove(target_path)

get_shapefile_urls()





