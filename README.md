<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 사장님 지시: 깃허브 테마 및 유령 텍스트 완전 말살 */
    header, footer, .site-header, .site-footer, .title, b, span:first-of-type { 
      display: none !important; opacity: 0 !important; visibility: hidden !important; 
    }

    :root { 
      --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7;
      --modal-bg: rgba(0,0,0,0.96);
    }

    /* 🛡️ 화면 전체 차폐막 (유령 텍스트 노출 절대 방지) */
    .museum-full-layer {
      position: relative; width: 100%; min-height: 100vh; background-color: var(--bg); z-index: 999999;
      font-family: 'Noto Sans KR', sans-serif;
    }

    body { margin: 0; padding: 0; background-color: var(--bg); overflow-x: hidden; }

    /* 🖼️ [개선] 명예의 전당 자동 슬라이드 섹션 */
    .main-title-area { 
      padding: 50px 0; display: flex; align-items: center; justify-content: center;
      max-width: 1400px; margin: 0 auto; gap: 60px;
    }
    
    .hall-of-fame { 
      width: 200px; height: 260px; position: relative; perspective: 1000px;
    }
    .fame-slide {
      position: absolute; inset: 0; background: white; border-radius: 20px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden;
      opacity: 0; transition: opacity 1s ease-in-out;
    }
    .fame-slide.active { opacity: 1; z-index: 2; }
    .fame-slide img { width: 100%; height: 100%; object-fit: cover; }

    .center-group { text-align: center; z-index: 10; }
    .header-mascot { 
      width: 180px; height: 180px; border-radius: 50%; background: white; 
      padding: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); transition: 0.4s; 
    }
    .museum-title { 
      font-weight: 900; font-size: 4.2rem; color: var(--dark); 
      margin: 15px 0 5px; cursor: pointer; display: inline-block; letter-spacing: -3px;
    }

    /* 📌 스마트 책갈피 (슬림 & 최소화) */
    .sticky-header { 
      background: #2d2926; padding: 12px 0; position: sticky; top: 0; z-index: 1000; 
      box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    }
    .toggle-bar { max-width: 1200px; margin: 0 auto; display: flex; justify-content: flex-end; padding: 0 25px 5px; }
    .toggle-btn { background: none; border: 1px solid #555; color: #888; font-size: 0.7rem; padding: 3px 10px; border-radius: 5px; cursor: pointer; }

    .bookmark-container { 
      max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; 
      gap: 10px; padding: 0 25px 15px; overflow: hidden; transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      max-height: 800px; 
    }
    .bookmark-container.collapsed { max-height: 0; padding-bottom: 0; }

    .category-row { display: flex; align-items: center; gap: 15px; background: rgba(255,255,255,0.08); padding: 10px 18px; border-radius: 15px; }
    .main-label { color: var(--primary); font-weight: 900; min-width: 100px; font-size: 0.85rem; border-right: 1px solid #555; }
    .sub-btns-scroll { display: flex; gap: 10px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }
    
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 7px 18px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; }
    .filter-btn.active { background: var(--primary); color: #1a1a1a; font-weight: 800; }

    /* 🏛️ 전시 그리드 (가로 3개 복구) */
    .container { max-width: 1400px; margin: 50px auto; padding: 0 30px 150px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 50px; }
    
    .card { background: white; border-radius: 35px; overflow: hidden; box-shadow: 0 15px 45px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-15px); box-shadow: 0 35px 70px rgba(0,0,0,0.12); }
    .img-box { width: 100%; height: 400px; display: flex; align-items: center; justify-content: center; padding: 30px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 35px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.55rem; font-weight: 800; color: var(--dark); margin-bottom: 15px; }
    .tag-wrap { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; }
    .tag { font-size: 0.8rem; background: var(--tag-gold); color: #d35400; padding: 5px 14px; border-radius: 12px; font-weight: 700; }

    /* 🖼️ 사장님 극찬: 럭셔리 상세 모달창 복구 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 9999999; justify-content: center; align-items: center; padding: 30px; backdrop-filter: blur(20px); }
    .modal-content { background: white; max-width: 1200px; width: 98%; height: 85vh; border-radius: 55px; display: flex; overflow: hidden; position: relative; animation: modalUp 0.5s ease; }
    
    .modal-img-area { flex: 1.3; background: #fff; padding: 50px; display: flex; align-items: center; justify-content: center; position: relative; border-right: 1px solid #f0f0f0; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; transition: 0.4s ease; cursor: zoom-in; }
    .modal-img-area img.zoomed { transform: scale(2.2); cursor: zoom-out; }

    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 60px; height: 60px; background: rgba(255,255,255,0.9); border: none; border-radius: 50%; font-size: 1.5rem; cursor: pointer; color: #333; box-shadow: 0 5px 15px rgba(0,0,0,0.1); z-index: 10; transition: 0.3s; }
    .nav-btn:hover { background: var(--primary); color: white; transform: translateY(-50%) scale(1.1); }

    .modal-info-area { flex: 0.7; padding: 70px; background: #fafafa; overflow-y: auto; text-align: left; }
    .close-btn { position: absolute; top: 40px; right: 50px; font-size: 4rem; cursor: pointer; color: #ccc; line-height: 0.7; z-index: 100; transition: 0.3s; }
    .close-btn:hover { color: var(--dark); transform: rotate(90deg); }

    .info-label { font-size: 0.95rem; color: var(--primary); font-weight: 900; margin-top: 35px; display: block; letter-spacing: 1.5px; text-transform: uppercase; }
    .info-value { font-size: 1.5rem; font-weight: 600; border-bottom: 2px solid #eee; padding-bottom: 12px; display: block; color: var(--dark); }

    @keyframes modalUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
    @media (max-width: 1100px) { .grid { grid-template-columns: repeat(2, 1fr); } }
  </style>
</head>
<body>

<div class="museum-full-layer" id="museumLayer">
  <div class="main-title-area">
    <div class="hall-of-fame" id="fameLeft"></div>
    
    <div class="center-group">
      <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
      <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
      <p id="total-stats" style="color:#8c847d; font-size: 1.15rem; font-weight: 300;">Synchronizing Masterpieces...</p>
    </div>

    <div class="hall-of-fame" id="fameRight"></div>
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
      <button class="nav-btn" style="left:25px" onclick="changeImg(-1)">&lt;</button>
      <img id="modalImg" src="" onclick="toggleZoom(event)">
      <button class="nav-btn" style="right:25px" onclick="changeImg(1)">&gt;</button>
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
      document.getElementById('total-stats').innerText = `Total ${allData.length} Masterpieces Exhibited`;

      startFameSlide(); // 자동 슬라이드 시작
      renderFilters();
      renderGrid(allData);

      // 🚨 유령 박멸 감시 루틴
      setInterval(() => {
        document.querySelectorAll('header, footer, .title, b, span:first-of-type').forEach(el => {
          if(!el.closest('#museumLayer')) el.remove();
        });
      }, 100);

    } catch (e) { console.error(e); }
  }

  // 🎲 사장님 지시: 1장씩 보여주는 자동 슬라이드 (3장 로테이션)
  function startFameSlide() {
    const portraits = allData.filter(item => !(/\d/.test(item[8].split(',')[0].trim())));
    const shuffle = portraits.sort(() => 0.5 - Math.random());
    
    function buildSlides(targetId, count) {
      const target = document.getElementById(targetId);
      const items = shuffle.splice(0, count);
      target.innerHTML = items.map((item, idx) => `
        <div class="fame-slide ${idx === 0 ? 'active' : ''}">
          <img src="${imageBaseURL}${encodeURIComponent(item[8].split(',')[0].trim())}.jpg">
        </div>
      `).join('');
      
      let current = 0;
      setInterval(() => {
        const slides = target.querySelectorAll('.fame-slide');
        slides[current].classList.remove('active');
        current = (current + 1) % slides.length;
        slides[current].classList.add('active');
      }, 4000); // 4초마다 교체
    }

    buildSlides('fameLeft', 3);
    buildSlides('fameRight', 3);
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
        <div class="card" data-series="${item[2]}" onclick="openModal(${idx})">
          <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>
          <div class="content">
            <div class="char-name">${name}</div>
            <div class="tag-wrap">
              <span class="tag">#${item[10]}</span> <span class="tag" style="background:#eee;color:#777;">#${item[2]}</span>
            </div>
          </div>
        </div>`;
    }).join('');
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
      <h2 style="font-size:3.2rem; font-weight:900; color:#2d2926; margin:0 0 10px 0;">${item[12] || item[3]}</h2>
      <span class="info-label">제조사</span><span class="info-value">${item[1]}</span>
      <span class="info-label">시리즈</span><span class="info-value">${item[2]}</span>
      <span class="info-label">스케일</span><span class="info-value">${item[4] || '-'}</span>
      <span class="info-label">출시가격</span><span class="info-value">${item[5] || '-'}</span>
      <span class="info-label">수집가 메모</span><p style="line-height:2; color:#555; font-size:1.15rem; margin-top:15px;">${item[9] || '내용이 없습니다.'}</p>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  function updateModalImg() {
    const img = document.getElementById('modalImg');
    img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`;
    img.classList.remove('zoomed');
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
