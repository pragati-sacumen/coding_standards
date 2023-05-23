""" Slack Demo File"""
import logging
import requests

logging.basicConfig(
    filename="slack_data.log",
    level=logging.INFO,
    format="[%(asctime)s] ->  %(levelname)s -> %(message)s",
    filemode="w",
)


def get_data(meta_data: str, url: str, key: dict, limit: int) -> None:
    """ Fetches data from the url"""
    try:
        response = requests.get(url, headers=key, params={"limit": limit},timeout=20)
        if response.json()["ok"] is True and response.status_code == 200:
            cursor = response.json()["response_metadata"]["next_cursor"]
            pagination("USER DATA", url, key, 2)
    except Exception as e:
        logging.error(f"{meta_data} Error-> {str(e)}")
    return response.status_code


def pagination(meta_data: str, url: str, key: dict, limit: int) -> None:
    """Handles pagination of the url data"""
    response = requests.get(url, headers=key, params={"limit": limit},timeout=20)
    cursor = response.json()["response_metadata"]["next_cursor"]

    while cursor != "":
        for i in range(limit):
            # logging.info(f"{meta_data} -> {response.json()}")
            logging.info(f"{meta_data} -> {response.json()['members'][i]['id']}")
            logging.info(f"count: {len(response.json()['members'])}")
        try:
            response = requests.get(
                url, headers=key, params={"limit": limit, "cursor": cursor}
                ,timeout=20
            )
            cursor = response.json()["response_metadata"]["next_cursor"]
        except Exception as e:
            logging.error(f"{meta_data} Error-> {str(e)}")
    print(response.status_code)



USER_KEY = {
"Authorization": "Bearer 23445"
}


# group_url = "https://slack.com/api/users.list"
USER_URL = "https://slack.com/api/users.list"

get_data("USER DATA", USER_URL, USER_KEY, 2)
# get_data("GROUP DATA", group_url, group_key,2)

"""
    Comment the function call in the python file while testing that file. 
    Particularly, comment that fuction call which is being tested.
"""
