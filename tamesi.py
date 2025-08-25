
from PIL import Image, ImageDraw, ImageFont

# 画像を作成（サイズは任意）
img = Image.new('RGB', (600, 400), color='white')
draw = ImageDraw.Draw(img)

# フォントを指定（環境に応じてパスを調整）
font = ImageFont.truetype("arial.ttf", size=50)

# 描画するテキスト
text = "中央に配置！"

# textbboxでテキストのバウンディングボックスを取得
bbox = draw.textbbox((0, 0), text, font=font)

# 幅と高さを計算
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# 中央座標を計算
image_width, image_height = img.size
x = (image_width - text_width) / 2
y = (image_height - text_height) / 2

# テキストを描画
draw.text((x, y), text, font=font, fill='black')

# 表示または保存
img.show()
# img.save("centered_text.png")



