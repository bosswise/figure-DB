<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    header, footer, .site-header, .site-footer, .title, b, span:first-of-type, .gh-header { 
      display: none !important; opacity: 0 !important; visibility: hidden !important; 
    }
    :root { --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7; --modal-bg: rgba(0,0,0,0.98); }
    .museum-full-layer { position: relative; width: 100%; min-height: 100vh; background-color: var(--bg); z-index: 999999; font-family: 'Noto Sans KR', sans-serif; }
    body { margin: 0; padding: 0; background-color: var(--bg); overflow-x: hidden; }

    /* 상단 영역 */
    .main-title-area { padding: 60px 0; display: flex; align-items: center; justify-content: center; max-width: 1500px; margin: 0 auto; gap: 50px; }
    .hall-of-fame { width: 300px; height: 400px; position: relative; cursor: pointer; border-radius: 35px; box-shadow: 0 20px 50px rgba(0,0,0,0.12); overflow: hidden; background: #fff; }
    .fame-slide { position: absolute; inset: 0; background: white; opacity: 0; transition: opacity 1.5s ease; }
    .fame-slide.active { opacity: 1; z-index: 2; }
    .fame-slide img { width: 100%; height: 100%; object-fit: cover; }
    .header-mascot { width: 180px; height: 180px; border-radius: 50%; background: white; padding: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); margin-bottom: 20px; }
    .museum-title { font-weight: 900; font-size: 4rem; color: var(--dark); margin: 0; cursor: pointer; letter-spacing: -3px; }

    /* 필터 및 그리드 */
    .sticky-header { background: #2d2926; padding: 15px 0; position: sticky; top: 0; z-index: 1000; }
    .container { max-width: 1550px; margin: 60px auto; padding: 0 45px 150px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; }
    .card { background: white; border-radius: 45px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; }
    .img-box { width: 100%; height: 450px; display: flex; align-items: center; justify-content: center; padding: 40px; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 45px; text-align: center; }
    .char-name { font-size: 1.7rem; font-weight: 800; color: var(--dark); margin-bottom: 20px; }
    .tag { font-size: 0.85rem; background: var(--tag-gold); color: #d35400; padding: 6px 18px; border-radius: 15px; font-weight: 800; margin-right: 8px; }

    /* 💎 사장님이 원하신 '설명 라벨링' 상세창 디자인 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 9999999; justify-content: center; align-items: center; padding: 40px; backdrop-filter: blur(30px); }
    .modal-content { background: white; max-width: 1300px; width: 98%; height: 88vh; border-radius: 65px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.4; background: #fff; overflow: hidden; display: flex; align-items: center; justify-content: center; position: relative; border-right: 1px solid #f0f0f0; }
    .modal-img-wrapper { width: 100%; height: 100%; overflow: hidden; display: flex; align-items: center; justify-content: center; }
    #modalImg { max-width: 90%; max-height: 90%; object-fit: contain; transition: transform 0.1s ease-out; transform-origin: center; cursor: zoom-in; }
    #modalImg.zoomed { cursor: zoom-out; transform: scale(3.5); }
    
    .modal-info-area { flex: 0.6; padding: 80px; background: #fafafa; overflow-y: auto; text-align: left; }
    .info-item { margin-bottom: 30px; border-bottom: 2px solid #eee; padding-bottom: 12px; }
    .info-label { font-size: 1rem; color: var(--primary); font-weight: 900; display: block; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px; }
    .info-value { font-size: 1.7rem; font-weight: 600; display: block; color: var(--dark); }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 70px; height: 70px; background: rgba(255,255,255,0.95); border-radius: 50%; border: none; font-size: 2.5rem; cursor: pointer; z-index: 10; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    .close-btn { position: absolute; top: 40px; right: 60px; font-size: 4.5rem; cursor: pointer; color: #ddd; z-index: 100; line-height: 0.7; }
  </style>
</head>
<body>
<div class="museum-full-layer" id="museumLayer">
  <div class="main-title-area">
    <div class="hall-of-fame" id="fameLeft"></div>
    <div class="center-group">
      <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
      <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
      <div id="totalStats" style="margin-top:15px; font-weight:800; color:var(--primary); background:var(--dark); padding:8px 20px; border-radius:20px; display:inline-block;">총 0점의 명작 전시 중</div>
    </div>
    <div class="hall-of-fame" id="fameRight"></div>
  </div>
  <div class="sticky-header">
    <div style="max-width:1200px; margin:0 auto; padding: 0 25px;"><div id="filterMenu" style="display:flex; flex-direction:column; gap:10px;"></div></div>
  </div>
  <div class="container"><div id="figureGrid" class="grid"></div></div>
</div>

<div id="detailModal" class="modal" onclick="closeModal()">
  <div class="modal-content" onclick="event.stopPropagation()">
    <span class="close-btn" onclick="closeModal()">&times;</span>
    <div class="modal-img-area">
      <button class="nav-btn" style="left:35px" onclick="changeImg(-1)">‹</button>
      <div class="modal-img-wrapper" onmousemove="handleZoomMove(event)"><img id="modalImg" src="" onclick="toggleZoom(event)"></div>
      <button class="nav-btn" style="right:35px" onclick="changeImg(1)">›</button>
    </div>
    <div class="modal-info-area" id="modalInfo"></div>
  </div>
</div>

<script>
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
  let allData = [], currentImages = [], currentImgIdx = 0, isZoomed = false;

  async function init() {
    try {
      const response = await fetch(csvURL);
      const text = await response.text();
      const rows = text.split(/\r?\n/).map(row => {
        const m = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
        return m ? m.map(v => v.replace(/^"|"$/g, '').trim()) : [];
      });
      allData = rows.slice(1).filter(r => r[8]);
      document.getElementById('totalStats').innerText = `총 ${allData.length}점의 명작 전시 중`;
      startFameSlide(); renderFilters(); renderGrid(allData);
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
      target.innerHTML = items.map((it, idx) => `<div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="openModal(${allData.indexOf(it)})"><img src="${imageBaseURL}${encodeURIComponent(it[8].split(',')[0].trim())}.jpg"></div>`).join('');
      let cur = 0; setInterval(() => { const slides = target.querySelectorAll('.fame-slide'); if(slides.length > 0) { slides[cur].classList.remove('active'); cur = (cur + 1) % slides.length; slides[cur].classList.add('active'); } }, 4500);
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
    filterMenu.innerHTML = `<div style="display:flex; gap:10px; flex-wrap:wrap; padding:15px 0;"><button onclick="filterBy('all', this)" style="background:var(--primary); color:#1a1a1a; padding:8px 20px; border-radius:20px; border:none; font-weight:800; cursor:pointer;">전체보기</button></div>`;
    for (const [cat, seriesSet] of Object.entries(menuMap)) {
      const row = document.createElement('div');
      row.innerHTML = `<span style="color:var(--primary); font-weight:900; margin-right:15px;">${cat}</span>`;
      seriesSet.forEach(s => {
        const btn = document.createElement('button');
        btn.innerText = s;
        btn.style = "background:#45403c; color:#a5a09c; border:none; padding:6px 15px; border-radius:15px; cursor:pointer; margin-right:8px;";
        btn.onclick = (e) => filterBy(s, e.target);
        row.appendChild(btn);
      });
      filterMenu.appendChild(row);
    }
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    grid.innerHTML = data.map((item, idx) => {
      const name = (item[12] && item[12] !== "") ? item[12] : item[3];
      const img = item[8].split(',')[0].trim();
      return `<div class="card" data-series="${item[2]}" onclick="openModal(${allData.indexOf(item)})"><div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div><div class="content"><div class="char-name">${name}</div><div style="display:flex; justify-content:center; gap:8px;"><span class="tag">#${item[10]}</span><span class="tag" style="background:#eee;color:#777;">#${item[2]}</span></div></div></div>`;
    }).join('');
  }

  function openModal(idx) {
    const item = allData[idx]; currentImages = item[8].split(',').map(s => s.trim()); currentImgIdx = 0; isZoomed = false; updateModalImg();
    const name = (item[12] && item[12] !== "") ? item[12] : item[3];
    
    // 💎 사장님 지시: 상세 라벨링 완벽 반영
    document.getElementById('modalInfo').innerHTML = `
      <div class="info-item"><h2 style="font-size:3.5rem; font-weight:900; color:#2d2926; margin:0;">${name}</h2></div>
      <div class="info-item"><span class="info-label">제조사</span><span class="info-value">${item[1]}</span></div>
      <div class="info-item"><span class="info-label">시리즈</span><span class="info-value">${item[2]}</span></div>
      <div class="info-item"><span class="info-label">유형</span><span class="info-value">${item[7]} (${item[6] === 'TRUE' ? '한정판' : '일반판'})</span></div>
      <div class="info-item"><span class="info-label">크기(mm)</span><span class="info-value">${item[4] || '-'}</span></div>
      <div class="info-item"><span class="info-label">가격</span><span class="info-value">${isNaN(item[5]) ? item[5] : Number(item[5]).toLocaleString() + ' KRW'}</span></div>
      <div class="info-item" style="border:none;"><span class="info-label">특이사항</span><p style="line-height:2.2; color:#555; font-size:1.1rem; margin:0;">${item[9] || '내용이 없습니다.'}</p></div>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  function toggleZoom(e) { isZoomed = !isZoomed; document.getElementById('modalImg').classList.toggle('zoomed'); if (!isZoomed) document.getElementById('modalImg').style.transform = 'scale(1)'; }
  function handleZoomMove(e) { if (!isZoomed) return; const img = document.getElementById('modalImg'); const wrapper = e.currentTarget; const { left, top, width, height } = wrapper.getBoundingClientRect(); const x = ((e.pageX - left - window.scrollX) / width) * 100; const y = ((e.pageY - top - window.scrollY) / height) * 100; img.style.transformOrigin = `${x}% ${y}%`; img.style.transform = 'scale(3.5)'; }
  function updateModalImg() { const img = document.getElementById('modalImg'); img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`; isZoomed = false; img.classList.remove('zoomed'); img.style.transform = 'scale(1)'; }
  function changeImg(dir) { currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; updateModalImg(); }
  function closeModal() { document.getElementById('detailModal').style.display = 'none'; document.body.style.overflow = 'auto'; }
  function filterBy(s, btn) { document.querySelectorAll('.card').forEach(c => c.style.display = (s === 'all' || c.dataset.series === s) ? 'block' : 'none'); }
  init();
</script>
</body>
</html>
