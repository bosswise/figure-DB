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
    
    /* 🆕 정렬 선택창 스타일 */
    .sort-select {
      background: #45403c; color: white; border: 1px solid #555; padding: 8px 15px; border-radius: 20px;
      font-family: inherit; font-size: 0.85rem; cursor: pointer; outline: none;
    }
    .sort-select:focus { border-color: var(--primary); }

    .toggle-btn { background: none; border: 1px solid #666; color: #999; font-size: 0.75rem; padding: 5px 15px; border-radius: 8px; cursor: pointer; }
    .bookmark-container { max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding: 0 25px 15px; transition: 0.6s ease; overflow: hidden; max-height: 1000px; }
    .bookmark-container.collapsed { max-height: 0; padding-bottom: 0; }
    .category-row { display: flex; align-items: center; gap: 20px; background: rgba(255,255,255,0.08); padding: 12px 25px; border-radius: 18px; }
    
    /* 🛠️ 가로 짤림 해결: 버튼 스크롤 영역 수정 */
    .sub-btns-scroll { 
      display: flex; 
      gap: 10px; 
      overflow-x: auto; 
      white-space: nowrap; 
      scrollbar-width: none; /* 파이어폭스용 */
      -ms-overflow-style: none; /* 인터넷 익스플로러용 */
      flex-wrap: wrap; /* 💡 일정 길이가 넘으면 자동으로 다음 줄로 넘김 */
    }
    .sub-btns-scroll::-webkit-scrollbar { display: none; } /* 크롬용 스크롤바 숨기기 */

    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 8px 20px; border-radius: 25px; cursor: pointer; font-size: 0.85rem; transition: 0.2s; }
    .filter-btn.active, .filter-btn:hover { background: var(--primary); color: #1a1a1a; font-weight: 800; transform: scale(1.05); }

    /* 🆕 제조사 필터 행 스타일 - 짤림 방지 보강 */
    .maker-row { 
      display: flex; 
      align-items: flex-start; /* 높이가 변해도 정렬 유지 */
      gap: 15px; 
      padding: 15px 25px; 
      border-top: 1px solid rgba(255,255,255,0.1); 
      margin-top: 5px; 
    }
    .maker-label { color: #888; font-size: 0.75rem; font-weight: 800; white-space: nowrap; margin-top: 8px; }
    .filter-count { font-size: 0.7rem; background: rgba(0,0,0,0.3); color: #ccc; padding: 2px 6px; border-radius: 10px; margin-left: 5px; }
    
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
    
    /* 🆕 페이지네이션 스타일 최적화 */
    .pagination { display: flex; justify-content: center; align-items: center; gap: 8px; margin-top: 60px; padding-bottom: 40px; }
    .page-btn { 
      min-width: 45px; height: 45px; border-radius: 22.5px; border: 1px solid #ddd; 
      background: white; color: var(--dark); font-weight: 700; cursor: pointer; 
      transition: 0.3s; display: flex; align-items: center; justify-content: center; padding: 0 15px;
    }
    .page-btn:hover { background: #f0f0f0; border-color: #bbb; }
    .page-btn.active { background: var(--dark); color: var(--primary); border-color: var(--dark); }
    .page-btn:disabled { opacity: 0.3; cursor: not-allowed; }

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

    /* 🆕 [추가] 모달 내 하단 버튼 스타일 */
    .official-btn {
      display: block; text-align: center; background: var(--dark); color: var(--primary); 
      padding: 18px; border-radius: 20px; text-decoration: none; font-weight: 900; 
      font-size: 1.1rem; transition: 0.3s; margin-top: 20px; border: 2px solid var(--dark);
    }
    .official-btn:hover { background: white; color: var(--dark); }

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
    
    /* 🆕 [신규] 푸터 (사이트 하단 마무리 - 1인 개발자 멘트 보강) */
    .museum-footer { text-align: center; padding: 80px 0; color: #777; font-size: 0.95rem; border-top: 1px solid #e0e0e0; margin-top: 80px; line-height: 1.8; }
    .footer-dev-text { color: var(--dark); font-weight: 800; margin-bottom: 10px; font-size: 1.1rem; }

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
    <div id="grid-top"></div> 
    <div id="figureGrid" class="grid"></div>
    
    <div id="pagination" class="pagination"></div>
    
    <div class="museum-footer">
      <div class="footer-dev-text">피규어를 너무 좋아하는 1인 개발자입니다 ㅎㅎ</div>
      <p>본 사이트는 개인적인 팬심으로 운영되는 아카이브 공간이며, 수익형 광고가 포함되어 있습니다.</p>
      <p>이미지의 모든 저작권은 ⓒ SHIFT UP, 제조사 및 공식 판매처에 있으며, 인용의 목적으로 사용되었습니다.</p>
      <p>저작권 관련 조치나 삭제 요청은 아래 메일로 연락 주시면 즉시 반영하겠습니다.</p>
      <p style="color:var(--dark); font-weight:900; margin-top:10px;">Contact: [사장님 메일 주소]</p>
      <p style="margin-top:30px; font-size:0.8rem;">© 2026 Figure Museum Archive. All rights reserved.</p>
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
  // 사장님의 구글 시트 게시 URL
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  // 깃허브 이미지 저장 경로
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
  
  let allData = [], currentDisplayData = []; 
  let currentImages = [], currentImgIdx = 0, isZoomed = false;
  let activeFilter = 'all'; 
  let activeMaker = 'all';

  // 페이지네이션 설정
  let currentPage = 1;
  const rowsPerPage = 12;

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
      
      // 인덱스 조정: 사장님 엑셀의 이미지파일명이 들어있는 열(7번 또는 8번)을 체크하여 필터링
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
    } catch (e) { console.error("에러 발생:", e); }
  }

  // 상품 이름 추출 (인덱스 3번)
  function getProductName(item) {
    return item[3] ? item[3].trim() : "이름 정보 없음"; 
  }

  // 🆕 필터 렌더링 (인덱스 수정: 제조사 1번, 검색어/시리즈 2번)
  function renderFilters() {
    const seriesSet = new Set();
    const makerSet = new Set();
    const seriesCount = {};
    const makerCount = {};

    allData.forEach(item => {
      const series = item[2] || "ETC";
      const maker = item[1] || "정보없음";
      seriesSet.add(series);
      makerSet.add(maker);
      seriesCount[series] = (seriesCount[series] || 0) + 1;
      makerCount[maker] = (makerCount[maker] || 0) + 1;
    });

    const seriesContainer = document.getElementById('seriesButtons');
    let seriesHtml = `<div class="category-row"><button class="filter-btn active" data-type="series" onclick="filterBy('series', 'all', this)">전체보기 <span class="filter-count">${allData.length}</span></button><div class="sub-btns-scroll">`;
    Array.from(seriesSet).sort().forEach(s => {
      seriesHtml += `<button class="filter-btn" data-type="series" onclick="filterBy('series', '${s}', this)">${s} <span class="filter-count">${seriesCount[s]}</span></button>`;
    });
    seriesContainer.innerHTML = seriesHtml + `</div></div>`;

    const makerList = document.getElementById('makerList');
    let makerHtml = `<button class="filter-btn active" data-type="maker" onclick="filterBy('maker', 'all', this)">ALL</button>`;
    Array.from(makerSet).sort().forEach(m => {
      makerHtml += `<button class="filter-btn" data-type="maker" onclick="filterBy('maker', '${m}', this)">${m} <span class="filter-count">${makerCount[m]}</span></button>`;
    });
    makerList.innerHTML = makerHtml;
  }

  window.applyFilters = function() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const sortVal = document.getElementById('sortOrder').value;

    let filtered = allData.filter(item => {
      const seriesMatch = (activeFilter === 'all' || item[2] === activeFilter);
      const makerMatch = (activeMaker === 'all' || item[1] === activeMaker);
      const name = getProductName(item).toLowerCase();
      const maker = (item[1] || "").toLowerCase();
      const series = (item[2] || "").toLowerCase();
      const textMatch = name.includes(query) || maker.includes(query) || series.includes(query);
      return seriesMatch && makerMatch && textMatch;
    });

    // 가격 정렬 (인덱스 4번)
    if (sortVal === 'priceHigh') filtered.sort((a, b) => (parseInt(b[4].replace(/,/g, '')) || 0) - (parseInt(a[4].replace(/,/g, '')) || 0));
    else if (sortVal === 'priceLow') filtered.sort((a, b) => (parseInt(a[4].replace(/,/g, '')) || 0) - (parseInt(b[4].replace(/,/g, '')) || 0));
    else if (sortVal === 'nameAsc') filtered.sort((a, b) => (getProductName(a)).localeCompare(getProductName(b)));

    currentDisplayData = filtered;
    currentPage = 1;
    updateDisplay();
  }

  window.filterBy = function(type, value, btn) {
    if (type === 'series') {
      activeFilter = value;
      document.querySelectorAll('[data-type="series"]').forEach(b => b.classList.remove('active'));
    } else {
      activeMaker = value;
      document.querySelectorAll('[data-type="maker"]').forEach(b => b.classList.remove('active'));
    }
    btn.classList.add('active');
    applyFilters();
  }

  function updateDisplay() {
    const totalPages = Math.ceil(currentDisplayData.length / rowsPerPage);
    const start = (currentPage - 1) * rowsPerPage;
    const end = start + rowsPerPage;
    const pagedData = currentDisplayData.slice(start, end);

    renderGrid(pagedData);
    renderPagination(totalPages);
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    if (data.length === 0) {
      grid.innerHTML = `<div class="no-result"><h3>😢 전시된 피규어가 없습니다.</h3><p>다른 필터나 검색어를 사용해 보세요.</p></div>`;
      return;
    }

    grid.innerHTML = data.map((item) => {
      const name = getProductName(item); 
      // 이미지파일명 인덱스 7번 사용
      const imgList = item[7] ? item[7].split(',') : ["default"];
      const img = imgList[0].trim();
      
      return `<div class="card" onclick="window.openModal(${allData.indexOf(item)})">
        <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}" loading="lazy" onerror="this.src='https://via.placeholder.com/300?text=No+Image'"></div>
        <div class="content">
          <div class="char-name">${name}</div>
          <div class="tag-wrap">
            <span class="tag">#${item[1] || '제조사'}</span>
            <span class="tag sec">#${item[2] || '시리즈'}</span>
          </div>
        </div>
      </div>`;
    }).join('');
  }

  function renderPagination(totalPages) {
    const pagination = document.getElementById('pagination');
    if (totalPages <= 1) { pagination.innerHTML = ''; return; }

    let html = '';
    html += `<button class="page-btn" onclick="changePage(1)" ${currentPage === 1 ? 'disabled' : ''}>&lt;&lt;</button>`;
    html += `<button class="page-btn" onclick="changePage(${currentPage - 1})" ${currentPage === 1 ? 'disabled' : ''}>&lt;</button>`;

    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, startPage + 4);
    if (endPage - startPage < 4) startPage = Math.max(1, endPage - 4);

    for (let i = startPage; i <= endPage; i++) {
      if(i > 0) html += `<button class="page-btn ${i === currentPage ? 'active' : ''}" onclick="changePage(${i})">${i}</button>`;
    }

    html += `<button class="page-btn" onclick="changePage(${currentPage + 1})" ${currentPage === totalPages ? 'disabled' : ''}>&gt;</button>`;
    html += `<button class="page-btn" onclick="changePage(${totalPages})" ${currentPage === totalPages ? 'disabled' : ''}>&gt;&gt;</button>`;
    pagination.innerHTML = html;
  }

  window.changePage = function(page) {
    currentPage = page;
    updateDisplay();
    document.getElementById('museum-wrapper').scrollTo({
      top: 500,
      behavior: 'smooth'
    });
  }

  function startFameSlide() {
    const portraits = allData.slice(0, 10); // 상위 10개로 슬라이드 구성
    const shuffle = portraits.sort(() => 0.5 - Math.random());
    function build(id, startIdx) {
      const target = document.getElementById(id);
      const items = shuffle.slice(startIdx, startIdx + 3);
      if(items.length === 0) return;
      target.innerHTML = items.map((it, idx) => {
        const imgName = it[7] ? it[7].split(',')[0].trim() : "";
        return `<div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="window.openModal(${allData.indexOf(it)})"><img src="${imageBaseURL}${encodeURIComponent(imgName)}"></div>`
      }).join('');
      let cur = 0; setInterval(() => { const slides = target.querySelectorAll('.fame-slide'); if(slides.length > 0) { slides[cur].classList.remove('active'); cur = (cur + 1) % slides.length; slides[cur].classList.add('active'); } }, 4000);
    }
    build('fameLeft', 0); build('fameRight', 3);
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
    if (recent.length === 0) { menu.style.display = 'none'; return; }
    menu.style.display = 'block';
    container.innerHTML = recent.map(idx => {
      const item = allData[idx];
      if (!item || !item[7]) return '';
      return `<div class="quick-item" onclick="window.openModal(${idx})"><img src="${imageBaseURL}${encodeURIComponent(item[7].split(',')[0].trim())}"></div>`;
    }).join('');
  }

  function scrollToTop() { document.getElementById('museum-wrapper').scrollTo({ top: 0, behavior: 'smooth' }); }

  // 🖱️ 사장님의 새로운 데이터 인덱스에 맞춘 모달 업데이트
  window.openModal = function(idx) {
    saveRecentView(idx);
    const item = allData[idx]; 
    if(!item || !item[7]) return;

    // 인덱스 정의
    const name = item[3];
    const brand = item[1];
    const series = item[2];
    const price = item[4];
    const size = item[5];
    const releaseDate = item[6]; // 발매일 (6번)
    const imgStr = item[7]; // 이미지파일명 (7번)
    const officialLink = item[8]; // 링크 (8번)

    currentImages = imgStr.split(',').map(s => s.trim()); 
    currentImgIdx = 0; isZoomed = false; updateModalImg();

    document.getElementById('modalInfo').innerHTML = `
      <div class="info-item"><h2 style="font-size:3.2rem; font-weight:900; color:#2d2926; margin:0; line-height:1.2;">${name}</h2></div>
      <div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${brand || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${series || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 발매일 ]</span><span class="info-value" style="color:#d35400;">${releaseDate || '정보없음'}</span></div>
      <div class="info-item"><span class="info-label">[ 크기 ]</span><span class="info-value">${size || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 가격 ]</span><span class="info-value">${price} KRW</span></div>
      
      <a href="${officialLink}" target="_blank" class="official-btn">🌐 공식 판매처 / 상세정보 보기</a>
      
      <div style="margin-top:30px; text-align:center; color:#999; font-size:0.85rem;">
        본 저작권은 제조사 및 판매처에 있으며,<br>문제가 될 시 즉시 조치하겠습니다. 메일로 연락주세요!
      </div>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  window.toggleZoom = function(e) { isZoomed = !isZoomed; document.getElementById('modalImg').classList.toggle('zoomed'); if (!isZoomed) document.getElementById('modalImg').style.transform = 'scale(1)'; }
  window.handleZoomMove = function(e) { if (!isZoomed) return; const img = document.getElementById('modalImg'); const wrapper = e.currentTarget; const { left, top, width, height } = wrapper.getBoundingClientRect(); const x = ((e.pageX - left - window.scrollX) / width) * 100; const y = ((e.pageY - top - window.scrollY) / height) * 100; img.style.transformOrigin = `${x}% ${y}%`; img.style.transform = 'scale(3.5)'; }
  window.updateModalImg = function() { 
    const img = document.getElementById('modalImg'); 
    img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}`; 
    isZoomed = false; 
    img.classList.remove('zoomed'); 
    img.style.transform = 'scale(1)'; 
  }
  window.changeImg = function(dir) { currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; updateModalImg(); }
  window.closeModal = function() { document.getElementById('detailModal').style.display = 'none'; document.body.style.overflow = 'auto'; }
  window.toggleFilters = function() { 
    const menu = document.getElementById('filterMenu'); 
    menu.classList.toggle('collapsed'); 
    document.getElementById('toggleBtn').innerText = menu.classList.contains('collapsed') ? '[ 필터 열기 ]' : '[ 필터 접기 ]'; 
  }
  
  init();
</script>
</body>
</html>
