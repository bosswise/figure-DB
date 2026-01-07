<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 기본 설정 */
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
    
    /* 레이아웃 */
    .main-title-area { padding: 60px 0 40px; display: flex; align-items: center; justify-content: center; max-width: 1500px; margin: 0 auto; gap: 50px; }
    .hall-of-fame { width: 300px; height: 400px; position: relative; cursor: pointer; border-radius: 40px; box-shadow: 0 20px 50px rgba(0,0,0,0.12); overflow: hidden; background: #fff; flex-shrink: 0; }
    .fame-slide { position: absolute; inset: 0; background: white; opacity: 0; transition: opacity 1.5s ease; }
    .fame-slide.active { opacity: 1; z-index: 2; }
    .fame-slide img { width: 100%; height: 100%; object-fit: cover; }
    .center-group { text-align: center; flex: 0 0 450px; }
    .header-mascot { width: 180px; height: 180px; border-radius: 50%; background: white; padding: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); margin-bottom: 20px; }
    .museum-title { font-weight: 900; font-size: 4rem; color: var(--dark); margin: 0; cursor: pointer; letter-spacing: -3px; }
    .total-stats-badge { display: inline-block; background: var(--dark); color: var(--primary); padding: 8px 22px; border-radius: 20px; font-size: 1rem; font-weight: 800; margin-top: 15px; }
    
    /* 🆕 검색창 및 필터 바 */
    .sticky-header { background: #2d2926; padding: 20px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 10px 40px rgba(0,0,0,0.4); }
    .control-bar { max-width: 1200px; margin: 0 auto; padding: 0 25px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
    
    /* 🆕 검색창 디자인 */
    .search-box { position: relative; width: 300px; }
    .search-input { width: 100%; padding: 10px 20px 10px 40px; border-radius: 25px; border: 1px solid #555; background: #45403c; color: white; font-family: inherit; transition: 0.3s; }
    .search-input:focus { background: white; color: var(--dark); border-color: var(--primary); outline: none; }
    .search-icon { position: absolute; left: 15px; top: 50%; transform: translateY(-50%); color: #999; font-size: 14px; }
    
    .toggle-btn { background: none; border: 1px solid #666; color: #999; font-size: 0.75rem; padding: 5px 15px; border-radius: 8px; cursor: pointer; }
    .bookmark-container { max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding: 0 25px 15px; transition: 0.6s ease; overflow: hidden; max-height: 1000px; }
    .bookmark-container.collapsed { max-height: 0; padding-bottom: 0; }
    .category-row { display: flex; align-items: center; gap: 20px; background: rgba(255,255,255,0.08); padding: 12px 25px; border-radius: 18px; }
    .sub-btns-scroll { display: flex; gap: 10px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 8px 20px; border-radius: 25px; cursor: pointer; font-size: 0.85rem; transition: 0.2s; }
    .filter-btn.active, .filter-btn:hover { background: var(--primary); color: #1a1a1a; font-weight: 800; transform: scale(1.05); }
    
    /* 그리드 */
    .container { max-width: 1550px; margin: 60px auto; padding: 0 45px 150px; min-height: 60vh; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; }
    .card { background: white; border-radius: 45px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; border: 1px solid #f2f2f2; position: relative; }
    .card:hover { transform: translateY(-20px); box-shadow: 0 45px 90px rgba(0,0,0,0.15); }
    .img-box { width: 100%; height: 450px; display: flex; align-items: center; justify-content: center; padding: 40px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 30px; text-align: center; border-top: 1px solid #f9f9f9; }
    .char-name { font-size: 1.7rem; font-weight: 800; color: var(--dark); margin-bottom: 15px; }
    .tag-wrap { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
    .tag { font-size: 0.85rem; background: var(--tag-gold); color: #d35400; padding: 6px 14px; border-radius: 12px; font-weight: 800; white-space: nowrap; display: inline-block; }
    .tag.sec { background: #eee; color: #777; }
    
    /* 모달 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 99999; justify-content: center; align-items: center; padding: 40px; backdrop-filter: blur(30px); }
    .modal-content { background: white; max-width: 1300px; width: 98%; height: 88vh; border-radius: 65px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.4; background: #fff; position: relative; border-right: 1px solid #f0f0f0; overflow: hidden; display: flex; align-items: center; justify-content: center; }
    .modal-img-wrapper { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; cursor: zoom-in; }
    #modalImg { max-width: 90%; max-height: 90%; object-fit: contain; transition: transform 0.1s ease-out; transform-origin: center; }
    #modalImg.zoomed { cursor: zoom-out; transform: scale(3.5); }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 70px; height: 70px; background: rgba(255,255,255,0.98); border: none; border-radius: 50%; font-size: 2.5rem; cursor: pointer; z-index: 10; display: flex; align-items: center; justify-content: center; color: #333; box-shadow: 0 10px 30px rgba(0,0,0,0.15); transition: 0.3s; }
    .nav-btn:hover { background: var(--primary); color: white; transform: translateY(-50%) scale(1.1); }
    .modal-info-area { flex: 0.6; padding: 80px; background: #fafafa; overflow-y: auto; text-align: left; }
    .close-btn { position: absolute; top: 40px; right: 60px; font-size: 4.5rem; cursor: pointer; color: #ddd; z-index: 100; line-height: 0.7; }
    .info-item { margin-bottom: 30px; border-bottom: 2px solid #eee; padding-bottom: 12px; display: flex; flex-direction: column; }
    .info-label { font-size: 1rem; color: var(--primary); font-weight: 900; letter-spacing: 1px; margin-bottom: 8px; }
    .info-value { font-size: 1.7rem; font-weight: 700; color: var(--dark); line-height: 1.4; }

    /* 퀵 메뉴 */
    #quick-menu {
      position: fixed; right: 30px; top: 150px; width: 110px;
      background: white; border: 1px solid #ddd; z-index: 9900;
      text-align: center; border-radius: 12px; overflow: hidden;
      box-shadow: 0 5px 20px rgba(0,0,0,0.1);
      font-family: 'Noto Sans KR', sans-serif;
      display: none; 
    }
    .quick-header { background: #2d2926; color: white; padding: 10px 0; font-size: 0.8rem; font-weight: 700; }
    .quick-list { display: flex; flex-direction: column; }
    .quick-item { width: 100%; height: 110px; padding: 5px; border-bottom: 1px solid #eee; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.2s; }
    .quick-item:hover { background: #f9f9f9; }
    .quick-item img { max-width: 90%; max-height: 90%; object-fit: contain; }
    .top-btn { width: 100%; border: none; background: var(--primary); color: #2d2926; font-weight: 900; padding: 10px 0; cursor: pointer; font-size: 0.9rem; }
    .top-btn:hover { background: #e09e05; }

    /* 로딩 화면 */
    #loading-screen {
      position: fixed; inset: 0; background: var(--bg); z-index: 999999;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      transition: opacity 0.5s;
    }
    .loader {
      width: 60px; height: 60px; border: 5px solid var(--primary);
      border-bottom-color: transparent; border-radius: 50%;
      animation: spin 1s linear infinite; margin-bottom: 20px;
    }
    .loading-text { font-weight: 800; color: var(--dark); font-size: 1.2rem; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    /* 한정판 배지 */
    .card-badge {
      position: absolute; top: 25px; left: 25px;
      background: var(--primary); color: #2d2926;
      padding: 6px 14px; border-radius: 20px;
      font-weight: 900; font-size: 0.85rem;
      box-shadow: 0 5px 15px rgba(250, 176, 5, 0.4);
      z-index: 5; letter-spacing: 0.5px;
    }

    /* 🆕 [신규] 검색 결과 없음 메시지 */
    .no-result { text-align: center; padding: 100px 0; grid-column: 1 / -1; color: #999; }
    .no-result h3 { font-size: 2rem; margin-bottom: 10px; color: #ccc; }
    
    /* 🆕 [신규] 푸터 (사이트 하단 마무리) */
    .museum-footer { text-align: center; padding: 50px 0; color: #999; font-size: 0.9rem; border-top: 1px solid #e0e0e0; margin-top: 50px; }

    /* 모바일 반응형 */
    @media (max-width: 1024px) {
      .grid { grid-template-columns: repeat(2, 1fr); gap: 30px; } 
      .main-title-area { flex-direction: column; gap: 30px; padding-top: 30px; }
      .hall-of-fame { display: none; } 
      .museum-title { font-size: 2.5rem; }
      #quick-menu { display: none !important; }
      .modal-content { height: 80vh; width: 95%; }
      .search-box { width: 200px; }
    }
    @media (max-width: 600px) {
      .grid { grid-template-columns: repeat(1, 1fr); }
      .modal-content { flex-direction: column; height: 100vh; border-radius: 0; width: 100%; }
      .modal-img-area { flex: 1; height: 45%; }
      .modal-info-area { flex: 1; padding: 30px; }
      .close-btn { top: 15px; right: 15px; color: #333; z-index: 200; }
      .container { padding: 0 20px 100px; margin: 30px auto; }
      .card-badge { top: 15px; left: 15px; }
      .control-bar { flex-direction: column; gap: 15px; align-items: stretch; }
      .search-box { width: 100%; }
      .toggle-bar { justify-content: center; }
    }
  </style>
</head>
<body>

<div id="loading-screen">
  <div class="loader"></div>
  <div class="loading-text">명작들을 진열하고 있습니다...</div>
</div>

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
        <input type="text" id="searchInput" class="search-input" placeholder="이름, 제조사 검색..." onkeyup="filterSearch()">
      </div>
      <div class="toggle-bar" style="margin:0; padding:0;">
        <button class="toggle-btn" onclick="toggleFilters()" id="toggleBtn">[ 책갈피 접기 ]</button>
      </div>
    </div>
    <div class="bookmark-container" id="filterMenu"></div>
  </div>

  <div class="container">
    <div id="figureGrid" class="grid"></div>
    
    <div class="museum-footer">
      <p>© 2024 Figure Museum Archive. All rights reserved.</p>
      <p>Data collected from ManiaHouse & Personal Collection.</p>
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
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
  let allData = [], currentImages = [], currentImgIdx = 0, isZoomed = false;
  let activeFilter = 'all'; // 현재 필터 상태 저장

  async function init() {
    try {
      const wrapper = document.getElementById('museum-wrapper');
      const modal = document.getElementById('detailModal');
      if(document.body && wrapper) document.body.appendChild(wrapper);
      if(document.body && modal) document.body.appendChild(modal);

      const response = await fetch(csvURL);
      const text = await response.text();
      
      const rows = text.split(/\r?\n/).map(row => {
        const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
        return cols.map(c => c ? c.trim().replace(/^"|"$/g, '').replace(/""/g, '"') : "");
      });
      
      allData = rows.slice(1).filter(r => r[8]);
      
      document.getElementById('totalStats').innerText = `총 ${allData.length}점의 명작 전시 중`;
      startFameSlide(); renderFilters(); renderGrid(allData);
      renderRecentView();

      setTimeout(() => {
        const loader = document.getElementById('loading-screen');
        if(loader) {
          loader.style.opacity = '0';
          setTimeout(() => { loader.style.display = 'none'; }, 500);
        }
      }, 800);

    } catch (e) { console.error("에러 발생:", e); }
  }

  function getProductName(item) {
    return item[3] ? item[3].trim() : ""; 
  }

  function startFameSlide() {
    const portraits = allData.filter(item => {
        const img = item[8] ? item[8].split(',')[0].trim() : "";
        return img && !(/\d/.test(img));
    });
    const shuffle = portraits.sort(() => 0.5 - Math.random());
    function build(id, startIdx) {
      const target = document.getElementById(id);
      const items = shuffle.slice(startIdx, startIdx + 3);
      if(items.length === 0) return;
      target.innerHTML = items.map((it, idx) => {
          const img = it[8].split(',')[0].trim();
          return `<div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="window.openModal(${allData.indexOf(it)})"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>`;
      }).join('');
      let cur = 0; setInterval(() => { const slides = target.querySelectorAll('.fame-slide'); if(slides.length > 0) { slides[cur].classList.remove('active'); cur = (cur + 1) % slides.length; slides[cur].classList.add('active'); } }, 4000);
    }
    build('fameLeft', 0); build('fameRight', 3);
  }

  function renderFilters() {
    const menuMap = {};
    allData.forEach(item => {
      const cat = item[10] || "ETC"; const series = item[2] || "ETC";
      if (!menuMap[cat]) menuMap[cat] = new Set(); menuMap[cat].add(series);
    });
    const filterMenu = document.getElementById('filterMenu');
    filterMenu.innerHTML = `<div class="category-row"><button class="filter-btn active" onclick="filterBy('all', this)">전체보기</button></div>`;
    for (const [cat, seriesSet] of Object.entries(menuMap)) {
      const row = document.createElement('div'); row.className = 'category-row';
      let icon = cat.includes('GAME') ? '🎮 ' : cat.includes('VOCAL') ? '🎤 ' : '📦 ';
      let html = `<span class="main-label">${icon}${cat.toUpperCase()}</span><div class="sub-btns-scroll">`;
      seriesSet.forEach(s => { html += `<button class="filter-btn" onclick="filterBy('${s}', this)">${s}</button>`; });
      row.innerHTML = html + `</div></div>`;
      filterMenu.appendChild(row);
    }
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    
    // 🆕 데이터가 없을 때 표시할 화면 (Empty State)
    if (data.length === 0) {
      grid.innerHTML = `<div class="no-result"><h3>😢 전시된 피규어가 없습니다.</h3><p>다른 검색어로 찾아보세요.</p></div>`;
      return;
    }

    grid.innerHTML = data.map((item, idx) => {
      const name = getProductName(item); 
      if (!item[8]) return '';
      const img = item[8].split(',')[0].trim();
      
      const badgeHtml = (item[6] && item[6].toUpperCase() === 'TRUE') 
        ? `<div class="card-badge">LIMITED</div>` 
        : '';

      // 🆕 loading="lazy" 속성 추가 (이미지 최적화)
      return `<div class="card" data-series="${item[2]}" onclick="window.openModal(${allData.indexOf(item)})">
        ${badgeHtml}
        <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg" loading="lazy"></div>
        <div class="content">
          <div class="char-name">${name}</div>
          <div class="tag-wrap">
            <span class="tag">#${item[10] || ''}</span>
            <span class="tag sec">#${item[2] || ''}</span>
          </div>
        </div>
      </div>`;
    }).join('');
  }

  // 🆕 실시간 검색 기능 (이름 + 시리즈 + 제조사 검색)
  window.filterSearch = function() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    
    // 현재 선택된 카테고리 필터 안에서 검색
    const filtered = allData.filter(item => {
      // 1. 카테고리 필터 체크
      const seriesMatch = (activeFilter === 'all' || item[2] === activeFilter);
      
      // 2. 검색어 체크 (이름, 제조사, 시리즈, 카테고리 다 뒤짐)
      const name = getProductName(item).toLowerCase();
      const maker = (item[1] || "").toLowerCase();
      const series = (item[2] || "").toLowerCase();
      const textMatch = name.includes(query) || maker.includes(query) || series.includes(query);
      
      return seriesMatch && textMatch;
    });
    
    renderGrid(filtered);
  }

  // 기존 필터 함수 업데이트 (검색창과 연동)
  window.filterBy = function(s, btn) { 
    activeFilter = s; // 현재 필터 상태 저장
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active')); 
    btn.classList.add('active'); 
    
    // 검색창 초기화 (카테고리 바꾸면 검색어 지우는 게 일반적 UX)
    document.getElementById('searchInput').value = '';
    
    const filtered = allData.filter(item => s === 'all' || item[2] === s);
    renderGrid(filtered);
  }

  function saveRecentView(idx) {
    let recent = JSON.parse(localStorage.getItem('recentFigures') || '[]');
    recent = recent.filter(id => id !== idx);
    recent.unshift(idx);
    if (recent.length > 5) recent.pop();
    localStorage.setItem('recentFigures', JSON.stringify(recent));
    renderRecentView();
  }

  function renderRecentView() {
    const recent = JSON.parse(localStorage.getItem('recentFigures') || '[]');
    const container = document.getElementById('quick-items-container');
    const menu = document.getElementById('quick-menu');
    
    if (recent.length === 0) {
      menu.style.display = 'none';
      return;
    }
    menu.style.display = 'block';

    container.innerHTML = recent.map(idx => {
      const item = allData[idx];
      if (!item) return '';
      const img = item[8].split(',')[0].trim();
      return `<div class="quick-item" onclick="window.openModal(${idx})">
        <img src="${imageBaseURL}${encodeURIComponent(img)}.jpg">
      </div>`;
    }).join('');
  }

  function scrollToTop() {
    document.getElementById('museum-wrapper').scrollTo({ top: 0, behavior: 'smooth' });
  }

  window.openModal = function(idx) {
    saveRecentView(idx);
    const item = allData[idx]; 
    if(!item || !item[8]) return;
    currentImages = item[8].split(',').map(s => s.trim()); currentImgIdx = 0; isZoomed = false; updateModalImg();
    const name = getProductName(item);
    
    document.getElementById('modalInfo').innerHTML = `
      <div class="info-item"><h2 style="font-size:3.5rem; font-weight:900; color:#2d2926; margin:0; line-height:1.2;">${name}</h2></div>
      <div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${item[1] || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${item[2]}</span></div>
      <div class="info-item"><span class="info-label">[ 유형 ]</span><span class="info-value">${item[7] || '-'} (${item[6] === 'TRUE' ? '한정판' : '일반판'})</span></div>
      <div class="info-item"><span class="info-label">[ 크기(mm) ]</span><span class="info-value">${item[4] || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 가격 ]</span><span class="info-value">${isNaN(item[5]) ? item[5] : Number(item[5]).toLocaleString() + ' KRW'}</span></div>
      <div class="info-item" style="border:none;"><span class="info-label">[ 특이사항 ]</span><p style="line-height:1.8; color:#555; font-size:1.2rem; margin:0;">${item[9] || '내용이 없습니다.'}</p></div>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  window.toggleZoom = function(e) { isZoomed = !isZoomed; document.getElementById('modalImg').classList.toggle('zoomed'); if (!isZoomed) document.getElementById('modalImg').style.transform = 'scale(1)'; }
  window.handleZoomMove = function(e) { if (!isZoomed) return; const img = document.getElementById('modalImg'); const wrapper = e.currentTarget; const { left, top, width, height } = wrapper.getBoundingClientRect(); const x = ((e.pageX - left - window.scrollX) / width) * 100; const y = ((e.pageY - top - window.scrollY) / height) * 100; img.style.transformOrigin = `${x}% ${y}%`; img.style.transform = 'scale(3.5)'; }
  window.updateModalImg = function() { const img = document.getElementById('modalImg'); img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`; isZoomed = false; img.classList.remove('zoomed'); img.style.transform = 'scale(1)'; }
  window.changeImg = function(dir) { currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; updateModalImg(); }
  window.closeModal = function() { document.getElementById('detailModal').style.display = 'none'; document.body.style.overflow = 'auto'; }
  window.toggleFilters = function() { const menu = document.getElementById('filterMenu'); menu.classList.toggle('collapsed'); document.getElementById('toggleBtn').innerText = menu.classList.contains('collapsed') ? '[ 책갈피 접기 ]' : '[ 카테고리 열기 ]'; }
  // 필터 함수는 위에서 재정의됨
  
  init();
</script>
</body>
</html>
