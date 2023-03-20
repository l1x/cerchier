from sonic import IngestChannel, SearchChannel, ControlChannel


def connect():
    try:
        return SearchChannel("localhost:1491", "SecretPassword")
    except Exception as ex:
        return None


querycl = connect()

if querycl:
    print(querycl.ping())
    print(querycl.query("wiki", "articles", "for"))
    print(querycl.query("wiki", "articles", "love"))
    print(querycl.suggest("wiki", "articles", "hell"))
else:
    print("fukk")
