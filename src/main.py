import os
import sys
import json
import logging

from described_services.DescribeEc2 import DescribeEc2
from described_services.DescribeLambda import DescribeLambda

log_formatter = "%(asctime)s [%(levelname)s] " \
                "(l.%(lineno)d) <%(funcName)s> %(message)s"
logging.basicConfig(level=os.getenv("LOGGER_LEVEL", "INFO"), format=log_formatter)


def main(argv):
    json_data = read_setting(arguments=argv)

    for service in json_data:
        describe_service = get_descibe_class(service)
        describe_service.describe()
        describe_service.extract_contents()


def read_setting(arguments):

    try:
        with open(get_json_path(arguments), "r") as file:
            json_data = json.load(file)
    except json.JSONDecodeError as e:
        logging.error(e)

    return json_data


def get_json_path(arguments):
    if len(arguments) < 1:
        logging.info("No arguments")
        return "config/services.json"

    logging.info("Using json path is {}".format(arguments[0]))
    return arguments[0]


def get_descibe_class(service):
    describe_objects = {
        "ec2": DescribeEc2,
        "lambda": DescribeLambda
    }

    return describe_objects[service]()


if __name__ == '__main__':
    main(sys.argv[1:])
