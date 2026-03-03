<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2624340884962829"
     crossorigin="anonymous"></script>

  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 깃허브 찌꺼기 가림막 (위험한 코드 제거) */
    .page-header, .project-name, .project-tagline, .repository-name, .site-header, .site-footer { 
      display: none !important; opacity: 0 !important; position: absolute !important; top: -9999px !important; z-index: -999 !important;
    }
    
    :root { --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7; --modal-bg: rgba(0,0,0,0.98); }
    * { box-sizing: border-box; }
    
    body {
      margin: 0; padding: 0;
      background-color: var(--bg);
    }

    /* 🛡️ [수정됨] 배경을 투명하게 하지 않고 불투명하게 해서 깃허브 테마를 완전히 덮어버림! */
    #museum-wrapper { 
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
      background-color: var(--bg); 
      background-image: radial-gradient(#e5e5e5 1.5px, transparent 1.5px);
      background-size: 24px 24px;
      z-index: 99990; overflow-y: auto; 
      font-family: 'Noto Sans KR', sans-serif; scroll-behavior: smooth; 
    }
    
    /* 레이아웃 */
    .main-title-area { padding: 60px 0 40px; display: flex; align-items: center; justify-content: center; max-width: 1500px; margin: 0 auto; gap: 50px; }
    .hall-of-fame { width: 300px; height: 400px; position: relative; cursor: pointer; border-radius: 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.15); overflow: hidden; background: #fff; flex-shrink: 0; border: 4px solid white; }
    
    /* 📸 명예의 전당 이미지 완벽 중앙 정렬 */
    .fame-slide { position: absolute; inset: 0; background: white; opacity: 0; transition: opacity 1.5s ease; display: flex; align-items: center; justify-content: center; }
    .fame-slide.active { opacity: 1; z-index: 2; }
    .fame-slide img { max-width: 100%; max-height: 100%; object-fit: cover; object-position: center; margin: 0 auto; display: block; }
    
    .center-group { text-align: center; flex: 0 0 450px; position: relative; z-index: 2; }
    .center-group::before {
      content: ''; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
      width: 300px; height: 300px; background: radial-gradient(circle, rgba(250, 176, 5, 0.2) 0%, rgba(255,255,255,0) 70%);
      border-radius: 50%; z-index: -1; filter: blur(20px);
    }

    .header-mascot { width: 180px; height: 180px; border-radius: 50%; background: white; padding: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); margin-bottom: 20px; }
    .museum-title { font-weight: 900; font-size: 4rem; color: var(--dark); margin: 0; cursor: pointer; letter-spacing: -3px; }
    .total-stats-badge { display: inline-block; background: var(--dark); color: var(--primary); padding: 8px 22px; border-radius: 20px; font-size: 1rem; font-weight: 800; margin-top: 15px; }
    
    .sticky-header { background: #2d2926; padding: 20px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 10px 40px rgba(0,0,0,0.4); }
    .control-bar { max-width: 1200px; margin: 0 auto; padding: 0 25px; display: flex; justify-content: space-between; align-items: center; }
    
    .search-box { position: relative; width: 300px; }
    .search-input { width: 100%; padding: 10px 20px 10px 40px; border-radius: 25px; border: 1px solid #555; background: #45403c; color: white; font-family: inherit; transition: 0.3s; }
    .search-input:focus { background: white; color: var(--dark); border-color: var(--primary); outline: none; }
    .search-icon { position: absolute; left: 15px; top: 50%; transform: translateY(-50%); color: #999; font-size: 14px; }
    
    .sort-select { background: #45403c; color: white; border: 1px solid #555; padding: 8px 15px; border-radius: 20px; font-family: inherit; font-size: 0.85rem; cursor: pointer; outline: none; }
    .sort-select:focus { border-color: var(--primary); }
    .toggle-btn { background: none; border: 1px solid #666; color: #999; font-size: 0.75rem; padding: 5px 15px; border-radius: 8px; cursor: pointer; }
    
    #filterMenu {
      position: fixed; top: 83px; left: 0; width: 320px; height: calc(100vh - 83px);
      background: rgba(30, 30, 30, 0.98); backdrop-filter: blur(10px);
      z-index: 9990; border-right: 1px solid #444; box-shadow: 5px 0 25px rgba(0,0,0,0.3);
      transform: translateX(0); transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
      overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 20px;
    }
    #filterMenu.collapsed { transform: translateX(-120%); }

    .index-tab-bar { display: flex; flex-wrap: wrap; gap: 5px; padding-bottom: 15px; border-bottom: 1px solid #555; justify-content: center; position: sticky; top: -20px; background: rgba(30,30,30,0.98); z-index: 10; margin-top: -10px; padding-top: 10px; }
    .index-tab { background: transparent; color: #aaa; border: 1px solid #555; width: 32px; height: 32px; padding: 0; border-radius: 8px; cursor: pointer; font-size: 0.8rem; transition: 0.2s; display: flex; align-items: center; justify-content: center; }
    .index-tab:hover, .index-tab.active { background: var(--primary); color: var(--dark); border-color: var(--primary); font-weight: bold; }
    
    .sub-btns-scroll { display: flex; flex-direction: column; gap: 8px; width: 100%; }
    .filter-btn { background: rgba(255,255,255,0.05); color: #a5a09c; border: 1px solid rgba(255,255,255,0.1); padding: 10px 15px; border-radius: 12px; cursor: pointer; font-size: 0.85rem; transition: 0.2s; text-align: left; display: flex; justify-content: space-between; width: 100%; }
    .filter-btn.active, .filter-btn:hover { background: var(--primary); color: #1a1a1a; font-weight: 800; border-color: var(--primary); }
    
    .filter-section { border-top: 1px solid #555; padding-top: 20px; display: flex; flex-direction: column; gap: 10px; }
    .filter-title { color: var(--primary); font-size: 0.9rem; font-weight: 800; margin-bottom: 5px; }
    .year-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .year-btn { background: #444; color: #ccc; border: 1px solid #555; border-radius: 10px; padding: 8px 0; font-size: 0.8rem; cursor: pointer; transition: 0.2s; }
    .year-btn.active { background: var(--primary); color: var(--dark); font-weight: 800; border-color: var(--primary); }

    .maker-row { display: flex; flex-direction: column; gap: 10px; padding-top: 20px; border-top: 1px solid #555; margin-top: 10px; }
    .maker-label { color: var(--primary); font-size: 0.9rem; font-weight: 800; }
    .filter-count { font-size: 0.7rem; background: rgba(0,0,0,0.3); color: #ccc; padding: 2px 6px; border-radius: 10px; }
    
    #filterMenu::-webkit-scrollbar { width: 6px; }
    #filterMenu::-webkit-scrollbar-thumb { background: #555; border-radius: 3px; }
    
    /* 🚀 3. 필터 열었을 때 중앙 쏠림 해결 */
    .container { max-width: 1550px; margin: 60px auto; padding: 0 45px 150px; min-height: 60vh; transition: margin-left 0.4s, max-width 0.4s; }
    @media (min-width: 1300px) {
      .container.shifted { 
        margin-left: 320px; /* 사이드바 크기(320px)만큼만 밀기 */
        max-width: calc(100% - 320px); /* 남은 영역 꽉 채우기 */
      } 
    }

    /* 🚨 4. 그리드를 남은 영역의 한가운데로 무조건 고정 */
    .grid { 
      display: grid; 
      grid-template-columns: repeat(3, 1fr); 
      gap: 60px; 
      max-width: 1200px; /* 사진들이 너무 양옆으로 퍼지지 않게 제한 */
      margin: 0 auto; /* ★ 이게 핵심! 어떤 상황이든 중앙에 정렬됨 ★ */
    }
    
    .card { background: white; border-radius: 45px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; border: 1px solid #f2f2f2; position: relative; }
    .card:hover { transform: translateY(-20px); box-shadow: 0 45px 90px rgba(0,0,0,0.15); }
    
    .img-box { width: 100%; height: 450px; display: flex; align-items: center; justify-content: center; padding: 40px; background: #f9f9f9; text-align: center; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; transition: opacity 0.3s; }
    
    .content { padding: 30px; text-align: center; border-top: 1px solid #f9f9f9; }
    .char-name { font-size: 1.7rem; font-weight: 800; color: var(--dark); margin-bottom: 15px; }
    .tag-wrap { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
    .tag { font-size: 0.85rem; background: var(--tag-gold); color: #d35400; padding: 6px 14px; border-radius: 12px; font-weight: 800; white-space: nowrap; display: inline-block; }
    .tag.sec { background: #eee; color: #777; }
    .card-badge { position: absolute; top: 25px; left: 25px; background: var(--primary); color: #2d2926; padding: 6px 14px; border-radius: 20px; font-weight: 900; font-size: 0.85rem; box-shadow: 0 5px 15px rgba(250, 176, 5, 0.4); z-index: 5; letter-spacing: 0.5px; }

    /* 페이지네이션 */
    .pagination { display: flex; justify-content: center; align-items: center; gap: 8px; margin-top: 60px; padding-bottom: 40px; }
    .page-btn { min-width: 45px; height: 45px; border-radius: 22.5px; border: 1px solid #ddd; background: white; color: var(--dark); font-weight: 700; cursor: pointer; transition: 0.3s; display: flex; align-items: center; justify-content: center; padding: 0 15px; }
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

    /* 가격비교 박스 */
    .price-compare-box { background: #f1f3f5; border-radius: 20px; padding: 25px; margin-top: 20px; margin-bottom: 20px; border: 1px solid #e9ecef; }
    .price-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 1.1rem; }
    .price-label { color: #868e96; font-weight: 700; font-size: 0.95rem; }
    .price-val-old { text-decoration: line-through; color: #adb5bd; font-size: 1.1rem; }
    .price-val-new { font-weight: 900; font-size: 1.6rem; color: #2d2926; }
    .price-status { font-size: 0.9rem; font-weight: bold; padding: 4px 10px; border-radius: 10px; margin-left: 5px; }

    /* 🆕 소장처 비교 가이드 버튼 스타일 (유지 및 확장) */
    .shop-guide-title { font-size: 1.1rem; font-weight: 800; color: #333; margin-top: 25px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
    .shop-btn-wrap { display: grid; grid-template-columns: 1fr; gap: 10px; margin-bottom: 15px; }
    .shop-btn { display: block; width: 100%; padding: 15px; color: white; text-align: center; text-decoration: none; border-radius: 12px; font-weight: 800; font-size: 1rem; transition: 0.2s; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05); }
    .shop-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.15); filter: brightness(1.05); }
    
    .shop-btn.mania { background: #008BCC; } /* 매니아하우스 블루 */
    .shop-btn.comics { background: #E50914; } /* 코믹스아트 레드 */
    .shop-btn.presso { background: #FFD400; color: #111; } /* 피규어프레소 옐로우 */
    .shop-btn.aladin { background: #EB118A; } /* 알라딘 핑크 */
    
    /* 🆕 해외 직구 버튼 전용 컬러 추가 */
    .shop-btn.amiami { background: #FFCC00; color: #111; } /* 아미아미 옐로우 */
    .shop-btn.mandarake { background: #333333; } /* 만다라케 블랙 */

    .shop-notice { font-size: 0.8rem; color: #888; text-align: center; margin-top: 5px; }

    /* 퀵 메뉴 */
    #quick-menu { position: fixed; right: 30px; top: 150px; width: 110px; background: white; border: 1px solid #ddd; z-index: 9900; text-align: center; border-radius: 12px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.1); display: none; }
    .quick-header { background: #2d2926; color: white; padding: 10px 0; font-size: 0.8rem; font-weight: 700; }
    .quick-list { display: flex; flex-direction: column; }
    .quick-item { width: 100%; height: 110px; padding: 5px; border-bottom: 1px solid #eee; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.2s; }
    .quick-item:hover { background: #f9f9f9; }
    .quick-item img { max-width: 90%; max-height: 90%; object-fit: contain; }
    .top-btn { width: 100%; border: none; background: var(--primary); color: #2d2926; font-weight: 900; padding: 10px 0; cursor: pointer; font-size: 0.9rem; }
    .top-btn:hover { background: #e09e05; }

    /* 로딩 화면 */
    #loading-screen { position: fixed; inset: 0; background: var(--bg); z-index: 999999; display: flex; flex-direction: column; align-items: center; justify-content: center; transition: opacity 0.5s; }
    .loader { width: 60px; height: 60px; border: 5px solid var(--primary); border-bottom-color: transparent; border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 20px; }
    .loading-text { font-weight: 800; color: var(--dark); font-size: 1.2rem; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .no-result { text-align: center; padding: 100px 0; grid-column: 1 / -1; color: #999; }
    .no-result h3 { font-size: 2rem; margin-bottom: 10px; color: #ccc; }

    /* 푸터 */
    .museum-footer { background: #2d2926; color: #888; padding: 60px 20px; margin-top: 80px; border-top: 4px solid var(--primary); text-align: center; font-size: 0.85rem; line-height: 1.6; width: 100%; }
    .footer-content { max-width: 800px; margin: 0 auto; }
    .copyright { color: white; font-weight: 700; font-size: 1rem; margin-bottom: 10px; }
    .disclaimer-box { margin-top: 30px; padding-top: 20px; border-top: 1px solid #444; font-size: 0.8rem; color: #666; }
    .contact-email { margin-top: 15px; color: var(--primary); font-weight: bold; }

    /* 기증 버튼 */
    #donation-btn { position: fixed; bottom: 20px; left: 30px; background: #ff4757; color: white; padding: 15px 25px; border-radius: 50px; font-weight: 900; cursor: pointer; z-index: 99995; box-shadow: 0 10px 30px rgba(255, 71, 87, 0.4); display: flex; align-items: center; gap: 10px; border: none; transition: 0.3s; font-size: 1rem; opacity: 1; }
    #donation-btn:hover { transform: scale(1.1) translateY(-5px); background: #ff6b81; opacity: 1 !important; }
    #donation-btn.faded { opacity: 0.5; transform: scale(0.9); pointer-events: none; }
    .donate-modal-body { text-align: left; padding: 20px; font-family: 'Noto Sans KR', sans-serif; }
    .donate-step { margin-bottom: 20px; padding: 15px; background: #fff5f6; border-radius: 15px; border-left: 5px solid #ff4757; }
    .donate-step h4 { margin: 0 0 10px; color: #ff4757; font-weight: 800; }
    .donate-link-btn { display: block; width: 100%; padding: 18px; background: #ff4757; color: white; text-align: center; text-decoration: none; border-radius: 15px; font-weight: 900; margin-top: 25px; transition: 0.3s; font-size: 1.1rem; box-shadow: 0 5px 15px rgba(255, 71, 87, 0.3); }
    .donate-link-btn:hover { background: #2d2926; transform: translateY(-3px); }
    
    .floating-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; overflow: hidden; pointer-events: none; }
    .float-shape { position: absolute; border-radius: 50%; background: linear-gradient(45deg, var(--primary), #fff); opacity: 0.15; animation: floatMove 20s infinite ease-in-out; filter: blur(5px); }
    .shape-1 { width: 150px; height: 150px; top: 10%; left: 5%; animation-duration: 25s; }
    .shape-2 { width: 200px; height: 200px; top: 60%; right: 10%; animation-duration: 30s; animation-delay: -5s; background: #6c5ce7; }
    .shape-3 { width: 80px; height: 80px; top: 30%; right: 20%; animation-duration: 18s; animation-delay: -10s; background: #ff7675; }
    .shape-4 { width: 120px; height: 120px; bottom: 10%; left: 15%; animation-duration: 22s; animation-delay: -2s; }
    @keyframes floatMove { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-40px) rotate(10deg); } }
    
    /* 모바일 반응형 */
    @media (max-width: 1024px) {
      .grid { grid-template-columns: repeat(2, 1fr); gap: 30px; } 
      .main-title-area { flex-direction: column; gap: 30px; padding-top: 30px; }
      .hall-of-fame { display: none; } 
      .museum-title { font-size: 2.5rem; }
      #quick-menu { display: none !important; }
      .modal-content { height: 80vh; width: 95%; }
      .search-box { width: 200px; }
      #filterMenu { transform: translateX(-120%); }
      #filterMenu.active { transform: translateX(0); }
    }
    @media (max-width: 600px) {
      #filterMenu { width: 85%; top: 130px; height: calc(100vh - 130px); }
      .grid { grid-template-columns: repeat(1, 1fr); }
      .modal-content { flex-direction: column; height: 100vh; border-radius: 0; width: 100%; }
      .modal-img-area { flex: 1; height: 45%; }
      .modal-info-area { flex: 1; padding: 30px; }
      .close-btn { top: 15px; right: 15px; color: #333; z-index: 200; }
      .container { padding: 0 20px 100px; margin: 30px auto; }
      .card-badge { top: 15px; left: 15px; }
      .control-bar { flex-direction: column; gap: 15px; align-items: stretch; }
      .search-box { width: 100%; }
      #donation-btn { bottom: 20px; left: 50%; transform: translateX(-50%); width: auto; white-space: nowrap; }
      #donation-btn:hover { transform: translateX(-50%) scale(1.1); }
    }
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
  <div class="float-shape shape-3"></div>
  <div class="float-shape shape-4"></div>
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
      <h1 class="museum-title" onclick="window.location.href='/'">피규어 박물관</h1>
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
          <option value="dateDesc">🚀 출시 임박순</option>
          <option value="priceHigh">높은 가격순</option>
          <option value="priceLow">낮은 가격순</option>
          <option value="nameAsc">이름 (가나다)</option>
        </select>
        <button class="toggle-btn" onclick="toggleFilters()" id="toggleBtn">[ 필터 열기 ]</button>
      </div>
    </div>

    <div class="bookmark-container collapsed" id="filterMenu">
      
      <div class="filter-section">
        <span class="filter-title">📅 출시 연도 (Release Year)</span>
        <div class="year-grid" id="yearButtons"></div>
      </div>

      <div id="seriesButtons"></div>
      <div class="maker-row" id="makerButtons">
        <span class="maker-label">MAKER</span>
        <div class="sub-btns-scroll" id="makerList"></div>
      </div>
    </div>
  </div>

  <div class="container" id="mainContainer">
    <div id="grid-top"></div> 
    <div id="figureGrid" class="grid"></div>
    
    <div id="pagination" class="pagination"></div>
  </div> 

  <div class="museum-footer">
    <div class="footer-content">
      <p class="copyright">© 2026 Figure Museum Archive. All rights reserved.</p>
      <p class="source-info">모든 데이터는 다양한 온라인 소스에서 수집되었습니다.</p>
      
      <div class="disclaimer-box">
        <p>본 사이트는 수익을 창출하지 않는 <strong>비영리 개인 팬 사이트</strong>입니다.</p>
        <p>게시된 이미지와 정보의 저작권은 각 제조사 및 유통사에 있으며, 악의적인 저작권 침해 의도는 없습니다.</p>
        <p>관계자분의 삭제 요청이 있을 경우, 확인 즉시 해당 콘텐츠를 비공개 처리하겠습니다.</p>
        <p class="contact-email">문의: iiopasd2003@gmail.com</p>
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
  <div class="modal-content" onclick="event.stopPropagation()" style="max-width: 600px; height: auto; flex-direction: column; padding: 40px; border-radius: 40px; z-index: 100000;">
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
  let activeFilter = 'all'; 
  let activeMaker = 'all';
  let activeYear = 'all'; 

  let seriesGrouped = {}; 
  let currentPage = 1;
  const rowsPerPage = 12;

  async function init() {
    try {
      const wrapper = document.getElementById('museum-wrapper');
      const modal = document.getElementById('detailModal');
      const dModal = document.getElementById('donateModal');
      if(document.body && wrapper) document.body.appendChild(wrapper);
      if(document.body && modal) document.body.appendChild(modal);
      if(document.body && dModal) document.body.appendChild(dModal);

      checkScreenSize();
      window.addEventListener('resize', checkScreenSize);

      const response = await fetch(csvURL, { redirect: "follow" });
      const text = await response.text();
      
      const rows = text.split(/\r?\n/).map(row => {
        const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
        return cols.map(c => c ? c.trim().replace(/^"|"$/g, '').replace(/""/g, '"') : "");
      });
      
      allData = rows.slice(1).filter(r => r[8]);
      currentDisplayData = [...allData];
      
      document.getElementById('totalStats').innerText = `총 ${allData.length}점의 명작 전시 중`;
      startFameSlide(); 
      renderFilters(); 
      updateDisplay(); 
      renderRecentView();

      checkUrlParam();

      setTimeout(() => {
        const loader = document.getElementById('loading-screen');
        if(loader) { loader.style.opacity = '0'; setTimeout(() => { loader.style.display = 'none'; }, 500); }
      }, 800);
      
      const wrapperEl = document.getElementById('museum-wrapper');
      let scrollTimer = null;
      wrapperEl.addEventListener('scroll', () => {
         const btn = document.getElementById('donation-btn');
         btn.classList.add('faded');
         if(scrollTimer) clearTimeout(scrollTimer);
         scrollTimer = setTimeout(() => { btn.classList.remove('faded'); }, 300);
      });

    } catch (e) { console.error("에러 발생:", e); }
  }

  function checkScreenSize() {
    const menu = document.getElementById('filterMenu');
    const container = document.getElementById('mainContainer');
    const btn = document.getElementById('toggleBtn');
    
    if (window.innerWidth >= 1300) {
       menu.classList.remove('collapsed');
       container.classList.add('shifted'); 
       btn.innerText = '[ 필터 접기 ]';
    } else {
       menu.classList.add('collapsed'); 
       container.classList.remove('shifted');
       btn.innerText = '[ 필터 열기 ]';
    }
  }

  function getProductName(item) {
    return item[3] ? item[3].trim() : ""; 
  }

  function getHangulInitial(str) {
    const initialChars = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"];
    const charCode = str.charCodeAt(0);
    if (charCode >= 0xAC00 && charCode <= 0xD7A3) {
      const initialIdx = Math.floor((charCode - 0xAC00) / 588); 
      return initialChars[initialIdx];
    }
    if (/^[A-Za-z]/.test(str)) return str.charAt(0).toUpperCase();
    if (/^[0-9]/.test(str)) return "0-9";
    return "ETC";
  }

  function renderFilters() {
    const seriesSet = new Set();
    const makerSet = new Set();
    const yearSet = new Set(); 
    const seriesCount = {};
    const makerCount = {};

    allData.forEach(item => {
      const series = item[2] || "ETC";
      const maker = item[1] || "정보없음";
      
      // 🌟 [추가/수정] V열(item[21])에 영문이 들어오면서 밀린 발매일(W열, item[22])까지 모두 체크하여 에러 방지
      const rawDate = item[22] ? item[22].trim() : (item[21] ? item[21].trim() : ""); 
      let year = "미정";
      if(rawDate.match(/^\d{4}/)) {
        year = rawDate.substring(0, 4);
      }
      yearSet.add(year);

      seriesSet.add(series);
      makerSet.add(maker);
      seriesCount[series] = (seriesCount[series] || 0) + 1;
      makerCount[maker] = (makerCount[maker] || 0) + 1;
    });

    const yearContainer = document.getElementById('yearButtons');
    let yearHtml = `<button class="year-btn active" onclick="filterBy('year', 'all', this)">ALL</button>`;
    Array.from(yearSet).sort().reverse().forEach(y => {
       yearHtml += `<button class="year-btn" onclick="filterBy('year', '${y}', this)">${y}</button>`;
    });
    yearContainer.innerHTML = yearHtml;

    seriesGrouped = {};
    Array.from(seriesSet).sort().forEach(s => {
      const initial = getHangulInitial(s);
      if (!seriesGrouped[initial]) seriesGrouped[initial] = [];
      seriesGrouped[initial].push({ name: s, count: seriesCount[s] });
    });

    const seriesContainer = document.getElementById('seriesButtons');
    let tabHtml = `<div class="index-tab-bar">`;
    tabHtml += `<button class="index-tab active" onclick="renderSeriesButtons('ALL', this)">ALL</button>`;
    
    const sortedKeys = Object.keys(seriesGrouped).sort();
    sortedKeys.forEach(key => {
      tabHtml += `<button class="index-tab" onclick="renderSeriesButtons('${key}', this)">${key}</button>`;
    });
    tabHtml += `</div>`;
    
    tabHtml += `<div class="sub-btns-scroll" id="seriesList"></div>`;
    
    seriesContainer.innerHTML = tabHtml;
    renderSeriesButtons('ALL'); 

    const makerList = document.getElementById('makerList');
    let makerHtml = `<button class="filter-btn active" data-type="maker" onclick="filterBy('maker', 'all', this)">ALL</button>`;
    Array.from(makerSet).sort().forEach(m => {
      makerHtml += `<button class="filter-btn" data-type="maker" onclick="filterBy('maker', '${m}', this)">${m} <span class="filter-count">${makerCount[m]}</span></button>`;
    });
    makerList.innerHTML = makerHtml;
  }

  window.renderSeriesButtons = function(groupKey, btn) {
    if (btn) {
      document.querySelectorAll('.index-tab').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }

    const targetList = document.getElementById('seriesList');
    let html = `<button class="filter-btn ${activeFilter === 'all' ? 'active' : ''}" data-type="series" onclick="filterBy('series', 'all', this)">전체보기</button>`;
    
    let listToShow = [];
    if (groupKey === 'ALL') {
      Object.values(seriesGrouped).forEach(arr => listToShow.push(...arr));
    } else {
      listToShow = seriesGrouped[groupKey] || [];
    }

    listToShow.sort((a,b) => a.name.localeCompare(b.name));
    listToShow.forEach(item => {
       const isActive = activeFilter === item.name ? 'active' : '';
       html += `<button class="filter-btn ${isActive}" data-type="series" onclick="filterBy('series', '${item.name}', this)">${item.name} <span class="filter-count">${item.count}</span></button>`;
    });

    targetList.innerHTML = html;
  }

  window.applyFilters = function() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const sortVal = document.getElementById('sortOrder').value;

    let filtered = allData.filter(item => {
      const seriesMatch = (activeFilter === 'all' || item[2] === activeFilter);
      const makerMatch = (activeMaker === 'all' || item[1] === activeMaker);
      
      // 🌟 [추가/수정] V열(item[21])에 영문이 들어오면서 밀린 발매일(W열, item[22])까지 모두 체크
      const rawDate = item[22] ? item[22].trim() : (item[21] ? item[21].trim() : "");
      let itemYear = "미정";
      if(rawDate.match(/^\d{4}/)) itemYear = rawDate.substring(0, 4);
      const yearMatch = (activeYear === 'all' || itemYear === activeYear);

      const name = getProductName(item).toLowerCase();
      const maker = (item[1] || "").toLowerCase();
      const series = (item[2] || "").toLowerCase();
      const textMatch = name.includes(query) || maker.includes(query) || series.includes(query);
      
      return seriesMatch && makerMatch && yearMatch && textMatch;
    });

    if (sortVal === 'priceHigh') filtered.sort((a, b) => (parseInt(b[5]) || 0) - (parseInt(a[5]) || 0));
    else if (sortVal === 'priceLow') filtered.sort((a, b) => (parseInt(a[5]) || 0) - (parseInt(b[5]) || 0));
    else if (sortVal === 'nameAsc') filtered.sort((a, b) => (getProductName(a)).localeCompare(getProductName(b)));
    else if (sortVal === 'dateDesc') {
       filtered.sort((a, b) => {
         // 🌟 [추가/수정] 정렬 시에도 22번, 21번을 유연하게 체크
         const dateA = a[22] ? a[22] : (a[21] || "0000-00-00");
         const dateB = b[22] ? b[22] : (b[21] || "0000-00-00");
         return dateB.localeCompare(dateA);
       });
    }

    currentDisplayData = filtered;
    currentPage = 1;
    updateDisplay();
  }

  window.filterBy = function(type, value, btn) {
    if (type === 'series') {
      activeFilter = value;
      document.querySelectorAll('#seriesList .filter-btn').forEach(b => b.classList.remove('active'));
    } else if (type === 'maker') {
      activeMaker = value;
      document.querySelectorAll('[data-type="maker"]').forEach(b => b.classList.remove('active'));
    } else if (type === 'year') { 
      activeYear = value;
      const yearBtns = document.getElementById('yearButtons').children;
      for(let b of yearBtns) b.classList.remove('active');
    }
    
    if(btn) btn.classList.add('active');
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
      const img = item[8].split(',')[0].trim();
      const badgeHtml = (item[6] && item[6].toUpperCase() === 'TRUE') ? `<div class="card-badge">LIMITED</div>` : '';

      return `<div class="card" onclick="window.openModal(${allData.indexOf(item)})">
        ${badgeHtml}
        <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg" loading="lazy" alt="${name}"></div>
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
      top: document.querySelector('.main-title-area').offsetHeight + document.querySelector('.sticky-header').offsetHeight - 50,
      behavior: 'smooth'
    });
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
      target.innerHTML = items.map((it, idx) => `<div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="window.openModal(${allData.indexOf(it)})"><img src="${imageBaseURL}${encodeURIComponent(it[8].split(',')[0].trim())}.jpg"></div>`).join('');
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
      if (!item) return '';
      return `<div class="quick-item" onclick="window.openModal(${idx})"><img src="${imageBaseURL}${encodeURIComponent(item[8].split(',')[0].trim())}.jpg"></div>`;
    }).join('');
  }

  function scrollToTop() { document.getElementById('museum-wrapper').scrollTo({ top: 0, behavior: 'smooth' }); }

  window.onpopstate = function(event) {
    if (document.getElementById('detailModal').style.display === 'flex') {
      closeModal(true); 
    } else if (event.state && event.state.id !== undefined) {
      window.openModal(event.state.id, true);
    }
  };

  window.openModal = function(idx, isPopState = false) {
    saveRecentView(idx);
    const item = allData[idx]; 
    if(!item || !item[8]) return;
    
    const name = getProductName(item);
    document.title = `${name} - 피규어 박물관`;
    
    if(!isPopState) {
      const newURL = window.location.protocol + "//" + window.location.host + window.location.pathname + '?id=' + idx;
      const currentId = new URLSearchParams(window.location.search).get('id');
      if (currentId !== String(idx)) {
          window.history.pushState({modalOpen: true, id: idx}, '', newURL);
      }
    }

    currentImages = item[8].split(',').map(s => s.trim()); currentImgIdx = 0; isZoomed = false; updateModalImg();
    
    // 🌍 한글 제조사를 영문으로 변환하는 사전 마법
    const makerTranslate = {
      "굿스마일": "Good Smile Company",
      "알터": "Alter",
      "메가하우스": "MegaHouse",
      "코토부키야": "Kotobukiya",
      "맥스팩토리": "Max Factory",
      "반다이": "Bandai",
      "프링": "FREEing",
      "펫": "Phat!",
      "퓨처": "FuRyu",
      "카도카와": "Kadokawa"
    };

    // 🪄 한글 -> 로마자 간편 변환기 (해외 검색용 예비 장치)
    function koreanToRoman(text) {
      const chosung = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"];
      const jungsung = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"];
      const jongsung = ["", "g", "kk", "gs", "n", "nj", "nh", "d", "l", "lg", "lm", "lb", "ls", "lt", "lp", "lh", "m", "b", "bs", "s", "ss", "ng", "j", "ch", "k", "t", "p", "h"];
      
      let result = "";
      for (let i = 0; i < text.length; i++) {
        let code = text.charCodeAt(i);
        if (code >= 44032 && code <= 55203) {
          let uni = code - 44032;
          let cho = Math.floor(uni / 588);
          let jung = Math.floor((uni - (cho * 588)) / 28);
          let jong = uni % 28;
          result += chosung[cho] + jungsung[jung] + jongsung[jong];
        } else {
          result += text[i];
        }
      }
      return result;
    }

    const rawMaker = item[1] || "";
    const englishMaker = makerTranslate[rawMaker] || rawMaker;
    const searchKeyword = item[14] ? item[14].trim() : name; 
    
    // 특수문자 제거 및 로마자 변환 적용
    const cleanKeyword = searchKeyword.replace(/[\[\]\(\)]/g, '').trim(); 
    const romanKeyword = koreanToRoman(cleanKeyword);
    
    // 🌟 [새로 추가된 핵심 기능] V열(item[21])에 적힌 완벽한 영문 이름을 가져옵니다.
    const englishNameFromV = item[21] ? item[21].trim() : "";
    
    // 🌟 아미아미 검색어 결정
    let amiamiSearchQuery = "";
    // V열에 글자가 있고, 그게 날짜(예: 2023-01) 형식이 아니라면 V열을 최우선으로 사용!
    if (englishNameFromV !== "" && !englishNameFromV.match(/^\d{4}/)) {
        amiamiSearchQuery = englishNameFromV;
    } else {
        // 만약 V열이 비어있다면 기존처럼 [영문 제조사 + 로마자 변환 이름] 사용 (에러 방지용)
        amiamiSearchQuery = englishMaker + " " + romanKeyword;
    }
    
    // 🔗 링크 생성
    const encodedKeyword = encodeURIComponent(searchKeyword);
    const encodedAmiamiQuery = encodeURIComponent(amiamiSearchQuery);
    
    const maniaLink = "https://maniahouse.co.kr/product/search.html?keyword=" + encodedKeyword;
    const comicsLink = "https://comics-art.co.kr/product/search.html?keyword=" + encodedKeyword;
    const pressoLink = "https://figurepresso.com/product/search.html?keyword=" + encodedKeyword;
    const aladinLink = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=" + encodedKeyword;
    
    // 🌟 아미아미/만다라케 링크에 드디어 V열 데이터가 반영됩니다!
    const amiamiLink = "https://www.amiami.com/eng/search/list/?s_keywords=" + encodedAmiamiQuery;
    const mandarakeLink = "https://order.mandarake.co.kr/order/listPage/list.xhtml?keyword=" + encodedAmiamiQuery;
    
    const originalPrice = isNaN(item[5]) ? item[5] : Number(item[5]).toLocaleString() + '원';
    const maniaPrice = item[15] && !isNaN(item[15].replace(/,/g,'')) ? Number(item[15].replace(/,/g,'')).toLocaleString() + '원' : null;
    const diffStatus = item[18] || ""; 
    const donorName = item[20] ? item[20].trim() : ""; 
    
    // 🌟 [안전 장치 추가] 발매일이 V열(21)에서 W열(22)로 밀렸을 경우를 대비
    const releaseDate = (item[22] && item[22].match(/^\d{4}/)) ? item[22] : (item[21] ? item[21] : "정보확인중");

    let statusClass = "";
    if(diffStatus.includes("▲")) statusClass = "price-status up"; 
    else if(diffStatus.includes("▼")) statusClass = "price-status down"; 

    let priceHtml = "";
    if (maniaPrice) {
      priceHtml = `
        <div class="price-compare-box">
          <div class="price-row">
            <span class="price-label">박물관 기록가</span>
            <span class="price-val-old">${originalPrice}</span>
          </div>
          <div class="price-row" style="margin-bottom:0;">
            <span class="price-label">현재 실시간 시세</span>
            <div style="display:flex; align-items:center;">
              <span class="price-val-new">${maniaPrice}</span>
              <span class="${statusClass}" style="${statusClass.includes('up') ? 'color:#e03131' : 'color:#2f9e44'}">${diffStatus}</span>
            </div>
          </div>
        </div>
      `;
    } else {
      priceHtml = `
        <div class="price-compare-box">
          <div class="price-row" style="margin-bottom:0;">
            <span class="price-label">박물관 기록가</span>
            <span class="price-val-old" style="text-decoration:none; color:#2d2926; font-weight:bold;">${originalPrice}</span>
          </div>
        </div>
      `;
    }

    document.getElementById('modalInfo').innerHTML = `
      <div class="info-item"><h2 style="font-size:3.5rem; font-weight:900; color:#2d2926; margin:0; line-height:1.2;">${name}</h2></div>
      
      ${donorName ? `<div class="info-item"><span class="info-label" style="color:#ff4757;">[ 🎁 기증자 ]</span><span class="info-value">${donorName}</span></div>` : ''} 
      
      <div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${item[1] || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${item[2]}</span></div>
      <div class="info-item"><span class="info-label">[ 발매일 ]</span><span class="info-value">${releaseDate}</span></div>
      
      <div class="info-item"><span class="info-label">[ 유형 ]</span><span class="info-value">${item[7] || '-'} (${item[6] === 'TRUE' ? '한정판' : '일반판'})</span></div>
      <div class="info-item"><span class="info-label">[ 크기(mm) ]</span><span class="info-value">${item[4] || '-'}</span></div>
      
      ${priceHtml}

      <div class="shop-guide-title">🔍 국내 소장처 실시간 검색</div>
      <div class="shop-btn-wrap">
        <a href="${maniaLink}" target="_blank" class="shop-btn mania">매니아하우스에서 찾기</a>
        <a href="${comicsLink}" target="_blank" class="shop-btn comics">코믹스아트에서 찾기</a>
        <a href="${pressoLink}" target="_blank" class="shop-btn presso">피규어프레소 확인</a>
        <a href="${aladinLink}" target="_blank" class="shop-btn aladin">알라딘 재고 검색</a>
      </div>

      <div class="shop-guide-title">🌐 해외 직구/중고 시세 확인</div>
      <div class="shop-btn-wrap">
        <a href="${amiamiLink}" target="_blank" class="shop-btn amiami">AmiAmi (신품/중고)</a>
        <a href="${mandarakeLink}" target="_blank" class="shop-btn mandarake">Mandarake (레어템/중고)</a>
      </div>
      <div class="shop-notice">※ V열 전용 데이터가 반영되어 100% 정밀 검색이 지원됩니다!</div>

      <div class="info-item" style="border:none; margin-top:20px;"><span class="info-label">[ 특이사항 ]</span><p style="line-height:1.8; color:#555; font-size:1.2rem; margin:0;">${item[9] || '내용이 없습니다.'}</p></div>
      
      <button onclick="copyLink(${idx})" style="margin-top:20px; padding:10px 20px; background:#f0f0f0; border:1px solid #ccc; border-radius:8px; cursor:pointer; font-weight:bold; color:#555; width:100%;">
        🔗 이 피규어 링크 복사하기
      </button>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  window.toggleZoom = function(e) { isZoomed = !isZoomed; document.getElementById('modalImg').classList.toggle('zoomed'); if (!isZoomed) document.getElementById('modalImg').style.transform = 'scale(1)'; }
  window.handleZoomMove = function(e) { if (!isZoomed) return; const img = document.getElementById('modalImg'); const wrapper = e.currentTarget; const { left, top, width, height } = wrapper.getBoundingClientRect(); const x = ((e.pageX - left - window.scrollX) / width) * 100; const y = ((e.pageY - top - window.scrollY) / height) * 100; img.style.transformOrigin = `${x}% ${y}%`; img.style.transform = 'scale(3.5)'; }
  window.updateModalImg = function() { const img = document.getElementById('modalImg'); img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`; isZoomed = false; img.classList.remove('zoomed'); img.style.transform = 'scale(1)'; }
  window.changeImg = function(dir) { currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; updateModalImg(); }
  
  window.closeModal = function(isBackButton = false) { 
    document.getElementById('detailModal').style.display = 'none'; 
    document.body.style.overflow = 'auto'; 
    document.title = '피규어 박물관'; 

    if (!isBackButton) {
      const cleanURL = window.location.protocol + "//" + window.location.host + window.location.pathname;
      window.history.pushState({}, '', cleanURL);
    }
  }

  window.toggleFilters = function() { 
    const menu = document.getElementById('filterMenu'); 
    const container = document.getElementById('mainContainer');
    menu.classList.toggle('collapsed'); 
    
    if (window.innerWidth >= 1300) {
      container.classList.toggle('shifted');
    }

    document.getElementById('toggleBtn').innerText = menu.classList.contains('collapsed') ? '[ 필터 열기 ]' : '[ 필터 접기 ]'; 
  }

  function checkUrlParam() {
    const urlParams = new URLSearchParams(window.location.search);
    const figureId = urlParams.get('id'); 

    if (figureId !== null && allData[figureId]) {
      console.log("구글 검색 접속: " + figureId + "번 피규어 데이터를 로딩합니다.");
      setTimeout(() => {
        window.openModal(parseInt(figureId), true);
      }, 500); 
    }
  }

  window.copyLink = function(idx) {
    const url = `${window.location.origin}${window.location.pathname}?id=${idx}`;
    navigator.clipboard.writeText(url).then(() => {
      alert("링크가 복사되었습니다! 친구에게 붙여넣기(Ctrl+V) 하세요.");
    }).catch(err => {
      console.error('복사 실패:', err);
      prompt("이 링크를 복사하세요:", url);
    });
  }
  
  window.openDonateModal = function() {
    document.getElementById('donateModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
  window.closeDonateModal = function() {
    document.getElementById('donateModal').style.display = 'none';
    document.body.style.overflow = 'auto';
  }
  
  init();
</script>
</body>
</html>
