<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 사장님 전용: 유령 텍스트 박멸 시스템 */
    * { box-sizing: border-box; }
    header, footer, .site-header, .site-footer, .title, a[href*="github.com"], b, span:first-of-type { 
      display: none !important; opacity: 0 !important; pointer-events: none !important; 
    }

    :root { 
      --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7; --tag-grey: #eee;
      --modal-bg: rgba(0,0,0,0.95);
    }

    /* 🛡️ 화면 전체 차폐막: 깃허브 찌꺼기를 물리적으로 가립니다 */
    .museum-full-layer {
      position: fixed; inset: 0; background-color: var(--bg); z-index: 999999;
      overflow-y: auto; font-family: 'Noto Sans KR', sans-serif;
    }

    body { margin: 0; padding: 0; background-color: var(--bg); }

    /* 🖼️ 헤드 제목 섹션 (크기 복구) */
    .main-title-area { padding: 80px 0 40px; text-align: center; }
    .header-mascot { 
      width: 200px; height: 200px; border-radius: 50%; background: white; 
      padding: 12px; box-shadow: 0 15px 45px rgba(0,0,0,0.08); transition: 0.4s; 
    }
    .header-mascot:hover { transform: scale(1.1) rotate(3deg); }
    .museum-title { 
      font-weight: 900; font-size: 4.5rem; color: var(--dark); 
      margin: 20px 0 10px; cursor: pointer; display: inline-block; letter-spacing: -3px;
      transition: 0.3s;
    }
    .museum-title:hover { color: var(--primary); transform: translateY(-3px); }
    .stats-text { color: #8c847d; font-size: 1.2rem; font-weight: 300; }

    /* 📌 책갈피 필터 (가로 스크롤 & 겹침 해결) */
    .sticky-header { 
      background: #2d2926; padding: 20px 0; position: sticky; top: 0; 
      z-index: 1000; box-shadow: 0 8px 30px rgba(0,0,0,0.4); 
    }
    .bookmark-container { max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding: 0 25px; }
    .category-row { display: flex; align-items: center; gap: 20px; background: rgba(255,255,255,0.08); padding: 12px 20px; border-radius: 18px; }
    .main-label { color: var(--primary); font-weight: 900; min-width: 110px; font-size: 0.95rem; border-right: 2px solid #555; }
    .sub-btns-scroll { display: flex; gap: 10px; overflow-x: auto; white-space: nowrap; scrollbar-width: none; }
    .sub-btns-scroll::-webkit-scrollbar { display: none; }
    
    .filter-btn { 
      background: #45403c; color: #a5a09c; border: none; padding: 8px 20px; 
      border-radius: 25px; cursor: pointer; font-size: 0.9rem; transition: 0.3s; 
    }
    .filter-btn.active { background: var(--primary); color: #1a1a1a; font-weight: 800; box-shadow: 0 0 20px rgba(250,176,5,0.4); }

    /* 🏛️ 전시 그리드 (가로 3개 고정) */
    .container { max-width: 1400px; margin: 60px auto; padding: 0 30px 150px; }
    .grid { 
      display: grid; 
      grid-template-columns: repeat(3, 1fr); /* 사장님 지시: 가로 3개 고정 */
      gap: 50px; 
    }
    
    .card { background: white; border-radius: 35px; overflow: hidden; box-shadow: 0 12px 45px rgba(0,0,0,0.04); cursor: pointer; transition: 0.4s; }
    .card:hover { transform: translateY(-15px); box-shadow: 0 35px 70px rgba(0,0,0,0.12); }
    .img-box { width: 100%; height: 420px; display: flex; align-items: center; justify-content: center; padding: 30px; background: #fff; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 35px; text-align: center; border-top: 1px solid #f8f9fa; }
    .char-name { font-size: 1.6rem; font-weight: 800; color: var(--dark); margin-bottom: 15px; }
    
    /* 태그 다양화 디자인 */
    .tag-wrap { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; }
    .tag { font-size: 0.8rem; background: var(--tag-gold); color: #d35400; padding: 5px 14px; border-radius: 12px; font-weight: 700; }
    .tag.sec { background: var(--tag-grey); color: #777; }

    /* 🖼️ 확대 및 슬라이드 모달 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 9999999; justify-content: center; align-items: center; padding: 30px; backdrop-filter: blur(20px); }
    .modal-content { background: white; max-width: 1250px; width: 98%; height: 85vh; border-radius: 55px; display: flex; overflow: hidden; position: relative; }
    
    .modal-img-area { flex: 1.3; background: #fff; padding: 50px; display: flex; align-items: center; justify-content: center; position: relative; border-right: 1px solid #f0f0f0; overflow: hidden; }
    .modal-img-area img { max-width: 100%; max-height: 100%; object-fit: contain; transition: 0.4s ease; cursor: zoom-in; }
    .modal-img-area img.zoomed { transform: scale(2.2); cursor: zoom-out; }

    .nav-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 65px; height: 65px; background: rgba(255,255,255,0.95); border: none; border-radius: 50%; font-size: 1.8rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.3s; color: #333; box-shadow: 0 6px 20px rgba(0,0,0,0.15); z-index: 10; }
    .nav-btn:hover { background: var(--primary); color: white; transform: translateY(-50%) scale(1.1); }
    .prev-btn { left: 35px; }
    .next-btn { right: 35px; }

    .modal-info-area { flex: 0.7; padding: 70px; background: #fafafa; overflow-y: auto; text-align: left; }
    .close-btn { position: absolute; top: 40px; right: 50px; font-size: 4rem; cursor: pointer; color: #ccc; z-index: 100; line-height: 0.7; transition: 0.3s; }
    .close-btn:hover { color: var(--dark); transform: rotate(90deg); }

    .info-label { font-size: 0.95rem; color: var(--primary); font-weight: 900; margin-top: 40px; display: block; letter-spacing: 1.5px; }
    .info-value { font-size: 1.5rem; font-weight: 600; border-bottom: 2px solid #eee; padding-bottom: 12px; display: block; color: var(--dark); }

    @media (max-width: 1100px) { .grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 700px) { .grid { grid-template-columns: 1fr; } }
  </style>
</head>
<body>

<div class="museum-full-layer" id="museumLayer">
  <div class="main-title-area">
    <img src="https://bosswise.github.io/figure-DB/images/mascot.png" class="header-mascot">
    <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
    <p id="total-stats" class="stats-text">The Grand Collection is Loading...</p>
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

      // 필터 생성 (K열: 10, C열: 2)
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
      
      // 🚨 사명: 유령 문구 삭제 루틴 (0.5초 뒤 한번 더 확인)
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
      // 사장님 보고: M열(12) 우선, 없으면 D열(3)
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

  function openModal(idx) {
    const item = allData[idx];
    const name = (item[12] && item[12] !== "") ? item[12] : item[3];
    currentImages = item[8].split(',').map(s => s.trim());
    currentImgIdx = 0;
    updateModalImg();
    document.getElementById('prevBtn').style.display = currentImages.length > 1 ? 'flex' : 'none';
    document.getElementById('nextBtn').style.display = currentImages.length > 1 ? 'flex' : 'none';
    document.getElementById('modalInfo').innerHTML = `
      <h2 style="font-size:3.2rem; font-weight:900; color:#2d2926; line-height:1.1;">${name}</h2>
      <span class="info-label">제조사</span><span class="info-value">${item[1]}</span>
      <span class="info-label">시리즈</span><span class="info-value">${item[2]}</span>
      <span class="info-label">스케일</span><span class="info-value">${item[4] || '-'}</span>
      <span class="info-label">출시가격</span><span class="info-value">${item[5] || '-'}</span>
      <span class="info-label">수집가 메모</span><p style="line-height:2; color:#555; font-size:1.15rem; margin-top:15px;">${item[9] || '내용이 없습니다.'}</p>
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
