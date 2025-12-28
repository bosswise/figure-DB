<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;400;900&family=Outfit:wght@300;600&family=Gowun+Batang:wght@700&display=swap" rel="stylesheet">
  <style>
    header[class*="header"], .site-header, h1.title, b, p:first-of-type { display: none !important; }

    :root { 
      --primary-color: #e67e22; /* 너무 쨍하지 않은 고급스러운 오렌지 */
      --bg-color: #f4f4f2; /* 허전함을 잡아주는 차분한 배경색 */
      --card-bg: #ffffff;
      --header-bg: #1e1e1e;
    }

    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg-color); margin: 0; color: #333; }

    /* 메인 타이틀 영역 - 날씬하고 세련되게 */
    .main-title-area { 
      background: white; 
      padding: 70px 0 50px; 
      text-align: center;
      border-bottom: 1px solid #ddd;
    }
    .main-title-area h1 { 
      font-weight: 900; 
      font-size: 3.2rem; 
      margin: 0; 
      color: #222;
      letter-spacing: -1px; /* 글자 사이 간격을 좁혀 세련미 추가 */
    }
    .main-title-area p {
      margin-top: 10px;
      color: #888;
      font-weight: 300;
      letter-spacing: 5px;
      text-transform: uppercase;
      font-size: 0.8rem;
    }

    /* 슬림 고정 헤더 */
    header { 
      background: var(--header-bg); 
      color: white; 
      padding: 15px 0; 
      position: sticky; top: 0; z-index: 100;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 12px; }

    .filter-container { display: flex; gap: 10px; }
    .filter-btn {
      background: transparent; color: #666; border: 1px solid #444; padding: 6px 18px;
      border-radius: 4px; cursor: pointer; transition: 0.3s; font-size: 0.8rem;
    }
    .filter-btn.active { background: var(--primary-color); color: white; border-color: var(--primary-color); font-weight: bold; }

    #searchInput { 
      width: 90%; max-width: 400px; padding: 10px 20px; border-radius: 4px; 
      border: 1px solid #333; background: #222; color: white; text-align: center; outline: none;
    }

    /* 그리드 및 카드 */
    .container { max-width: 1400px; margin: 50px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 40px; }
    
    .card { 
      background: var(--card-bg); border-radius: 0; /* 각진 디자인으로 박물관 느낌 강조 */
      overflow: hidden; box-shadow: 0 15px 45px rgba(0,0,0,0.05); 
      cursor: pointer; transition: 0.4s; border: 1px solid #eee;
    }
    .card:hover { transform: translateY(-15px); box-shadow: 0 30px 60px rgba(0,0,0,0.1); }
    .card.hidden { display: none; }
    
    .img-box { width: 100%; height: 350px; display: flex; align-items: center; justify-content: center; padding: 30px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }

    .content { padding: 30px; text-align: left; }
    .category-tag { font-size: 0.7rem; color: var(--primary-color); font-weight: 900; margin-bottom: 10px; display: block; border-bottom: 2px solid var(--primary-color); width: fit-content; }
    .char-name { font-size: 1.3rem; font-weight: 900; color: #111; margin-top: 10px; }

    /* 초대형 상세 팝업 */
    .modal {
      display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(255,255,255,0.98); z-index: 1000; justify-content: center; align-items: center;
    }
    .modal-content {
      width: 95%; height: 90vh; max-width: 1400px; display: flex; position: relative; animation: fadeIn 0.4s;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

    .modal-img-area { flex: 1.5; display: flex; align-items: center; justify-content: center; background: white; }
    .modal-img-area img { max-width: 90%; max-height: 80vh; object-fit: contain; }
    
    .modal-info-area { flex: 1; padding: 60px; display: flex; flex-direction: column; justify-content: center; background: #fdfdfd; }
    .close-btn { position: fixed; top: 30px; right: 40px; font-size: 3rem; cursor: pointer; color: #111; font-weight: 100; }

    .info-label { font-size: 0.75rem; color: #aaa; font-weight: 900; margin-top: 30px; text-transform: uppercase; letter-spacing: 2px; }
    .info-value { font-size: 1.4rem; font-weight: 400; margin-bottom: 10px; color: #111; border-bottom: 1px solid #eee; padding-bottom: 10px; }
  </style>
</head>
<body>

  <div class="main-title-area">
    <h1>피규어 박물관</h1>
    <p>The Grand Archive of Masterpiece Figures</p>
  </div>

  <header>
    <div class="header-content">
      <div class="filter-container" id="categoryFilters"><button class="filter-btn active" onclick="filterCategory('all', this)">ALL</button></div>
      <input type="text" id="searchInput" placeholder="SEARCH COLLECTION" onkeyup="runFilter()">
    </div>
  </header>

  <div class="container">
    <div id="status" style="text-align:center; padding:100px;">LOADING ARCHIVE...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <div id="detailModal" class="modal" onclick="closeModal(event)">
    <span class="close-btn" onclick="document.getElementById('detailModal').style.display='none'">&times;</span>
    <div class="modal-content" onclick="event.stopPropagation()">
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
          btn.className = "filter-btn"; btn.innerText = cat.toUpperCase();
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
        <h2 style="font-weight:900; font-size:3rem; margin:0 0 30px 0; line-height:1.1;">${name}</h2>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
          <div><span class="info-label">MANUFACTURER</span><div class="info-value">${manu}</div></div>
          <div><span class="info-label">SCALE</span><div class="info-value">${scale}</div></div>
        </div>
        <span class="info-label">PRICE</span><div class="info-value">${isNaN(price) ? price : Number(price).toLocaleString() + ' KRW'}</div>
        <span class="info-label">DESCRIPTION</span><p style="line-height:1.8; color:#666; font-size:1.1rem; margin-top:10px;">${desc || 'No description available.'}</p>
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
