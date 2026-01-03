<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관 v3.0</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 기존 관장님 디자인 유지 + 책갈피 스타일 추가 */
    :root { --primary-color: #fab005; --bg-color: #f7f3f0; --text-dark: #2d2926; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; }

    /* 헤더 캐릭터 영역 */
    .main-title-area { padding: 60px 0; text-align: center; }
    .header-mascot { width: 180px; height: 180px; border-radius: 50%; background: white; padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .main-title-area h1 { font-weight: 900; font-size: 4rem; color: var(--text-dark); margin: 10px 0; }

    /* 📌 책갈피(Bookmark) 디자인 필터 */
    header { background: rgba(45, 41, 38, 0.98); padding: 20px 0; position: sticky; top: 0; z-index: 100; }
    .bookmark-container { max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; }
    .category-row { display: flex; align-items: center; gap: 15px; background: rgba(255,255,255,0.05); padding: 8px 15px; border-radius: 12px; }
    .main-label { color: var(--primary-color); font-weight: 900; min-width: 90px; font-size: 0.9rem; border-right: 1px solid #555; }
    .sub-btns { display: flex; flex-wrap: wrap; gap: 8px; }
    
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 6px 15px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; transition: 0.3s; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }

    /* 그리드 및 카드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 35px; }
    .card { background: white; border-radius: 25px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.03); cursor: pointer; transition: 0.3s; }
    .card:hover { transform: translateY(-10px); }
    .img-box { width: 100%; height: 320px; background: #fff; display: flex; align-items: center; justify-content: center; padding: 20px; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 25px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.3rem; font-weight: 800; color: var(--text-dark); margin-bottom: 10px; }
    .tag-wrap { display: flex; justify-content: center; gap: 5px; flex-wrap: wrap; }
    .tag { font-size: 0.75rem; background: #f0f0f0; color: #777; padding: 3px 10px; border-radius: 15px; }

    /* 모달 디자인 유지... (중략) */
    #detailModal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 1000; justify-content: center; align-items: center; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1>피규어 박물관</h1>
    <p id="total-stats" style="color:#8c847d;">컬렉션을 불러오는 중...</p>
  </div>

  <header>
    <div class="bookmark-container" id="filterMenu">
      </div>
  </header>

  <div class="container">
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    // ★★★ 중요: JSON 배포 주소를 여기에 넣으세요! ★★★
    const SHEET_URL = "여기에_JSON_배포_주소_입력"; 
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    let allData = [];

    async function init() {
      const res = await fetch(SHEET_URL);
      allData = await res.json();
      
      document.getElementById('total-stats').innerText = `Total ${allData.length} Masterpieces`;

      // 1. 책갈피 메뉴 생성 (K열: 카테고리, B열: 시리즈 기반)
      const menuMap = {};
      allData.forEach(item => {
        const k = item.category || "ETC";
        const b = item.series || "ETC";
        if (!menuMap[k]) menuMap[k] = new Set();
        menuMap[k].add(b);
      });

      const filterMenu = document.getElementById('filterMenu');
      filterMenu.innerHTML = `<div class="category-row"><button class="filter-btn active" onclick="filterBy('all', this)">전체보기</button></div>`;

      for (const [cat, seriesSet] of Object.entries(menuMap)) {
        const row = document.createElement('div');
        row.className = 'category-row';
        let html = `<span class="main-label">${cat.toUpperCase()}</span><div class="sub-btns">`;
        seriesSet.forEach(s => {
          html += `<button class="filter-btn" onclick="filterBy('${s}', this)">${s}</button>`;
        });
        row.innerHTML = html + `</div></div>`;
        filterMenu.appendChild(row);
      }

      render(allData);
    }

    function render(data) {
      const grid = document.getElementById('figureGrid');
      grid.innerHTML = data.map(item => {
        // ★ 3가지 통합 기능 핵심 로직 ★
        // 1. 이름 결정: M열(display_name) 우선, 없으면 D열(character)
        const finalName = (item.display_name && item.display_name.trim()) ? item.display_name : item.character;
        
        // 2. 이미지 경로
        const firstImg = item.image.split(',')[0].trim();
        const imgPath = `${imageBaseURL}${encodeURIComponent(firstImg)}.jpg`;

        // 3. 카드 및 태그 출력
        return `
          <div class="card" data-series="${item.series}">
            <div class="img-box"><img src="${imgPath}" onerror="this.src='https://placehold.co/400x400?text=No+Image'"></div>
            <div class="content">
              <div class="char-name">${finalName}</div>
              <div class="tag-wrap">
                <span class="tag">#${item.maker}</span>
                <span class="tag">#${item.series}</span>
              </div>
            </div>
          </div>`;
      }).join('');
    }

    function filterBy(series, btn) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.card').forEach(c => {
        c.style.display = (series === 'all' || c.dataset.series === series) ? 'block' : 'none';
      });
    }

    init();
  </script>
</body>
</html>
