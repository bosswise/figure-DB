<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 박물관</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;800;900&display=swap" rel="stylesheet">
  <style>
    /* 🚨 기본 UI 초기화 및 라벨 가시성 확보 */
    header, footer, .site-header, .site-footer, .title, b, .gh-header { 
      display: none !important; opacity: 0 !important; visibility: hidden !important; 
    }
    
    :root { --primary: #fab005; --bg: #f7f3f0; --dark: #2d2926; --tag-gold: #ffeaa7; --modal-bg: rgba(0,0,0,0.98); }
    
    #museum-wrapper {
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
      background-color: var(--bg); z-index: 99990; overflow-y: auto;
      font-family: 'Noto Sans KR', sans-serif;
    }

    /* 레이아웃 및 카드 디자인 */
    .main-title-area { padding: 60px 0 40px; display: flex; align-items: center; justify-content: center; max-width: 1500px; margin: 0 auto; gap: 50px; }
    .hall-of-fame { width: 300px; height: 400px; border-radius: 40px; box-shadow: 0 20px 50px rgba(0,0,0,0.12); overflow: hidden; background: #fff; position: relative; }
    .fame-slide { position: absolute; inset: 0; opacity: 0; transition: opacity 1.5s ease; }
    .fame-slide.active { opacity: 1; z-index: 2; }
    .fame-slide img { width: 100%; height: 100%; object-fit: cover; }
    
    .museum-title { font-weight: 900; font-size: 4rem; color: var(--dark); cursor: pointer; letter-spacing: -3px; }
    .total-stats-badge { background: var(--dark); color: var(--primary); padding: 8px 22px; border-radius: 20px; font-size: 1rem; font-weight: 800; margin-top: 15px; display: inline-block; }

    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; max-width: 1550px; margin: 60px auto; padding: 0 45px 150px; }
    .card { background: white; border-radius: 45px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.05); cursor: pointer; transition: 0.4s; border: 1px solid #f2f2f2; }
    .card:hover { transform: translateY(-20px); box-shadow: 0 45px 90px rgba(0,0,0,0.15); }
    .img-box { width: 100%; height: 450px; display: flex; align-items: center; justify-content: center; padding: 40px; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 30px; text-align: center; border-top: 1px solid #f9f9f9; }
    .char-name { font-size: 1.7rem; font-weight: 800; color: var(--dark); }

    /* 상세 모달 */
    .modal { display: none; position: fixed; inset: 0; background: var(--modal-bg); z-index: 99999; justify-content: center; align-items: center; backdrop-filter: blur(30px); }
    .modal-content { background: white; width: 95%; height: 88vh; max-width: 1300px; border-radius: 65px; display: flex; overflow: hidden; position: relative; }
    .modal-img-area { flex: 1.2; position: relative; display: flex; align-items: center; justify-content: center; background: #fff; }
    #modalImg { max-width: 90%; max-height: 90%; object-fit: contain; transition: 0.2s; }
    .modal-info-area { flex: 0.8; padding: 60px; background: #fafafa; overflow-y: auto; }
    .info-label { display: block; font-size: 0.9rem; color: var(--primary); font-weight: 900; margin-bottom: 5px; }
    .info-value { font-size: 1.5rem; font-weight: 700; color: var(--dark); margin-bottom: 25px; display: block; }
  </style>
</head>
<body>

<div id="museum-wrapper">
  <div class="main-title-area">
    <div class="hall-of-fame" id="fameLeft"></div>
    <div class="center-group" style="text-align:center;">
      <h1 class="museum-title" onclick="window.location.reload()">피규어 박물관</h1>
      <div id="totalStats" class="total-stats-badge">로딩 중...</div>
    </div>
    <div class="hall-of-fame" id="fameRight"></div>
  </div>

  <div id="figureGrid" class="grid"></div>
</div>

<div id="detailModal" class="modal" onclick="closeModal()">
  <div class="modal-content" onclick="event.stopPropagation()">
    <div class="modal-img-area">
      <img id="modalImg" src="">
    </div>
    <div class="modal-info-area" id="modalInfo"></div>
  </div>
</div>

<script>
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
  let allData = [];

  async function init() {
    try {
      const response = await fetch(csvURL);
      const text = await response.text();
      const rows = text.split(/\r?\n/).map(row => {
        const m = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
        return m ? m.map(v => v.replace(/^"|"$/g, '').trim()) : [];
      });
      // 8번 인덱스(파일명)가 있는 데이터만 필터링
      allData = rows.slice(1).filter(r => r[8]);
      document.getElementById('totalStats').innerText = `총 ${allData.length}점의 명작 전시 중`;
      renderGrid(allData);
    } catch (e) { console.error("데이터 로딩 실패:", e); }
  }

  // 💡 상품명 결정 로직 (B열 vs M열)
  function getProductName(item) {
    // M열(index 12)이 비었거나 공백이면 B열(index 1)을 사용
    const mColName = item[12];
    const bColName = item[1];
    return (mColName && mColName.trim() !== "") ? mColName : bColName;
  }

  function renderGrid(data) {
    const grid = document.getElementById('figureGrid');
    grid.innerHTML = data.map((item, idx) => {
      const name = getProductName(item); // 💡 수정된 이름 로직 적용
      const img = item[8].split(',')[0].trim();
      return `
        <div class="card" onclick="openModal(${idx})">
          <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>
          <div class="content">
            <div class="char-name">${name}</div>
            <div style="margin-top:10px;">
              <span style="font-size:0.8rem; color:#999;">#${item[2]}</span>
            </div>
          </div>
        </div>`;
    }).join('');
  }

  window.openModal = function(idx) {
    const item = allData[idx];
    const name = getProductName(item); // 💡 모달에서도 동일 로직 적용
    const images = item[8].split(',').map(s => s.trim());
    
    document.getElementById('modalImg').src = `${imageBaseURL}${encodeURIComponent(images[0])}.jpg`;
    document.getElementById('modalInfo').innerHTML = `
      <h2 style="font-size:2.5rem; margin-bottom:40px;">${name}</h2>
      <div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${item[1]}</span></div>
      <div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${item[2]}</span></div>
      <div class="info-item"><span class="info-label">[ 크기 ]</span><span class="info-value">${item[4] || '-'} mm</span></div>
      <div class="info-item"><span class="info-label">[ 가격 ]</span><span class="info-value">${Number(item[5]).toLocaleString()} KRW</span></div>
    `;
    document.getElementById('detailModal').style.display = 'flex';
  }

  window.closeModal = function() { document.getElementById('detailModal').style.display = 'none'; }
  
  init();
</script>
</body>
</html>
