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

    :root { --primary-color: #fab005; --bg-color: #f4f4f2; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 🖼️ 마스코트가 포함된 타이틀 영역 */
    .main-title-area { background: white; padding: 50px 0 40px; text-align: center; border-bottom: 1px solid #eee; }
    
    .title-wrapper { 
      display: flex; 
      align-items: center; 
      justify-content: center; 
      gap: 20px; 
      margin-bottom: 10px;
    }

    .header-mascot {
      width: 100px; /* 캐릭터 크기 */
      height: 100px;
      object-fit: contain;
      /* 둥둥 떠있는 애니메이션 */
      animation: mascotFloat 3s ease-in-out infinite;
    }

    @keyframes mascotFloat {
      0%, 100% { transform: translateY(0) rotate(-3deg); }
      50% { transform: translateY(-15px) rotate(3deg); }
    }

    .main-title-area h1 { font-weight: 900; font-size: 3.2rem; margin: 0; color: #1a1a1a; letter-spacing: -1.5px; }

    /* 고정 헤더 */
    header { background: rgba(26,26,26,0.98); color: white; padding: 15px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }

    .filter-container { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
    .filter-btn { background: #333; color: #888; border: none; padding: 6px 16px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }
    #searchInput { width: 90%; max-width: 400px; padding: 10px 20px; border-radius: 25px; border: none; background: #222; color: white; text-align: center; outline: none; }

    /* 그리드 & 카드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px 50px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 35px; min-height: 500px; }
    
    @media (max-width: 1100px) { .grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 650px) { .grid { grid-template-columns: 1fr; } }

    .card { background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-10px); box-shadow: 0 20px 50px rgba(0,0,0,0.12); }
    .img-box { width: 100%; height: 320px; display: flex; align-items: center; justify-content: center; padding: 20px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 25px; border-top: 1px solid #f8f9fa; text-align: center; }
    .char-name { font-size: 1.25rem; font-weight: 800; color: #1a1a1a; }

    /* 페이지네이션 */
    .pagination { display: flex; justify-content: center; gap: 10px; margin: 50px 0; }
    .page-btn { background: white; color: #555; border: 1px solid #ddd; padding: 8px 16px; border-radius: 8px; cursor: pointer; transition: 0.3s; }
    .page-btn.active { background: var(--primary-color); color: #1a1a1a; border-color: var(--primary-color); font-weight: 800; }

    /* 팝업 모달 */
    .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); backdrop-filter: blur(10px); z-index: 1000; justify-content: center; align-items: center; padding: 20px; }
    .modal-content { background: white; max-width: 1250px; width: 95%; height: 85vh; border-radius: 35px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.4; background: #fff; padding: 40px; display: flex; align-items: center; justify-content: center; border-right: 1px solid #f0f0f0; position: relative; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(0,0,0,0.1); color: #ccc; border: none; font-size: 2.5rem; padding: 20px; cursor: pointer; border-radius: 50%; }
    .modal-info-area { flex: 0.8; padding: 60px; background: #fafafa; overflow-y: auto; }
    .close-btn { position: absolute; top: 25px; right: 35px; font-size: 3rem; cursor: pointer; color: #ddd; z-index: 20; }
    .info-label { font-size: 0.8rem; color: var(--primary-color); font-weight: 800; margin-top: 30px; display: block; }
    .info-value { font-size: 1.3rem; font-weight: 500; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 8px; display: block; }
    .ad-slot { margin-top: 50px; width: 100%; min-height: 150px; background: #f0f0f0; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: #999; border: 1px dashed #ccc; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <div class="title-wrapper">
      <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot" onerror="this.style.display='none'">
      <h1>피규어 박물관</h1>
    </div>
    <p>The Grand Archive of Masterpiece Figures</p>
  </div>

  <header>
    <div class="header-content">
      <div class="filter-container" id="categoryFilters"><button class="filter-btn active" onclick="filterCategory('all', this)">전체보기</button></div>
      <input type="text" id="searchInput" placeholder="찾으시는 피규어를 입력하세요..." onkeyup="onSearch()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; color:#aaa;">전시물을 불러오고 있습니다...</div>
    <div id="figureGrid" class="grid"></div>
    <div id="pagination" class="pagination"></div>
  </div>

  <div id="detailModal" class="modal" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <span class="close-btn" onclick="closeModal()">&times;</span>
      <div class="modal-img-area" id="modalImgContainer"></div>
      <div class="modal-info-area" id="modalInfo"></div>
    </div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
    
    let allData = [];
    let filteredData = [];
    let currentPage = 1;
    const itemsPerPage = 12;
    let imagesArray = [];
    let currentImgIdx = 0;
    let currentCategory = 'all';

    async function loadDatabase() {
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

        allData = rows.slice(1).filter(cols => cols[8]?.trim());
        filteredData = [...allData];
        document.getElementById("status").style.display = "none";
        
        const categories = [...new Set(allData.map(r => r[10]?.trim()).filter(c => c))];
        categories.forEach(cat => {
          const btn = document.createElement("button");
          btn.className = "filter-btn"; btn.innerText = cat;
          btn.onclick = (e) => filterCategory(cat, e.target);
          document.getElementById("categoryFilters").appendChild(btn);
        });

        displayPage(1);
      } catch (err) { console.error(err); }
    }

    function displayPage(page) {
      currentPage = page;
      const grid = document.getElementById("figureGrid");
      grid.innerHTML = "";
      const start = (page - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      const pageData = filteredData.slice(start, end);

      pageData.forEach(cols => {
        const fileName = cols[8]?.trim();
        const card = document.createElement("div");
        card.className = "card";
        card.onclick = () => openModal(fileName, cols[3], cols[1], cols[4], cols[5], cols[9]);
        card.innerHTML = `
          <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(fileName.split(',')[0].trim())}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'"></div>
          <div class="content">
            <span class="category-tag">${cols[10] || 'ETC'}</span>
            <div class="char-name">${cols[3]}</div>
          </div>`;
        grid.appendChild(card);
      });
      renderPagination();
      window.scrollTo(0, 0);
    }

    function renderPagination() {
      const pagination = document.getElementById("pagination");
      pagination.innerHTML = "";
      const totalPages = Math.ceil(filteredData.length / itemsPerPage);
      for (let i = 1; i <= totalPages; i++) {
        const btn = document.createElement("button");
        btn.className = `page-btn ${i === currentPage ? 'active' : ''}`;
        btn.innerText = i;
        btn.onclick = () => displayPage(i);
        pagination.appendChild(btn);
      }
    }

    function onSearch() {
      const query = document.getElementById("searchInput").value.toLowerCase();
      applyFilters(currentCategory, query);
    }

    function filterCategory(cat, btn) {
      currentCategory = cat;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const query = document.getElementById("searchInput").value.toLowerCase();
      applyFilters(cat, query);
    }

    function applyFilters(cat, query) {
      filteredData = allData.filter(cols => {
        const matchesCat = (cat === 'all' || cols[10]?.trim() === cat);
        const matchesSearch = `${cols[3]} ${cols[1]}`.toLowerCase().includes(query);
        return matchesCat && matchesSearch;
      });
      displayPage(1);
    }

    function openModal(imgString, name, manu, scale, price, desc) {
      imagesArray = imgString.split(',').map(s => s.trim());
      currentImgIdx = 0;
      const imgArea = document.getElementById("modalImgContainer");
      imgArea.innerHTML = `
        <img id="modalImg" src="${imageBaseURL}${encodeURIComponent(imagesArray[0])}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'">
        ${imagesArray.length > 1 ? `
          <button class="nav-btn prev-btn" onclick="changeImg(-1, event)">&lt;</button>
          <button class="nav-btn next-btn" onclick="changeImg(1, event)">&gt;</button>
        ` : ''}
      `;
      document.getElementById("modalInfo").innerHTML = `
        <h2 style="font-weight:900; font-size:2.8rem; margin:0 0 15px 0;">${name}</h2>
        <span class="info-label">제조사</span><span class="info-value">${manu}</span>
        <span class="info-label">스케일</span><span class="info-value">${scale}</span>
        <span class="info-label">가격</span><span class="info-value">${isNaN(price) ? price : Number(price).toLocaleString() + ' KRW'}</span>
        <span class="info-label">노트</span><p style="line-height:1.8; color:#444;">${desc || '정보가 없습니다.'}</p>
        <div class="ad-slot">ADVERTISEMENT</div>
      `;
      document.getElementById("detailModal").style.display = "flex";
      document.body.style.overflow = "hidden";
    }

    function changeImg(dir, e) {
      e.stopPropagation();
      currentImgIdx += dir;
      if (currentImgIdx < 0) currentImgIdx = imagesArray.length - 1;
      if (currentImgIdx >= imagesArray.length) currentImgIdx = 0;
      document.getElementById("modalImg").src = `${imageBaseURL}${encodeURIComponent(imagesArray[currentImgIdx])}.jpg`;
    }

    function closeModal() { document.getElementById("detailModal").style.display = "none"; document.body.style.overflow = "auto"; }

    loadDatabase();
  </script>
</body>
</html>
