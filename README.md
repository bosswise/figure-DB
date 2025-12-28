<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@300;500;800&display=swap" rel="stylesheet">
  <style>
    /* 기존 스타일 유지 및 팝업(모달) 스타일 추가 */
    header[class*="header"], .site-header, h1.title, b, p:first-of-type { display: none !important; }
    :root { --primary-color: #fab005; --bg-color: #f1f3f5; --card-bg: #ffffff; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; overflow-x: hidden; }

    /* 메인 타이틀 & 헤더 */
    .main-title-area { background: white; padding: 60px 0 40px; text-align: center; border-bottom: 1px solid #eee; }
    .main-title-area h1 { font-family: 'Black Han Sans', sans-serif; font-size: 3.5rem; margin: 0; color: #1a1a1a; }
    header { background: rgba(26,26,26,0.98); color: white; padding: 15px 0; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }

    /* 필터 & 검색 */
    .filter-container { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
    .filter-btn { background: #333; color: #888; border: none; padding: 6px 16px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; }
    .filter-btn.active { background: var(--primary-color); color: #1a1a1a; font-weight: 800; }
    #searchInput { width: 90%; max-width: 400px; padding: 10px 20px; border-radius: 25px; border: none; background: #222; color: white; text-align: center; outline: none; }

    /* 그리드 & 카드 */
    .container { max-width: 1200px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; }
    .card { background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); cursor: pointer; transition: 0.3s; position: relative; }
    .card:hover { transform: translateY(-8px); }
    .card.hidden { display: none; }
    
    .img-box { width: 100%; height: 320px; display: flex; align-items: center; justify-content: center; padding: 20px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }

    .content { padding: 25px; border-top: 1px solid #f8f9fa; }
    .category-tag { font-size: 0.75rem; color: var(--primary-color); font-weight: 800; display: block; margin-bottom: 5px; }
    .char-name { font-size: 1.2rem; font-weight: 800; color: #1a1a1a; }

    /* 메모 섹션 */
    .memo-section { max-height: 0; overflow: hidden; transition: 0.4s; background: #fff9db; }
    .card.active .memo-section { max-height: 200px; border-top: 1px dashed #ffd43b; }
    .memo-content { padding: 20px; font-size: 0.9rem; line-height: 1.6; }

    /* 🏛️ 상세정보 팝업(모달) 스타일 */
    .modal {
      display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.9); z-index: 1000; justify-content: center; align-items: center; padding: 20px;
    }
    .modal-content {
      background: white; max-width: 900px; width: 100%; max-height: 90vh; border-radius: 25px;
      display: flex; overflow: hidden; position: relative; box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    .modal-img-area { flex: 1.2; background: #fff; padding: 40px; display: flex; align-items: center; justify-content: center; }
    .modal-img-area img { max-width: 100%; max-height: 70vh; object-fit: contain; }
    .modal-info-area { flex: 0.8; padding: 40px; background: #fdfdfd; border-left: 1px solid #eee; overflow-y: auto; }
    .close-btn { position: absolute; top: 20px; right: 25px; font-size: 2rem; cursor: pointer; color: #999; z-index: 10; }
    
    /* 상세 정보 텍스트 */
    .info-label { font-size: 0.8rem; color: var(--primary-color); font-weight: 800; margin-top: 20px; display: block; }
    .info-value { font-size: 1.1rem; font-weight: 500; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 5px; display: block; }

    /* 모바일 대응 */
    @media (max-width: 800px) {
      .modal-content { flex-direction: column; overflow-y: auto; }
      .modal-img-area { padding: 20px; }
      .modal-info-area { padding: 30px; border-left: none; border-top: 1px solid #eee; }
    }
  </style>
</head>
<body>

  <div class="main-title-area"><h1>피규어 박물관</h1></div>
  <header>
    <div class="header-content">
      <div class="filter-container" id="categoryFilters"><button class="filter-btn active" onclick="filterCategory('all', this)">전체보기</button></div>
      <input type="text" id="searchInput" placeholder="무엇을 찾으시나요?" onkeyup="runFilter()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px;">컬렉션을 불러오는 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <div id="detailModal" class="modal" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <span class="close-btn" onclick="document.getElementById('detailModal').style.display='none'">&times;</span>
      <div class="modal-img-area"><img id="modalImg" src=""></div>
      <div class="modal-info-area" id="modalInfo">
        </div>
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
        
        // 카테고리 버튼 생성 로직
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
          
          card.innerHTML = `
            <div class="img-box" onclick="handleImageClick(event, this, '${fileName}', '${cols[3]}', '${cols[1]}', '${cols[4]}', '${cols[5]}', '${cols[9]}')">
              <img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'">
            </div>
            <div class="content" onclick="this.parentElement.classList.toggle('active')">
              <span class="category-tag">${cols[10] || 'ETC'}</span>
              <div class="char-name">${cols[3]}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content">${cols[9]}</div>
            </div>
          `;
          grid.appendChild(card);
        });
      } catch (err) { console.error(err); }
    }

    // 사진 클릭 핸들러: 메모장이 열려있을 때만 상세 모달 오픈
    function handleImageClick(event, el, fileName, name, manu, scale, price, desc) {
      event.stopPropagation();
      const card = el.parentElement;
      if (card.classList.contains('active')) {
        openModal(fileName, name, manu, scale, price, desc);
      } else {
        card.classList.add('active');
      }
    }

    function openModal(img, name, manu, scale, price, desc) {
      document.getElementById("modalImg").src = `${imageBaseURL}${encodeURIComponent(img)}.jpg`;
      document.getElementById("modalInfo").innerHTML = `
        <h2 style="font-family:'Black Han Sans'; font-size:2rem; margin-bottom:10px;">${name}</h2>
        <span class="info-label">MANUFACTURER</span><span class="info-value">${manu}</span>
        <span class="info-label">SCALE</span><span class="info-value">${scale}</span>
        <span class="info-label">ORIGINAL PRICE</span><span class="info-value">${Number(price).toLocaleString()} KRW</span>
        <span class="info-label">COLLECTOR'S NOTE</span><p style="line-height:1.7; color:#555;">${desc}</p>
      `;
      document.getElementById("detailModal").style.display = "flex";
      document.body.style.overflow = "hidden"; // 배경 스크롤 방지
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
