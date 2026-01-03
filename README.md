<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 [강력 차단] 좌측 상단 figure-DB 등 모든 유령 텍스트/코드 제거 */
    * :not(.museum-content):not(script):not(style) { border: none; }
    header, footer, .title, .site-header, .site-footer { display: none !important; visibility: hidden !important; }
    body > b, body > p, body > span { display: none !important; }

    :root { --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg); margin: 0; padding: 0; overflow-x: hidden; }

    /* 🏛️ 전체 레이아웃 (유령 텍스트 차단을 위한 래퍼) */
    .museum-content { position: relative; z-index: 1; display: block; }

    .main-title-area { padding: 60px 0 30px; text-align: center; }
    .header-mascot { width: 160px; height: 160px; border-radius: 50%; background: white; padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    
    /* 제목 클릭 시 홈으로 */
    .museum-title { 
      font-weight: 900; font-size: 3.5rem; color: var(--dark); 
      margin: 15px 0 5px; cursor: pointer; display: inline-block;
      text-decoration: none; border: none;
    }

    /* 📌 [솔루션] 가로 스크롤형 책갈피 필터 */
    .sticky-filter { 
      background: #2d2926; padding: 15px 0; 
      position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 20px rgba(0,0,0,0.3); 
    }
    .bookmark-container { max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; gap: 10px; padding: 0 20px; }
    
    .category-row { 
      display: flex; align-items: center; gap: 15px; 
      background: rgba(255,255,255,0.05); padding: 8px 15px; border-radius: 12px;
      overflow: hidden; /* 영역 밖 숨김 */
    }
    .main-label { color: var(--primary); font-weight: 900; min-width: 90px; font-size: 0.85rem; border-right: 1px solid #555; }
    
    /* 중단원 버튼들 가로 스크롤 처리 */
    .sub-btns-scroll { 
      display: flex; gap: 8px; overflow-x: auto; white-space: nowrap; 
      padding-bottom: 5px; scrollbar-width: none; /* 파이어폭스 휠 숨김 */
    }
    .sub-btns-scroll::-webkit-scrollbar { display: none; /* 크롬/사파리 휠 숨김 */ }
    
    .filter-btn { 
      background: #45403c; color: #a5a09c; border: none; padding: 6px 16px; 
      border-radius: 20px; cursor: pointer; font-size: 0.85rem; flex-shrink: 0; /* 버튼 크기 유지 */
    }
    .filter-btn.active { background: var(--primary); color: #1a1a1a; font-weight: 800; }

    /* 그리드 및 카드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; }
    .card { background: white; border-radius: 25px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.03); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-10px); }
    .img-box { width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; padding: 15px; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 20px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.2rem; font-weight: 800; color: var(--dark); margin-bottom: 8px; }
  </style>
</head>
<body>

<div class="museum-content">
  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
    <p id="total-stats" style="color:#8c847d;">컬렉션 동기화 중...</p>
  </div>

  <div class="sticky-filter">
    <div class="bookmark-container" id="filterMenu"></div>
  </div>

  <div class="container">
    <div id="figureGrid" class="grid"></div>
  </div>
</div>

<script>
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

  async function init() {
    try {
      const response = await fetch(csvURL);
      const text = await response.text();
      const rows = text.split(/\r?\n/).map(row => {
        const m = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
        return m ? m.map(v => v.replace(/^"|"$/g, '').trim()) : [];
      });

      const allData = rows.slice(1).filter(r => r[8]);
      document.getElementById('total-stats').innerText = `Total ${allData.length} Masterpieces`;

      const menuMap = {};
      allData.forEach(item => {
        const k = item[10] || "ETC"; const b = item[2] || "ETC";
        if (!menuMap[k]) menuMap[k] = new Set();
        menuMap[k].add(b);
      });

      const filterMenu = document.getElementById('filterMenu');
      filterMenu.innerHTML = `<div class="category-row"><button class="filter-btn active" onclick="filterBy('all', this)">전체보기</button></div>`;

      for (const [cat, seriesSet] of Object.entries(menuMap)) {
        const row = document.createElement('div');
        row.className = 'category-row';
        let html = `<span class="main-label">${cat.toUpperCase()}</span><div class="sub-btns-scroll">`;
        seriesSet.forEach(s => { html += `<button class="filter-btn" onclick="filterBy('${s}', this)">${s}</button>`; });
        row.innerHTML = html + `</div></div>`;
        filterMenu.appendChild(row);
      }

      const grid = document.getElementById('figureGrid');
      grid.innerHTML = allData.map(item => {
        const name = (item[12] && item[12] !== "") ? item[12] : item[3];
        const imgPath = `${imageBaseURL}${encodeURIComponent(item[8].split(',')[0].trim())}.jpg`;
        return `
          <div class="card" data-series="${item[2]}" onclick="window.open('${imgPath}', '_blank')">
            <div class="img-box"><img src="${imgPath}" loading="lazy" onerror="this.src='https://placehold.co/400x400?text=No+Image'"></div>
            <div class="content">
              <div class="char-name">${name}</div>
              <div style="font-size:0.75rem; color:#aaa;">#${item[1]} #${item[2]}</div>
            </div>
          </div>`;
      }).join('');
    } catch (e) { console.error(e); }
  }

  function filterBy(s, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.card').forEach(c => {
      c.style.display = (s === 'all' || c.dataset.series === s) ? 'block' : 'none';
    });
  }

  init();
</script>
</body>
</html>
