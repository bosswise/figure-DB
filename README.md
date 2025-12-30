<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    header[class*="header"], .site-header, .site-footer, h1.title, b, p:first-of-type { display: none !important; }
    :root { --primary-color: #fab005; --bg-color: #f7f3f0; --text-dark: #2d2926; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 🖼️ 헤더 & 마스코트 */
    .main-title-area { padding: 60px 0; text-align: center; }
    .title-wrapper { display: flex; align-items: center; justify-content: center; gap: 40px; max-width: 1200px; margin: 0 auto; }
    .header-mascot { width: 180px; height: 180px; object-fit: cover; border-radius: 50%; background: white; padding: 10px; box-shadow: 0 15px 45px rgba(0,0,0,0.08); animation: mascotFloat 3s ease-in-out infinite; }
    @keyframes mascotFloat { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }
    .main-title-area h1 { font-weight: 900; font-size: 4rem; margin: 0; color: var(--text-dark); letter-spacing: -3px; }
    .main-title-area p { color: #8c847d; margin-top: 10px; font-size: 1.2rem; }

    /* 🔍 검색바 */
    header { background: rgba(45, 41, 38, 0.98); padding: 15px 0; position: sticky; top: 0; z-index: 100; }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 6px 18px; border-radius: 20px; cursor: pointer; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }
    #searchInput { width: 90%; max-width: 450px; padding: 12px 25px; border-radius: 30px; border: none; background: #1a1a1a; color: white; text-align: center; outline: none; }

    /* 🏛️ 그리드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px 80px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 35px; }
    .card { background: white; border-radius: 25px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.03); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-10px); }
    .img-box { width: 100%; height: 350px; display: flex; align-items: center; justify-content: center; padding: 20px; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 25px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-weight: 800; color: var(--text-dark); word-break: keep-all; }
    .name-long { font-size: 1.1rem; }
    .name-short { font-size: 1.4rem; }

    /* 🔢 페이지네이션 */
    .pagination { display: flex; justify-content: center; gap: 10px; margin-top: 50px; }
    .page-btn { background: white; border: 1px solid #eee; padding: 8px 18px; border-radius: 12px; cursor: pointer; }
    .page-btn.active { background: var(--primary-color); font-weight: 800; }

    /* 🖼️ 모달 & 확대 기능 */
    .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 1000; justify-content: center; align-items: center; }
    .modal-content { background: white; max-width: 1400px; width: 95%; height: 90vh; border-radius: 40px; display: flex; overflow: hidden; position: relative; }
    
    /* 이미지 영역: 확대 시 넘치는 부분 숨김 처리 */
    .modal-img-area { flex: 1.6; background: #fdfdfd; position: relative; overflow: hidden; display: flex; align-items: center; justify-content: center; cursor: zoom-in; }
    #modalImg { max-width: 100%; max-height: 100%; transition: transform 0.3s ease; transform-origin: center; pointer-events: none; }
    .modal-img-area.zoomed { cursor: zoom-out; }
    .modal-img-area.zoomed #modalImg { transform: scale(2.5); } /* 확대 배율 설정 */

    /* 내비게이션 버튼 */
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.3); backdrop-filter: blur(10px); border: none; width: 55px; height: 55px; border-radius: 50%; cursor: pointer; z-index: 100; transition: 0.3s; }
    .nav-btn:hover { background: var(--primary-color); color: white; }
    .prev-btn { left: 20px; }
    .next-btn { right: 20px; }

    .modal-info-area { flex: 0.8; padding: 50px; background: #fafafa; overflow-y: auto; z-index: 50; }
    .close-btn { position: absolute; top: 25px; right: 35px; font-size: 3rem; cursor: pointer; color: #ccc; z-index: 200; }
    .info-label { font-size: 0.85rem; color: var(--primary-color); font-weight: 800; margin-top: 30px; display: block; }
    .info-value { font-size: 1.3rem; font-weight: 500; border-bottom: 2px solid #eee; padding-bottom: 8px; display: block; }
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
      <input type="text" id="searchInput" placeholder="검색어를 입력하세요..." onkeyup="onSearch()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px; color:#aaa;">데이터 로딩 중...</div>
    <div id="figureGrid" class="grid"></div>
    <div id="pagination" class="pagination"></div>
  </div>

  <div id="detailModal" class="modal" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <span class="close-btn" onclick="closeModal()">&times;</span>
      <div class="modal-img-area" id="modalImgContainer" onclick="toggleZoom(event)"></div>
      <div class="modal-info-area" id="modalInfo"></div>
    </div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
    
    let allData = [], filteredData = [], currentPage = 1, itemsPerPage = 12;
    let imagesArray = [], currentImgIdx = 0, currentCategory = 'all';

    async function loadDatabase() {
      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        const rows = csvText.split(/\r?\n/).map(row => {
          const regex = /(?!\s*$)\s*(?:'([^']*)'|"([^"]*)"|([^,]*))\s*(?:,|$)/g;
          const parts = []; let m;
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
      const pageData = filteredData.slice((page - 1) * itemsPerPage, page * itemsPerPage);

      pageData.forEach(cols => {
        const name = cols[3] || "";
        const fileName = cols[8]?.trim();
        const nameClass = name.length >= 8 ? "name-long" : "name-short";
        const card = document.createElement("div");
        card.className = "card";
        card.onclick = () => openModal(fileName, name, cols[1], cols[4], cols[5], cols[9]);
        card.innerHTML = `
          <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(fileName.split(',')[0].trim())}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'"></div>
          <div class="content">
            <span style="color:var(--primary-color); font-weight:800; font-size:0.8rem; display:block; margin-bottom:5px;">${cols[10] || 'ETC'}</span>
            <div class="char-name ${nameClass}">${name}</div>
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

    function filterCategory(cat, btn) {
      currentCategory = cat;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const query = document.getElementById("searchInput").value.toLowerCase();
      filteredData = allData.filter(cols => (cat === 'all' || cols[10]?.trim() === cat) && `${cols[3]} ${cols[1]}`.toLowerCase().includes(query));
      displayPage(1);
    }

    function onSearch() {
      const query = document.getElementById("searchInput").value.toLowerCase();
      filteredData = allData.filter(cols => (currentCategory === 'all' || cols[10]?.trim() === currentCategory) && `${cols[3]} ${cols[1]}`.toLowerCase().includes(query));
      displayPage(1);
    }

    function openModal(imgString, name, manu, scale, price, desc) {
      imagesArray = imgString.split(',').map(s => s.trim());
      currentImgIdx = 0;
      updateModalImage();
      document.getElementById("modalInfo").innerHTML = `
        <h2 style="font-weight:900; font-size:2.8rem; margin-bottom:15px;">${name}</h2>
        <span class="info-label">제조사</span><span class="info-value">${manu}</span>
        <span class="info-label">스케일</span><span class="info-value">${scale}</span>
        <span class="info-label">가격</span><span class="info-value">${isNaN(price) ? price : Number(price).toLocaleString() + ' KRW'}</span>
        <span class="info-label">노트</span><p style="line-height:1.8; color:#555;">${desc || '정보가 없습니다.'}</p>
      `;
      document.getElementById("detailModal").style.display = "flex";
      document.body.style.overflow = "hidden";
    }

    function updateModalImage() {
      const container = document.getElementById("modalImgContainer");
      container.classList.remove('zoomed');
      container.innerHTML = `
        <img id="modalImg" src="${imageBaseURL}${encodeURIComponent(imagesArray[currentImgIdx])}.jpg" style="transform: scale(1); translate: 0 0;">
        ${imagesArray.length > 1 ? `
          <button class="nav-btn prev-btn" onclick="changeImg(-1, event)">&#10094;</button>
          <button class="nav-btn next-btn" onclick="changeImg(1, event)">&#10095;</button>
        ` : ''}
      `;
    }

    /* ✨ 확대/축소 및 마우스 트래킹 기능 */
    function toggleZoom(e) {
      const container = document.getElementById("modalImgContainer");
      const img = document.getElementById("modalImg");
      container.classList.toggle('zoomed');
      
      if (container.classList.contains('zoomed')) {
        updateZoomPosition(e);
        container.onmousemove = updateZoomPosition;
      } else {
        img.style.transform = "scale(1)";
        img.style.transformOrigin = "center";
        container.onmousemove = null;
      }
    }

    function updateZoomPosition(e) {
      const container = document.getElementById("modalImgContainer");
      const img = document.getElementById("modalImg");
      const rect = container.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      img.style.transformOrigin = `${x}% ${y}%`;
      img.style.transform = "scale(2.5)";
    }

    function changeImg(dir, e) {
      e.stopPropagation();
      currentImgIdx = (currentImgIdx + dir + imagesArray.length) % imagesArray.length;
      updateModalImage();
    }

    function closeModal() {
      document.getElementById("detailModal").style.display = "none";
      document.body.style.overflow = "auto";
    }

    loadDatabase();
  </script>
</body>
</html>
