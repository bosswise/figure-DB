<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 [파란 글자 박멸] 깃허브 테마 강제 차단 시스템 */
    html, body { margin: 0; padding: 0; width: 100%; height: 100%; }
    /* 깃허브 자동 생성 요소를 이름/ID/클래스 상관없이 모두 숨김 */
    header, footer, .site-header, .site-footer, .title, a[href*="github.com"] { 
      display: none !important; visibility: hidden !important; height: 0 !important; width: 0 !important; opacity: 0 !important; pointer-events: none !important;
    }
    
    :root { 
      --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-bg: #ffeaa7; 
      --modal-bg: rgba(0,0,0,0.92);
    }

    /* 전체 화면을 우리 레이어로 덮어 유령 텍스트 노출 방지 */
    .museum-body-wrapper { 
      position: relative; width: 100%; min-height: 100vh; background-color: var(--bg); z-index: 9999;
      font-family: 'Noto Sans KR', sans-serif;
    }

    /* 🖼️ 헤더 & 타이틀 */
    .main-title-area { padding: 60px 0 30px; text-align: center; }
    .header-mascot { width: 170px; height: 170px; border-radius: 50%; background: white; padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: 0.3s; }
    .header-mascot:hover { transform: rotate(5deg) scale(1.05); }
    .museum-title { font-weight: 900; font-size: 3.8rem; color: var(--dark); margin: 15px 0 5px; cursor: pointer; display: inline-block; letter-spacing: -2px; }
    .stats-text { color: #8c847d; font-size: 1.1rem; font-weight: 300; }

    /* 📌 스마트 책갈피 필터 */
    .sticky-header { background: #2d2926; padding: 18px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 5px 25px rgba(0,0,0,0.3); }
    .bookmark-container { max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding: 0 25px; }
    .category-row { display: flex; align-items: center; gap: 15px; background: rgba(255,255,255,0.06); padding: 10px 18px; border-radius: 15px; }
    .main-label { color: var(--primary); font-weight: 900; min-width: 100px; font-size: 0.9rem; border-right: 1px solid #555; text-transform: uppercase; }
    .sub-btns-scroll { display: flex; gap: 10px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }
    
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 7px 18px; border-radius: 25px; cursor: pointer; font-size: 0.85rem; transition: 0.3s; flex-shrink: 0; }
    .filter-btn.active { background: var(--primary); color: #1a1a1a; font-weight: 800; box-shadow: 0 0 15px rgba(250,176,5,0.3); }

    /* 🏛️ 전시 카드 그리드 */
    .container { max-width: 1400px; margin: 50px auto; padding: 0 25px 120px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 40px; }
    .card { background: white; border-radius: 30px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.03); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-15px); box-shadow: 0 30px 60px rgba(0,0,0,0.1); }
    .img-box { width: 100%; height: 350px; display: flex; align-items: center; justify-content: center; padding: 25px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 30px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.4rem; font-weight: 800; color: var(--dark); margin-bottom: 12px; }
    .tag-wrap { display: flex; justify-content: center; gap: 6px; }
    .tag { font-size: 0.75rem; background: var(--tag-bg); color: #d35400; padding: 4px 12px; border-radius: 10px; font-weight: 700; }

    /* 🖼️ [부활] 모던 화살표 & 확대 모달 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 99999; justify-content: center; align-items: center; padding: 25px; backdrop-filter: blur(15px); }
    .modal-content { background: white; max-width: 1200px; width: 98%; height: 88vh; border-radius: 50px; display: flex; overflow: hidden; position: relative; }
    
    .modal-img-area { flex: 1.3; background: #fff; padding: 40px; display: flex; align-items: center; justify-content: center; position: relative; border-right: 1px solid #f0f0f0; overflow: hidden; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; transition: 0.3s ease; cursor: zoom-in; }
    .modal-img-area img.zoomed { transform: scale(2.2); cursor: zoom-out; }

    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 55px; height: 55px; background: rgba(255,255,255,0.9); border: none; border-radius: 50%; font-size: 1.5rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.3s; color: #333; box-shadow: 0 4px 15px rgba(0,0,0,0.1); z-index: 5; }
    .nav-btn:hover { background: var(--primary); color: white; transform: translateY(-50%) scale(1.1); }
    .prev-btn { left: 25px; }
    .next-btn { right: 25px; }

    .modal-info-area { flex: 0.7; padding: 60px; background: #fafafa; overflow-y: auto; text-align: left; }
    .close-btn { position: absolute; top: 40px; right: 50px; font-size: 3.5rem; cursor: pointer; color: #ccc; z-index: 20; transition: 0.3s; }
    .close-btn:hover { color: var(--dark); transform: rotate(90deg); }

    .info-label { font-size: 0.9rem; color: var(--primary); font-weight: 900; margin-top: 35px; display: block; }
    .info-value { font-size: 1.4rem; font-weight: 600; border-bottom: 2px solid #eee; padding-bottom: 10px; display: block; color: var(--dark); }
  </style>
</head>
<body>

<div class="museum-body-wrapper">
  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
    <p id="total-stats" class="stats-text">전시실 준비 중...</p>
  </div>

  <div class="sticky-header">
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
        const k = item[10] || "ETC"; const b = item[2] || "ETC";
        if (!menuMap[k]) menuMap[k] = new Set();
        menuMap[k].add(b);
      });

      const filterMenu = document.getElementById('filterMenu');
      filterMenu.innerHTML = `<div class="category-row"><button class="filter-btn active" onclick="filterBy('all', this)">전체보기</button></div>`;
      for (const [cat, seriesSet] of Object.entries(menuMap)) {
        const row = document.createElement('div');
        row.className = 'category-row';
        let html = `<span class="main-label">${cat.toUpperCase()}</span><div class="sub-btns-scroll">`;
        seriesSet.forEach(s => { html += `<button class="filter-btn" onclick="filterBy('${s}', this)">${s}</button>`; });
        row.innerHTML = html + `</div></div>`;
        filterMenu.appendChild(row);
      }

      renderGrid(allData);
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
            <div class="tag-wrap"><span class="tag">#${item[1]}</span><span class="tag" style="background:#eee;color:#777;">#${item[2]}</span></div>
          </div>
        </div>`;
    }).join('');
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
      <h2 style="font-size:3rem; font-weight:900; color:#2d2926; margin:0 0 10px 0;">${name}</h2>
      <span class="info-label">제조사</span><span class="info-value">${item[1]}</span>
      <span class="info-label">시리즈</span><span class="info-value">${item[2]}</span>
      <span class="info-label">스케일</span><span class="info-value">${item[4] || '-'}</span>
      <span class="info-label">출시가격</span><span class="info-value">${item[5] || '-'}</span>
      <span class="info-label">메모</span><p style="line-height:2; color:#555; font-size:1.1rem; margin-top:10px;">${item[9] || '내용이 없습니다.'}</p>
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

  function toggleZoom(e) {
    e.target.classList.toggle('zoomed');
  }

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
