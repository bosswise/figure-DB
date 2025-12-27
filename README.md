<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figure Archive - Interactive Memo</title>
  <style>
    /* 폰트 및 기본 설정 */
    body { 
      font-family: 'Pretendard', sans-serif; 
      background-color: #f1f3f5; 
      color: #333; 
      margin: 0; padding: 0; 
    }

    header {
      background: #1a1a1a;
      color: white;
      padding: 50px 20px;
      text-align: center;
      margin-bottom: 40px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    .container { max-width: 1200px; margin: 0 auto; padding: 0 20px 60px; }
    .grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
      gap: 30px; 
    }

    /* 카드 베이스 */
    .card { 
      background: #fff; 
      border-radius: 15px; 
      overflow: hidden; 
      box-shadow: 0 5px 15px rgba(0,0,0,0.05);
      cursor: pointer;
      transition: all 0.3s ease;
      position: relative;
      border: 1px solid #e9ecef;
    }

    .card:hover { transform: translateY(-5px); }

    /* 이미지 영역 */
    .img-box { 
      width: 100%; height: 300px; 
      background: #fff;
      display: flex; align-items: center; justify-content: center;
      padding: 15px; box-sizing: border-box;
    }
    .img-box img { 
      max-width: 100%; max-height: 100%; 
      object-fit: contain;
      transition: transform 0.3s ease;
    }
    .card:hover .img-box img { transform: scale(1.05); }

    /* 카드 텍스트 정보 */
    .content { padding: 20px; background: white; z-index: 2; position: relative; }
    .manufac { color: #868e96; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
    .char-name { font-size: 1.15rem; font-weight: 800; margin: 5px 0; color: #212529; }
    .series { font-size: 0.85rem; color: #495057; }

    /* 💡 메모장 영역 (기본적으로 숨겨짐) */
    .memo-section {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      background: #fff9db; /* 메모지 노란빛 */
      border-top: 1px dashed #fab005;
    }

    /* 클릭 시 활성화될 클래스 */
    .card.active .memo-section {
      max-height: 300px; /* 적당한 높이까지 열림 */
    }

    .memo-content {
      padding: 20px;
      font-size: 0.9rem;
      color: #5c940d;
      background-image: radial-gradient(#e9ecef 1px, transparent 1px);
      background-size: 20px 20px; /* 모눈종이 느낌 */
      line-height: 1.7;
      white-space: pre-wrap; /* 줄바꿈 유지 */
    }

    .memo-title {
      font-weight: bold;
      color: #f08c00;
      margin-bottom: 8px;
      display: block;
      border-bottom: 1px solid #ffe066;
      padding-bottom: 5px;
    }

    #status { text-align: center; padding: 40px; font-weight: bold; }
  </style>
</head>
<body>

  <header>
    <h1>FIGURE MUSEUM</h1>
    <p>사진을 클릭하면 수집가의 노트를 확인할 수 있습니다.</p>
  </header>

  <div class="container">
    <div id="status">박물관 입장 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadDatabase() {
      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        const rows = csvText.split(/\r?\n/).map(row => {
          const regex = /(?!\s*$)\s*(?:'([^']*)'|"([^"]*)"|([^,]*))\s*(?:,|$)/g;
          const res = [];
          let m;
          while (m = regex.exec(row)) {
            res.push(m[1] || m[2] || m[3] || "");
          }
          return res;
        });

        const grid = document.getElementById("figureGrid");
        document.getElementById("status").style.display = "none";

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          if (cols.length < 9) continue;

          const manufacturer = cols[1]?.trim() || "";
          const series = cols[2]?.trim() || "";
          const character = cols[3]?.trim() || "Figure";
          const fileName = cols[8]?.trim();
          const description = cols[9]?.trim() || "기록된 상세 정보가 없습니다.";

          if (!fileName) continue;

          const imgSrc = `${imageBaseURL}${encodeURIComponent(fileName)}.jpg`;

          const card = document.createElement("div");
          card.className = "card";
          // 클릭 이벤트 추가
          card.onclick = function() { this.classList.toggle('active'); };

          card.innerHTML = `
            <div class="img-box">
              <img src="${imgSrc}" loading="lazy" onerror="this.src='https://placehold.co/400x400/fff/999?text=No+Photo'">
            </div>
            <div class="content">
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${character}</div>
              <div class="series">${series}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content">
                <span class="memo-title">Collector's Note</span>
                ${description}
              </div>
            </div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        document.getElementById("status").innerText = "데이터 로드 실패";
      }
    }
    loadDatabase();
  </script>
</body>
</html>
