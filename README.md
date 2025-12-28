<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@300;500;800&display=swap" rel="stylesheet">
  <style>
    /* 1. 깃허브 기본 텍스트 강제 차단 */
    header[class*="header"], .site-header, h1.title, b, p:first-of-type { display: none !important; }

    :root {
      --primary-color: #fab005;
      --bg-color: #f1f3f5;
      --card-bg: #ffffff;
      --text-main: #212529;
      --text-sub: #868e96;
    }

    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; padding: 0; color: var(--text-main); }
    
    /* 메인 타이틀 */
    .main-title-area {
      background-color: white;
      padding: 60px 0 40px 0;
      text-align: center;
    }
    .main-title-area h1 {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 3.8rem;
      margin: 0;
      background: linear-gradient(45-deg, #1a1a1a, #444);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* 슬림 고정 헤더 */
    header { 
      background: rgba(26, 26, 26, 0.95);
      backdrop-filter: blur(10px);
      color: white; 
      padding: 15px 0; 
      position: sticky; top: 0; z-index: 100;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }

    .filter-container { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
    .filter-btn {
      background: #333; color: #999; border: none; padding: 6px 16px;
      border-radius: 20px; cursor: pointer; transition: 0.3s; font-size: 0.85rem;
    }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; transform: scale(1.05); }

    .search-container { width: 90%; max-width: 400px; }
    #searchInput {
      width: 100%; padding: 10px 20px; border-radius: 25px; border: 1px solid #444; outline: none;
      font-size: 0.9rem; background: #222; color: white; text-align: center; transition: 0.3s;
    }
    #searchInput:focus { border-color: var(--primary-color); background: #000; }

    /* 카드 그리드 */
    .container { max-width: 1200px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; }
    
    .card { 
      background: var(--card-bg); border-radius: 20px; overflow: hidden; 
      box-shadow: 0 10px 30px rgba(0,0,0,0.05); cursor: pointer; border: 1px solid rgba(0,0,0,0.03);
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.12); }
    .card.hidden { display: none; }
    
    .img-box { width: 100%; height: 320px; display: flex; align-items: center; justify-content: center; padding: 20px; background: #fff; position: relative; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; transition: 0.5s; }
    .card:hover .img-box img { transform: scale(1.08); }
    
    .content { padding: 25px; border-top: 1px solid #f8f9fa; }
    .category-tag { font-size: 0.7rem; color: var(--primary-color); font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; display: block; }
    .manufac { color: var(--text-sub); font-size: 0.75rem; font-weight: 500; }
    .char-name { font-size: 1.25rem; font-weight: 800; margin: 6px 0; color: var(--text-main); }

    /* 메모 섹션 가독성 */
    .memo-section { max-height: 0; overflow: hidden; transition: all 0.5s ease; background: #fdfdfe; }
    .card.active .memo-section { max-height: 400px; border-top: 1px solid #eee; }
    .memo-content { padding: 25px; font-size: 0.95rem; color: #495057; line-height: 1.8; }
    .memo-title { color: var(--primary-color); font-weight: 800; font-size: 0.8rem; margin-bottom: 10px; display: block; border-left: 3px solid var(--primary-color); padding-left: 10px; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <h1>피규어 박물관</h1>
  </div>

  <header>
    <div class="header-content">
      <div class="filter-container" id="categoryFilters">
        <button class="filter-btn active" onclick="filterCategory('all', this)">전체보기</button>
      </div>
      <div class="search-container">
        <input type="text" id="searchInput" placeholder="무엇을 찾으시나요?" onkeyup="runFilter()">
      </div>
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; font-weight:300; font-size:1.2rem;">컬렉션을 정리 중입니다...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    // 기존 스크립트 로직과 동일
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
    let currentCategory = 'all';

    async function loadDatabase() {
      const grid = document.getElementById("figureGrid");
      const filterBox = document.getElementById("categoryFilters");
      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        const rows = csvText.split(/\r?\n/).map(row => {
          const regex = /(?!\s*$)\s*(?:'([^']*)'|"([^"]*)"|([^,]*))\s*(?:,|$)/g;
          const parts = [];
          let m;
          while (m = regex.exec(row)) { parts.push(m[1] || m[2] || m[3] || ""); }
          return parts;
        });
        document.getElementById("status").style.display = "none";
        const categories = [...new Set(rows.slice(1).map(r => r[10]?.trim()).filter(c => c))];
        categories.forEach(cat => {
          const btn = document.createElement("button");
          btn.className = "filter-btn";
          btn.innerText = cat;
          btn.onclick = (e) => filterCategory(cat, e.target);
          filterBox.appendChild(btn);
        });
        rows.slice(1).forEach(cols => {
          const fileName = cols[8]?.trim();
          if (!fileName) return;
          const manufacturer = cols[1]?.trim() || "N/A";
          const charName = cols[3]?.trim() || "Unknown";
          const category = cols[10]?.trim() || "ETC";
          const desc = cols[9]?.trim() || "상세 설명이 준비되지 않았습니다.";
          const card = document.createElement("div");
          card.className = "card";
          card.setAttribute("data-category", category);
          card.setAttribute("data-search", `${charName} ${manufacturer}`.toLowerCase());
          card.onclick = function() { this.classList.toggle('active'); };
          card.innerHTML = `
            <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'"></div>
            <div class="content">
              <span class="category-tag">${category}</span>
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${charName}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content">
                <span class="memo-title">COLLECTOR'S NOTE</span>
                ${desc}
              </div>
            </div>`;
          grid.appendChild(card);
        });
      } catch (err) { console.error(err); }
    }
    function filterCategory(cat, btn) {
      currentCategory = cat;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      runFilter();
    }
    function runFilter() {
      const query = document.getElementById("searchInput").value.toLowerCase();
      const cards = document.querySelectorAll(".card");
      cards.forEach(card => {
        const cat = card.getAttribute("data-category");
        const search = card.getAttribute("data-search");
        const matchesCat = (currentCategory === 'all' || cat === currentCategory);
        const matchesSearch = search.includes(query);
        if (matchesCat && matchesSearch) card.classList.remove("hidden");
        else card.classList.add("hidden");
      });
    }
    loadDatabase();
  </script>
</body>
</html>
