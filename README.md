<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 1. 깃허브 기본 텍스트 및 코드 파편 완벽 제거 */
    header[class*="header"], .site-header, .site-footer, .title, b, p:first-of-type { display: none !important; }
    
    :root { 
      --primary-color: #fab005; 
      --bg-color: #f7f3f0; 
      --text-dark: #2d2926; 
      --accent-tag: #ffeaa7;
    }

    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; padding: 0; }

    /* 🖼️ 헤더 & 제목 */
    .main-title-area { padding: 60px 0 40px; text-align: center; }
    .header-mascot { width: 180px; height: 180px; border-radius: 50%; background: white; padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    
    /* 제목 클릭 시 홈으로 */
    .main-title-area h1 { 
      font-weight: 900; font-size: 3.5rem; color: var(--text-dark); 
      margin: 15px 0 5px; cursor: pointer; transition: 0.2s;
      display: inline-block;
    }
    .main-title-area h1:hover { transform: scale(1.05); color: var(--primary-color); }
    .stats-text { color: #8c847d; font-size: 1.1rem; }

    /* 📌 책갈피 필터 (고정 헤더) */
    .sticky-header { 
      background: rgba(45, 41, 38, 0.98); padding: 20px 0; 
      position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 20px rgba(0,0,0,0.2); 
    }
    .bookmark-container { max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding: 0 20px; }
    .category-row { display: flex; align-items: center; gap: 15px; background: rgba(255,255,255,0.05); padding: 10px 15px; border-radius: 12px; }
    .main-label { color: var(--primary-color); font-weight: 900; min-width: 100px; font-size: 0.85rem; border-right: 1px solid #555; text-transform: uppercase; }
    
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 6px 16px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; transition: 0.3s; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }

    /* 🏛️ 전시 그리드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 35px; }
    .card { background: white; border-radius: 25px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.03); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-12px); box-shadow: 0 25px 50px rgba(0,0,0,0.1); }
    .img-box { width: 100%; height: 320px; display: flex; align-items: center; justify-content: center; padding: 20px; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 25px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.3rem; font-weight: 800; color: var(--text-dark); margin-bottom: 10px; }
    .tag-wrap { display: flex; justify-content: center; gap: 6px; flex-wrap: wrap; }
    .tag { font-size: 0.75rem; background: var(--accent-tag); color: #d35400; padding: 4px 10px; border-radius: 8px; font-weight: 700; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1 onclick="window.location.reload()">피규어 박물관</h1>
    <p id="total-stats" class="stats-text">로딩 중...</p>
  </div>

  <div class="sticky-header">
    <div class="bookmark-container" id="filterMenu"></div>
  </div>

  <div class="container">
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    // 관장님의 CSV 주소 그대로 사용
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function init() {
      try {
        const response = await fetch(csvURL);
        const text = await response.text();
        
        // CSV 파싱 (쉼표로 분할 및 큰따옴표 처리)
        const rows = text.split(/\r?\n/).map(row => {
          const parts = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
          return parts ? parts.map(p => p.replace(/^"|"$/g, '').trim()) : [];
        });

        // 8번 열(이미지)이 있는 데이터만 필터
        const allData = rows.slice(1).filter(r => r[8]);
        document.getElementById('total-stats').innerText = `Total ${allData.length} Masterpieces`;

        // 책갈피 메뉴 생성 (K열: 10번 카테고리, C열: 2번 시리즈)
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
          let html = `<span class="main-label">${cat.toUpperCase()}</span><div class="sub-btns">`;
          seriesSet.forEach(s => {
            html += `<button class="filter-btn" onclick="filterBy('${s}', this)">${s}</button>`;
          });
          row.innerHTML = html + `</div></div>`;
          filterMenu.appendChild(row);
        }

        // 아이템 그리기
        const grid = document.getElementById('figureGrid');
        grid.innerHTML = allData.map(item => {
          const name = (item[12] && item[12] !== "") ? item[12] : item[3];
          const firstImg = item[8].split(',')[0].trim();
          const imgPath = `${imageBaseURL}${encodeURIComponent(firstImg)}.jpg`;
          
          return `
            <div class="card" data-series="${item[2]}">
              <div class="img-box"><img src="${imgPath}" loading="lazy" onerror="this.src='https://placehold.co/400x400?text=No+Image'"></div>
              <div class="content">
                <div class="char-name">${name}</div>
                <div class="tag-wrap">
                  <span class="tag">#${item[1]}</span>
                  <span class="tag" style="background:#eee; color:#777;">#${item[2]}</span>
                </div>
              </div>
            </div>`;
        }).join('');

      } catch (e) {
        console.error("데이터 로딩 실패:", e);
        document.getElementById('total-stats').innerText = "데이터를 로드하지 못했습니다.";
      }
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
