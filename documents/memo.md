0. --awsprofileでオプションで、awsのprofile名を受け取り、指定できるようにする
1. jsonで、aws のサービス名（botoのclient名）を指定する。
2. arnと取得する値を配列で指定する

```json
{
  "ec2": {
    "arn": [
      "arn:aws:ec2:...."
    ],
    "items": [
      "instance-name"
    ]
  }
}
```

3. profileオプションから、STSでセッションの作成
4. 各サービスにある、describe関数を呼び出す。


# クラス設計
Descibe
- describe() abstract method
- extract_contents() 取得したDescribe変数を、JSON情報からfilterして、返す 
- Json形式から、md形式に出力する

DescribeEC2(Describe)
DescribeLambda(Describe)


