<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 도감</title>
  <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Noto Sans KR', sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }
    
    /* 1. 상단 큰 제목 (스크롤 시 같이 올라감) */
    .main-title-area {
      background-color: white;
      padding: 40px 0 20px 0;
      text-align: center;
    }
    .main-title-area h1 {
      font-family: 'Black Han Sans', sans-serif; /* 임팩트 있는 글꼴 */
      font-size: 3rem;
      color: #1a1a1a;
      margin: 0;
      letter-spacing: 2px;
    }

    /* 2. 슬림한 고정 헤더 (검은색 네모 축소) */
    header { 
      background: #1a1a1a; 
      color: white; 
      padding: 10px 0; /* 두께 대폭 축소 */
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
      gap: 8px;
    }

    /* 카테고리 버튼 슬림화 */
    .filter-container { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
    .filter-btn {
      background: #333; color: #aaa; border: none; padding: 4px 12px;
      border-radius: 15px; cursor: pointer; transition: 0.2s; font-size: 0.8rem;
    }
    .filter-btn.active { background: #fab005; color: #1a1a1a; font-weight: bold; }

    /* 검색창 슬림화 */
    .search-container { width: 90%; max-width: 400px; }
    #searchInput {
      width: 100%; padding: 6px 15px; border-radius: 20px; border: none; outline: none;
      font-size: 0.85rem; background: #2a2a2a; color: white;
    }
    #searchInput::placeholder { color: #666; }

    /* 그리드 및 카드 */
    .container { max-width: 1200px; margin: 20px auto; padding: 0 20px 60px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
    .card { background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05); cursor: pointer; border: 1px solid #e9ecef; transition: 0.3s; }
    .card.hidden { display: none; }
    
    .img-box { width: 100%; height: 250px; display: flex; align-items: center; justify-content: center; padding: 10px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 15px; border-top: 1px solid #f1f3f5; }
    .category-tag { font-size: 0.7rem; color: #fab005; font-weight: bold; }
    .manufac { color: #adb5bd; font-size: 0.7rem; font-weight: bold; }
    .char-name { font-size: 1rem; font-weight: bold; margin: 3px 0; color: #212529; }

    /* 메모장 */
    .memo-section { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out; background: #fff9db; }
    .card.active .memo-section { max-height: 500px; }
    .memo-content { padding: 15px; font-size: 0.85rem; color: #444; border-top: 1px dashed #ffd43b; }
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
        <input type="text" id="searchInput" placeholder="캐릭터 또는 제조사 검색..." onkeyup="runFilter()">
      </div>
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:50px;">데이터를 불러오는 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
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
        
        // 카테고리 추출
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
              <div class="category-tag">#${category}</div>
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${charName}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content"><strong>[상세 정보]</strong><br>${desc}</div>
            </div>
          `;
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
