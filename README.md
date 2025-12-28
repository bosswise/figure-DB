<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 1. 깃허브 기본 요소(figure-DB 텍스트 등) 완벽 차단 */
    header[class*="header"], .site-header, .site-footer, h1.title, b, p:first-of-type { display: none !important; }

    :root { 
      --primary-color: #fab005; 
      --bg-color: #f7f3f0; /* 마스코트 배경과 일치하는 따뜻한 베이지 */
      --text-dark: #2d2926; /* 캐릭터 톤에 맞춘 고급스러운 회갈색 */
    }

    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 🖼️ 헤더 디자인: 캐릭터와 제목의 조화 */
    .main-title-area { padding: 80px 0 60px; text-align: center; }
    
    .title-wrapper { 
      display: flex; 
      flex-direction: row; 
      align-items: center; 
      justify-content: center; 
      gap: 50px; 
      max-width: 1200px;
      margin: 0 auto;
    }

    .header-mascot {
      width: 220px;
      height: 220px;
      object-fit: cover;
      /* 하얀 사각형 테두리를 동그랗게 깎고 부드러운 그림자 부여 */
      border-radius: 50%; 
      background: white; 
      padding: 10px;
      box-shadow: 0 15px 45px rgba(0,0,0,0.08);
      animation: mascotFloat 3s ease-in-out infinite;
    }

    @keyframes mascotFloat {
      0%, 100% { transform: translateY(0) rotate(-2deg); }
      50% { transform: translateY(-20px) rotate(2deg); }
    }

    .title-text-group { text-align: left; }
    /* 제목 폰트 크기 및 색상 최적화 */
    .main-title-area h1 { 
      font-weight: 900; 
      font-size: 5rem; 
      margin: 0; 
      color: var(--text-dark); 
      letter-spacing: -4px; 
      line-height: 1;
      text-shadow: 3px 3px 0px rgba(255,255,255,0.5);
    }
    .main-title-area p { color: #8c847d; margin-top: 15px; font-size: 1.4rem; font-weight: 300; letter-spacing: 1px; }

    /* 🔍 고정 검색바 디자인: 캐릭터 톤에 맞춰 다듬기 */
    header { background: rgba(45, 41, 38, 0.98); padding: 18px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 30px rgba(0,0,0,0.1); }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 15px; }

    .filter-container { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 8px 20px; border-radius: 25px; cursor: pointer; font-size: 0.95rem; transition: 0.3s; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }
    
    #searchInput { 
      width: 90%; max-width: 500px; padding: 14px 30px; border-radius: 35px; border: 2px solid #555; 
      background: #1a1a1a; color: white; text-align: center; outline: none; font-size: 1.1rem; transition: 0.3s;
    }
    #searchInput:focus { border-color: var(--primary-color); width: 100%; max-width: 550px; }

    /* 🏛️ 그리드 및 카드 디자인: 박물관 전시품 느낌 */
    .container { max-width: 1300px; margin: 50px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 45px; }
    
    .card { background: white; border-radius: 30px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.03); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-15px); box-shadow: 0 30px 70px rgba(0,0,0,0.1); }
    
    .img-box { width: 100%; height: 380px; display: flex; align-items: center; justify-content: center; padding: 30px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 35px; border-top: 1px solid #f8f9fa; text-align: center; }
    .char-name { font-size: 1.5rem; font-weight: 800; color: var(--text-dark); }

    /* 🔢 페이지네이션 */
    .pagination { display: flex; justify-content: center; gap: 15px; margin-top: 70px; }
    .page-btn { background: white; color: #666; border: 1.5px solid #eee; padding: 12px 22px; border-radius: 15px; cursor: pointer; transition: 0.3s; font-weight: 700; }
    .page-btn.active { background: var(--primary-color); color: #1a1a1a; border-color: var(--primary-color); }

    /* 🖼️ 팝업 모달 */
    .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.88); backdrop-filter: blur(15px); z-index: 1000; justify-content: center; align-items: center; padding: 20px; }
    .modal-content { background: white; max-width: 1300px; width: 95%; height: 88vh; border-radius: 45px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.4; background: #fff; padding: 50px; display: flex; align-items: center; justify-content: center; border-right: 1px solid #f0f0f0; position: relative; }
    .modal-info-area { flex: 0.9; padding: 70px; background: #fafafa; overflow-y: auto; }
    .close-btn { position: absolute; top: 35px; right: 45px; font-size: 4rem; cursor: pointer; color: #ddd; z-index: 20; }
    .info-label { font-size: 0.95rem; color: var(--primary-color); font-weight: 900; margin-top: 40px; display: block; letter-spacing: 1.5px; }
    .info-value { font-size: 1.5rem; font-weight: 500; margin-bottom: 15px; border-bottom: 2px solid #f0f0f0; padding-bottom: 12px; display: block; color: var(--text-dark); }
    
    @media (max-width: 1000px) {
      .title-wrapper { flex-direction: column; gap: 20px; }
      .title-text-group { text-align: center; }
      .main-title-area h1 { font-size: 3.5rem; }
      .grid { grid-template-columns: repeat(2, 1fr); }
    }
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
      <input type="text" id="searchInput" placeholder="무엇을 찾으시나요?" onkeyup="onSearch()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; color:#999; font-size: 1.2rem;">컬렉션을 배치하는 중...</div>
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
            <span style="color:#fab005; font-weight:900; font-size:0.85rem; margin-bottom:8px; display:block;">${cols[10] || 'ETC'}</span>
            <div class="char-name">${cols[3]}</div>
          </div>`;
        grid.appendChild(card);
      });
      renderPagination();
      window.scrollTo({top: 400, behavior: 'smooth'});
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
        <h2 style="font-weight:900; font-size:3.2rem; margin:0 0 15px 0; color:#2d2926;">${name}</h2>
        <span class="info-label">제조사</span><span class="info-value">${manu}</span>
        <span class="info-label">스케일</span><span class="info-value">${scale}</span>
        <span class="info-label">가격</span><span class="info-value">${isNaN(price) ? price : Number(price).toLocaleString() + ' KRW'}</span>
        <span class="info-label">수집가 노트</span><p style="line-height:2; color:#555; font-size:1.15rem;">${desc || '정보가 없습니다.'}</p>
        <div class="ad-slot" style="margin-top:50px; padding:30px; background:#f0f0f0; border-radius:20px; text-align:center; color:#999;">광고 및 협업 문의는 환영입니다.</div>
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
