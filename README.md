<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    header[class*="header"], .site-header, h1.title, b, p:first-of-type { display: none !important; }

    /* 🎨 전체 배경을 마스코트와 어울리는 따뜻한 베이지색으로 통일 */
    :root { 
      --primary-color: #fab005; 
      --bg-color: #f7f3f0; /* 따뜻한 연베이지 톤 */
    }

    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 🖼️ 마스코트 & 타이틀 영역 대형화 */
    .main-title-area { 
      background-color: var(--bg-color); /* 배경색 일치시켜 경계선 제거 */
      padding: 60px 0; 
      text-align: center; 
    }
    
    .title-wrapper { 
      display: flex; 
      flex-direction: row; 
      align-items: center; 
      justify-content: center; 
      gap: 40px; /* 간격 더 넓게 */
      max-width: 1200px;
      margin: 0 auto;
    }

    .header-mascot {
      width: 220px; /* 더 큼직하게 키움 */
      height: 220px;
      object-fit: contain;
      animation: mascotFloat 3s ease-in-out infinite;
      filter: drop-shadow(0 15px 20px rgba(0,0,0,0.08));
    }

    @keyframes mascotFloat {
      0%, 100% { transform: translateY(0) rotate(-2deg); }
      50% { transform: translateY(-15px) rotate(2deg); }
    }

    .title-text-group { text-align: left; }
    /* 폰트 크기를 4.5rem으로 대폭 키워 시원시원하게 배치 */
    .main-title-area h1 { font-weight: 900; font-size: 4.5rem; margin: 0; color: #1a1a1a; letter-spacing: -2px; line-height: 1.1; }
    .main-title-area p { color: #666; margin-top: 15px; font-size: 1.3rem; font-weight: 300; margin-bottom: 0; }

    /* 고정 헤더 */
    header { background: rgba(26,26,26,0.98); color: white; padding: 15px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }

    .filter-container { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
    .filter-btn { background: #333; color: #888; border: none; padding: 6px 18px; border-radius: 20px; cursor: pointer; font-size: 0.9rem; transition: 0.3s; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }
    #searchInput { width: 90%; max-width: 450px; padding: 12px 25px; border-radius: 30px; border: none; background: #222; color: white; text-align: center; outline: none; font-size: 1rem; }

    /* 그리드 & 카드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; min-height: 500px; }
    
    @media (max-width: 1100px) { .grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 750px) { 
        .grid { grid-template-columns: 1fr; }
        .title-wrapper { flex-direction: column; gap: 20px; }
        .title-text-group { text-align: center; }
        .main-title-area h1 { font-size: 3rem; }
        .header-mascot { width: 160px; height: 160px; }
    }

    .card { background: white; border-radius: 25px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.04); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-12px); box-shadow: 0 20px 60px rgba(0,0,0,0.1); }
    .img-box { width: 100%; height: 350px; display: flex; align-items: center; justify-content: center; padding: 25px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 30px; border-top: 1px solid #f8f9fa; text-align: center; }
    .char-name { font-size: 1.4rem; font-weight: 800; color: #1a1a1a; }

    /* 페이지네이션 */
    .pagination { display: flex; justify-content: center; gap: 12px; margin-top: 60px; }
    .page-btn { background: white; color: #555; border: 1px solid #ddd; padding: 10px 20px; border-radius: 12px; cursor: pointer; transition: 0.3s; font-weight: 600; }
    .page-btn.active { background: var(--primary-color); color: #1a1a1a; border-color: var(--primary-color); font-weight: 800; }

    /* 팝업 모달 */
    .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); backdrop-filter: blur(12px); z-index: 1000; justify-content: center; align-items: center; padding: 20px; }
    .modal-content { background: white; max-width: 1250px; width: 95%; height: 85vh; border-radius: 40px; display: flex; overflow: hidden; position: relative; box-shadow: 0 30px 100px rgba(0,0,0,0.5); }
    .modal-img-area { flex: 1.4; background: #fff; padding: 50px; display: flex; align-items: center; justify-content: center; border-right: 1px solid #eee; position: relative; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(0,0,0,0.05); color: #bbb; border: none; font-size: 3rem; padding: 25px; cursor: pointer; border-radius: 50%; transition: 0.3s; }
    .nav-btn:hover { background: rgba(0,0,0,0.7); color: white; }
    .modal-info-area { flex: 0.9; padding: 60px; background: #fafafa; overflow-y: auto; }
    .close-btn { position: absolute; top: 30px; right: 40px; font-size: 3.5rem; cursor: pointer; color: #ccc; z-index: 20; }
    .close-btn:hover { color: #333; }
    .info-label { font-size: 0.9rem; color: var(--primary-color); font-weight: 800; margin-top: 35px; display: block; text-transform: uppercase; letter-spacing: 1px; }
    .info-value { font-size: 1.4rem; font-weight: 500; margin-bottom: 15px; border-bottom: 1.5px solid #f0f0f0; padding-bottom: 10px; display: block; color: #111; }
    .ad-slot { margin-top: 60px; width: 100%; min-height: 180px; background: #f0f0f0; border-radius: 25px; display: flex; align-items: center; justify-content: center; color: #aaa; border: 1px dashed #ddd; font-size: 0.9rem; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <div class="title-wrapper">
      <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot" onerror="this.style.display='none'">
      <div class="title-text-group">
        <h1>피규어 박물관</h1>
        <p>The Grand Archive of Masterpiece Figures</p>
      </div>
    </div>
  </div>

  <header>
    <div class="header-content">
      <div class="filter-container" id="categoryFilters"><button class="filter-btn active" onclick="filterCategory('all', this)">전체보기</button></div>
      <input type="text" id="searchInput" placeholder="찾으시는 피규어를 검색하세요..." onkeyup="onSearch()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; color:#aaa; font-size: 1.2rem;">컬렉션을 불러오는 중입니다...</div>
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
            <span class="category-tag" style="color:#fab005; font-weight:800; font-size:0.8rem; margin-bottom:8px; display:block;">${cols[10] || 'ETC'}</span>
            <div class="char-name">${cols[3]}</div>
          </div>`;
        grid.appendChild(card);
      });
      renderPagination();
      window.scrollTo({top: 350, behavior: 'smooth'});
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
        <h2 style="font-weight:900; font-size:3rem; margin:0 0 15px 0; color:#1a1a1a;">${name}</h2>
        <span class="info-label">제조사</span><span class="info-value">${manu}</span>
        <span class="info-label">스케일</span><span class="info-value">${scale}</span>
        <span class="info-label">가격</span><span class="info-value">${isNaN(price) ? price : Number(price).toLocaleString() + ' KRW'}</span>
        <span class="info-label">수집가 노트</span><p style="line-height:1.8; color:#444; font-size:1.1rem;">${desc || '정보가 없습니다.'}</p>
        <div class="ad-slot">광고 협력 문의 : (여기에 광고 코드를 넣으세요)</div>
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
