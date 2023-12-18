import requests


def get_surah_ayah_no(index_no):
    url = f"https://pro.proggamoyquran.com/api/v1/filter/surah&ayat/{index_no}"

    # Make a GET request to the API
    response = requests.get(url)

    ayat_number, surah_number = -1, -1

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()

        # Extract values and save them in variables
        ayat_number = data['data']['ayatNumber']
        surah_number = data['data']['surahNumber']

        # Now you can use these variables as needed
        print("Ayat Number:", ayat_number)
        print("Surah Number:", surah_number)
    else:
        # If the request was not successful, print an error message
        print(f"Error: {response.status_code}")

    return surah_number, ayat_number
