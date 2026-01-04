<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 사장님 지시: 모든 유령 문구 및 깃허브 찌꺼기 강제 차단 */
    header, footer, .site-header, .site-footer, .title, b, span:first-of-type, .gh-header { 
      display: none !important; opacity: 0 !important; visibility: hidden !important; height: 0 !important; 
    }

    :root { 
      --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7;
      --modal-bg: rgba(0,0,0,0.97);
    }

    /* 🛡️ 화면 보호 레이어: 유령 문구가 절대 뚫지 못하도록 설정 */
    .museum-full-layer {
      position: relative; width: 100%; min-height: 100vh; background-color: var(--bg); z-index: 999999;
      font-family: 'Noto Sans KR', sans-serif;
    }

    body { margin: 0; padding: 0; background-color: var(--bg); overflow-x: hidden; }

    /* 🖼️ 상단 레이아웃 황금비율 고정 */
    .main-title-area { 
      padding: 50px 0; display: flex; align-items: center; justify-content: center;
      max-width: 1500px; margin: 0 auto; gap: 40px;
    }
    
    .hall-of-fame { 
      width: 320px; height: 420px; position: relative; cursor: pointer; flex-shrink: 0;
      border-radius: 40px; box-shadow: 0 20px 50px rgba(0,0,0,0.12); overflow: hidden;
      background: #fff;
    }
    .fame-slide {
      position: absolute; inset: 0; background: white; opacity: 0; transition: opacity 1.5s ease-in-out;
    }
    .fame-slide.active { opacity: 1; z-index: 2; }
    .fame-slide img { width: 100%; height: 100%; object-fit: cover; }

    .center-group { text-align: center; flex: 0 0 400px; }
    .header-mascot { 
      width: 180px; height: 180px; border-radius: 50%; background: white; 
      padding: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); transition: 0.5s;
    }
    .header-mascot:hover { transform: scale(1.1) rotate(5deg); }
    .museum-title { 
      font-weight: 900; font-size: 3.8rem; color: var(--dark); 
      margin: 20px 0 10px; cursor: pointer; display: inline-block; letter-spacing: -3px;
    }

    /* 📌 스마트 책갈피 (슬림 UI) */
    .sticky-header { background: #2d2926; padding: 15px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 10px 40px rgba(0,0,0,0.4); }
    .toggle-bar { max-width: 1200px; margin: 0 auto; display: flex; justify-content: flex-end; padding: 0 25px 8px; }
    .toggle-btn { background: none; border: 1px solid #666; color: #999; font-size: 0.75rem; padding: 5px 15px; border-radius: 8px; cursor: pointer; transition: 0.3s; }
    .toggle-btn:hover { border-color: var(--primary); color: var(--primary); }

    .bookmark-container { 
      max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; 
      gap: 12px; padding: 0 25px 20px; overflow: hidden; transition: 0.6s cubic-bezier(0.4, 0, 0.2, 1); max-height: 1000px; 
    }
    .bookmark-container.collapsed { max-height: 0; padding-bottom: 0; }
    .category-row { display: flex; align-items: center; gap: 20px; background: rgba(255,255,255,0.08); padding: 15px 25px; border-radius: 20px; }
    .main-label { color: var(--primary); font-weight: 900; min-width: 120px; font-size: 0.95rem; border-right: 2px solid #555; }
    
    .sub-btns-scroll { display: flex; gap: 12px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 10px 22px; border-radius: 25px; cursor: pointer; font-size: 0.9rem; transition: 0.3s; }
    .filter-btn.active { background: var(--primary); color: #1a1a1a; font-weight: 800; box-shadow: 0 0 20px rgba(250,176,5,0.4); }

    /* 🏛️ 전시 그리드 (가로 3개 고정) */
    .container { max-width: 1500px; margin: 60px auto; padding: 0 40px 150px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; }
    .card { background: white; border-radius: 45px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; border: 1px solid #f2f2f2; }
    .card:hover { transform: translateY(-20px); box-shadow: 0 45px 90px rgba(0,0,0,0.15); }
    
    .img-box { width: 100%; height: 450px; display: flex; align-items: center; justify-content: center; padding: 40px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 45px; text-align: center; border-top: 1px solid #f9f9f9; }
    .char-name { font-size: 1.7rem; font-weight: 800; color: var(--dark); margin-bottom: 20px; }
    
    /* #태그 스타일 */
    .tag-wrap { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
    .tag { font-size: 0.85rem; background: var(--tag-gold); color: #d35400; padding: 6px 18px; border-radius: 15px; font-weight: 800; }
    .tag.sec { background: #f0f0f0; color: #888; }

    /* 🖼️ 사장님 지시: 마우스 자유 이동 확대 모달 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 9999999; justify-content: center; align-items: center; padding: 40px; backdrop-filter: blur(30px); }
    .modal-content { background: white; max-width: 1300px; width: 98%; height: 88vh; border-radius: 65px; display: flex; overflow: hidden; position: relative; }
    
    .modal-img-area { flex: 1.4; background: #fff; position: relative; border-right: 1px solid #f0f0f0; overflow: hidden; display: flex; align-items: center; justify-content: center; }
    .modal-img-wrapper { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; }
    
    #modalImg { 
      max-width: 90%; max-height: 90%; object-fit: contain; 
      cursor: zoom-in; transition: transform 0.1s ease-out; transform-origin: center;
    }
    #modalImg.zoomed { cursor: zoom-out; transform: scale(3); }

    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 70px; height: 70px; background: rgba(255,255,255,0.98); border: none; border-radius: 50%; font-size: 2rem; cursor: pointer; z-index: 10; box-shadow: 0 10px 30px rgba(0,0,0,0.15); transition: 0.3s; }
    .nav-btn:hover { background: var(--primary); color: white; transform: translateY(-50%) scale(1.1); }

    .modal-info-area { flex: 0.6; padding: 80px; background: #fafafa; overflow-y: auto; }
    .close-btn { position: absolute; top: 45px; right: 60px; font-size: 4.5rem; cursor: pointer; color: #ddd; z-index: 100; transition: 0.3s; line-height: 0.7; }
    .close-btn:hover { color: var(--dark); transform: rotate(90deg); }

    /* 상세창 직관적 라벨링 */
    .info-item { margin-bottom: 35px; border-bottom: 2px solid #eee; padding-bottom: 15px; }
    .info-label { font-size: 1.05rem; color: var(--primary); font-weight: 900; display: block; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px; }
    .info-value { font-size: 1.7rem; font-weight: 600; display: block; color: var(--dark); }

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
      <p id="total-stats" style="color:#8c847d; font-size: 1.3rem; font-weight: 300;">총 0점의 명작 전시 중</p>
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
      <button class="nav-btn" style="left:35px" onclick="changeImg(-1)">&lt;</button>
      <div class="modal-img-wrapper" onmousemove="handleZoomMove(event)">
        <img id="modalImg" src="" onclick="toggleZoom(event)">
      </div>
      <button class="nav-btn" style="right:35px" onclick="changeImg(1)">&gt;</button>
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
  let isZoomed = false;

  async function init() {
    try {
      const response = await fetch(csvURL);
      const text = await response.text();
      const rows = text.split(/\r?\n/).map(row => {
        const m = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
        return m ? m.map(v => v.replace(/^"|"$/g, '').trim()) : [];
      });

      allData = rows.slice(1).filter(r => r[8]);
      document.getElementById('total-stats').innerText = `총 ${allData.length}점의 명작 전시 중`;

      startFameSlide(); 
      renderFilters();
      renderGrid(allData);

      // 🚨 사장님 지시: 유령 문구 박멸 무한 감시 루프
      setInterval(() => {
        document.querySelectorAll('header, footer, .title, b, span:first-of-type, h2').forEach(el => {
          if(!el.closest('#museumLayer') && !el.closest('#detailModal')) el.remove();
        });
      }, 200);

    } catch (e) { console.error(e); }
  }

  function startFameSlide() {
    const portraits = allData.filter(item => !(/\d/.test(item[8].split(',')[0].trim())));
    const shuffle = portraits.sort(() => 0.5 - Math.random());
    function build(id, startIdx) {
      const target = document.getElementById(id);
      const items = shuffle.slice(startIdx, startIdx + 3);
      target.innerHTML = items.map((it, idx) => `
        <div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="openModal(${allData.indexOf(it)})">
          <img src="${imageBaseURL}${encodeURIComponent(it[8].split(',')[0].trim())}.jpg">
        </div>`).join('');
      let cur = 0;
      setInterval(() => {
        const slides = target.querySelectorAll('.fame-slide');
        if(slides.length > 0) {
          slides[cur].classList.remove('active'); cur = (cur + 1) % slides.length; slides[cur].classList.add('active');
        }
      }, 4000);
    }
    build('fameLeft', 0); build('fameRight', 3);
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
    grid.innerHTML = data.map((item, idx) => {
      const name = item[12] || item[3];
      const img = item[8].split(',')[0].trim();
      return `
        <div class="card" data-series="${item[2]}" onclick="openModal(${idx})">
          <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>
          <div class="content">
            <div class="char-name">${name}</div>
            <div class="tag-wrap">
              <span class="tag">#${item[10]}</span>
              <span class="tag sec">#${item[2]}</span>
            </div>
          </div>
        </div>`;
    }).join('');
  }

  function openModal(idx) {
    const item = allData[idx];
    currentImages = item[8].split(',').map(s => s.trim());
    currentImgIdx = 0; isZoomed = false;
    updateModalImg();
    
    document.getElementById('modalInfo').innerHTML = `
      <div class="info-item"><h2 style="font-size:3.5rem; font-weight:900; color:#2d2926; margin:0;">${item[12] || item[3]}</h2></div>
      <div class="info-item"><span class="info-label">제조사</span><span class="info-value">${item[1]}</span></div>
      <div class="info-item"><span class="info-label">시리즈</span><span class="info-value">${item[2]}</span></div>
      <div class="info-item"><span class="info-label">스케일</span><span class="info-value">${item[4] || '-'}</span></div>
      <div class="info-item"><span class="info-label">출시가격</span><span class="info-value">${isNaN(item[5]) ? item[5] : Number(item[5]).toLocaleString() + ' KRW'}</span></div>
      <div class="info-item" style="border:none;"><span class="info-label">수집가 메모</span><p style="line-height:2.2; color:#555; font-size:1.2rem; margin:0;">${item[9] || '내용이 없습니다.'}</p></div>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  function toggleZoom(e) {
    const img = document.getElementById('modalImg');
    isZoomed = !isZoomed;
    img.classList.toggle('zoomed');
    if (!isZoomed) img.style.transform = 'scale(1)';
  }

  function handleZoomMove(e) {
    if (!isZoomed) return;
    const img = document.getElementById('modalImg');
    const wrapper = e.currentTarget;
    const { left, top, width, height } = wrapper.getBoundingClientRect();
    const x = ((e.pageX - left - window.scrollX) / width) * 100;
    const y = ((e.pageY - top - window.scrollY) / height) * 100;
    img.style.transformOrigin = `${x}% ${y}%`;
    img.style.transform = 'scale(3)';
  }

  function updateModalImg() {
    const img = document.getElementById('modalImg');
    img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`;
    isZoomed = false; img.classList.remove('zoomed'); img.style.transform = 'scale(1)';
  }

  function changeImg(dir) { currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; updateModalImg(); }
  function closeModal() { document.getElementById('detailModal').style.display = 'none'; document.body.style.overflow = 'auto'; }
  function toggleFilters() {
    const menu = document.getElementById('filterMenu');
    menu.classList.toggle('collapsed');
    document.getElementById('toggleBtn').innerText = menu.classList.contains('collapsed') ? '[ 카테고리 열기 ]' : '[ 책갈피 접기 ]';
  }
  function filterBy(s, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.card').forEach(c => c.style.display = (s === 'all' || c.dataset.series === s) ? 'block' : 'none');
  }
  init();
</script>
</body>
</html>
