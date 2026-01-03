<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관 v3.1</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    :root { --primary-color: #fab005; --bg-color: #f7f3f0; --text-dark: #2d2926; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 헤더 디자인 */
    .main-title-area { padding: 60px 0; text-align: center; }
    .header-mascot { width: 180px; height: 180px; border-radius: 50%; background: white; padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .main-title-area h1 { font-weight: 900; font-size: 4rem; color: var(--text-dark); margin: 10px 0; }
    .stats-text { color: #8c847d; font-size: 1.1rem; }

    /* 📌 책갈피(Bookmark) 스타일 필터 */
    header { background: rgba(45, 41, 38, 0.98); padding: 20px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
    .bookmark-container { max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding: 0 20px; }
    .category-row { display: flex; align-items: center; gap: 15px; background: rgba(255,255,255,0.05); padding: 10px 15px; border-radius: 12px; }
    .main-label { color: var(--primary-color); font-weight: 900; min-width: 100px; font-size: 0.9rem; border-right: 1px solid #555; }
    .sub-btns { display: flex; flex-wrap: wrap; gap: 8px; }
    
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 6px 15px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; transition: 0.3s; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }

    /* 그리드 및 카드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 35px; }
    .card { background: white; border-radius: 25px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.03); cursor: pointer; transition: 0.3s; }
    .card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
    .img-box { width: 100%; height: 320px; background: #fff; display: flex; align-items: center; justify-content: center; padding: 20px; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 25px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.3rem; font-weight: 800; color: var(--text-dark); margin-bottom: 10px; }
    .tag-wrap { display: flex; justify-content: center; gap: 5px; flex-wrap: wrap; }
    .tag { font-size: 0.75rem; background: #f0f0f0; color: #777; padding: 3px 10px; border-radius: 15px; }

    /* 모달 */
    .modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 1000; justify-content: center; align-items: center; }
    .modal-content { background: white; width: 90%; max-width: 1000px; border-radius: 30px; padding: 40px; position: relative; }
    .close-btn { position: absolute; top: 20px; right: 30px; font-size: 2rem; cursor: pointer; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1>피규어 박물관</h1>
    <p id="total-stats" class="stats-text">데이터 로딩 중...</p>
  </div>

  <header>
    <div class="bookmark-container" id="filterMenu"></div>
  </header>

  <div class="container">
    <div id="figureGrid" class="grid"></div>
  </div>

  <div id="detailModal" class="modal" onclick="this.style.display='none'">
    <div class="modal-content" onclick="event.stopPropagation()">
      <span class="close-btn" onclick="document.getElementById('detailModal').style.display='none'">&times;</span>
      <div id="modalBody"></div>
    </div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    let allData = [];

    async function init() {
      try {
        const response = await fetch(csvURL);
        const text = await response.text();
        
        // CSV 파싱 로직
        const rows = text.split('\n').map(row => {
          const matches = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
          return matches ? matches.map(m => m.replace(/^"|"$/g, '')) : [];
        });

        // 헤더 제외 데이터 (8번 열에 이미지 이름이 있는 것만 필터)
        allData = rows.slice(1).filter(r => r[8]);

        document.getElementById('total-stats').innerText = `Total ${allData.length} Masterpieces`;

        // 책갈피 메뉴 생성 (K열: 10번, B열: 2번)
        const menuMap = {};
        allData.forEach(item => {
          const k = item[10] || "ETC";
          const b = item[2] || "ETC";
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
      } catch (e) {
        console.error(e);
        document.getElementById('total-stats').innerText = "데이터를 불러오지 못했습니다.";
      }
    }

    function render(data) {
      const grid = document.getElementById('figureGrid');
      grid.innerHTML = data.map(item => {
        // 1. 이름 결정: M열(12번) 우선, 없으면 D열(3번)
        const finalName = (item[12] && item[12].trim()) ? item[12] : item[3];
        const firstImg = item[8].split(',')[0].trim();
        const imgPath = `${imageBaseURL}${encodeURIComponent(firstImg)}.jpg`;

        return `
          <div class="card" data-series="${item[2]}">
            <div class="img-box"><img src="${imgPath}" onerror="this.src='https://placehold.co/400x400?text=No+Image'"></div>
            <div class="content">
              <div class="char-name">${finalName}</div>
              <div class="tag-wrap">
                <span class="tag">#${item[1]}</span>
                <span class="tag">#${item[2]}</span>
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
