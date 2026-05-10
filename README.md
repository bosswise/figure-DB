<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- ✅ [수정 1] 페이지 제목 - 키워드 포함, 명확한 사이트 설명 -->
  <title>피규어 박물관 - 넨도로이드·피그마·스케일 피규어 정보 & 시세 아카이브</title>

  <!-- ✅ [수정 2] 메타 디스크립션 - 구체적이고 가치 있는 설명 -->
  <meta name="description" content="2,700점 이상의 피규어 정보를 한눈에! 넨도로이드, 피그마, 스케일 피규어의 발매일, 가격, 실시간 시세를 확인하고 국내외 구매처를 비교하세요. 굿스마일, 알터, 맥스팩토리 등 주요 제조사 완벽 정리.">
  <meta name="keywords" content="피규어, 넨도로이드, 피그마, 스케일 피규어, 피규어 시세, 피규어 정보, 굿스마일, 알터, 맥스팩토리, 피규어 박물관, 피규어 아카이브, 피규어 가격">
  <meta name="author" content="피규어 박물관">
  <meta name="robots" content="index, follow">

  <!-- ✅ [수정 3] Open Graph 태그 - SNS 공유 최적화 -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="피규어 박물관 - 넨도로이드·피그마·스케일 피규어 정보 & 시세 아카이브">
  <meta property="og:description" content="2,700점 이상의 피규어 정보를 한눈에! 넨도로이드, 피그마, 스케일 피규어의 발매일, 가격, 실시간 시세를 확인하세요.">
  <meta property="og:url" content="https://figure-museum.co.kr/">
  <meta property="og:image" content="https://bosswise.github.io/figure-DB/images/mascot.png">
  <meta property="og:site_name" content="피규어 박물관">
  <meta property="og:locale" content="ko_KR">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="피규어 박물관 - 피규어 정보 & 시세 아카이브">
  <meta name="twitter:description" content="2,700점 이상의 피규어 정보를 한눈에 확인하세요.">
  <meta name="twitter:image" content="https://bosswise.github.io/figure-DB/images/mascot.png">

  <!-- ✅ [수정 4] Canonical URL -->
  <link rel="canonical" href="https://figure-museum.co.kr/">

  <!-- ✅ [수정 5] 구글 애드센스 스크립트 (기존 유지) -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2624340884962829"
     crossorigin="anonymous"></script>

  <!-- ✅ [수정 6] 구조화 데이터 (JSON-LD) - 구글이 사이트를 이해하도록 도움 -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "피규어 박물관",
    "alternateName": "Figure Museum",
    "url": "https://figure-museum.co.kr/",
    "description": "2,700점 이상의 피규어 정보와 시세를 제공하는 개인 아카이브 사이트입니다.",
    "inLanguage": "ko",
    "potentialAction": {
      "@type": "SearchAction",
      "target": {
        "@type": "EntryPoint",
        "urlTemplate": "https://figure-museum.co.kr/?q={search_term_string}"
      },
      "query-input": "required name=search_term_string"
    }
  }
  </script>

  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">

  <style>
    /* GitHub Pages 기본 헤더/푸터 숨김 */
    .page-header, .project-name, .project-tagline, .repository-name, .site-header, .site-footer { 
      display: none !important; opacity: 0 !important; position: absolute !important; top: -9999px !important; z-index: -999 !important;
    }
    
    :root { --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7; --modal-bg: rgba(0,0,0,0.98); }
    * { box-sizing: border-box; }
    
    body {
      margin: 0; padding: 0;
      background-color: var(--bg);
    }

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

    /* ✅ [수정 7] 사이트 소개 텍스트 영역 - 구글봇이 읽을 수 있는 실질적 콘텐츠 */
    .site-intro-section {
      max-width: 1200px; margin: 0 auto 40px; padding: 0 45px;
      text-align: center;
    }
    .site-intro-section p {
      font-size: 1rem; color: #666; line-height: 1.8; margin: 0;
    }
    
    /* ✅ [수정 8] 광고 영역 스타일 - 콘텐츠와 명확히 구분 */
    .ad-container {
      max-width: 1200px; margin: 0 auto 30px; padding: 0 45px;
      text-align: center;
    }
    .ad-label {
      font-size: 0.75rem; color: #aaa; margin-bottom: 5px; display: block;
      text-transform: uppercase; letter-spacing: 1px;
    }
    .ad-slot {
      background: #f0f0f0; border: 1px solid #ddd; border-radius: 8px;
      min-height: 90px; display: flex; align-items: center; justify-content: center;
      overflow: hidden;
    }
    
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
    
    .container { max-width: 1550px; margin: 60px auto; padding: 0 45px 150px; min-height: 60vh; transition: margin-left 0.4s, max-width 0.4s; }
    @media (min-width: 1300px) {
      .container.shifted { 
        margin-left: 320px;
        max-width: calc(100% - 320px);
      } 
    }

    .grid { 
      display: grid; 
      grid-template-columns: repeat(3, 1fr); 
      gap: 60px; 
      max-width: 1200px;
      margin: 0 auto;
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
    .modal-info-area { flex: 0.6; padding: 80px; background: #fafafa; overflow-y: auto; text-align: left; position: relative; }
    .close-btn { position: absolute; top: 40px; right: 60px; font-size: 4.5rem; cursor: pointer; color: #ccc; line-height: 1; z-index: 10; transition: 0.3s; }
    .close-btn:hover { color: var(--primary); transform: scale(1.1); }
    
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

    /* 소장처 비교 가이드 버튼 스타일 */
    .shop-guide-title { font-size: 1.1rem; font-weight: 800; color: #333; margin-top: 25px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
    .shop-btn-wrap { display: grid; grid-template-columns: 1fr; gap: 10px; margin-bottom: 15px; }
    .shop-btn { display: block; width: 100%; padding: 15px; color: white; text-align: center; text-decoration: none; border-radius: 12px; font-weight: 800; font-size: 1rem; transition: 0.2s; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05); }
    .shop-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.15); filter: brightness(1.05); }
    
    .shop-btn.mania { background: #008BCC; }
    .shop-btn.comics { background: #E50914; }
    .shop-btn.presso { background: #FFD400; color: #111; }
    .shop-btn.aladin { background: #EB118A; }
    .shop-btn.amiami { background: #FFCC00; color: #111; }
    .shop-btn.mandarake { background: #333333; }

    .shop-notice { font-size: 0.8rem; color: #888; text-align: center; margin-top: 5px; }

    /* 7대 기능 전용 스타일 */
    .modal-top-nav { display: flex; gap: 10px; margin-bottom: 20px; }
    .nav-link { background: rgba(0,0,0,0.05); padding: 8px 15px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; font-weight: 800; color: #555; transition: 0.2s; }
    .nav-link:hover { background: var(--primary); color: var(--dark); }
    .rarity-label { display: inline-block; background: #2d2926; color: var(--primary); padding: 5px 15px; border-radius: 20px; font-weight: 900; font-size: 0.85rem; margin-bottom: 15px; letter-spacing: 1px; }
    .rarity-label.limited { background: #e03131; color: white; }
    
    .action-row { display: flex; gap: 10px; margin-top: 35px; }
    .action-btn { flex: 1; padding: 15px 5px; border-radius: 12px; font-weight: 900; cursor: pointer; border: none; display: flex; align-items: center; justify-content: center; gap: 5px; font-size: 0.95rem; transition: 0.3s; }
    .action-btn:hover { transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
    .btn-like { background: #fff0f0; color: #ff6b6b; border: 1px solid #ffc9c9; }
    .btn-like.active { background: #ff6b6b; color: white; }
    .btn-share { background: #fae100; color: #3c1e1e; }
    .btn-random { background: #2d2926; color: var(--primary); }
    
    .related-section { margin-top: 40px; border-top: 2px dashed #eee; padding-top: 25px; position: relative; z-index: 2; }
    .related-title { font-size: 1.1rem; font-weight: 900; margin-bottom: 15px; color: #333; }
    .related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
    .related-card { cursor: pointer; text-align: center; font-size: 0.8rem; font-weight: bold; transition: 0.3s; }
    .related-card:hover { transform: translateY(-5px); }
    .related-card img { width: 100%; height: 100px; object-fit: contain; background: white; border: 1px solid #eee; border-radius: 12px; margin-bottom: 8px; padding: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    
    .seal-watermark { position: absolute; right: -20px; bottom: 20px; font-size: 10rem; opacity: 0.04; pointer-events: none; z-index: 1; font-weight: 900; transform: rotate(-15deg); line-height: 1; }

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

    /* ✅ [수정 9] 방명록 섹션 */
    .guestbook-section { max-width: 1200px; margin: 0 auto 60px; padding: 0 45px; }
    .guestbook-section h2 { font-size: 1.5rem; font-weight: 900; color: var(--dark); margin-bottom: 20px; }
    .guestbook-input-area { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }
    .gb-input { padding: 12px 18px; border: 1px solid #ddd; border-radius: 12px; font-family: inherit; font-size: 0.9rem; background: white; flex: 1; min-width: 120px; }
    .gb-input:focus { outline: none; border-color: var(--primary); }
    .gb-submit { background: var(--dark); color: var(--primary); border: none; padding: 12px 25px; border-radius: 12px; font-weight: 900; cursor: pointer; font-family: inherit; white-space: nowrap; }
    .gb-submit:hover { background: #444; }
    .guestbook-list { display: flex; flex-direction: column; gap: 10px; }
    .gb-item { background: white; padding: 15px 20px; border-radius: 12px; border: 1px solid #eee; display: flex; gap: 15px; align-items: flex-start; }
    .gb-name { font-weight: 800; color: var(--dark); font-size: 0.9rem; white-space: nowrap; min-width: 80px; }
    .gb-msg { color: #555; font-size: 0.9rem; line-height: 1.5; }

    /* ✅ [수정 10] 개선된 푸터 - 필수 페이지 링크 포함 */
    .museum-footer { background: #2d2926; color: #888; padding: 60px 20px; margin-top: 80px; border-top: 4px solid var(--primary); text-align: center; font-size: 0.85rem; line-height: 1.6; width: 100%; }
    .footer-content { max-width: 800px; margin: 0 auto; }
    .copyright { color: white; font-weight: 700; font-size: 1rem; margin-bottom: 10px; }
    .footer-nav { display: flex; justify-content: center; gap: 20px; margin: 20px 0; flex-wrap: wrap; }
    .footer-nav a { color: #aaa; text-decoration: none; font-size: 0.85rem; transition: 0.2s; }
    .footer-nav a:hover { color: var(--primary); }
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

    /* 모달 스타일 */
    .modal { background: rgba(250, 248, 245, 0.85) !important; backdrop-filter: blur(25px) saturate(120%); }
    .modal-content { box-shadow: 0 40px 100px rgba(100, 90, 80, 0.15) !important; border: 1px solid rgba(255, 255, 255, 0.8) !important; }
    .modal-img-area { background: radial-gradient(circle at center, #ffffff 0%, #f4f1eb 80%, #eae5dd 100%) !important; position: relative; }
    .modal-img-wrapper::before { content: ''; position: absolute; width: 60%; height: 60%; background: radial-gradient(circle, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 70%); top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 0; pointer-events: none; }
    #modalImg { position: relative; z-index: 1; filter: drop-shadow(0 20px 30px rgba(0,0,0,0.08)); }
    .nav-btn { background: rgba(255, 255, 255, 0.6) !important; color: #888 !important; box-shadow: 0 10px 20px rgba(0,0,0,0.05) !important; backdrop-filter: blur(5px); }
    .nav-btn:hover { background: #ff9f87 !important; color: white !important; }
    .modal-info-area { background: #fdfbf9 !important; }
    .close-btn { color: #bbb !important; text-shadow: 0 2px 10px rgba(255,255,255,0.8); }
    .close-btn:hover { color: #ff9f87 !important; }
    .info-label { color: #ff8fa3 !important; }
    .info-value { color: #4a4440 !important; }
    .rarity-label { background: #fcf1f1 !important; color: #ff6b81 !important; border: 1px solid #ffccd5; box-shadow: 0 5px 15px rgba(255, 107, 129, 0.1); }
    .rarity-label.limited { background: #ff6b81 !important; color: white !important; border: none; box-shadow: 0 8px 20px rgba(255, 107, 129, 0.3); }
    .nav-link { background: white !important; color: #888 !important; border: 1px solid #eee; box-shadow: 0 2px 10px rgba(0,0,0,0.02); }
    .nav-link:hover { background: #fff3f0 !important; color: #ff9f87 !important; border-color: #ffccd5; }
    .price-compare-box { background: white !important; border: 1px solid #f0eaea !important; box-shadow: 0 10px 30px rgba(0,0,0,0.03) !important; }
    .price-val-new { color: #e03131 !important; }
    .action-btn.btn-random { background: #2d2926 !important; color: #fab005 !important; }
    .action-btn.btn-share { background: #fae100 !important; color: #3c1e1e !important; }

    /* ✅ [수정 11] 다크 모드 */
    body.dark-mode #museum-wrapper { background-color: #1a1a1a; background-image: radial-gradient(#2a2a2a 1.5px, transparent 1.5px); }
    body.dark-mode .card { background: #2d2926; border-color: #444; }
    body.dark-mode .char-name { color: #f0f0f0; }
    body.dark-mode .tag.sec { background: #444; color: #aaa; }
    body.dark-mode .museum-title { color: #f0f0f0; }
    body.dark-mode .total-stats-badge { background: #fab005; color: #1a1a1a; }
    body.dark-mode .site-intro-section p { color: #999; }
    body.dark-mode .gb-input { background: #2d2926; border-color: #555; color: #f0f0f0; }
    body.dark-mode .gb-item { background: #2d2926; border-color: #444; }
    body.dark-mode .gb-name { color: #f0f0f0; }
    body.dark-mode .gb-msg { color: #aaa; }
    body.dark-mode .page-btn { background: #2d2926; border-color: #555; color: #f0f0f0; }
    body.dark-mode .page-btn.active { background: #fab005; color: #1a1a1a; }

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
      .action-row { flex-direction: column; }
      .site-intro-section { padding: 0 20px; }
      .ad-container { padding: 0 20px; }
      .guestbook-section { padding: 0 20px; }
    }

    /* ✅ [수정 12] 개인정보처리방침 / 소개 페이지 스타일 */
    .policy-page { display: none; position: fixed; inset: 0; background: white; z-index: 999998; overflow-y: auto; padding: 60px 40px; font-family: 'Noto Sans KR', sans-serif; }
    .policy-page.active { display: block; }
    .policy-page h1 { font-size: 2rem; font-weight: 900; color: var(--dark); margin-bottom: 30px; }
    .policy-page h2 { font-size: 1.3rem; font-weight: 800; color: var(--dark); margin: 30px 0 15px; }
    .policy-page p, .policy-page li { font-size: 0.95rem; color: #555; line-height: 1.8; }
    .policy-page ul { padding-left: 20px; }
    .policy-back-btn { background: var(--dark); color: var(--primary); border: none; padding: 12px 25px; border-radius: 12px; font-weight: 900; cursor: pointer; font-family: inherit; font-size: 1rem; margin-bottom: 30px; }
    .policy-content { max-width: 800px; margin: 0 auto; }
  </style>
</head>
<body>

<!-- ✅ [수정 13] 로딩 화면 -->
<div id="loading-screen">
  <div class="loader"></div>
  <p class="loading-text">명작들을 진열하고 있습니다...</p>
</div>

<!-- ✅ [수정 14] 개인정보처리방침 페이지 (필수 페이지) -->
<div id="privacyPage" class="policy-page">
  <div class="policy-content">
    <button class="policy-back-btn" onclick="closePolicyPage('privacyPage')">← 박물관으로 돌아가기</button>
    <h1>개인정보처리방침</h1>
    <p>피규어 박물관(이하 "본 사이트")은 이용자의 개인정보를 소중히 여기며, 관련 법령을 준수합니다.</p>
    
    <h2>1. 수집하는 개인정보 항목</h2>
    <p>본 사이트는 별도의 회원가입 없이 이용 가능하며, 다음과 같은 정보를 자동으로 수집할 수 있습니다.</p>
    <ul>
      <li>방문 기록 (Google Analytics를 통한 익명 통계)</li>
      <li>브라우저 로컬 스토리지에 저장되는 최근 본 피규어 목록 (서버에 전송되지 않음)</li>
      <li>방명록 작성 시 입력한 닉네임 및 메시지 (로컬 스토리지에만 저장)</li>
    </ul>

    <h2>2. 개인정보의 수집 및 이용 목적</h2>
    <ul>
      <li>사이트 이용 통계 분석 및 서비스 개선</li>
      <li>개인화된 최근 본 항목 표시</li>
    </ul>

    <h2>3. 광고 서비스</h2>
    <p>본 사이트는 Google AdSense를 통해 광고를 게재합니다. Google은 쿠키를 사용하여 이용자에게 맞춤형 광고를 제공할 수 있습니다. Google의 광고 쿠키 사용에 대한 자세한 내용은 <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">Google 광고 정책</a>에서 확인하실 수 있습니다.</p>

    <h2>4. 쿠키(Cookie) 사용</h2>
    <p>본 사이트는 Google AdSense 및 Google Analytics 운영을 위해 쿠키를 사용합니다. 브라우저 설정을 통해 쿠키 저장을 거부할 수 있으나, 일부 서비스 이용이 제한될 수 있습니다.</p>

    <h2>5. 제3자 제공</h2>
    <p>본 사이트는 이용자의 개인정보를 제3자에게 제공하지 않습니다. 단, Google AdSense 운영을 위해 Google에 광고 관련 데이터가 전달될 수 있습니다.</p>

    <h2>6. 개인정보 보호 책임자</h2>
    <p>이메일: iiopasd2003@gmail.com</p>

    <h2>7. 시행일</h2>
    <p>본 방침은 2026년 1월 1일부터 시행됩니다.</p>
  </div>
</div>

<!-- ✅ [수정 15] 사이트 소개 페이지 (필수 페이지) -->
<div id="aboutPage" class="policy-page">
  <div class="policy-content">
    <button class="policy-back-btn" onclick="closePolicyPage('aboutPage')">← 박물관으로 돌아가기</button>
    <h1>피규어 박물관 소개</h1>
    <p>피규어 박물관은 넨도로이드, 피그마, 스케일 피규어 등 다양한 피규어 정보를 수집·정리한 개인 아카이브 사이트입니다.</p>
    
    <h2>운영 목적</h2>
    <p>피규어 수집 취미를 가진 분들이 원하는 피규어 정보를 쉽게 찾고, 국내외 구매처와 실시간 시세를 비교할 수 있도록 돕는 것을 목적으로 합니다.</p>

    <h2>주요 기능</h2>
    <ul>
      <li>2,700점 이상의 피규어 정보 데이터베이스</li>
      <li>제조사, 시리즈, 출시 연도별 필터링</li>
      <li>국내 주요 쇼핑몰 실시간 재고 검색 연동</li>
      <li>해외 직구 사이트(AmiAmi, Mandarake) 가격 비교</li>
      <li>한정판 피규어 별도 표시</li>
    </ul>

    <h2>데이터 출처</h2>
    <p>본 사이트의 피규어 정보는 각 제조사 공식 사이트, 피규어 전문 쇼핑몰, 커뮤니티 등 다양한 공개 소스에서 수집되었습니다. 모든 이미지와 정보의 저작권은 해당 제조사에 있습니다.</p>

    <h2>문의</h2>
    <p>정보 오류 신고, 삭제 요청, 제보 등은 아래 이메일로 연락 주세요.</p>
    <p><strong>이메일:</strong> iiopasd2003@gmail.com</p>
    <p>또는 <a href="https://docs.google.com/forms/d/e/1FAIpQLSdfyj75_8hnUXpRxQAeeDqFuDLhg_3WHNJYXz26VJR1in7aDQ/viewform?usp=header" target="_blank" rel="noopener">명작 기증 폼</a>을 통해 새로운 피규어 정보를 제보해 주실 수 있습니다.</p>
  </div>
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

  <!-- ✅ [수정 16] 헤더 영역 - h1 태그 단일화, 구조 개선 -->
  <header class="main-title-area">
    <div class="hall-of-fame" id="fameLeft" aria-hidden="true"></div>
    <div class="center-group">
      <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot" alt="피규어 박물관 마스코트">
      <h1 class="museum-title" onclick="window.location.href='/'">피규어 박물관</h1>
      <div id="totalStats" class="total-stats-badge" aria-live="polite">총 0점의 명작 전시 중</div>
    </div>
    <div class="hall-of-fame" id="fameRight" aria-hidden="true"></div>
  </header>

  <!-- ✅ [수정 17] 사이트 소개 텍스트 - 구글봇이 읽는 실질적 콘텐츠 -->
  <section class="site-intro-section" aria-label="사이트 소개">
    <p>넨도로이드, 피그마, 스케일 피규어 등 <strong>2,700점 이상의 피규어 정보</strong>를 한눈에 확인하세요. 굿스마일, 알터, 맥스팩토리 등 주요 제조사의 발매일, 가격, 실시간 시세와 국내외 구매처를 비교할 수 있습니다.</p>
  </section>

  <!-- ✅ [수정 18] 상단 광고 배너 (애드센스 자동 광고 또는 수동 배치) -->
  <div class="ad-container" role="complementary" aria-label="광고">
    <span class="ad-label">Advertisement</span>
    <div class="ad-slot">
      <ins class="adsbygoogle"
           style="display:block"
           data-ad-client="ca-pub-2624340884962829"
           data-ad-slot="auto"
           data-ad-format="auto"
           data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
    </div>
  </div>

  <!-- 검색/필터 컨트롤 바 -->
  <nav class="sticky-header" aria-label="검색 및 필터">
    <div class="control-bar">
      <div class="search-box">
        <span class="search-icon" aria-hidden="true">🔍</span>
        <label for="searchInput" class="sr-only">피규어 검색</label>
        <input type="search" id="searchInput" class="search-input" placeholder="이름, 제조사 검색..." onkeyup="applyFilters()" aria-label="피규어 이름 또는 제조사 검색">
      </div>
      
      <div style="display: flex; gap: 15px; align-items: center;">
        <label for="sortOrder" class="sr-only">정렬 기준</label>
        <select id="sortOrder" class="sort-select" onchange="applyFilters()" aria-label="정렬 기준 선택">
          <option value="default">기본 순서</option>
          <option value="dateDesc">🚀 출시 임박순</option>
          <option value="priceHigh">높은 가격순</option>
          <option value="priceLow">낮은 가격순</option>
          <option value="nameAsc">이름 (가나다)</option>
        </select>
        <button class="toggle-btn" onclick="toggleFilters()" id="toggleBtn" aria-expanded="false" aria-controls="filterMenu">[ 필터 열기 ]</button>
        <button class="toggle-btn" onclick="toggleDarkMode()" id="darkModeBtn" style="background:#2d2926; color:white; border:none;" aria-label="다크 모드 전환">🌙 다크 모드</button>
      </div>
    </div>

    <aside id="filterMenu" class="bookmark-container collapsed" aria-label="필터 메뉴">
      
      <div class="filter-section">
        <span class="filter-title">📅 출시 연도 (Release Year)</span>
        <div class="year-grid" id="yearButtons" role="group" aria-label="출시 연도 필터"></div>
      </div>

      <div id="seriesButtons" role="group" aria-label="시리즈 필터"></div>
      <div class="maker-row" id="makerButtons">
        <span class="maker-label">MAKER</span>
        <div class="sub-btns-scroll" id="makerList" role="group" aria-label="제조사 필터"></div>
      </div>
    </aside>
  </nav>

  <!-- 메인 피규어 그리드 -->
  <main class="container" id="mainContainer">
    <div id="grid-top"></div> 
    <div id="figureGrid" class="grid" role="list" aria-label="피규어 목록"></div>
    
    <!-- ✅ [수정 19] 그리드 중간 광고 (페이지네이션 위) -->
    <div class="ad-container" style="margin-top: 40px;" role="complementary" aria-label="광고">
      <span class="ad-label">Advertisement</span>
      <div class="ad-slot">
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-2624340884962829"
             data-ad-slot="auto"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
      </div>
    </div>

    <div id="pagination" class="pagination" role="navigation" aria-label="페이지 이동"></div>
  </main>

  <!-- 방명록 섹션 -->
  <section class="guestbook-section" id="guestbookSection" aria-label="방명록">
    <h2>🖋️ 박물관 관람 방명록</h2>
    <div class="guestbook-input-area">
      <label for="gbName" class="sr-only">닉네임</label>
      <input type="text" id="gbName" class="gb-input" placeholder="닉네임 (최대 10자)" maxlength="10" aria-label="닉네임 입력">
      <label for="gbMsg" class="sr-only">방명록 내용</label>
      <input type="text" id="gbMsg" class="gb-input" placeholder="박물관 관람 소감이나 명작 제보를 한 줄로 남겨주세요!" maxlength="80" onkeypress="if(event.keyCode==13) addGuestbook()" aria-label="방명록 내용 입력">
      <button class="gb-submit" onclick="addGuestbook()">남기기</button>
    </div>
    <div class="guestbook-list" id="guestbookList" aria-live="polite"></div>
  </section>

  <!-- ✅ [수정 20] 개선된 푸터 - 필수 페이지 링크 포함 -->
  <footer class="museum-footer">
    <div class="footer-content">
      <p class="copyright">© 2026 Figure Museum Archive. All rights reserved.</p>
      
      <!-- ✅ 필수 페이지 링크 (애드센스 승인 필수 요건) -->
      <nav class="footer-nav" aria-label="사이트 정보">
        <a href="#" onclick="openPolicyPage('aboutPage'); return false;">사이트 소개</a>
        <a href="#" onclick="openPolicyPage('privacyPage'); return false;">개인정보처리방침</a>
        <a href="mailto:iiopasd2003@gmail.com">문의하기</a>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSdfyj75_8hnUXpRxQAeeDqFuDLhg_3WHNJYXz26VJR1in7aDQ/viewform?usp=header" target="_blank" rel="noopener">피규어 제보</a>
      </nav>

      <p class="source-info">모든 데이터는 다양한 온라인 소스에서 수집되었습니다.</p>
      
      <div class="disclaimer-box">
        <p>본 사이트는 개인 소장품 기록 및 정보 공유를 목적으로 운영되는 <strong>개인 아카이브</strong>입니다.</p>
        <p>게시된 이미지와 정보의 저작권은 각 제조사 및 유통사에 있으며, 악의적인 저작권 침해 의도는 없습니다.</p>
        <p>관계자분의 삭제 요청이 있을 경우, 확인 즉시 해당 콘텐츠를 비공개 처리하겠습니다.</p>
        <p class="contact-email">문의: iiopasd2003@gmail.com</p>
      </div>
    </div>
  </footer>

</div> 

<!-- 상세 모달 -->
<div id="detailModal" class="modal" onclick="closeModal()" role="dialog" aria-modal="true" aria-label="피규어 상세 정보">
  <div class="modal-content" onclick="event.stopPropagation()">
    <button class="close-btn" onclick="closeModal()" aria-label="닫기">&times;</button>
    <div class="modal-img-area">
      <button class="nav-btn" style="left:35px" onclick="changeImg(-1)" aria-label="이전 이미지">‹</button>
      <div class="modal-img-wrapper" onmousemove="handleZoomMove(event)">
        <img id="modalImg" src="" onclick="toggleZoom(event)" onerror="this.src='https://bosswise.github.io/figure-DB/images/mascot.png'" alt="피규어 이미지">
      </div>
      <button class="nav-btn" style="right:35px" onclick="changeImg(1)" aria-label="다음 이미지">›</button>
    </div>
    <div class="modal-info-area" id="modalInfo"></div>
  </div>
</div>

<!-- 기증 모달 -->
<div id="donateModal" class="modal" onclick="closeDonateModal()" role="dialog" aria-modal="true" aria-label="명작 기증 시스템">
  <div class="modal-content" onclick="event.stopPropagation()" style="max-width: 600px; height: auto; flex-direction: column; padding: 40px; border-radius: 40px; z-index: 100000;">
    <button class="close-btn" onclick="closeDonateModal()" aria-label="닫기">&times;</button>
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
      <a href="https://docs.google.com/forms/d/e/1FAIpQLSdfyj75_8hnUXpRxQAeeDqFuDLhg_3WHNJYXz26VJR1in7aDQ/viewform?usp=header" target="_blank" rel="noopener" class="donate-link-btn">명작 기증 폼 작성하러 가기 🚀</a>
    </div>
  </div>
</div>

<!-- ✅ [수정 21] 스크린 리더용 숨김 텍스트 스타일 -->
<style>
  .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }
</style>

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

  const makerTranslate = { "굿스마일": "Good Smile Company", "알터": "Alter", "메가하우스": "MegaHouse", "코토부키야": "Kotobukiya", "맥스팩토리": "Max Factory", "반다이": "Bandai", "프링": "FREEing", "펫": "Phat!", "퓨처": "FuRyu", "카도카와": "Kadokawa" };

  function koreanToRoman(text) {
    const chosung = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"];
    const jungsung = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"];
    const jongsung = ["", "g", "kk", "gs", "n", "nj", "nh", "d", "l", "lg", "lm", "lb", "ls", "lt", "lp", "lh", "m", "b", "bs", "s", "ss", "ng", "j", "ch", "k", "t", "p", "h"];
    let result = ""; 
    for (let i = 0; i < text.length; i++) {
      let code = text.charCodeAt(i);
      if (code >= 44032 && code <= 55203) { 
        let uni = code - 44032; let cho = Math.floor(uni / 588); let jung = Math.floor((uni - (cho * 588)) / 28); let jong = uni % 28; result += chosung[cho] + jungsung[jung] + jongsung[jong]; 
      } else { 
        result += text[i]; 
      }
    }
    return result;
  }

  function escapeHTML(str) {
    if (!str) return "";
    return str.replace(/[&<>"']/g, function(m) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m];
    });
  }

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

      checkDarkMode();
      initGuestbook();

      const response = await fetch(csvURL, { redirect: "follow" });
      const text = await response.text();
      
      const rows = text.split(/\r?\n/).map(row => {
        const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
        return cols.map(c => c ? c.trim().replace(/^"|"$/g, '').replace(/""/g, '"') : "");
      });
      
      allData = rows.slice(1).filter(r => r[8]).map((r, i) => {
        r._idx = i;
        return r;
      });
      
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
       btn.setAttribute('aria-expanded', 'true');
    } else {
       menu.classList.add('collapsed'); 
       container.classList.remove('shifted');
       btn.innerText = '[ 필터 열기 ]';
       btn.setAttribute('aria-expanded', 'false');
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
      const series = item[2] || "기타";
      const maker = item[1] || "정보없음";
      
      const rawDate = item[13] ? item[13].trim() : ""; 
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
      
      const rawDate = item[13] ? item[13].trim() : "";
      let itemYear = "미정";
      if(rawDate.match(/^\d{4}/)) itemYear = rawDate.substring(0, 4);
      const yearMatch = (activeYear === 'all' || itemYear === activeYear);
      
      const name = getProductName(item).toLowerCase();
      const maker = (item[1] || "").toLowerCase();
      const series = (item[2] || "").toLowerCase();
      const textMatch = name.includes(query) || maker.includes(query) || series.includes(query);
      
      return seriesMatch && makerMatch && yearMatch && textMatch;
    });

    if (sortVal === 'priceHigh') {
      filtered.sort((a, b) => (parseInt(b[5]) || 0) - (parseInt(a[5]) || 0));
    } else if (sortVal === 'priceLow') {
      filtered.sort((a, b) => (parseInt(a[5]) || 0) - (parseInt(b[5]) || 0));
    } else if (sortVal === 'nameAsc') {
      filtered.sort((a, b) => (getProductName(a)).localeCompare(getProductName(b)));
    } else if (sortVal === 'dateDesc') {
       filtered.sort((a, b) => {
         const dateA = a[13] ? a[13] : "0000-00-00";
         const dateB = b[13] ? b[13] : "0000-00-00";
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
      grid.innerHTML = `<div class="no-result" role="status"><h3>😢 전시된 피규어가 없습니다.</h3><p>다른 필터나 검색어를 사용해 보세요.</p></div>`; 
      return; 
    }
    grid.innerHTML = data.map((item) => {
      const name = escapeHTML(getProductName(item)); 
      const img = item[8].split(',')[0].trim();
      const badgeHtml = (item[6] && item[6].toUpperCase() === 'TRUE') ? `<div class="card-badge">LIMITED</div>` : '';
      return `<article class="card" onclick="window.openModal(${item._idx})" role="listitem" tabindex="0" onkeypress="if(event.key==='Enter')window.openModal(${item._idx})" aria-label="${name} 피규어 상세 보기">
        ${badgeHtml}
        <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg" loading="lazy" alt="${name} 피규어 이미지" onerror="this.src='https://bosswise.github.io/figure-DB/images/mascot.png'"></div>
        <div class="content">
          <h2 class="char-name">${name}</h2>
          <div class="tag-wrap">
            <span class="tag">#${escapeHTML(item[10] || '')}</span>
            <span class="tag sec">#${escapeHTML(item[2] || '')}</span>
          </div>
        </div>
      </article>`;
    }).join('');
  }

  function renderPagination(totalPages) {
    const pagination = document.getElementById('pagination');
    if (totalPages <= 1) { pagination.innerHTML = ''; return; }
    let html = '';
    html += `<button class="page-btn" onclick="changePage(1)" ${currentPage === 1 ? 'disabled' : ''} aria-label="첫 페이지">&lt;&lt;</button>`;
    html += `<button class="page-btn" onclick="changePage(${currentPage - 1})" ${currentPage === 1 ? 'disabled' : ''} aria-label="이전 페이지">&lt;</button>`;
    
    let startPage = Math.max(1, currentPage - 2); 
    let endPage = Math.min(totalPages, startPage + 4);
    if (endPage - startPage < 4) startPage = Math.max(1, endPage - 4);
    
    for (let i = startPage; i <= endPage; i++) { 
      if(i > 0) html += `<button class="page-btn ${i === currentPage ? 'active' : ''}" onclick="changePage(${i})" aria-label="${i}페이지" ${i === currentPage ? 'aria-current="page"' : ''}>${i}</button>`; 
    }
    
    html += `<button class="page-btn" onclick="changePage(${currentPage + 1})" ${currentPage === totalPages ? 'disabled' : ''} aria-label="다음 페이지">&gt;</button>`;
    html += `<button class="page-btn" onclick="changePage(${totalPages})" ${currentPage === totalPages ? 'disabled' : ''} aria-label="마지막 페이지">&gt;&gt;</button>`;
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
      target.innerHTML = items.map((it, idx) => `<div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="window.openModal(${it._idx})"><img src="${imageBaseURL}${encodeURIComponent(it[8].split(',')[0].trim())}.jpg" alt="${escapeHTML(getProductName(it))} 피규어" onerror="this.src='https://bosswise.github.io/figure-DB/images/mascot.png'"></div>`).join('');
      let cur = 0; 
      setInterval(() => { 
        const slides = target.querySelectorAll('.fame-slide'); 
        if(slides.length > 0) { 
          slides[cur].classList.remove('active'); 
          cur = (cur + 1) % slides.length; 
          slides[cur].classList.add('active'); 
        } 
      }, 4000);
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
      return `<div class="quick-item" onclick="window.openModal(${idx})" tabindex="0" aria-label="${escapeHTML(getProductName(item))} 다시 보기"><img src="${imageBaseURL}${encodeURIComponent(item[8].split(',')[0].trim())}.jpg" alt="${escapeHTML(getProductName(item))}" onerror="this.src='https://bosswise.github.io/figure-DB/images/mascot.png'"></div>`;
    }).join('');
  }

  function scrollToTop() { 
    document.getElementById('museum-wrapper').scrollTo({ top: 0, behavior: 'smooth' }); 
  }

  window.onpopstate = function(event) {
    if (document.getElementById('detailModal').style.display === 'flex') { 
      closeModal(true); 
    } else if (event.state && event.state.id !== undefined) { 
      window.openModal(event.state.id, true); 
    }
  };

  window.addEventListener('keydown', function(e) {
    const modal = document.getElementById('detailModal');
    if (modal.style.display === 'flex') {
      if (e.key === 'Escape') closeModal();
      else if (e.key === 'ArrowLeft') changeImg(-1);
      else if (e.key === 'ArrowRight') changeImg(1);
    }
  });

  window.openModal = function(idx, isPopState = false) {
    saveRecentView(idx);
    const item = allData[idx]; 
    if(!item || !item[8]) return;
    
    const name = escapeHTML(getProductName(item)); 
    const series = escapeHTML(item[2] || "기타");
    const maker = escapeHTML(item[1] || "정보없음");

    document.title = `${name} - 피규어 박물관`;
    
    let metaDesc = document.querySelector('meta[name="description"]');
    if (!metaDesc) {
      metaDesc = document.createElement('meta');
      metaDesc.name = "description";
      document.head.appendChild(metaDesc);
    }
    metaDesc.content = `${series} 시리즈의 ${name} (${maker}). 피규어 박물관에서 상세 정보와 실시간 시세를 확인하세요.`;

    if(!isPopState) {
      const newURL = window.location.protocol + "//" + window.location.host + window.location.pathname + '?id=' + idx;
      const currentId = new URLSearchParams(window.location.search).get('id');
      if (currentId !== String(idx)) { 
        window.history.pushState({modalOpen: true, id: idx}, '', newURL); 
      }
    }
    
    currentImages = item[8].split(',').map(s => s.trim()); 
    currentImgIdx = 0; 
    isZoomed = false; 
    updateModalImg();

    const rawMaker = item[1] || ""; 
    const englishMaker = makerTranslate[rawMaker] || rawMaker;
    const searchKeyword = item[14] ? item[14].trim() : getProductName(item); 
    const cleanKeyword = searchKeyword.replace(/[\[\]\(\)]/g, '').trim(); 
    const romanKeyword = koreanToRoman(cleanKeyword);
    
    const englishNameFromV = item[21] ? item[21].trim() : "";
    let amiamiSearchQuery = "";
    if (englishNameFromV !== "") {
        amiamiSearchQuery = englishNameFromV;
    } else {
        amiamiSearchQuery = englishMaker + " " + romanKeyword;
    }
    
    const encodedKeyword = encodeURIComponent(searchKeyword);
    const encodedAmiamiQuery = encodeURIComponent(amiamiSearchQuery);
    const maniaLink = "https://maniahouse.co.kr/product/search.html?keyword=" + encodedKeyword;
    const comicsLink = "https://comics-art.co.kr/product/search.html?keyword=" + encodedKeyword;
    const pressoLink = "https://figurepresso.com/product/search.html?keyword=" + encodedKeyword;
    const aladinLink = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=" + encodedKeyword;
    const amiamiLink = "https://www.amiami.com/eng/search/list/?s_keywords=" + encodedAmiamiQuery;
    const mandarakeLink = "https://order.mandarake.co.jp/order/listPage/list.xhtml?keyword=" + encodedAmiamiQuery;
    
    const originalPrice = isNaN(item[5]) ? escapeHTML(item[5]) : Number(item[5]).toLocaleString() + '원';
    const maniaPrice = item[15] && !isNaN(item[15].replace(/,/g,'')) ? Number(item[15].replace(/,/g,'')).toLocaleString() + '원' : null;
    const diffStatus = escapeHTML(item[18] || ""); 
    const donorName = escapeHTML(item[20] ? item[20].trim() : ""); 
    
    const releaseDate = escapeHTML((item[13] && item[13].trim() !== "") ? item[13].trim() : "정보확인중");

    let statusClass = ""; 
    if(diffStatus.includes("▲")) statusClass = "price-status up"; 
    else if(diffStatus.includes("▼")) statusClass = "price-status down"; 
    
    let priceHtml = maniaPrice ? `
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
        </div>` : `
        <div class="price-compare-box">
          <div class="price-row" style="margin-bottom:0;">
            <span class="price-label">박물관 기록가</span>
            <span class="price-val-old" style="text-decoration:none; color:#2d2926; font-weight:bold;">${originalPrice}</span>
          </div>
        </div>`;

    const uid = 'like_' + idx;
    const liked = localStorage.getItem(uid);
    const pseudoRandom = (idx * 17) % 50 + 10;
    const initialLike = pseudoRandom + (liked ? 1 : 0);

    const related = allData.filter(x => x[2] === item[2] && x._idx !== idx).sort(() => 0.5 - Math.random()).slice(0, 3);
    let relatedHtml = '';
    if (related.length > 0) {
       relatedHtml = `<section class="related-section" aria-label="같은 시리즈 피규어">
         <div class="related-title">🔍 같은 시리즈의 다른 명작</div>
         <div class="related-grid">`;
       related.forEach(r => {
           relatedHtml += `<div class="related-card" onclick="window.openModal(${r._idx})" tabindex="0" aria-label="${escapeHTML(getProductName(r))} 보기">
             <img src="${imageBaseURL}${encodeURIComponent(r[8].split(',')[0].trim())}.jpg" alt="${escapeHTML(getProductName(r))} 피규어" onerror="this.src='https://bosswise.github.io/figure-DB/images/mascot.png'" loading="lazy">
             <div style="white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${escapeHTML(getProductName(r))}</div>
           </div>`;
       });
       relatedHtml += `</div></section>`;
    }

    document.getElementById('modalInfo').innerHTML = `
      <div style="position:relative; z-index:2;">
        
        <div class="modal-top-nav">
          <span class="nav-link" onclick="closeModal()" tabindex="0" role="button">🏠 박물관 메인으로</span>
          <span class="nav-link" onclick="scrollToTop(); closeModal();" tabindex="0" role="button">📋 전체 목록 보기</span>
        </div>

        <div class="rarity-label ${item[6] === 'TRUE' ? 'limited' : ''}">
          ${item[6] === 'TRUE' ? '👑 MUSEUM GRADE (한정판)' : '🎖️ STANDARD GRADE'}
        </div>

        <div class="info-item"><h2 style="font-size:3.5rem; font-weight:900; color:#2d2926; margin:0; line-height:1.2;">${name}</h2></div>
        ${donorName ? `<div class="info-item"><span class="info-label" style="color:#ff4757;">[ 🎁 기증자 ]</span><span class="info-value">${donorName}</span></div>` : ''} 
        <div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${maker || '-'}</span></div>
        <div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${series}</span></div>
        <div class="info-item"><span class="info-label">[ 발매일 ]</span><span class="info-value">${releaseDate}</span></div>
        <div class="info-item"><span class="info-label">[ 유형 ]</span><span class="info-value">${escapeHTML(item[7]) || '-'}</span></div>
        <div class="info-item"><span class="info-label">[ 크기(mm) ]</span><span class="info-value">${escapeHTML(item[4]) || '-'}</span></div>
        
        ${priceHtml}
        
        <div class="shop-guide-title">🔍 국내 소장처 실시간 검색</div>
        <div class="shop-btn-wrap">
          <a href="${maniaLink}" target="_blank" rel="noopener" class="shop-btn mania">매니아하우스에서 찾기</a>
          <a href="${comicsLink}" target="_blank" rel="noopener" class="shop-btn comics">코믹스아트에서 찾기</a>
          <a href="${pressoLink}" target="_blank" rel="noopener" class="shop-btn presso">피규어프레소 확인</a>
          <a href="${aladinLink}" target="_blank" rel="noopener" class="shop-btn aladin">알라딘 재고 검색</a>
        </div>
        <div class="shop-guide-title">🌐 해외 직구/중고 시세 확인</div>
        <div class="shop-btn-wrap">
          <a href="${amiamiLink}" target="_blank" rel="noopener" class="shop-btn amiami">AmiAmi (신품/중고)</a>
          <a href="${mandarakeLink}" target="_blank" rel="noopener" class="shop-btn mandarake">Mandarake (일본 본점/중고)</a>
        </div>
        <div class="shop-notice">※ 실시간 재고 상황에 따라 검색 결과가 없을 수 있으며, 미등록 명작은 계속 업데이트 중입니다.</div>
        
        <div class="info-item" style="border:none; margin-top:20px;">
          <span class="info-label">[ 특이사항 ]</span>
          <p style="line-height:1.8; color:#555; font-size:1.2rem; margin:0;">${escapeHTML(item[9]) || '내용이 없습니다.'}</p>
        </div>

        <div class="action-row">
           <button class="action-btn btn-like ${liked ? 'active' : ''}" id="likeBtnModal" onclick="toggleLikeModal(${idx})" aria-label="추천하기">❤️ 추천 <span id="likeCountModal">${initialLike}</span></button>
           <button class="action-btn btn-share" onclick="shareKakao(${idx}, '${name.replace(/'/g, "\\'")}')" aria-label="공유하기">💬 공유하기</button>
           <button class="action-btn btn-random" onclick="openRandom()" aria-label="랜덤 피규어 보기">🎲 다른 전시물 보기</button>
        </div>

        ${relatedHtml}

      </div>
      
      <div class="seal-watermark" aria-hidden="true">🏛️</div>
    `;
    
    document.getElementById('detailModal').style.display = 'flex'; 
    document.body.style.overflow = 'hidden';
  }

  window.toggleLikeModal = function(idx) {
      const uid = 'like_' + idx;
      const btn = document.getElementById('likeBtnModal');
      const countSpan = document.getElementById('likeCountModal');
      let count = parseInt(countSpan.innerText);
      if(localStorage.getItem(uid)) {
          localStorage.removeItem(uid);
          btn.classList.remove('active');
          countSpan.innerText = count - 1;
      } else {
          localStorage.setItem(uid, 'true');
          btn.classList.add('active');
          countSpan.innerText = count + 1;
      }
  }

  window.openRandom = function() {
      if(allData.length > 0) {
          const randomIdx = allData[Math.floor(Math.random() * allData.length)]._idx;
          window.openModal(randomIdx);
      }
  }

  window.shareKakao = function(idx, title) {
      const url = `${window.location.origin}${window.location.pathname}?id=${idx}`;
      if(navigator.share) {
          navigator.share({ title: title, text: '피규어 박물관에서 이 명작을 확인해보세요!', url: url }).catch(console.error);
      } else {
          window.copyLink(idx);
      }
  }

  window.toggleZoom = function(e) { 
    isZoomed = !isZoomed; 
    document.getElementById('modalImg').classList.toggle('zoomed'); 
    if (!isZoomed) document.getElementById('modalImg').style.transform = 'scale(1)'; 
  }
  
  window.handleZoomMove = function(e) { 
    if (!isZoomed) return; 
    const img = document.getElementById('modalImg'); 
    const wrapper = e.currentTarget; 
    const { left, top, width, height } = wrapper.getBoundingClientRect(); 
    const x = ((e.pageX - left - window.scrollX) / width) * 100;
    const y = ((e.pageY - top - window.scrollY) / height) * 100; 
    img.style.transformOrigin = `${x}% ${y}%`; 
    img.style.transform = 'scale(3.5)'; 
  }
  
  window.updateModalImg = function() { 
    const img = document.getElementById('modalImg'); 
    img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`; 
    isZoomed = false; 
    img.classList.remove('zoomed'); 
    img.style.transform = 'scale(1)'; 
  }
  
  window.changeImg = function(dir) { 
    currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; 
    updateModalImg(); 
  }
  
  window.closeModal = function(isBackButton = false) { 
    document.getElementById('detailModal').style.display = 'none'; 
    document.body.style.overflow = 'auto'; 
    document.title = '피규어 박물관 - 넨도로이드·피그마·스케일 피규어 정보 & 시세 아카이브'; 
    if (!isBackButton) { 
      const cleanURL = window.location.protocol + "//" + window.location.host + window.location.pathname; 
      window.history.pushState({}, '', cleanURL); 
    } 
  }
  
  window.toggleFilters = function() { 
    const menu = document.getElementById('filterMenu'); 
    const container = document.getElementById('mainContainer'); 
    const btn = document.getElementById('toggleBtn');
    menu.classList.toggle('collapsed'); 
    if (window.innerWidth >= 1300) { 
      container.classList.toggle('shifted'); 
    } 
    const isCollapsed = menu.classList.contains('collapsed');
    btn.innerText = isCollapsed ? '[ 필터 열기 ]' : '[ 필터 접기 ]';
    btn.setAttribute('aria-expanded', isCollapsed ? 'false' : 'true');
  }
  
  function checkUrlParam() { 
    const urlParams = new URLSearchParams(window.location.search); 
    const figureId = urlParams.get('id'); 
    if (figureId !== null) { 
      const parsedId = parseInt(figureId);
      if (allData[parsedId]) {
        setTimeout(() => { window.openModal(parsedId, true); }, 500); 
      }
    } 
  }
  
  window.copyLink = function(idx) { 
    const url = `${window.location.origin}${window.location.pathname}?id=${idx}`; 
    navigator.clipboard.writeText(url).then(() => { 
      alert("링크가 복사되었습니다! 친구에게 붙여넣기(Ctrl+V) 하세요."); 
    }).catch(err => { 
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

  /* ✅ [수정 22] 개인정보처리방침/소개 페이지 열기/닫기 */
  window.openPolicyPage = function(pageId) {
    document.getElementById(pageId).classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  window.closePolicyPage = function(pageId) {
    document.getElementById(pageId).classList.remove('active');
    document.body.style.overflow = 'auto';
  }

  /* 다크 모드 */
  function checkDarkMode() {
      const isDark = localStorage.getItem('museum_dark_mode') === 'true';
      if (isDark) {
          document.body.classList.add('dark-mode');
          document.getElementById('darkModeBtn').innerText = '☀️ 라이트 모드';
      }
  }

  window.toggleDarkMode = function() {
      const body = document.body;
      const btn = document.getElementById('darkModeBtn');
      body.classList.toggle('dark-mode');
      
      if (body.classList.contains('dark-mode')) {
          localStorage.setItem('museum_dark_mode', 'true');
          btn.innerText = '☀️ 라이트 모드';
      } else {
          localStorage.setItem('museum_dark_mode', 'false');
          btn.innerText = '🌙 다크 모드';
      }
  }

  /* 방명록 */
  function initGuestbook() {
      let gb = JSON.parse(localStorage.getItem('museum_guestbook') || '[]');
      if(gb.length === 0) {
          gb = [
              {name: "관람객A", msg: "정리가 너무 잘 되어있네요! 피규어 시세 볼 때 자주 올게요."},
              {name: "피규어매니아", msg: "제가 찾던 정보가 다 있습니다. 명작들 퀄리티 최고!"}
          ];
          localStorage.setItem('museum_guestbook', JSON.stringify(gb));
      }
      renderGuestbook();
  }

  window.addGuestbook = function() {
      const nameInput = document.getElementById('gbName');
      const msgInput = document.getElementById('gbMsg');
      
      const name = nameInput.value.trim() || '익명 관람객';
      const msg = msgInput.value.trim();
      
      if(!msg) {
          alert('방명록 내용을 입력해주세요!');
          msgInput.focus();
          return;
      }
      
      let gb = JSON.parse(localStorage.getItem('museum_guestbook') || '[]');
      gb.unshift({name: escapeHTML(name), msg: escapeHTML(msg)});
      
      if(gb.length > 50) gb.pop();
      
      localStorage.setItem('museum_guestbook', JSON.stringify(gb));
      msgInput.value = '';
      
      renderGuestbook();
  }

  function renderGuestbook() {
      let gb = JSON.parse(localStorage.getItem('museum_guestbook') || '[]');
      const html = gb.map(item => `
          <div class="gb-item">
              <span class="gb-name">${item.name}</span>
              <span class="gb-msg">${item.msg}</span>
          </div>
      `).join('');
      document.getElementById('guestbookList').innerHTML = html;
  }
  
  init();
</script>
</body>
</html>
