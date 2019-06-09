from src.main import get_json_path


def test_get_json_path():

    assert_default_path = get_json_path([])

    assert assert_default_path == "config/services.json"


# def test_read_setting():
#
#     json_data = read_setting(["config/test_services.py"])
#
#     assert_dictionary = {
#         "ec2": {
#             "arn": [
#                 "arn:aws:ec2:AAA"
#             ],
#             "items": [
#                 "instance-name"
#             ]
#         }
#     }
#
#     assert json_data == assert_dictionary
