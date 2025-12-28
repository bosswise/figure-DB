<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 1. 깃허브 기본 텍스트 차단 */
    header[class*="header"], .site-header, h1.title, b, p:first-of-type { display: none !important; }

    :root { 
      --primary-color: #fab005; 
      --bg-color: #f4f4f2; /* 허전함을 달래주는 고급스러운 배경색 */
    }

    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 메인 타이틀 - 날씬하고 세련되게 */
    .main-title-area { background: white; padding: 60px 0 40px; text-align: center; border-bottom: 1px solid #eee; }
    .main-title-area h1 { 
      font-weight: 900; /* 너무 두껍지 않은 세련된 두께 */
      font-size: 3.2rem; 
      margin: 0; 
      color: #1a1a1a; 
      letter-spacing: -1px;
    }

    /* 고정 헤더 */
    header { background: rgba(26,26,26,0.98); color: white; padding: 15px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }

    /* 필터 & 검색 */
    .filter-container { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
    .filter-btn { background: #333; color: #888; border: none; padding: 6px 16px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }
    #searchInput { width: 90%; max-width: 400px; padding: 10px 20px; border-radius: 25px; border: none; background: #222; color: white; text-align: center; outline: none; }

    /* 🏛️ 그리드 (3열 고정) */
    .container { max-width: 1200px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { 
      display: grid; 
      grid-template-columns: repeat(3, 1fr); /* 3열 강제 고정 */
      gap: 30px; 
    }
    
    /* 화면이 좁아질 때만 열 개수 조절 (반응형) */
    @media (max-width: 1000px) { .grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 600px) { .grid { grid-template-columns: 1fr; } }

    .card { background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); cursor: pointer; transition: 0.3s; }
    .card:hover { transform: translateY(-8px); box-shadow: 0 15px 40px rgba(0,0,0,0.1); }
    .card.hidden { display: none; }
    
    .img-box { width: 100%; height: 320px; display: flex; align-items: center; justify-content: center; padding: 20px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }

    .content { padding: 25px; border-top: 1px solid #f8f9fa; text-align: center; }
    .category-tag { font-size: 0.75rem; color: var(--primary-color); font-weight: 800; display: block; margin-bottom: 5px; }
    .char-name { font-size: 1.2rem; font-weight: 800; color: #1a1a1a; }

    /* 🏛️ 이전의 세련된 초대형 팝업 모달 복구 */
    .modal {
      display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.9); backdrop-filter: blur(8px); z-index: 1000; 
      justify-content: center; align-items: center; padding: 20px;
    }
    .modal-content {
      background: white; max-width: 1100px; width: 95%; height: 85vh; border-radius: 30px;
      display: flex; overflow: hidden; position: relative; animation: modalPop 0.3s ease-out;
    }
    @keyframes modalPop { from { transform: scale(0.95); opacity: 0; } to { transform: scale(1); opacity: 1; } }

    .modal-img-area { flex: 1.3; background: #fff; padding: 30px; display: flex; align-items: center; justify-content: center; border-right: 1px solid #f0f0f0; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .modal-info-area { flex: 0.7; padding: 50px; background: #fafafa; overflow-y: auto; text-align: left; }
    .close-btn { position: absolute; top: 20px; right: 30px; font-size: 2.5rem; cursor: pointer; color: #ccc; z-index: 10; }

    .info-label { font-size: 0.8rem; color: var(--primary-color); font-weight: 800; margin-top: 25px; display: block; }
    .info-value { font-size: 1.2rem; font-weight: 500; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 6px; display: block; color: #111; }
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
      <input type="text" id="searchInput" placeholder="찾으시는 피규어를 검색하세요..." onkeyup="runFilter()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; color:#aaa;">데이터 로딩 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <div id="detailModal" class="modal" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <span class="close-btn" onclick="document.getElementById('detailModal').style.display='none'">&times;</span>
      <div class="modal-img-area"><img id="modalImg" src=""></div>
      <div class="modal-info-area" id="modalInfo"></div>
    </div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
    let currentCategory = 'all';

    async function loadDatabase() {
      const grid = document.getElementById("figureGrid");
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
          btn.className = "filter-btn"; btn.innerText = cat;
          btn.onclick = (e) => filterCategory(cat, e.target);
          document.getElementById("categoryFilters").appendChild(btn);
        });

        rows.slice(1).forEach(cols => {
          const fileName = cols[8]?.trim();
          if (!fileName) return;
          const card = document.createElement("div");
          card.className = "card";
          card.setAttribute("data-category", cols[10]?.trim() || "");
          card.setAttribute("data-search", `${cols[3]} ${cols[1]}`.toLowerCase());
          card.onclick = () => openModal(fileName, cols[3], cols[1], cols[4], cols[5], cols[9]);
          card.innerHTML = `
            <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'"></div>
            <div class="content">
              <span class="category-tag">${cols[10] || 'ETC'}</span>
              <div class="char-name">${cols[3]}</div>
            </div>`;
          grid.appendChild(card);
        });
      } catch (err) { console.error(err); }
    }

    function openModal(img, name, manu, scale, price, desc) {
      document.getElementById("modalImg").src = `${imageBaseURL}${encodeURIComponent(img)}.jpg`;
      document.getElementById("modalInfo").innerHTML = `
        <h2 style="font-weight:900; font-size:2.5rem; margin:0 0 20px 0;">${name}</h2>
        <span class="info-label">제조사</span><span class="info-value">${manu}</span>
        <span class="info-label">스케일</span><span class="info-value">${scale}</span>
        <span class="info-label">출시 가격</span><span class="info-value">${isNaN(price) ? price : Number(price).toLocaleString() + ' KRW'}</span>
        <span class="info-label">상세 설명</span><p style="line-height:1.8; color:#444; font-size:1.05rem;">${desc || '정보가 없습니다.'}</p>
      `;
      document.getElementById("detailModal").style.display = "flex";
      document.body.style.overflow = "hidden";
    }

    function closeModal(e) {
      document.getElementById("detailModal").style.display = "none";
      document.body.style.overflow = "auto";
    }

    function filterCategory(cat, btn) {
      currentCategory = cat;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      runFilter();
    }

    function runFilter() {
      const query = document.getElementById("searchInput").value.toLowerCase();
      document.querySelectorAll(".card").forEach(card => {
        const matchesCat = (currentCategory === 'all' || card.getAttribute("data-category") === currentCategory);
        const matchesSearch = card.getAttribute("data-search").includes(query);
        card.classList.toggle("hidden", !(matchesCat && matchesSearch));
      });
    }
    loadDatabase();
  </script>
</body>
</html>
