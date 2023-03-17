from PIL import Image, ImageDraw, ImageFont
import random
import os

# 保存先ディレクトリを作成
if not os.path.exists('icons'):
    os.mkdir('icons')

# アイコンのサイズ
icon_size = (100, 100)

# ランダムなアルファベット文字列の生成
def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(length))

# 100個のアイコンを生成して保存
for i in range(100):
    # ランダムな色の生成
    color = tuple(random.randint(0, 255) for _ in range(3))

    # アイコン画像の作成
    icon = Image.new('RGB', icon_size, color)

    # テキストの作成
    text = random_string(1)

    # フォントの作成
    font = ImageFont.truetype('arial.ttf', 50)

    # テキストの描画
    draw = ImageDraw.Draw(icon)
    text_width, text_height = draw.textsize(text, font)
    draw.text(((icon_size[0] - text_width) / 2, (icon_size[1] - text_height) / 2), text, font=font, fill=(255, 255, 255))

    # 画像を保存
    filename = f'icons/icon_{i}.png'
    icon.save(filename)