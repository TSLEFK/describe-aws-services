import boto3

from src.Describe import Describe


class DescribeLambda(Describe):

    def __init__(self):
        super().__init__('lambda')

    def describe(self):
        super().describe()

    def extract_contents(self):
        """
        取得したDescribe変数を、JSON情報からfilterして、返す
        Json形式から、md形式に出力する
        :return:
        :rtype: dict
        """
        pass