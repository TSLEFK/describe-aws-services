import logging

from abc import ABCMeta, abstractmethod

import boto3


class Describe(metaclass=ABCMeta):
    service = ''
    client = boto3.session.Session.client

    def __init__(self, service):
        self.service = service
        self.client = self._make_client(service)

    @classmethod
    def _make_client(cls, service):
        """

        :return:
        :rtype: boto3.session.Session.client
        """
        client = boto3.client(service)

        return client

    @abstractmethod
    def describe(self):
        logging.info("%s does not have describe method.", self.service)


    @abstractmethod
    def extract_contents(self):
        """
        取得したDescribe変数を、JSON情報からfilterして、返す
        Json形式から、md形式に出力する
        :return:
        :rtype: dict
        """
        pass
