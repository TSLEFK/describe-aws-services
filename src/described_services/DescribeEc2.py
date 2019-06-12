from src.Describe import Describe


class DescribeEc2(Describe):

    def __init__(self):
        super().__init__("ec2")
        self.instances = []

    def describe(self):
        response = self.client.describe_instances()
        self.instances = response["Reservations"]

    def extract_contents(self):
        """
        取得したDescribe変数を、JSON情報からfilterして、返す
        Json形式から、md形式に出力する
        :return:
        :rtype: dict
        """
        pass
