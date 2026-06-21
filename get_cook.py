import requests

def get_cook_url(bzid):
    durl = "https://buzzheavier.com/api/fs/13n9a1y85c2x"
    head = {
        'Authorization': f'Bearer {bzid}'
    }
    response = requests.get(durl, headers=head)
    response.raise_for_status()
    data = response.json()
    for item in data["data"]["children"]:
        if item["name"] == "cookies.txt":
            print("get_cook_url ok!")
            return f"https://ts.buzzheavier.com/d/{item["id"]}"
    raise "Not Found cookies.txt"

def download_cook(bzid):
    url = get_cook_url(bzid)
    head = {
        'Authorization': f'Bearer {bzid}'
    }
    with requests.get(url, headers=head, stream=True) as response:
        response.raise_for_status()
        
        with open("cookies.txt", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
    
    print("download_cook ok!")