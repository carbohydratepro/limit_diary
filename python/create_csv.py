import csv
from faker import Faker
import random
from datetime import datetime
from transformers import T5Tokenizer, AutoModelForCausalLM
import mojimoji
import re
from topics_data import topic


def createData(tablename, debug=False, run=False):
    def users():
        # 名前のリストを生成
        faker = Faker()
        names = [faker.name() for _ in range(100)]
        random.shuffle(names)

        # 趣味のリスト
        hobbies = ['reading', 'writing', 'drawing', 'cooking', 'playing sports', 'traveling', 'watching movies', 'listening to music']

        # データのリストを作成
        data = [] #name, password, email, introduction, created_at, updated_at
        for i, name in enumerate(names):
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
            password = "password"
            email = name.replace(" ", ".")+"@gmail.com"
            hobby = random.choice(hobbies)
            introduction = f"My name is {name} and I enjoy {hobby}."

            data.append([name, password, email, introduction, formatted_now, formatted_now])

        return data

    def blogs():
        # t.string "title"
        # t.text "body"
        # t.integer "user_id"
        # t.datetime "created_at", null: false
        # t.datetime "updated_at", null: false

        # textを全角にして返す関数
        def to_full_width(text):
            return mojimoji.zen_to_han(text, kana=False)

        # target以前の文字列とtargetを削除する関数
        def delete_until_string(string, target):
            pattern = re.compile('.*?(' + re.escape(target) + ')')
            return re.sub(pattern, r'\1', string).replace(target, '')

        # topics_data.pyに格納してあるデータを読み込み
        topics = topic()

        # データのリストを作成
        data = [] #title, body, user_id, created_at, updated_at

        # トークナイザーとモデルの準備
        tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
        model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")

        # データを生成する。機械学習を用いているため結構時間かかる。
        for i in range(300):
            if (i+1) % 10 == 0:
                print("-----------------", i+1, "/ 300", "-----------------")
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
            user_id = random.randint(0, 100)

            # gpt-2モデルを使用して文章を生成
            # 接頭辞（Prefix）
            PREFIX_TEXT = random.choice(topics)

            # 推論
            input = tokenizer.encode(PREFIX_TEXT, return_tensors="pt")
            output = model.generate(input, do_sample=True, max_length=120, num_return_sequences=1)

            title = PREFIX_TEXT
            content = to_full_width(tokenizer.batch_decode(output)[0])
            content = delete_until_string(content, '</s>')

            data.append([title, content[0:120], user_id, formatted_now, formatted_now])

        return data


    def create():
        if tablename == "users":
            data = users()
        elif tablename == "blogs":
            data = blogs()


        # CSVファイルを書き込みモードで開く
        if debug:
            print(data[0])
        else:
            with open(f'{tablename}.csv', mode='w', newline='', encoding='utf-8') as file:

                # csv.writerオブジェクトを作成
                writer = csv.writer(file)

                # データを書き込む
                writer.writerows(data)

    if run:
        create()



def main():
    tablenames = [["users", True, False],
                   ["blogs", False, True]
                  ]
    for tablename, debug, run in tablenames:
        createData(tablename, debug, run)

if __name__ == "__main__":
    main()