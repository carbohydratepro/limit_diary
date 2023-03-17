import csv
from faker import Faker
import random
from datetime import datetime

  # create_table "users", force: :cascade do |t|
  #   t.string "email", default: "", null: false
  #   t.string "encrypted_password", default: "", null: false
  #   t.string "reset_password_token"
  #   t.datetime "reset_password_sent_at"
  #   t.datetime "remember_created_at"
  #   t.datetime "created_at", null: false
  #   t.datetime "updated_at", null: false
  #   t.string "name"
  #   t.text "introduction"
  #   t.string "image"
  #   t.index ["email"], name: "index_users_on_email", unique: true
  #   t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  # end

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


# CSVファイルを書き込みモードで開く
with open('users.csv', mode='w', newline='') as file:

    # csv.writerオブジェクトを作成
    writer = csv.writer(file)

    # データを書き込む
    writer.writerows(data)
