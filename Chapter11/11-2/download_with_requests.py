import requests


# 11.2.1 requests.get()関数を用いてWebページをダウンロードする
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))

print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

# 11.2.2 エラーをチェックする
res = requests.get("http://inventwithpython.com/page_that_does_not_exist")
try:
    res.raise_for_status()
except Exception as exc:
    print("問題あり： {}".format(exc))

# 11.2.3 ダウンロードしたファイルをハードドライブに保存する
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
play_file = open("RomeoAndJulient.txt", "wb")
for chunk in res.iter_content(100000):
    play_file.write(chunk)
play_file.close()
