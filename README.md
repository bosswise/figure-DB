<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figure Archive - Category Edition</title>
  <style>
    body { font-family: 'Pretendard', sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }
    
    /* 헤더 & 검색/필터 영역 */
    header { 
      background: #1a1a1a; color: white; padding: 25px 20px; text-align: center;
      position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* 카테고리 버튼 스타일 */
    .filter-container { margin-top: 20px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
    .filter-btn {
      background: #333; color: #ccc; border: 1px solid #444; padding: 8px 18px;
      border-radius: 20px; cursor: pointer; transition: 0.3s; font-size: 0.9rem;
    }
    .filter-btn:hover { background: #555; color: white; }
    .filter-btn.active { background: #fab005; color: #1a1a1a; border-color: #fab005; font-weight: bold; }

    .search-container { max-width: 500px; margin: 15px auto 0; }
    #searchInput {
      width: 100%; padding: 10px 20px; border-radius: 20px; border: none; outline: none;
      font-size: 0.9rem; box-sizing: border-box;
    }

    /* 그리드 및 카드 */
    .container { max-width: 1200px; margin: 30px auto; padding: 0 20px 60px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
    .card { background: #fff; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.05); cursor: pointer; border: 1px solid #e9ecef; transition: 0.3s; }
    .card.hidden { display: none; }
    
    .img-box { width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; padding: 15px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 20px; border-top: 1px solid #f1f3f5; }
    .manufac { color: #adb5bd; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
    .char-name { font-size: 1.15rem; font-weight: 800; margin: 5px 0; color: #212529; }
    .category-tag { font-size: 0.7rem; color: #fab005; font-weight: bold; margin-bottom: 5px; display: block; }

    /* 메모장 */
    .memo-section { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out; background: #fff9db; }
    .card.active .memo-section { max-height: 600px; }
    .memo-content { padding: 20px; font-size: 0.9rem; color: #5c940d; line-height: 1.7; white-space: pre-wrap; border-top: 1px dashed #fab005; }
  </style>
</head>
<body>

  <header>
    <h1 onclick="location.reload()" style="cursor:pointer">FIGURE ARCHIVE</h1>
    
    <div class="filter-container" id="categoryFilters">
      <button class="filter-btn active" onclick="filterCategory('all', this)">전체</button>
    </div>

    <div class="search-container">
      <input type="text" id="searchInput" placeholder="캐릭터 또는 제조사 검색..." onkeyup="runFilter()">
    </div>
  </header>

  <div class="container">
    <div id="status">박물관 데이터를 불러오는 중...</div>
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
        
        // 카테고리 목록 추출 (K열 = 인덱스 10)
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
            <div class="img-box">
              <img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'">
            </div>
            <div class="content">
              <span class="category-tag">#${category}</span>
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${charName}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content"><strong>Collector's Note</strong><br>${desc}</div>
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
        
        if (matchesCat && matchesSearch) {
          card.classList.remove("hidden");
        } else {
          card.classList.add("hidden");
        }
      });
    }

    loadDatabase();
  </script>
</body>
</html>
