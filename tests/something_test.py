import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMassages

def test_getting_posts():
    resource = requests.get(url=SERVICE_URL)
    received_posts = resource.json()

    assert resource.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMassages.WRONG_ELEMENT_COUNT.value
    #print(resource.json())