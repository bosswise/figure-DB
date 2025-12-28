<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 도감</title>
  <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
  <style>
    /* 1. 상단에 삐져나오는 깃허브 기본 텍스트 숨기기 */
    header[class*="header"], .site-header, h1.title, b, p:first-of-type { display: none !important; }

    body { font-family: 'Noto Sans KR', sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }
    
    /* 큰 한글 제목 영역 */
    .main-title-area {
      background-color: white;
      padding: 50px 0 30px 0;
      text-align: center;
      border-bottom: 1px solid #eee;
    }
    .main-title-area h1 {
      font-family: 'Black Han Sans', sans-serif;
      font-size: 3.5rem;
      color: #1a1a1a;
      margin: 0;
    }

    /* 얇고 슬림한 검은색 고정 헤더 */
    header { 
      background: #1a1a1a; 
      color: white; 
      padding: 12px 0; 
      position: sticky; 
      top: 0; 
      z-index: 100; 
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .header-content {
      max-width: 1000px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
    }

    /* 필터 버튼 슬림화 */
    .filter-container { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
    .filter-btn {
      background: #333; color: #aaa; border: none; padding: 5px 15px;
      border-radius: 20px; cursor: pointer; transition: 0.2s; font-size: 0.85rem;
    }
    .filter-btn.active { background: #fab005; color: #1a1a1a; font-weight: bold; }

    /* 검색창 슬림화 */
    .search-container { width: 90%; max-width: 450px; }
    #searchInput {
      width: 100%; padding: 8px 18px; border-radius: 20px; border: none; outline: none;
      font-size: 0.9rem; background: #2a2a2a; color: white; text-align: center;
    }

    /* 그리드 및 카드 */
    .container { max-width: 1200px; margin: 30px auto; padding: 0 20px 60px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 25px; }
    .card { background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.06); cursor: pointer; border: 1px solid #e9ecef; transition: 0.3s; }
    .card.hidden { display: none; }
    .card:hover { transform: translateY(-5px); }
    
    .img-box { width: 100%; height: 280px; display: flex; align-items: center; justify-content: center; padding: 10px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 18px; border-top: 1px solid #f1f3f5; }
    .category-tag { font-size: 0.75rem; color: #fab005; font-weight: bold; margin-bottom: 4px; display: block; }
    .manufac { color: #adb5bd; font-size: 0.75rem; font-weight: bold; }
    .char-name { font-size: 1.1rem; font-weight: bold; margin: 4px 0; color: #212529; }

    /* 메모장 */
    .memo-section { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out; background: #fff9db; }
    .card.active .memo-section { max-height: 500px; }
    .memo-content { padding: 18px; font-size: 0.9rem; color: #444; border-top: 1px dashed #ffd43b; line-height: 1.6; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <h1>피규어 도감</h1>
  </div>

  <header>
    <div class="header-content">
      <div class="filter-container" id="categoryFilters">
        <button class="filter-btn active" onclick="filterCategory('all', this)">전체</button>
      </div>
      <div class="search-container">
        <input type="text" id="searchInput" placeholder="찾으시는 피규어를 검색하세요..." onkeyup="runFilter()">
      </div>
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; color:#999;">유물을 불러오는 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    // 기존 스크립트 로직 유지 (K열 카테고리 포함)
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
          const manufacturer = cols[1]?.trim() || "";
          const charName = cols[3]?.trim() || "";
          const category = cols[10]?.trim() || "기타";
          const desc = cols[9]?.trim() || "상세 정보가 없습니다.";
          const card = document.createElement("div");
          card.className = "card";
          card.setAttribute("data-category", category);
          card.setAttribute("data-search", `${charName} ${manufacturer}`.toLowerCase());
          card.onclick = function() { this.classList.toggle('active'); };
          card.innerHTML = `
            <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'"></div>
            <div class="content">
              <span class="category-tag">#${category}</span>
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${charName}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content"><strong>[Collector's Note]</strong><br>${desc}</div>
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
