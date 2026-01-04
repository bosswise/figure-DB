<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 사장님 전용: 깃허브 유령 텍스트 박멸 시스템 */
    * { box-sizing: border-box; }
    header, footer, .site-header, .site-footer, .title, a[href*="github.com"], b, span:first-of-type { 
      display: none !important; opacity: 0 !important; pointer-events: none !important; 
    }

    :root { 
      --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7; --tag-grey: #eee;
      --modal-bg: rgba(0,0,0,0.95);
    }

    .museum-full-layer {
      position: relative; width: 100%; min-height: 100vh; background-color: var(--bg); z-index: 999999;
      font-family: 'Noto Sans KR', sans-serif;
    }

    body { margin: 0; padding: 0; background-color: var(--bg); overflow-x: hidden; }

    /* 🖼️ 헤드 제목 섹션 */
    .main-title-area { padding: 60px 0 30px; text-align: center; }
    .header-mascot { 
      width: 170px; height: 170px; border-radius: 50%; background: white; 
      padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: 0.4s; 
    }
    .museum-title { 
      font-weight: 900; font-size: 4rem; color: var(--dark); 
      margin: 15px 0 5px; cursor: pointer; display: inline-block; letter-spacing: -3px;
    }
    .stats-text { color: #8c847d; font-size: 1.1rem; font-weight: 300; }

    /* 📌 [NEW] 최소화 기능이 추가된 책갈피 필터 */
    .sticky-header { 
      background: #2d2926; position: sticky; top: 0; z-index: 1000; 
      box-shadow: 0 5px 20px rgba(0,0,0,0.3); transition: all 0.4s ease;
    }
    .toggle-bar {
      max-width: 1200px; margin: 0 auto; display: flex; justify-content: flex-end; padding: 5px 25px;
    }
    .toggle-btn {
      background: none; border: 1px solid #555; color: #aaa; font-size: 0.7rem; 
      padding: 3px 10px; border-radius: 5px; cursor: pointer; transition: 0.3s;
    }
    .toggle-btn:hover { color: var(--primary); border-color: var(--primary); }

    .bookmark-container { 
      max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; 
      gap: 8px; padding: 0 25px 15px; overflow: hidden; transition: max-height 0.4s ease;
      max-height: 500px; /* 열렸을 때 높이 */
    }
    .bookmark-container.collapsed { max-height: 0; padding-bottom: 0; }

    .category-row { 
      display: flex; align-items: center; gap: 12px; 
      background: rgba(255,255,255,0.06); padding: 8px 15px; border-radius: 12px; 
    }
    .main-label { color: var(--primary); font-weight: 900; min-width: 95px; font-size: 0.8rem; border-right: 1px solid #555; }
    .sub-btns-scroll { display: flex; gap: 8px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }
    
    .filter-btn { 
      background: #45403c; color: #a5a09c; border: none; padding: 6px 16px; 
      border-radius: 20px; cursor: pointer; font-size: 0.8rem; transition: 0.2s; 
    }
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
    .tag-wrap { display: flex; justify-content: center; gap: 6px; flex-wrap: wrap; }
    .tag { font-size: 0.75rem; background: var(--tag-gold); color: #d35400; padding: 4px 12px; border-radius: 10px; font-weight: 700; }
    .tag.sec { background: var(--tag-grey); color: #777; }

    /* 🖼️ 모달 (슬라이드 & 줌) */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 9999999; justify-content: center; align-items: center; padding: 30px; backdrop-filter: blur(15px); }
    .modal-content { background: white; max-width: 1200px; width: 98%; height: 85vh; border-radius: 50px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.3; background: #fff; padding: 40px; display: flex; align-items: center; justify-content: center; position: relative; border-right: 1px solid #f0f0f0; overflow: hidden; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; transition: 0.4s ease; cursor: zoom-in; }
    .modal-img-area img.zoomed { transform: scale(2.2); cursor: zoom-out; }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 55px; height: 55px; background: rgba(255,255,255,0.95); border: none; border-radius: 50%; font-size: 1.5rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.3s; color: #333; box-shadow: 0 4px 15px rgba(0,0,0,0.1); z-index: 10; }
    .nav-btn:hover { background: var(--primary); color: white; transform: translateY(-50%) scale(1.1); }
    .prev-btn { left: 30px; }
    .next-btn { right: 30px; }
    .modal-info-area { flex: 0.7; padding: 60px; background: #fafafa; overflow-y: auto; }
    .close-btn { position: absolute; top: 35px; right: 45px; font-size: 3.5rem; cursor: pointer; color: #ccc; z-index: 100; line-height: 0.7; }
    .info-label { font-size: 0.85rem; color: var(--primary); font-weight: 900; margin-top: 30px; display: block; letter-spacing: 1px; }
    .info-value { font-size: 1.35rem; font-weight: 600; border-bottom: 1px solid #eee; padding-bottom: 10px; display: block; color: var(--dark); }

    @media (max-width: 1100px) { .grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 700px) { .grid { grid-template-columns: 1fr; } }
  </style>
</head>
<body>

<div class="museum-full-layer" id="museumLayer">
  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
    <p id="total-stats" class="stats-text">The Collection is Syncing...</p>
  </div>

  <div class="sticky-header">
    <div class="toggle-bar">
      <button class="toggle-btn" onclick="toggleFilters()" id="toggleBtn">[ 책갈피 접기 ]</button>
    </div>
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
      <button class="nav-btn prev-btn" id="prevBtn" onclick="changeImg(-1)">&lt;</button>
      <img id="modalImg" src="" onclick="toggleZoom(event)">
      <button class="nav-btn next-btn" id="nextBtn" onclick="changeImg(1)">&gt;</button>
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
        let icon = cat.toUpperCase().includes('GAME') ? '🎮 ' : cat.toUpperCase().includes('VOCAL') ? '🎤 ' : '📦 ';
        let html = `<span class="main-label">${icon}${cat.toUpperCase()}</span><div class="sub-btns-scroll">`;
        seriesSet.forEach(s => { html += `<button class="filter-btn" onclick="filterBy('${s}', this)">${s}</button>`; });
        row.innerHTML = html + `</div></div>`;
        filterMenu.appendChild(row);
      }
      renderGrid(allData);

      // 🚨 유령 문구 삭제 루틴
      setTimeout(() => {
        document.querySelectorAll('header, footer, b, p:first-of-type').forEach(el => {
          if(!el.closest('#museumLayer')) el.remove();
        });
      }, 500);

    } catch (e) { console.error(e); }
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    grid.innerHTML = data.map((item, idx) => {
      const name = (item[12] && item[12] !== "") ? item[12] : item[3];
      const firstImg = item[8].split(',')[0].trim();
      return `
        <div class="card" data-series="${item[2]}" onclick="openModal(${idx})">
          <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(firstImg)}.jpg" loading="lazy"></div>
          <div class="content">
            <div class="char-name">${name}</div>
            <div class="tag-wrap">
              <span class="tag">#${item[1]}</span>
              <span class="tag sec">#${item[2]}</span>
              <span class="tag sec">#${item[4] || 'Scale'}</span>
            </div>
          </div>
        </div>`;
    }).join('');
  }

  function toggleFilters() {
    const menu = document.getElementById('filterMenu');
    const btn = document.getElementById('toggleBtn');
    menu.classList.toggle('collapsed');
    btn.innerText = menu.classList.contains('collapsed') ? '[ 카테고리 열기 ]' : '[ 책갈피 접기 ]';
  }

  function openModal(idx) {
    const item = allData[idx];
    const name = (item[12] && item[12] !== "") ? item[12] : item[3];
    currentImages = item[8].split(',').map(s => s.trim());
    currentImgIdx = 0;
    updateModalImg();
    document.getElementById('prevBtn').style.display = currentImages.length > 1 ? 'flex' : 'none';
    document.getElementById('nextBtn').style.display = currentImages.length > 1 ? 'flex' : 'none';
    document.getElementById('modalInfo').innerHTML = `
      <h2 style="font-size:2.8rem; font-weight:900; color:#2d2926; line-height:1.1;">${name}</h2>
      <span class="info-label">제조사</span><span class="info-value">${item[1]}</span>
      <span class="info-label">시리즈</span><span class="info-value">${item[2]}</span>
      <span class="info-label">스케일</span><span class="info-value">${item[4] || '-'}</span>
      <span class="info-label">출시가격</span><span class="info-value">${item[5] || '-'}</span>
      <span class="info-label">수집가 메모</span><p style="line-height:1.8; color:#555; font-size:1.1rem; margin-top:10px;">${item[9] || '내용이 없습니다.'}</p>
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
  function closeModal() {
    document.getElementById('detailModal').style.display = 'none';
    document.body.style.overflow = 'auto';
  }

  function filterBy(s, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.card').forEach(c => {
      c.style.display = (s === 'all' || c.dataset.series === s) ? 'block' : 'none';
    });
  }

  init();
</script>
</body>
</html>
