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
    
    /* 🆕 검색창 및 필터 바 (헤더) */
    .sticky-header { background: #2d2926; padding: 20px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 10px 40px rgba(0,0,0,0.4); }
    .control-bar { max-width: 1200px; margin: 0 auto; padding: 0 25px; display: flex; justify-content: space-between; align-items: center; }
    
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
    
    /* 🚀 [업그레이드] 필터 메뉴를 사이드바 형태로 변경 */
    #filterMenu {
      position: fixed;
      top: 83px; 
      left: 0;
      width: 320px; 
      height: calc(100vh - 83px); 
      background: rgba(30, 30, 30, 0.98); 
      backdrop-filter: blur(10px);
      z-index: 9990;
      border-right: 1px solid #444;
      box-shadow: 5px 0 25px rgba(0,0,0,0.3);
      transform: translateX(0);
      transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
      overflow-y: auto;
      padding: 20px;
      display: flex;
      flex-direction: column; 
      gap: 20px;
    }

    #filterMenu.collapsed { transform: translateX(-120%); }

    /* 사이드바 내부 구성 */
    .index-tab-bar { 
      display: flex; flex-wrap: wrap; gap: 5px; 
      padding-bottom: 15px; border-bottom: 1px solid #555;
      justify-content: center;
      position: sticky; top: -20px; background: rgba(30,30,30,0.98); z-index: 10;
      margin-top: -10px; padding-top: 10px;
    }
    .index-tab { 
      background: transparent; color: #aaa; border: 1px solid #555; 
      width: 32px; height: 32px; padding: 0;
      border-radius: 8px; cursor: pointer; 
      font-size: 0.8rem; transition: 0.2s; 
      display: flex; align-items: center; justify-content: center;
    }
    .index-tab:hover, .index-tab.active { background: var(--primary); color: var(--dark); border-color: var(--primary); font-weight: bold; }

    .sub-btns-scroll { display: flex; flex-direction: column; gap: 8px; width: 100%; }

    .filter-btn { 
      background: rgba(255,255,255,0.05); color: #a5a09c; 
      border: 1px solid rgba(255,255,255,0.1); 
      padding: 10px 15px; border-radius: 12px; 
      cursor: pointer; font-size: 0.85rem; transition: 0.2s; 
      text-align: left; display: flex; justify-content: space-between;
      width: 100%;
    }
    .filter-btn.active, .filter-btn:hover { background: var(--primary); color: #1a1a1a; font-weight: 800; border-color: var(--primary); }

    .maker-row { display: flex; flex-direction: column; gap: 10px; padding-top: 20px; border-top: 1px solid #555; margin-top: 10px; }
    .maker-label { color: var(--primary); font-size: 0.9rem; font-weight: 800; }
    .filter-count { font-size: 0.7rem; background: rgba(0,0,0,0.3); color: #ccc; padding: 2px 6px; border-radius: 10px; }
    
    #filterMenu::-webkit-scrollbar { width: 6px; }
    #filterMenu::-webkit-scrollbar-thumb { background: #555; border-radius: 3px; }
    
    /* 그리드 */
    .container { max-width: 1550px; margin: 60px auto; padding: 0 45px 150px; min-height: 60vh; transition: margin-left 0.4s; }
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

    /* 퀵 메뉴 */
    #quick-menu {
      position: fixed; right: 30px; top: 150px; width: 110px;
      background: white; border: 1px solid #ddd; z-index: 9900;
      text-align: center; border-radius: 12px; overflow: hidden;
      box-shadow: 0 5px 20px rgba(0,0,0,0.1); display: none; 
    }
    .quick-header { background: #2d2926; color: white; padding: 10px 0; font-size: 0.8rem; font-weight: 700; }
    .quick-list { display: flex; flex-direction: column; }
    .quick-item { width: 100%; height: 110px; padding: 5px; border-bottom: 1px solid #eee; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.2s; }
    .quick-item:hover { background: #f9f9f9; }
    .quick-item img { max-width: 90%; max-height: 90%; object-fit: contain; }
    .top-btn { width: 100%; border: none; background: var(--primary); color: #2d2926; font-weight: 900; padding: 10px 0; cursor: pointer; font-size: 0.9rem; }

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

    /* 장식 요소 */
    body { background-color: var(--bg); background-image: radial-gradient(#e5e5e5 1.5px, transparent 1.5px); background-size: 24px 24px; }
    .floating-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; overflow: hidden; pointer-events: none; }
    .float-shape { position: absolute; border-radius: 50%; background: linear-gradient(45deg, var(--primary), #fff); opacity: 0.15; animation: floatMove 20s infinite ease-in-out; filter: blur(5px); }
    .shape-1 { width: 150px; height: 150px; top: 10%; left: 5%; animation-duration: 25s; }
    .shape-2 { width: 200px; height: 200px; top: 60%; right: 10%; animation-duration: 30s; background: #6c5ce7; }
    @keyframes floatMove { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-40px) rotate(10deg); } }

    /* 푸터 */
    .museum-footer { background: #2d2926; color: #888; padding: 60px 20px; margin-top: 80px; border-top: 4px solid var(--primary); text-align: center; font-size: 0.85rem; line-height: 1.6; width: 100%; }
    .footer-content { max-width: 800px; margin: 0 auto; }
    .copyright { color: white; font-weight: 700; font-size: 1rem; margin-bottom: 10px; }
    .disclaimer-box { margin-top: 30px; padding-top: 20px; border-top: 1px solid #444; font-size: 0.8rem; }

    /* 🎁 기증 시스템 */
    #donation-btn {
      position: fixed; bottom: 20px; left: 30px; background: #ff4757; color: white;
      padding: 15px 25px; border-radius: 50px; font-weight: 900; cursor: pointer;
      z-index: 9900; box-shadow: 0 10px 30px rgba(255, 71, 87, 0.4);
      display: flex; align-items: center; gap: 10px; border: none; transition: 0.3s; font-size: 1rem;
    }
    #donation-btn:hover { transform: scale(1.1) translateY(-5px); background: #ff6b81; }

    .donate-modal-body { text-align: left; padding: 20px; }
    .donate-step { margin-bottom: 20px; padding: 15px; background: #fff5f6; border-radius: 15px; border-left: 5px solid #ff4757; }
    .donate-step h4 { margin: 0 0 10px; color: #ff4757; font-weight: 800; }
    .donate-step p { margin: 0; color: #555; font-size: 0.95rem; line-height: 1.6; }
    
    .donate-link-btn { 
      display: block; width: 100%; padding: 18px; background: #ff4757; color: white; 
      text-align: center; text-decoration: none; border-radius: 15px; font-weight: 900; 
      margin-top: 25px; transition: 0.3s; font-size: 1.1rem; box-shadow: 0 5px 15px rgba(255, 71, 87, 0.3);
    }
    .donate-link-btn:hover { background: #2d2926; transform: translateY(-3px); }
  </style>
</head>
<body>

<div id="loading-screen">
  <div class="loader"></div>
  <div class="loading-text">명작들을 진열하고 있습니다...</div>
</div>

<div class="floating-bg">
  <div class="float-shape shape-1"></div>
  <div class="float-shape shape-2"></div>
</div>

<button id="donation-btn" onclick="openDonateModal()">
  <span>🎁</span> 명작 기증하기
</button>

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
  </div> 

  <div class="museum-footer">
    <div class="footer-content">
      <p class="copyright">© 2026 Figure Museum Archive. All rights reserved.</p>
      <div class="disclaimer-box">
        <p>본 사이트는 비영리 개인 팬 사이트입니다. 삭제 요청 시 즉시 처리하겠습니다.</p>
        <p class="contact-email">문의: bosswise@example.com</p>
      </div>
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

<div id="donateModal" class="modal" onclick="closeDonateModal()">
  <div class="modal-content" onclick="event.stopPropagation()" style="max-width: 600px; height: auto; flex-direction: column; padding: 40px; border-radius: 40px;">
    <span class="close-btn" onclick="closeDonateModal()">&times;</span>
    <h2 style="font-weight: 900; font-size: 2.5rem; color: #2d2926; margin-bottom: 30px;">🎁 명작 기증 시스템</h2>
    
    <div class="donate-modal-body">
      <div class="donate-step">
        <h4>1. 기증 대상</h4>
        <p>박물관에 아직 등록되지 않은 소장용 피규어 정보를 제보해 주세요.</p>
      </div>
      <div class="donate-step">
        <h4>2. 기증 보상</h4>
        <p>기증해주신 정보는 사장님 검수 후 DB에 등록되며, 기증자님의 닉네임이 기록됩니다.</p>
      </div>
      
      <a href="https://docs.google.com/forms/d/e/1FAIpQLSdfyj75_8hnUXpRxQAeeDqFuDLhg_3WHNJYXz26VJR1in7aDQ/viewform?usp=header" target="_blank" class="donate-link-btn">명작 기증 폼 작성하러 가기 🚀</a>
    </div>
  </div>
</div>

<script>
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = window.location.origin + window.location.pathname.replace('index.html', '') + "images/";
  
  let allData = [], currentDisplayData = []; 
  let currentImages = [], currentImgIdx = 0, isZoomed = false;
  let activeFilter = 'all', activeMaker = 'all';
  let seriesGrouped = {}, currentPage = 1;
  const rowsPerPage = 12;

  async function init() {
    try {
      const response = await fetch(csvURL);
      const text = await response.text();
      const rows = text.split(/\r?\n/).map(row => {
        const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
        return cols.map(c => c ? c.trim().replace(/^"|"$/g, '').replace(/""/g, '"') : "");
      });
      allData = rows.slice(1).filter(r => r[8]);
      currentDisplayData = [...allData];
      document.getElementById('totalStats').innerText = `총 ${allData.length}점의 명작 전시 중`;
      startFameSlide(); renderFilters(); updateDisplay(); renderRecentView(); checkUrlParam();
      setTimeout(() => { document.getElementById('loading-screen').style.opacity = '0'; setTimeout(() => { document.getElementById('loading-screen').style.display = 'none'; }, 500); }, 800);
    } catch (e) { console.error(e); }
  }

  function getProductName(item) { return item[3] ? item[3].trim() : ""; }
  function getHangulInitial(str) {
    const initialChars = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"];
    const charCode = str.charCodeAt(0);
    if (charCode >= 0xAC00 && charCode <= 0xD7A3) return initialChars[Math.floor((charCode - 0xAC00) / 588)];
    return /^[A-Za-z]/.test(str) ? str.charAt(0).toUpperCase() : "ETC";
  }

  function renderFilters() {
    const seriesSet = new Set(), makerSet = new Set(), seriesCount = {}, makerCount = {};
    allData.forEach(item => {
      const series = item[2] || "ETC", maker = item[1] || "정보없음";
      seriesSet.add(series); makerSet.add(maker);
      seriesCount[series] = (seriesCount[series] || 0) + 1;
      makerCount[maker] = (makerCount[maker] || 0) + 1;
    });
    seriesGrouped = {};
    Array.from(seriesSet).sort().forEach(s => {
      const initial = getHangulInitial(s);
      if (!seriesGrouped[initial]) seriesGrouped[initial] = [];
      seriesGrouped[initial].push({ name: s, count: seriesCount[s] });
    });
    const seriesContainer = document.getElementById('seriesButtons');
    let tabHtml = `<div class="index-tab-bar"><button class="index-tab active" onclick="renderSeriesButtons('ALL', this)">ALL</button>`;
    Object.keys(seriesGrouped).sort().forEach(key => { tabHtml += `<button class="index-tab" onclick="renderSeriesButtons('${key}', this)">${key}</button>`; });
    tabHtml += `</div><div class="sub-btns-scroll" id="seriesList"></div>`;
    seriesContainer.innerHTML = tabHtml; renderSeriesButtons('ALL');
    let makerHtml = `<button class="filter-btn active" data-type="maker" onclick="filterBy('maker', 'all', this)">ALL</button>`;
    Array.from(makerSet).sort().forEach(m => { makerHtml += `<button class="filter-btn" data-type="maker" onclick="filterBy('maker', '${m}', this)">${m} <span class="filter-count">${makerCount[m]}</span></button>`; });
    document.getElementById('makerList').innerHTML = makerHtml;
  }

  window.renderSeriesButtons = function(groupKey, btn) {
    if (btn) { document.querySelectorAll('.index-tab').forEach(b => b.classList.remove('active')); btn.classList.add('active'); }
    let html = `<button class="filter-btn ${activeFilter === 'all' ? 'active' : ''}" data-type="series" onclick="filterBy('series', 'all', this)">전체보기</button>`;
    let listToShow = (groupKey === 'ALL') ? [].concat(...Object.values(seriesGrouped)) : seriesGrouped[groupKey] || [];
    listToShow.sort((a,b) => a.name.localeCompare(b.name)).forEach(item => { html += `<button class="filter-btn ${activeFilter === item.name ? 'active' : ''}" data-type="series" onclick="filterBy('series', '${item.name}', this)">${item.name} <span class="filter-count">${item.count}</span></button>`; });
    document.getElementById('seriesList').innerHTML = html;
  }

  window.applyFilters = function() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const sortVal = document.getElementById('sortOrder').value;
    let filtered = allData.filter(item => {
      const name = getProductName(item).toLowerCase();
      return (activeFilter === 'all' || item[2] === activeFilter) && (activeMaker === 'all' || item[1] === activeMaker) && (name.includes(query) || (item[1]||"").toLowerCase().includes(query));
    });
    if (sortVal === 'priceHigh') filtered.sort((a, b) => (parseInt(b[5]) || 0) - (parseInt(a[5]) || 0));
    else if (sortVal === 'priceLow') filtered.sort((a, b) => (parseInt(a[5]) || 0) - (parseInt(b[5]) || 0));
    else if (sortVal === 'nameAsc') filtered.sort((a, b) => getProductName(a).localeCompare(getProductName(b)));
    currentDisplayData = filtered; currentPage = 1; updateDisplay();
  }

  window.filterBy = function(type, value, btn) {
    if (type === 'series') { activeFilter = value; document.querySelectorAll('#seriesList .filter-btn').forEach(b => b.classList.remove('active')); }
    else { activeMaker = value; document.querySelectorAll('[data-type="maker"]').forEach(b => b.classList.remove('active')); }
    if(btn) btn.classList.add('active'); applyFilters();
  }

  function updateDisplay() {
    const totalPages = Math.ceil(currentDisplayData.length / rowsPerPage);
    renderGrid(currentDisplayData.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage)); renderPagination(totalPages);
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    if (data.length === 0) { grid.innerHTML = `<div class="no-result"><h3>😢 전시된 피규어가 없습니다.</h3></div>`; return; }
    grid.innerHTML = data.map((item) => {
      const img = item[8].split(',')[0].trim();
      return `<div class="card" onclick="window.openModal(${allData.indexOf(item)})"><div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg" loading="lazy"></div><div class="content"><div class="char-name">${getProductName(item)}</div><div class="tag-wrap"><span class="tag">#${item[10] || ''}</span><span class="tag sec">#${item[2] || ''}</span></div></div></div>`;
    }).join('');
  }

  function renderPagination(totalPages) {
    const pagination = document.getElementById('pagination');
    if (totalPages <= 1) { pagination.innerHTML = ''; return; }
    let html = `<button class="page-btn" onclick="changePage(1)" ${currentPage === 1 ? 'disabled' : ''}>&lt;&lt;</button>`;
    for (let i = Math.max(1, currentPage - 2); i <= Math.min(totalPages, Math.max(1, currentPage - 2) + 4); i++) html += `<button class="page-btn ${i === currentPage ? 'active' : ''}" onclick="changePage(${i})">${i}</button>`;
    html += `<button class="page-btn" onclick="changePage(${totalPages})" ${currentPage === totalPages ? 'disabled' : ''}>&gt;&gt;</button>`;
    pagination.innerHTML = html;
  }

  window.changePage = function(page) { currentPage = page; updateDisplay(); window.scrollTo({top: 0, behavior: 'smooth'}); }

  function startFameSlide() {
    const portraits = allData.filter(item => item[8] && !(/\d/.test(item[8].split(',')[0].trim()))).sort(() => 0.5 - Math.random());
    function build(id, startIdx) {
      const target = document.getElementById(id), items = portraits.slice(startIdx, startIdx + 3); if(items.length === 0) return;
      target.innerHTML = items.map((it, idx) => `<div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="window.openModal(${allData.indexOf(it)})"><img src="${imageBaseURL}${encodeURIComponent(it[8].split(',')[0].trim())}.jpg"></div>`).join('');
      let cur = 0; setInterval(() => { const slides = target.querySelectorAll('.fame-slide'); slides[cur].classList.remove('active'); cur = (cur + 1) % slides.length; slides[cur].classList.add('active'); }, 4000);
    }
    build('fameLeft', 0); build('fameRight', 3);
  }

  function renderRecentView() {
    const recent = JSON.parse(localStorage.getItem('recentFigures') || '[]');
    document.getElementById('quick-menu').style.display = recent.length ? 'block' : 'none';
    document.getElementById('quick-items-container').innerHTML = recent.map(idx => `<div class="quick-item" onclick="window.openModal(${idx})"><img src="${imageBaseURL}${encodeURIComponent(allData[idx][8].split(',')[0].trim())}.jpg"></div>`).join('');
  }

  window.openModal = function(idx) {
    let recent = JSON.parse(localStorage.getItem('recentFigures') || '[]'); recent = [idx, ...recent.filter(id => id !== idx)].slice(0, 5); localStorage.setItem('recentFigures', JSON.stringify(recent)); renderRecentView();
    const item = allData[idx]; currentImages = item[8].split(',').map(s => s.trim()); currentImgIdx = 0; updateModalImg();
    document.getElementById('modalInfo').innerHTML = `<div class="info-item"><h2>${getProductName(item)}</h2></div><div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${item[1] || '-'}</span></div><div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${item[2]}</span></div><div class="info-item"><span class="info-label">[ 가격 ]</span><span class="info-value">${isNaN(item[5]) ? item[5] : Number(item[5]).toLocaleString() + ' KRW'}</span></div>`;
    document.getElementById('detailModal').style.display = 'flex';
  }

  window.toggleZoom = function() { isZoomed = !isZoomed; document.getElementById('modalImg').classList.toggle('zoomed'); }
  window.handleZoomMove = function(e) { if (!isZoomed) return; const { left, top, width, height } = e.currentTarget.getBoundingClientRect(); document.getElementById('modalImg').style.transformOrigin = `${((e.pageX - left - window.scrollX) / width) * 100}% ${((e.pageY - top - window.scrollY) / height) * 100}%`; }
  window.updateModalImg = function() { document.getElementById('modalImg').src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`; isZoomed = false; document.getElementById('modalImg').classList.remove('zoomed'); }
  window.changeImg = function(dir) { currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; updateModalImg(); }
  window.closeModal = function() { document.getElementById('detailModal').style.display = 'none'; }
  window.toggleFilters = function() { document.getElementById('filterMenu').classList.toggle('collapsed'); }
  window.openDonateModal = function() { document.getElementById('donateModal').style.display = 'flex'; }
  window.closeDonateModal = function() { document.getElementById('donateModal').style.display = 'none'; }
  function checkUrlParam() { const id = new URLSearchParams(window.location.search).get('id'); if (id && allData[id]) setTimeout(() => window.openModal(id), 500); }
  function scrollToTop() { document.getElementById('museum-wrapper').scrollTo({ top: 0, behavior: 'smooth' }); }
  
  init();
</script>
</body>
</html>
