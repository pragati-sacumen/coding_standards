""" Test file for task2_ """
import pytest
import requests
from typing import Any, List, Dict
from  task2 import get_data

# def test_get_data_success():
#     """tests url passed to the function """
#     result = get_data("USER DATA", 

#                    "https://slack.com/api/users.list",
#                     {"Authorization": "Bearer xoxp-2815913105940-2806947464294-2890441256599-332c14130c781ff69d0ffaf4aba44207"}
#                     ,2)
#     assert result.status_code == 200 # this will be accourding to the method being tested else will through error 


# def test_get_data_mocks():
#     mocker.patch("request.get", mock_api_success)
#     result = get_data("USER DATA"," url","key",2)
#     assert result.status_code == 200
@pytest.mark.vcr
def test_get_data_vcr():
    """testing url with vcr"""
    response = get_data("USER DATA", "https://slack.com/api/users.list",{"Authorization": "Bearer xoxp-2815913105940-2806947464294-2890441256599-332c14130c781ff69d0ffaf4aba44207"},2)
    assert response == 200

