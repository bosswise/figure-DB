<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@300;500;800&display=swap" rel="stylesheet">
  <style>
    /* 1. 깃허브 기본 텍스트 차단 */
    header[class*="header"], .site-header, h1.title, b, p:first-of-type { display: none !important; }

    :root { --primary-color: #fab005; --bg-color: #f1f3f5; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 메인 타이틀 & 고정 헤더 */
    .main-title-area { background: white; padding: 60px 0 30px; text-align: center; }
    .main-title-area h1 { font-family: 'Black Han Sans', sans-serif; font-size: 3.5rem; margin: 0; color: #1a1a1a; }
    header { background: rgba(26,26,26,0.98); color: white; padding: 12px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 10px; }

    /* 필터 & 검색창 */
    .filter-container { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
    .filter-btn { background: #333; color: #888; border: none; padding: 5px 14px; border-radius: 20px; cursor: pointer; font-size: 0.8rem; transition: 0.3s; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }
    #searchInput { width: 90%; max-width: 380px; padding: 8px 20px; border-radius: 25px; border: none; background: #222; color: white; text-align: center; outline: none; font-size: 0.9rem; }

    /* 카드 그리드 */
    .container { max-width: 1200px; margin: 30px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 25px; }
    
    /* 카드 디자인: 메모장 제거로 슬림해짐 */
    .card { 
      background: white; border-radius: 18px; overflow: hidden; 
      box-shadow: 0 8px 20px rgba(0,0,0,0.04); cursor: pointer; transition: 0.4s ease; 
    }
    .card:hover { transform: translateY(-10px); box-shadow: 0 15px 35px rgba(0,0,0,0.1); }
    .card.hidden { display: none; }
    
    .img-box { width: 100%; height: 280px; display: flex; align-items: center; justify-content: center; padding: 15px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }

    .content { padding: 20px; border-top: 1px solid #f8f9fa; text-align: center; }
    .category-tag { font-size: 0.7rem; color: var(--primary-color); font-weight: 800; display: block; margin-bottom: 4px; }
    .char-name { font-size: 1.1rem; font-weight: 800; color: #1a1a1a; }
    .manufac-name { font-size: 0.8rem; color: #adb5bd; margin-top: 2px; }

    /* 🏛️ 팝업 모달 스타일 */
    .modal {
      display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.85); backdrop-filter: blur(5px); z-index: 1000; 
      justify-content: center; align-items: center; padding: 20px;
    }
    .modal-content {
      background: white; max-width: 850px; width: 100%; max-height: 85vh; border-radius: 30px;
      display: flex; overflow: hidden; position: relative; animation: modalPop 0.3s ease-out;
    }
    @keyframes modalPop { from { transform: scale(0.9); opacity: 0; } to { transform: scale(1); opacity: 1; } }

    .modal-img-area { flex: 1.1; background: #fff; padding: 30px; display: flex; align-items: center; justify-content: center; }
    .modal-img-area img { max-width: 100%; max-height: 60vh; object-fit: contain; }
    
    .modal-info-area { flex: 0.9; padding: 40px; background: #fafafa; border-left: 1px solid #eee; overflow-y: auto; }
    .close-btn { position: absolute; top: 15px; right: 20px; font-size: 2.2rem; cursor: pointer; color: #ccc; z-index: 10; transition: 0.2s; }
    .close-btn:hover { color: #333; }
    
    /* 모달 텍스트 */
    .info-label { font-size: 0.75rem; color: var(--primary-color); font-weight: 800; margin-top: 18px; display: block; letter-spacing: 0.5px; }
    .info-value { font-size: 1.05rem; font-weight: 500; margin-bottom: 12px; border-bottom: 1px solid #eee; padding-bottom: 4px; display: block; color: #333; }

    /* 모바일 레이아웃 */
    @media (max-width: 768px) {
      .modal-content { flex-direction: column; overflow-y: auto; }
      .modal-img-area { padding: 20px; min-height: 300px; }
      .modal-info-area { padding: 25px; border-left: none; border-top: 1px solid #eee; }
    }
  </style>
</head>
<body>

  <div class="main-title-area"><h1>피규어 박물관</h1></div>
  <header>
    <div class="header-content">
      <div class="filter-container" id="categoryFilters"><button class="filter-btn active" onclick="filterCategory('all', this)">전체보기</button></div>
      <input type="text" id="searchInput" placeholder="찾으시는 캐릭터나 제조사가 있나요?" onkeyup="runFilter()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; color:#aaa;">박물관 데이터를 연결 중입니다...</div>
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
        
        // 카테고리 버튼 자동 생성
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
          
          // 카드 클릭 시 바로 모달 오픈
          card.onclick = () => openModal(fileName, cols[3], cols[1], cols[4], cols[5], cols[9]);
          
          card.innerHTML = `
            <div class="img-box">
              <img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'">
            </div>
            <div class="content">
              <span class="category-tag">${cols[10] || 'ETC'}</span>
              <div class="char-name">${cols[3]}</div>
              <div class="manufac-name">${cols[1]}</div>
            </div>
          `;
          grid.appendChild(card);
        });
      } catch (err) { console.error(err); }
    }

    function openModal(img, name, manu, scale, price, desc) {
      document.getElementById("modalImg").src = `${imageBaseURL}${encodeURIComponent(img)}.jpg`;
      document.getElementById("modalInfo").innerHTML = `
        <h2 style="font-family:'Black Han Sans'; font-size:2.2rem; margin:0 0 15px 0; color:#1a1a1a;">${name}</h2>
        <span class="info-label">제조사</span><span class="info-value">${manu}</span>
        <span class="info-label">스케일</span><span class="info-value">${scale}</span>
        <span class="info-label">출시 가격</span><span class="info-value">${isNaN(price) ? price : Number(price).toLocaleString() + ' KRW'}</span>
        <span class="info-label">수집가 노트</span><p style="line-height:1.8; color:#444; margin-top:5px; font-size:0.95rem;">${desc || '정보가 없습니다.'}</p>
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
