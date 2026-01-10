<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 사장님의 원본 스타일 (절대 유지) */
    header, footer, .site-header, .site-footer-old, .title, b, .gh-header { 
      display: none !important; opacity: 0 !important; visibility: hidden !important; pointer-events: none !important;
    }
    :root { --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7; --modal-bg: rgba(0,0,0,0.98); }
    * { box-sizing: border-box; }
    
    #museum-wrapper { 
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
      background-color: var(--bg); z-index: 99990; overflow-y: auto; 
      font-family: 'Noto Sans KR', sans-serif; scroll-behavior: smooth; 
    }
    
    .main-title-area { padding: 60px 0 40px; display: flex; align-items: center; justify-content: center; max-width: 1500px; margin: 0 auto; gap: 50px; }
    .hall-of-fame { width: 300px; height: 400px; position: relative; cursor: pointer; border-radius: 40px; box-shadow: 0 20px 50px rgba(0,0,0,0.12); overflow: hidden; background: #fff; flex-shrink: 0; }
    .fame-slide { position: absolute; inset: 0; background: white; opacity: 0; transition: opacity 1.5s ease; }
    .fame-slide.active { opacity: 1; z-index: 2; }
    .fame-slide img { width: 100%; height: 100%; object-fit: cover; }
    .center-group { text-align: center; flex: 0 0 450px; }
    .header-mascot { width: 180px; height: 180px; border-radius: 50%; background: white; padding: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); margin-bottom: 20px; }
    .museum-title { font-weight: 900; font-size: 4rem; color: var(--dark); margin: 0; cursor: pointer; letter-spacing: -3px; }
    .total-stats-badge { display: inline-block; background: var(--dark); color: var(--primary); padding: 8px 22px; border-radius: 20px; font-size: 1rem; font-weight: 800; margin-top: 15px; }
    
    .sticky-header { background: #2d2926; padding: 20px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 10px 40px rgba(0,0,0,0.4); }
    .control-bar { max-width: 1200px; margin: 0 auto; padding: 0 25px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
    
    .search-box { position: relative; width: 300px; }
    .search-input { width: 100%; padding: 10px 20px 10px 40px; border-radius: 25px; border: 1px solid #555; background: #45403c; color: white; font-family: inherit; transition: 0.3s; }
    .search-input:focus { background: white; color: var(--dark); border-color: var(--primary); outline: none; }
    .search-icon { position: absolute; left: 15px; top: 50%; transform: translateY(-50%); color: #999; font-size: 14px; }
    
    .sort-select { background: #45403c; color: white; border: 1px solid #555; padding: 8px 15px; border-radius: 20px; font-family: inherit; font-size: 0.85rem; cursor: pointer; outline: none; }
    .sort-select:focus { border-color: var(--primary); }

    .toggle-btn { background: none; border: 1px solid #666; color: #999; font-size: 0.75rem; padding: 5px 15px; border-radius: 8px; cursor: pointer; }
    .bookmark-container { max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding: 0 25px 15px; transition: 0.6s ease; overflow: hidden; max-height: 1000px; }
    .bookmark-container.collapsed { max-height: 0; padding-bottom: 0; }
    .category-row { display: flex; align-items: center; gap: 20px; background: rgba(255,255,255,0.08); padding: 12px 25px; border-radius: 18px; }
    
    .sub-btns-scroll { display: flex; gap: 10px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; -ms-overflow-style: none; flex-wrap: wrap; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }

    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 8px 20px; border-radius: 25px; cursor: pointer; font-size: 0.85rem; transition: 0.2s; }
    .filter-btn.active, .filter-btn:hover { background: var(--primary); color: #1a1a1a; font-weight: 800; transform: scale(1.05); }

    .maker-row { display: flex; align-items: flex-start; gap: 15px; padding: 15px 25px; border-top: 1px solid rgba(255,255,255,0.1); margin-top: 5px; }
    .maker-label { color: #888; font-size: 0.75rem; font-weight: 800; white-space: nowrap; margin-top: 8px; }
    .filter-count { font-size: 0.7rem; background: rgba(0,0,0,0.3); color: #ccc; padding: 2px 6px; border-radius: 10px; margin-left: 5px; }
    
    .container { max-width: 1550px; margin: 60px auto; padding: 0 45px 150px; min-height: 60vh; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; }
    .card { background: white; border-radius: 45px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; border: 1px solid #f2f2f2; position: relative; }
    .card:hover { transform: translateY(-20px); box-shadow: 0 45px 90px rgba(0,0,0,0.15); }
    .img-box { width: 100%; height: 450px; display: flex; align-items: center; justify-content: center; padding: 40px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 30px; text-align: center; border-top: 1px solid #f9f9f9; }
    .char-name { font-size: 1.7rem; font-weight: 800; color: var(--dark); margin-bottom: 15px; }
    .tag-wrap { display: flex; justify(center); gap: 8px; flex-wrap: wrap; margin-top: 10px; }
    .tag { font-size: 0.85rem; background: var(--tag-gold); color: #d35400; padding: 6px 14px; border-radius: 12px; font-weight: 800; white-space: nowrap; display: inline-block; }
    .tag.sec { background: #eee; color: #777; }
    
    .pagination { display: flex; justify-content: center; align-items: center; gap: 8px; margin-top: 60px; padding-bottom: 40px; }
    .page-btn { min-width: 45px; height: 45px; border-radius: 22.5px; border: 1px solid #ddd; background: white; color: var(--dark); font-weight: 700; cursor: pointer; transition: 0.3s; display: flex; align-items: center; justify-content: center; padding: 0 15px; }
    .page-btn:hover { background: #f0f0f0; border-color: #bbb; }
    .page-btn.active { background: var(--dark); color: var(--primary); border-color: var(--dark); }
    .page-btn:disabled { opacity: 0.3; cursor: not-allowed; }

    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 99999; justify-content: center; align-items: center; padding: 40px; backdrop-filter: blur(30px); }
    .modal-content { background: white; max-width: 1300px; width: 98%; height: 88vh; border-radius: 65px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.4; background: #fff; position: relative; border-right: 1px solid #f0f0f0; overflow: hidden; display: flex; align-items: center; justify-content: center; }
    .modal-img-wrapper { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; cursor: zoom-in; }
    #modalImg { max-width: 90%; max-height: 90%; object-fit: contain; transition: transform 0.1s ease-out; transform-origin: center; }
    #modalImg.zoomed { cursor: zoom-out; transform: scale(3.5); }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 70px; height: 70px; background: rgba(255,255,255,0.98); border: none; border-radius: 50%; font-size: 2.5rem; cursor: pointer; z-index: 10; display: flex; align-items: center; justify-content: center; color: #333; box-shadow: 0 10px 30px rgba(0,0,0,0.15); transition: 0.3s; }
    .modal-info-area { flex: 0.6; padding: 80px; background: #fafafa; overflow-y: auto; text-align: left; }
    .close-btn { position: absolute; top: 40px; right: 60px; font-size: 4.5rem; cursor: pointer; color: #ddd; z-index: 100; line-height: 0.7; }
    .info-item { margin-bottom: 30px; border-bottom: 2px solid #eee; padding-bottom: 12px; display: flex; flex-direction: column; }
    .info-label { font-size: 1rem; color: var(--primary); font-weight: 900; letter-spacing: 1px; margin-bottom: 8px; }
    .info-value { font-size: 1.7rem; font-weight: 700; color: var(--dark); line-height: 1.4; }

    /* 🆕 공식몰 버튼 스타일 추가 */
    .official-btn {
      display: block; text-align: center; background: var(--dark); color: var(--primary); 
      padding: 18px; border-radius: 20px; text-decoration: none; font-weight: 900; 
      font-size: 1.1rem; transition: 0.3s; margin-top: 15px;
    }
    .official-btn:hover { background: #000; }

    #quick-menu { position: fixed; right: 30px; top: 150px; width: 110px; background: white; border: 1px solid #ddd; z-index: 9900; text-align: center; border-radius: 12px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.1); display: none; }
    .quick-header { background: #2d2926; color: white; padding: 10px 0; font-size: 0.8rem; font-weight: 700; }
    .quick-list { display: flex; flex-direction: column; }
    .quick-item { width: 100%; height: 110px; padding: 5px; border-bottom: 1px solid #eee; cursor: pointer; display: flex; align-items: center; justify-content: center; }
    .quick-item img { max-width: 90%; max-height: 90%; object-fit: contain; }
    .top-btn { width: 100%; border: none; background: var(--primary); color: #2d2926; font-weight: 900; padding: 10px 0; cursor: pointer; }

    #loading-screen { position: fixed; inset: 0; background: var(--bg); z-index: 999999; display: flex; flex-direction: column; align-items: center; justify-content: center; transition: opacity 0.5s; }
    .loader { width: 60px; height: 60px; border: 5px solid var(--primary); border-bottom-color: transparent; border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 20px; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    .card-badge { position: absolute; top: 25px; left: 25px; background: var(--primary); color: #2d2926; padding: 6px 14px; border-radius: 20px; font-weight: 900; font-size: 0.85rem; box-shadow: 0 5px 15px rgba(250, 176, 5, 0.4); z-index: 5; }

    /* 🆕 푸터 보강 */
    .museum-footer { text-align: center; padding: 80px 0; color: #777; font-size: 0.95rem; border-top: 1px solid #e0e0e0; margin-top: 80px; line-height: 1.8; }
    .footer-dev-text { color: var(--dark); font-weight: 800; margin-bottom: 5px; font-size: 1.1rem; }

    @media (max-width: 1024px) { .grid { grid-template-columns: repeat(2, 1fr); gap: 30px; } .museum-title { font-size: 2.5rem; } }
    @media (max-width: 600px) { .grid { grid-template-columns: repeat(1, 1fr); } .modal-content { flex-direction: column; height: 100vh; border-radius: 0; } }
  </style>
</head>
<body>

<div id="loading-screen"><div class="loader"></div><div class="loading-text">명작들을 진열하고 있습니다...</div></div>

<div id="museum-wrapper">
  <div id="quick-menu">
    <div class="quick-header">최근 본 상품</div>
    <div id="quick-items-container" class="quick-list"></div>
    <button class="top-btn" onclick="scrollToTop()">▲ TOP</button>
  </div>

  <div class="main-title-area">
    <div class="hall-of-fame" id="fameLeft"></div>
    <div class="center-group">
      <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
      <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
      <div id="totalStats" class="total-stats-badge">총 0점의 명작 전시 중</div>
    </div>
    <div class="hall-of-fame" id="fameRight"></div>
  </div>

  <div class="sticky-header">
    <div class="control-bar">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="이름, 제조사 검색..." onkeyup="applyFilters()">
      </div>
      <div style="display: flex; gap: 15px; align-items: center;">
        <select id="sortOrder" class="sort-select" onchange="applyFilters()">
          <option value="default">기본 순서</option>
          <option value="priceHigh">높은 가격순</option>
          <option value="priceLow">낮은 가격순</option>
          <option value="nameAsc">이름 (가나다)</option>
        </select>
        <button class="toggle-btn" onclick="toggleFilters()" id="toggleBtn">[ 필터 열기 ]</button>
      </div>
    </div>
    <div class="bookmark-container collapsed" id="filterMenu">
      <div id="seriesButtons"></div>
      <div class="maker-row" id="makerButtons">
        <span class="maker-label">MAKER</span>
        <div class="sub-btns-scroll" id="makerList"></div>
      </div>
    </div>
  </div>

  <div class="container">
    <div id="figureGrid" class="grid"></div>
    <div id="pagination" class="pagination"></div>
    
    <div class="museum-footer">
      <div class="footer-dev-text">피규어를 너무 좋아하는 1인 개발자입니다 ㅎㅎ</div>
      <p>본 사이트는 개인적인 팬심으로 운영되는 아카이브 공간입니다.<br>
      이미지의 저작권은 ⓒ SHIFT UP, 제조사 및 판매처에 있으며 인용의 목적으로 사용되었습니다.<br>
      문제가 될 시 즉시 조치하겠습니다. (Contact: [사장님 메일])</p>
    </div>
  </div>
</div>

<div id="detailModal" class="modal" onclick="closeModal()">
  <div class="modal-content" onclick="event.stopPropagation()">
    <span class="close-btn" onclick="closeModal()">&times;</span>
    <div class="modal-img-area">
      <button class="nav-btn" style="left:35px" onclick="changeImg(-1)">‹</button>
      <div class="modal-img-wrapper" onmousemove="handleZoomMove(event)">
        <img id="modalImg" src="" onclick="toggleZoom(event)">
      </div>
      <button class="nav-btn" style="right:35px" onclick="changeImg(1)">›</button>
    </div>
    <div class="modal-info-area" id="modalInfo"></div>
  </div>
</div>

<script>
  /* 🚨 스크립트 로직 완벽 복구 */
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
  
  let allData = [], currentDisplayData = []; 
  let currentImages = [], currentImgIdx = 0, isZoomed = false;
  let activeFilter = 'all', activeMaker = 'all';
  let currentPage = 1, rowsPerPage = 12;

  async function init() {
    try {
      const response = await fetch(csvURL);
      const text = await response.text();
      const rows = text.split(/\r?\n/).map(row => {
        const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
        return cols.map(c => c ? c.trim().replace(/^"|"$/g, '').replace(/""/g, '"') : "");
      });
      
      // 7번 인덱스(이미지파일명) 필터링
      allData = rows.slice(1).filter(r => r[7]); 
      currentDisplayData = [...allData];
      
      document.getElementById('totalStats').innerText = `총 ${allData.length}점의 명작 전시 중`;
      startFameSlide(); 
      renderFilters(); 
      updateDisplay(); 
      renderRecentView();

      setTimeout(() => {
        const loader = document.getElementById('loading-screen');
        if(loader) { loader.style.opacity = '0'; setTimeout(() => { loader.style.display = 'none'; }, 500); }
      }, 800);
    } catch (e) { console.error("데이터 로드 에러:", e); }
  }

  function getProductName(item) { return item[3] || "이름 정보 없음"; }

  function renderFilters() {
    const seriesSet = new Set(), makerSet = new Set();
    const sCount = {}, mCount = {};
    allData.forEach(item => {
      const s = item[2] || "ETC", m = item[1] || "정보없음";
      seriesSet.add(s); makerSet.add(m);
      sCount[s] = (sCount[s] || 0) + 1; mCount[m] = (mCount[m] || 0) + 1;
    });

    let sHtml = `<div class="category-row"><button class="filter-btn active" data-type="series" onclick="filterBy('series', 'all', this)">전체보기 <span class="filter-count">${allData.length}</span></button><div class="sub-btns-scroll">`;
    Array.from(seriesSet).sort().forEach(s => { sHtml += `<button class="filter-btn" data-type="series" onclick="filterBy('series', '${s}', this)">${s} <span class="filter-count">${sCount[s]}</span></button>`; });
    document.getElementById('seriesButtons').innerHTML = sHtml + `</div></div>`;

    let mHtml = `<button class="filter-btn active" data-type="maker" onclick="filterBy('maker', 'all', this)">ALL</button>`;
    Array.from(makerSet).sort().forEach(m => { mHtml += `<button class="filter-btn" data-type="maker" onclick="filterBy('maker', '${m}', this)">${m} <span class="filter-count">${mCount[m]}</span></button>`; });
    document.getElementById('makerList').innerHTML = mHtml;
  }

  window.applyFilters = function() {
    const q = document.getElementById('searchInput').value.toLowerCase();
    const sort = document.getElementById('sortOrder').value;
    let res = allData.filter(item => {
      const sMatch = (activeFilter === 'all' || item[2] === activeFilter);
      const mMatch = (activeMaker === 'all' || item[1] === activeMaker);
      const tMatch = getProductName(item).toLowerCase().includes(q) || (item[1]||"").toLowerCase().includes(q);
      return sMatch && mMatch && tMatch;
    });
    if (sort === 'priceHigh') res.sort((a,b) => (parseInt(b[4].replace(/\D/g,''))||0) - (parseInt(a[4].replace(/\D/g,''))||0));
    else if (sort === 'priceLow') res.sort((a,b) => (parseInt(a[4].replace(/\D/g,''))||0) - (parseInt(b[4].replace(/\D/g,''))||0));
    currentDisplayData = res; currentPage = 1; updateDisplay();
  }

  window.filterBy = function(type, val, btn) {
    if (type === 'series') { activeFilter = val; document.querySelectorAll('[data-type="series"]').forEach(b => b.classList.remove('active')); }
    else { activeMaker = val; document.querySelectorAll('[data-type="maker"]').forEach(b => b.classList.remove('active')); }
    btn.classList.add('active'); applyFilters();
  }

  function updateDisplay() {
    const total = Math.ceil(currentDisplayData.length / rowsPerPage);
    const start = (currentPage - 1) * rowsPerPage;
    renderGrid(currentDisplayData.slice(start, start + rowsPerPage)); 
    renderPagination(total);
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    if (data.length === 0) { grid.innerHTML = `<div class="no-result"><h3>😢 결과가 없습니다.</h3></div>`; return; }
    grid.innerHTML = data.map(item => {
      const img = (item[7]||"").split(',')[0].trim();
      const imgSrc = img.includes('.') ? img : img + ".jpg";
      return `<div class="card" onclick="window.openModal(${allData.indexOf(item)})">
        <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(imgSrc)}" loading="lazy"></div>
        <div class="content"><div class="char-name">${getProductName(item)}</div>
        <div class="tag-wrap"><span class="tag">#${item[1]}</span><span class="tag sec">#${item[2]}</span></div></div>
      </div>`;
    }).join('');
  }

  function renderPagination(total) {
    const nav = document.getElementById('pagination');
    if (total <= 1) { nav.innerHTML = ''; return; }
    let html = `<button class="page-btn" onclick="changePage(${currentPage-1})" ${currentPage===1?'disabled':''}>&lt;</button>`;
    for(let i=1; i<=total; i++) { if(Math.abs(currentPage-i)<3) html += `<button class="page-btn ${i===currentPage?'active':''}" onclick="changePage(${i})">${i}</button>`; }
    html += `<button class="page-btn" onclick="changePage(${currentPage+1})" ${currentPage===total?'disabled':''}>&gt;</button>`;
    nav.innerHTML = html;
  }

  window.changePage = function(p) { currentPage = p; updateDisplay(); window.scrollTo({top: 500, behavior:'smooth'}); }

  function startFameSlide() {
    const portraits = allData.slice(0, 6);
    function build(id, sIdx) {
      const target = document.getElementById(id);
      const items = portraits.slice(sIdx, sIdx + 3);
      target.innerHTML = items.map((it, idx) => {
        const img = it[7].split(',')[0].trim();
        const imgSrc = img.includes('.') ? img : img + ".jpg";
        return `<div class="fame-slide ${idx===0?'active':''}" onclick="window.openModal(${allData.indexOf(it)})"><img src="${imageBaseURL}${encodeURIComponent(imgSrc)}"></div>`
      }).join('');
      let cur = 0; setInterval(() => { const s = target.querySelectorAll('.fame-slide'); if(s.length>0){ s[cur].classList.remove('active'); cur=(cur+1)%s.length; s[cur].classList.add('active'); } }, 4000);
    }
    build('fameLeft', 0); build('fameRight', 3);
  }

  window.openModal = function(idx) {
    saveRecentView(idx);
    const item = allData[idx];
    currentImages = (item[7]||"").split(',').map(s => s.trim());
    currentImgIdx = 0; isZoomed = false; updateModalImg();
    
    document.getElementById('modalInfo').innerHTML = `
      <div class="info-item"><h2 style="font-size:2.8rem; font-weight:900; color:#2d2926; margin:0;">${getProductName(item)}</h2></div>
      <div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${item[1]}</span></div>
      <div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${item[2]}</span></div>
      <div class="info-item"><span class="info-label">[ 발매일 ]</span><span class="info-value" style="color:#d35400;">${item[6]||'정보없음'}</span></div>
      <div class="info-item"><span class="info-label">[ 크기 ]</span><span class="info-value">${item[5]||'-'}</span></div>
      <div class="info-item"><span class="info-label">[ 가격 ]</span><span class="info-value">${item[4]} KRW</span></div>
      <a href="${item[8]}" target="_blank" class="official-btn">🌐 공식 상세정보 확인하기</a>
    `;
    document.getElementById('detailModal').style.display = 'flex';
  }

  function updateModalImg() {
    const img = document.getElementById('modalImg');
    const name = currentImages[currentImgIdx];
    const imgSrc = name.includes('.') ? name : name + ".jpg";
    img.src = `${imageBaseURL}${encodeURIComponent(imgSrc)}`;
    isZoomed = false; img.classList.remove('zoomed'); img.style.transform = 'scale(1)';
  }

  function saveRecentView(idx) {
    let r = JSON.parse(localStorage.getItem('recentFigures') || '[]');
    r = r.filter(id => id !== idx); r.unshift(idx); if (r.length > 5) r.pop();
    localStorage.setItem('recentFigures', JSON.stringify(r)); renderRecentView();
  }

  function renderRecentView() {
    const r = JSON.parse(localStorage.getItem('recentFigures') || '[]');
    const m = document.getElementById('quick-menu');
    if (r.length === 0) { m.style.display='none'; return; }
    m.style.display='block';
    document.getElementById('quick-items-container').innerHTML = r.map(idx => {
      const it = allData[idx]; if(!it) return '';
      const img = it[7].split(',')[0].trim();
      const imgSrc = img.includes('.') ? img : img + ".jpg";
      return `<div class="quick-item" onclick="window.openModal(${idx})"><img src="${imageBaseURL}${encodeURIComponent(imgSrc)}"></div>`;
    }).join('');
  }

  window.toggleZoom = function() { isZoomed = !isZoomed; document.getElementById('modalImg').classList.toggle('zoomed'); }
  window.handleZoomMove = function(e) { if (!isZoomed) return; const img = document.getElementById('modalImg'); const w = e.currentTarget; const { left, top, width, height } = w.getBoundingClientRect(); const x = ((e.pageX - left - window.scrollX) / width) * 100; const y = ((e.pageY - top - window.scrollY) / height) * 100; img.style.transformOrigin = `${x}% ${y}%`; img.style.transform = 'scale(3.5)'; }
  window.changeImg = function(d) { currentImgIdx = (currentImgIdx + d + currentImages.length) % currentImages.length; updateModalImg(); }
  window.closeModal = function() { document.getElementById('detailModal').style.display = 'none'; document.body.style.overflow = 'auto'; }
  window.toggleFilters = function() { const m = document.getElementById('filterMenu'); m.classList.toggle('collapsed'); document.getElementById('toggleBtn').innerText = m.classList.contains('collapsed') ? '[ 필터 열기 ]' : '[ 필터 접기 ]'; }
  function scrollToTop() { document.getElementById('museum-wrapper').scrollTo({ top: 0, behavior: 'smooth' }); }
  
  init();
</script>
</body>
</html>
