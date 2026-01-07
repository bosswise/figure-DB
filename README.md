<script>
  const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
  const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";
  let allData = [], currentImages = [], currentImgIdx = 0, isZoomed = false;

  async function init() {
    try {
      const wrapper = document.getElementById('museum-wrapper');
      const modal = document.getElementById('detailModal');
      if(document.body && wrapper) document.body.appendChild(wrapper);
      if(document.body && modal) document.body.appendChild(modal);

      const response = await fetch(csvURL);
      const text = await response.text();
      
      // 🚨 [수정됨] 쉼표 문제 해결을 위해 더 똑똑한 파서(parseCSV) 사용
      const rows = parseCSV(text);
      
      // 헤더 제외하고 이미지(I열, Index 8)가 있는 것만 필터링
      allData = rows.slice(1).filter(r => r[8]);
      
      document.getElementById('totalStats').innerText = `총 ${allData.length}점의 명작 전시 중`;
      startFameSlide(); renderFilters(); renderGrid(allData);
    } catch (e) { console.error(e); }
  }

  // 💡 [새로 추가된 기능] 이름 중간에 쉼표가 있어도 쪼개지지 않게 막아주는 함수
  function parseCSV(str) {
    const arr = [];
    let quote = false;  // 따옴표 안에 있는지 체크
    let row = 0, col = 0;

    for (let c = 0; c < str.length; c++) {
      let cc = str[c], nc = str[c+1];
      arr[row] = arr[row] || [];
      arr[row][col] = arr[row][col] || "";

      if (cc == '"' && quote && nc == '"') { arr[row][col] += cc; ++c; } // 따옴표 안의 따옴표 처리
      else if (cc == '"') { quote = !quote; } // 따옴표 시작/끝
      else if (cc == ',' && !quote) { ++col; } // 따옴표 밖의 쉼표만 칸 나누기
      else if (cc == '\r' && nc == '\n' && !quote) { ++row; col = 0; ++c; } // 줄바꿈
      else if (cc == '\n' && !quote) { ++row; col = 0; } // 줄바꿈
      else { arr[row][col] += cc; }
    }
    return arr;
  }

  // 💡 D열(Index 3)을 캐릭터 이름으로 반환
  function getProductName(item) {
    // 혹시 데이터가 비어있을 경우를 대비해 안전장치 추가
    return item[3] ? item[3].trim() : "이름 없음"; 
  }

  function startFameSlide() {
    // 숫자만 있는 파일명 제외 (인물 사진만 골라내기 위함)
    const portraits = allData.filter(item => {
        const img = item[8] ? item[8].split(',')[0].trim() : "";
        return img && !(/\d/.test(img));
    });
    
    // 섞기
    const shuffle = portraits.sort(() => 0.5 - Math.random());
    
    function build(id, startIdx) {
      const target = document.getElementById(id);
      // 데이터가 부족할 경우를 대비해 slice 범위 조정
      const items = shuffle.slice(startIdx, startIdx + 3);
      
      if(items.length === 0) return; // 표시할 이미지가 없으면 중단

      target.innerHTML = items.map((it, idx) => {
          const img = it[8].split(',')[0].trim();
          return `<div class="fame-slide ${idx === 0 ? 'active' : ''}" onclick="window.openModal(${allData.indexOf(it)})"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>`;
      }).join('');

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

  function renderFilters() {
    const menuMap = {};
    allData.forEach(item => {
      const cat = item[10] || "ETC"; 
      const series = item[2] || "ETC";
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
      const name = getProductName(item); 
      // 이미지가 없는 경우 처리
      if (!item[8]) return '';
      const img = item[8].split(',')[0].trim();
      
      return `<div class="card" data-series="${item[2]}" onclick="window.openModal(${allData.indexOf(item)})">
        <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(img)}.jpg"></div>
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

  window.openModal = function(idx) {
    const item = allData[idx]; 
    if(!item || !item[8]) return;

    currentImages = item[8].split(',').map(s => s.trim()); 
    currentImgIdx = 0; isZoomed = false; updateModalImg();
    
    const name = getProductName(item);
    
    document.getElementById('modalInfo').innerHTML = `
      <div class="info-item"><h2 style="font-size:3.5rem; font-weight:900; color:#2d2926; margin:0; line-height:1.2;">${name}</h2></div>
      <div class="info-item"><span class="info-label">[ 제조사 ]</span><span class="info-value">${item[1] || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 시리즈 ]</span><span class="info-value">${item[2] || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 유형 ]</span><span class="info-value">${item[7] || '-'} (${item[6] === 'TRUE' ? '한정판' : '일반판'})</span></div>
      <div class="info-item"><span class="info-label">[ 크기(mm) ]</span><span class="info-value">${item[4] || '-'}</span></div>
      <div class="info-item"><span class="info-label">[ 가격 ]</span><span class="info-value">${isNaN(item[5]) ? item[5] : Number(item[5]).toLocaleString() + ' KRW'}</span></div>
      <div class="info-item" style="border:none;"><span class="info-label">[ 특이사항 ]</span><p style="line-height:1.8; color:#555; font-size:1.2rem; margin:0;">${item[9] || '내용이 없습니다.'}</p></div>
    `;
    document.getElementById('detailModal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  window.toggleZoom = function(e) { isZoomed = !isZoomed; document.getElementById('modalImg').classList.toggle('zoomed'); if (!isZoomed) document.getElementById('modalImg').style.transform = 'scale(1)'; }
  window.handleZoomMove = function(e) { if (!isZoomed) return; const img = document.getElementById('modalImg'); const wrapper = e.currentTarget; const { left, top, width, height } = wrapper.getBoundingClientRect(); const x = ((e.pageX - left - window.scrollX) / width) * 100; const y = ((e.pageY - top - window.scrollY) / height) * 100; img.style.transformOrigin = `${x}% ${y}%`; img.style.transform = 'scale(3.5)'; }
  window.updateModalImg = function() { const img = document.getElementById('modalImg'); img.src = `${imageBaseURL}${encodeURIComponent(currentImages[currentImgIdx])}.jpg`; isZoomed = false; img.classList.remove('zoomed'); img.style.transform = 'scale(1)'; }
  window.changeImg = function(dir) { currentImgIdx = (currentImgIdx + dir + currentImages.length) % currentImages.length; updateModalImg(); }
  window.closeModal = function() { document.getElementById('detailModal').style.display = 'none'; document.body.style.overflow = 'auto'; }
  window.toggleFilters = function() { const menu = document.getElementById('filterMenu'); menu.classList.toggle('collapsed'); document.getElementById('toggleBtn').innerText = menu.classList.contains('collapsed') ? '[ 카테고리 열기 ]' : '[ 책갈피 접기 ]'; }
  window.filterBy = function(s, btn) { document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active')); btn.classList.add('active'); document.querySelectorAll('.card').forEach(c => c.style.display = (s === 'all' || c.dataset.series === s) ? 'block' : 'none'); }
  
  init();
</script>
