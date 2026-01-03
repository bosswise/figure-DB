<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 깃허브 테마 찌꺼기 및 유령 문구 완전 차단 */
    header, footer, .site-header, .site-footer, .title, b, p:first-of-type { display: none !important; visibility: hidden !important; }
    
    :root { --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --accent-tag: #ffeaa7; }
    body { font-family: 'Noto Sans KR', sans-serif; background-color: var(--bg); margin: 0; padding: 0; }

    .museum-wrapper { position: relative; z-index: 10; }
    .main-title-area { padding: 50px 0 30px; text-align: center; }
    .header-mascot { width: 160px; height: 160px; border-radius: 50%; background: white; padding: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .museum-title { font-weight: 900; font-size: 3.5rem; color: var(--dark); margin: 15px 0 5px; cursor: pointer; display: inline-block; }

    /* 📌 책갈피 필터 (가로 스크롤) */
    .sticky-header { background: #2d2926; padding: 15px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
    .bookmark-container { max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; gap: 10px; padding: 0 20px; }
    .category-row { display: flex; align-items: center; gap: 15px; background: rgba(255,255,255,0.05); padding: 8px 15px; border-radius: 12px; }
    .main-label { color: var(--primary); font-weight: 900; min-width: 90px; font-size: 0.85rem; border-right: 1px solid #555; }
    .sub-btns-scroll { display: flex; gap: 8px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }
    .filter-btn { background: #45403c; color: #a5a09c; border: none; padding: 6px 16px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; flex-shrink: 0; }
    .filter-btn.active { background: var(--primary); color: #1a1a1a; font-weight: 800; }

    /* 🏛️ 그리드 및 카드 */
    .container { max-width: 1300px; margin: 40px auto; padding: 0 20px 100px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; }
    .card { background: white; border-radius: 25px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.03); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-10px); }
    .img-box { width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; padding: 15px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 20px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.25rem; font-weight: 800; color: var(--dark); margin-bottom: 8px; }

    /* 🖼️ 상세 정보 및 슬라이드 모달 */
    .modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 2000; justify-content: center; align-items: center; padding: 20px; backdrop-filter: blur(10px); }
    .modal-content { background: white; max-width: 1100px; width: 95%; height: 85vh; border-radius: 40px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.2; background: #fff; padding: 30px; display: flex; align-items: center; justify-content: center; position: relative; border-right: 1px solid #f0f0f0; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(0,0,0,0.1); border: none; color: #333; font-size: 2rem; padding: 10px 20px; cursor: pointer; border-radius: 50%; }
    .nav-btn:hover { background: var(--primary); color: #fff; }
    .prev-btn { left: 20px; }
    .next-btn { right: 20px; }

    .modal-info-area { flex: 0.8; padding: 60px; background: #fafafa; overflow-y: auto; }
    .close-btn { position: absolute; top: 30px; right: 40px; font-size: 3rem; cursor: pointer; color: #ddd; z-index: 10; }
    .info-label { font-size: 0.85rem; color: var(--primary); font-weight: 900; margin-top: 25px; display: block; }
    .info-value { font-size: 1.25rem; font-weight: 500; border-bottom: 1px solid #eee; padding-bottom: 8px; display: block; }
  </style>
</head>
<body>

<div class="museum-wrapper">
  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
    <p id="total-stats" style="color:#8c847d; font-size: 1.1rem;">컬렉션 동기화 중...</p>
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
      <img id="modalImg" src="">
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
      document.getElementById('total-stats').innerText = `Total ${allData.length} Masterpieces`;

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

      const grid = document.getElementById('figureGrid');
      grid.innerHTML = allData.map((item, idx) => {
        const name = (item[12] && item[12] !== "") ? item[12] : item[3];
        const firstImg = item[8].split(',')[0].trim();
        return `
          <div class="card" data-series="${item[2]}" onclick="openModal(${idx})">
            <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(firstImg)}.jpg" loading="lazy" onerror="this.src='https://placehold.co/400x400?text=No+Image'"></div>
            <div class="content">
              <div class="char-name">${name}</div>
              <div style="font-size:0.75rem; color:#aaa;">#${item[1]} #${item[2]}</div>
            </div>
          </div>`;
      }).join('');
    } catch (e) { console.error(e); }
  }

  function openModal(idx) {
    const item = allData[idx];
    const name = (item[12] && item[12] !== "") ? item[12] : item[3];
    currentImages = item[8].split(',').map(s => s.trim());
    currentImgIdx = 0;
    updateModalImg();
    document.getElementById('prevBtn').style.display = currentImages.length > 1 ? 'block' : 'none';
    document.getElementById('nextBtn').style.display = currentImages.length > 1 ? 'block' : 'none';
    document.getElementById('modalInfo').innerHTML = `
      <h2 style="font-size:2.8rem; font-weight:900; margin:0; color:#2d2926;">${name}</h2>
      <span class="info-label">제조사</span><span class="info-value">${item[1]}</span>
      <span class="info-label">시리즈</span><span class="info-value">${item[2]}</span>
      <span class="info-label">스케일</span><span class="info-value">${item[4] || '-'}</span>
      <span class="info-label">출시가격</span><span class="info-value">${item[5] || '-'}</span>
      <span class="info-label">수집가 메모</span><p style="line-height:1.8; color:#555;">${item[9] || '내용이 없습니다.'}</p>
    `;
    document.getElementById('detailModal').style.display = 'flex';
  }

  function updateModalImg() {
    document.getElementById('modalImg').src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`;
  }

  function changeImg(dir) {
    currentImgIdx += dir;
    if (currentImgIdx < 0) currentImgIdx = currentImages.length - 1;
    if (currentImgIdx >= currentImages.length) currentImgIdx = 0;
    updateModalImg();
  }

  function closeModal() { document.getElementById('detailModal').style.display = 'none'; }
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
