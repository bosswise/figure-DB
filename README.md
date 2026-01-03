<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>피규어 박물관</title>
    <style>
        :root { --p-color: #2c3e50; --a-color: #3498db; --bg: #f4f7f6; }
        body { font-family: 'Pretendard', sans-serif; background: var(--bg); margin: 0; padding: 20px; }
        
        /* 헤더 섹션 */
        .header { text-align: center; margin-bottom: 30px; }
        .stats-badge { background: #fff; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }

        /* 책갈피 스타일 필터 */
        .bookmark-area { max-width: 1200px; margin: 0 auto 30px; display: flex; flex-direction: column; gap: 15px; }
        .category-row { display: flex; align-items: center; gap: 10px; background: rgba(0,0,0,0.03); padding: 10px; border-radius: 10px; }
        .main-label { font-weight: 800; min-width: 100px; color: var(--p-color); font-size: 0.9rem; border-right: 2px solid #ccc; }
        .sub-buttons { display: flex; flex-wrap: wrap; gap: 8px; }
        
        .btn-tag { 
            background: #fff; border: 1px solid #ddd; padding: 5px 12px; border-radius: 5px; 
            cursor: pointer; font-size: 0.85rem; transition: all 0.2s; 
        }
        .btn-tag:hover, .btn-tag.active { background: var(--p-color); color: white; border-color: var(--p-color); }

        /* 그리드 */
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }
        .card { background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.08); transition: 0.3s; }
        .card:hover { transform: translateY(-5-px); }
        .card img { width: 100%; height: 280px; object-fit: cover; cursor: pointer; }
        
        .info { padding: 15px; }
        .name { font-weight: bold; font-size: 1rem; margin-bottom: 8px; color: #222; }
        .tag-wrap { display: flex; flex-wrap: wrap; gap: 4px; }
        .tag { font-size: 0.7rem; background: #eee; padding: 2px 6px; border-radius: 4px; color: #666; }

        /* 모달 */
        #modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 100; justify-content: center; align-items: center; }
        #modal img { max-width: 90%; max-height: 90%; box-shadow: 0 0 20px rgba(0,0,0,0.5); }
    </style>
</head>
<body>

    <div class="header">
        <h1>🏛️ 피규어 박물관</h1>
        <span id="total-count" class="stats-badge">로딩 중...</span>
    </div>

    <div class="bookmark-area" id="filter-section">
        </div>

    <div class="grid" id="museum-grid"></div>

    <div id="modal" onclick="this.style.display='none'"><img id="modal-img"></div>

    <script>
        const SHEET_URL = '여기에_JSON_배포주소_넣으세요';

        async function init() {
            const res = await fetch(SHEET_URL);
            const items = await res.json();
            
            document.getElementById('total-count').innerText = `현재 ${items.length}점의 작품 전시 중`;

            // 1. 카테고리(K열)와 시리즈(B열) 구조 파악
            const menuMap = {};
            items.forEach(item => {
                const k = item.category || "기타";
                const b = item.series || "기타";
                if (!menuMap[k]) menuMap[k] = new Set();
                menuMap[k].add(b);
            });

            // 2. 책갈피 메뉴 생성
            const filterSection = document.getElementById('filter-section');
            filterSection.innerHTML = `<div class="category-row"><button class="btn-tag active" onclick="filterBy('all')">전체보기</button></div>`;

            for (const [cat, seriesSet] of Object.entries(menuMap)) {
                const row = document.createElement('div');
                row.className = 'category-row';
                let btns = `<span class="main-label">${getIcon(cat)} ${cat.toUpperCase()}</span><div class="sub-buttons">`;
                seriesSet.forEach(s => {
                    btns += `<button class="btn-tag" onclick="filterBy('${s}')">${s}</button>`;
                });
                btns += `</div>`;
                row.innerHTML = btns;
                filterSection.appendChild(row);
            }

            render(items);
        }

        function getIcon(k) {
            if (k.toLowerCase().includes('game')) return '🎮';
            if (k.toLowerCase().includes('vocal')) return '🎤';
            return '📦';
        }

        function render(items) {
            const grid = document.getElementById('museum-grid');
            grid.innerHTML = items.map(item => {
                // M열(display_name) 우선, 없으면 D열(character)
                const finalName = (item.display_name && item.display_name.trim()) ? item.display_name : item.character;
                const firstImg = item.image.split(',')[0];
                const imgUrl = `https://raw.githubusercontent.com/아이디/저장소/main/images/${firstImg}.jpg`;

                return `
                    <div class="card" data-series="${item.series}">
                        <img src="${imgUrl}" onclick="viewImg('${imgUrl}')" onerror="this.src='https://via.placeholder.com/220x280'">
                        <div class="info">
                            <div class="name">${finalName}</div>
                            <div class="tag-wrap">
                                <span class="tag">#${item.maker}</span>
                                <span class="tag">#${item.series}</span>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function viewImg(url) {
            document.getElementById('modal').style.display = 'flex';
            document.getElementById('modal-img').src = url;
        }

        function filterBy(series) {
            document.querySelectorAll('.btn-tag').forEach(b => b.classList.remove('active'));
            // 클릭한 버튼 활성화 로직은 생략(간결화)
            document.querySelectorAll('.card').forEach(c => {
                c.style.display = (series === 'all' || c.dataset.series === series) ? 'block' : 'none';
            });
        }

        init();
    </script>
</body>
</html>
