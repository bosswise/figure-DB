<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 사장님 전용: 깃허브 유령 텍스트 박멸 시스템 */
    header, footer, .site-header, .site-footer, .title, b, span:first-of-type { 
      display: none !important; opacity: 0 !important; visibility: hidden !important; 
    }

    :root { 
      --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7;
      --modal-bg: rgba(0,0,0,0.95);
    }

    .museum-full-layer {
      position: relative; width: 100%; min-height: 100vh; background-color: var(--bg); z-index: 999999;
      font-family: 'Noto Sans KR', sans-serif;
    }

    body { margin: 0; padding: 0; background-color: var(--bg); overflow-x: hidden; }

    /* 🖼️ [공간 활용] 상단 랜덤 전시관 레이아웃 */
    .main-title-area { 
      padding: 40px 50px; display: flex; align-items: center; justify-content: center;
      max-width: 1600px; margin: 0 auto; gap: 40px;
    }
    
    .side-display { 
      flex: 1; height: 220px; display: flex; gap: 15px; justify-content: center;
      perspective: 1000px;
    }
    .random-card {
      width: 150px; height: 200px; background: white; border-radius: 15px;
      box-shadow: 0 10px 20px rgba(0,0,0,0.05); overflow: hidden;
      transition: 0.5s; animation: fadeIn 1s ease-out forwards;
    }
    .random-card img { width: 100%; height: 100%; object-fit: cover; }
    .random-card:hover { transform: translateY(-10px) rotateY(10deg); box-shadow: 0 15px 30px rgba(0,0,0,0.1); }

    .center-group { text-align: center; flex: 0.8; }
    .header-mascot { 
      width: 160px; height: 160px; border-radius: 50%; background: white; 
      padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: 0.4s; 
    }
    .museum-title { 
      font-weight: 900; font-size: 3.5rem; color: var(--dark); 
      margin: 10px 0; cursor: pointer; display: inline-block; letter-spacing: -3px;
    }

    /* 📌 책갈피 필터 (최소화 기능) */
    .sticky-header { 
      background: #2d2926; position: sticky; top: 0; z-index: 1000; 
      box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    }
    .toggle-bar { max-width: 1200px; margin: 0 auto; display: flex; justify-content: flex-end; padding: 5px 25px; }
    .toggle-btn { background: none; border: 1px solid #555; color: #aaa; font-size: 0.7rem; padding: 3px 10px; border-radius: 5px; cursor: pointer; }

    .bookmark-container { 
      max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; 
      gap: 8px; padding: 0 25px 15px; overflow: hidden; transition: 0.4s;
      max-height: 600px; 
    }
    .bookmark-container.collapsed { max-height: 0; padding-bottom: 0; }

    .category-row { display: flex; align-items: center; gap: 12px; background: rgba(255,255,255,0.06); padding: 8px 15px; border-radius: 12px; }
    .main-label { color: var(--primary); font-weight: 900; min-width: 95px; font-size: 0.8rem; border-right: 1px solid #555; }
    .sub-btns-scroll { display: flex; gap: 8px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }
    
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 6px 16px; border-radius: 20px; cursor: pointer; font-size: 0.8rem; }
    .filter-btn.active { background: var(--primary); color: #1a1a1a; font-weight: 800; }

    /* 🏛️ 전시 그리드 (가로 3개 고정) */
    .container { max-width: 1400px; margin: 40px auto; padding: 0 30px 150px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
    
    .card { background: white; border-radius: 30px; overflow: hidden; box-shadow: 0 10px 35px rgba(0,0,0,0.04); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-12px); box-shadow: 0 30px 60px rgba(0,0,0,0.1); }
    .img-box { width: 100%; height: 380px; display: flex; align-items: center; justify-content: center; padding: 25px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 30px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.45rem; font-weight: 800; color: var(--dark); margin-bottom: 12px; }
    .tag { font-size: 0.75rem; background: var(--tag-gold); color: #d35400; padding: 4px 12px; border-radius: 10px; font-weight: 700; margin-right: 5px; }

    /* 🖼️ 모달 시스템 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 9999999; justify-content: center; align-items: center; padding: 30px; backdrop-filter: blur(15px); }
    .modal-content { background: white; max-width: 1200px; width: 98%; height: 85vh; border-radius: 50px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.3; background: #fff; padding: 40px; display: flex; align-items: center; justify-content: center; position: relative; border-right: 1px solid #f0f0f0; overflow: hidden; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; transition: 0.4s ease; cursor: zoom-in; }
    .modal-img-area img.zoomed { transform: scale(2.2); cursor: zoom-out; }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 55px; height: 55px; background: rgba(255,255,255,0.95); border: none; border-radius: 50%; font-size: 1.5rem; cursor: pointer; display: flex; align-items: center; justify-content: center; z-index: 10; }
    .modal-info-area { flex: 0.7; padding: 60px; background: #fafafa; overflow-y: auto; text-align: left; }
    .close-btn { position: absolute; top: 35px; right: 45px; font-size: 3.5rem; cursor: pointer; color: #ccc; line-height: 0.7; }

    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 1200px) { .main-title-area { flex-direction: column; } .side-display { width: 100%; } .grid { grid-template-columns: repeat(2, 1fr); } }
  </style>
</head>
<body>

<div class="museum-full-layer" id="museumLayer">
  <div class="main-title-area">
    <div class="side-display" id="leftDisplay"></div> <div class="center-group">
      <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
      <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
      <p id="total-stats" style="color:#8c847d; font-size: 1.1rem;">Synchronization...</p>
    </div>

    <div class="side-display" id="rightDisplay">
      <input type="text" id="searchInput" placeholder="피규어 검색..." onkeyup="filterSearch()" style="padding:10px; border-radius:15px; border:1px solid #ddd; height:40px; align-self:center;">
    </div>
  </div>

  <div class="sticky-header">
    <div class="toggle-bar"><button class="toggle-btn" onclick="toggleFilters()" id="toggleBtn">[ 책갈피 접기 ]</button></div>
    <div class="bookmark-container" id="filterMenu"></div>
  </div>

  <div class="container">
    <div id="figureGrid" class="grid"></div>
  </div>
</div>

<div id="detailModal" class="modal" onclick="closeModal()">
  <div class="modal-content" onclick="event.stopPropagation()">
    <span class="close-btn" onclick="closeModal()">&times;</span>
    <div class="modal-img-area">
      <button class="nav-btn" style="left:20px" onclick="changeImg(-1)">&lt;</button>
      <img id="modalImg" src="" onclick="toggleZoom(event)">
      <button class="nav-btn" style="right:20px" onclick="changeImg(1)">&gt;</button>
    </div>
    <div class="modal-info-area" id="modalInfo"></div>
  </div>
</div>

<script>
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

  let allData = [];
  let currentImages = [];
  let currentImgIdx = 0;

  async function init() {
    try {
      const response = await fetch(csvURL);
      const text = await response.text();
      const rows = text.split(/\r?\n/).map(row => {
        const m = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
        return m ? m.map(v => v.replace(/^"|"$/g, '').trim()) : [];
      });

      allData = rows.slice(1).filter(r => r[8]);
      document.getElementById('total-stats').innerText = `Total ${allData.length} Masterpieces`;

      renderRandomDisplay(); // 랜덤 슬라이드 실행
      renderFilters();
      renderGrid(allData);

      // 🚨 유령 박멸 무한 루프
      setInterval(() => {
        document.querySelectorAll('header, footer, .title, b, span:first-of-type').forEach(el => {
          if(!el.closest('#museumLayer')) el.remove();
        });
      }, 100);

    } catch (e) { console.error(e); }
  }

  // 🎲 사장님 지시: 랜덤 3인방 슬라이드 (중복X, 정면샷 우선)
  function renderRandomDisplay() {
    // 숫자가 없는 정면 사진만 필터링 (예: 앨리스.jpg)
    const portraitData = allData.filter(item => {
      const firstImg = item[8].split(',')[0].trim();
      return !(/\d/.test(firstImg)); // 파일명에 숫자가 없는 것만 선택
    });

    const shuffle = portraitData.sort(() => 0.5 - Math.random());
    const selected = shuffle.slice(0, 3); // 3명 선발

    const left = document.getElementById('leftDisplay');
    left.innerHTML = selected.map(item => {
      const img = item[8].split(',')[0].trim();
      return `<div class="random-card"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>`;
    }).join('');
  }

  function renderFilters() {
    const menuMap = {};
    allData.forEach(item => {
      const cat = item[10] || "ETC"; const series = item[2] || "ETC";
      if (!menuMap[cat]) menuMap[cat] = new Set();
      menuMap[cat].add(series);
    });
    const filterMenu = document.getElementById('filterMenu');
    filterMenu.innerHTML = `<div class="category-row"><button class="filter-btn active" onclick="filterBy('all', this)">전체보기</button></div>`;
    for (const [cat, seriesSet] of Object.entries(menuMap)) {
      const row = document.createElement('div');
      row.className = 'category-row';
      let icon = cat.includes('GAME') ? '🎮 ' : cat.includes('VOCAL') ? '🎤 ' : '📦 ';
      let html = `<span class="main-label">${icon}${cat.toUpperCase()}</span><div class="sub-btns-scroll">`;
      seriesSet.forEach(s => { html += `<button class="filter-btn" onclick="filterBy('${s}', this)">${s}</button>`; });
      row.innerHTML = html + `</div></div>`;
      filterMenu.appendChild(row);
    }
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    grid.innerHTML = data.map((item, idx) => {
      const name = item[12] || item[3];
      const img = item[8].split(',')[0].trim();
      return `
        <div class="card" data-series="${item[2]}" data-name="${name}" onclick="openModal(${idx})">
          <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>
          <div class="content">
            <div class="char-name">${name}</div>
            <div style="margin-top:10px;"><span class="tag">#${item[1]}</span><span class="tag">#${item[2]}</span></div>
          </div>
        </div>`;
    }).join('');
  }

  function filterSearch() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    document.querySelectorAll('.card').forEach(card => {
      card.style.display = card.dataset.name.toLowerCase().includes(query) ? 'block' : 'none';
    });
  }

  function toggleFilters() {
    const menu = document.getElementById('filterMenu');
    menu.classList.toggle('collapsed');
    document.getElementById('toggleBtn').innerText = menu.classList.contains('collapsed') ? '[ 카테고리 열기 ]' : '[ 책갈피 접기 ]';
  }

  function openModal(idx) {
    const item = allData[idx];
    currentImages = item[8].split(',').map(s => s.trim());
    currentImgIdx = 0;
    updateModalImg();
    document.getElementById('modalInfo').innerHTML = `
      <h2 style="font-size:2.5rem; font-weight:900;">${item[12] || item[3]}</h2>
      <p><b>제조사:</b> ${item[1]}</p><p><b>시리즈:</b> ${item[2]}</p>
      <p><b>스케일:</b> ${item[4]}</p><p><b>메모:</b> ${item[9] || '내용 없음'}</p>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  function updateModalImg() {
    document.getElementById('modalImg').src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`;
  }

  function changeImg(dir) {
    currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length;
    updateModalImg();
  }

  function toggleZoom(e) { e.target.classList.toggle('zoomed'); }
  function closeModal() { document.getElementById('detailModal').style.display = 'none'; document.body.style.overflow = 'auto'; }
  function filterBy(s, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.card').forEach(c => c.style.display = (s === 'all' || c.dataset.series === s) ? 'block' : 'none');
  }

  init();
</script>
</body>
</html>
