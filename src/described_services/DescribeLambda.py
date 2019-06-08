import boto3

from src import Describe


class DescribeLamda(Describe):

    def extract_contents(self):
        """
        取得したDescribe変数を、JSON情報からfilterして、返す
        Json形式から、md形式に出力する
        :return:
        :rtype: dict
        """
    pass