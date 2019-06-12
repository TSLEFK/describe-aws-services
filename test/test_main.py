from src.described_services.DescribeEc2 import DescribeEc2

from src.main import \
    get_json_path, read_setting, \
    get_descibe_class


def test_get_json_path():

    assert_default_path = get_json_path([])

    assert assert_default_path == "config/services.json"


def test_read_setting():

    json_path = "/Users/takutokaji/Documents/describe-aws-services/test/config/test_services.json"

    json_data = read_setting([json_path])

    assert_dictionary = {
        "ec2": {
            "arn": [
                "arn:aws:ec2:AAA"
            ],
            "items": [
                "instance-name"
            ]
        }
    }

    assert json_data == assert_dictionary


def test_get_descibe_class():
    actual_object =  get_descibe_class("ec2")

    assert isinstance(actual_object, DescribeEc2)
