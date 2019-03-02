import requests
from bs4 import BeautifulSoup

url = "http://milo-beast506.c9users.io"

def test_home_page():
    print("testing home page")
    response = requests.get(url + "/notes")
    
    assert response.status_code == 200
    assert response.text > ""
    #assert "<HTML>" in response.text.upper()
    
def test_home_page_has_submit_button():
    print("testing home page has submit button")
    response = requests.get(url + "/notes")
    assert "type=\submit\"" in response.text.lower().replace(" ", "")
    soup = BeautifulSoup(response.text, "html.parser")
    inputs = soup.find_all("input")
    for input in inputs:
            print(input, input['type'])
    submit_inputs = [input for input in inputs if input['type'] == "submit"]
    
    
def test_home_page_submits_data_into_list():
    