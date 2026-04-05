import os
import requests
import csv

# 1. 사장님의 구글 시트 주소 (데이터 원천)
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv"

# 2. 개별 명함(HTML) 템플릿
def get_template(item, id):
    name = item[3].strip() if len(item) > 3 else "Unknown"
    maker = item[1].strip() if len(item) > 1 else "Unknown"
    series = item[2].strip() if len(item) > 2 else "Unknown"
    img = item[8].split(',')[0].strip() if len(item) > 8 else "mascot"
    
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} - 피규어 박물관</title>
  <meta name="description" content="{series} 시리즈의 명작 {name} ({maker}). 피규어 박물관에서 확인하세요.">
  <meta property="og:title" content="{name} - 피규어 박물관">
  <meta property="og:image" content="https://bosswise.github.io/figure-DB/images/{img}.jpg">
  <link rel="canonical" href="https://bosswise.github.io/figure-DB/items/{id}.html">
  <script>window.location.href = '/?id={id}';</script>
</head>
<body style="background:#fdfbf9; text-align:center; padding-top:100px; font-family:sans-serif;">
  <h1>{name}</h1>
  <p>피규어 박물관 정문으로 안내하고 있습니다...</p>
  <a href="/?id={id}">클릭하여 즉시 이동</a>
</body>
</html>"""

# 3. 실행 로직
def run():
    print("🚀 구글 시트에서 데이터를 가져오는 중...")
    response = requests.get(CSV_URL)
    response.encoding = 'utf-8'
    
    if response.status_code != 200:
        print("❌ 데이터를 가져오지 못했습니다. 주소를 확인해주세요.")
        return

    lines = response.text.splitlines()
    reader = csv.reader(lines)
    next(reader) # 헤더 건너뛰기

    # items 폴더 생성
    if not os.path.exists('items'):
        os.makedirs('items')
        print("📂 /items 폴더를 생성했습니다.")

    count = 0
    for idx, row in enumerate(reader):
        if len(row) > 8 and row[8]: # 이미지가 있는 행만 생성
            file_path = os.path.join('items', f"{idx}.html")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(get_template(row, idx))
            count += 1
            if count % 500 == 0:
                print(f"📦 {count}개 명함 제작 중...")

    print(f"✅ 완료! 총 {count}개의 HTML 명함이 /items 폴더에 담겼습니다!")

if __name__ == "__main__":
    run()