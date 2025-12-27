<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figure Archive - Premium Edition</title>
  <style>
    /* 1. 기본 스타일 & 배경 */
    body { 
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
      background-color: #f8f9fa; 
      color: #334155;
      margin: 0; 
      padding: 0;
      line-height: 1.6;
    }

    /* 2. 헤더 디자인 */
    header {
      background: #ffffff;
      padding: 40px 20px;
      text-align: center;
      border-bottom: 1px solid #e2e8f0;
      margin-bottom: 40px;
    }
    header h1 { 
      margin: 0; 
      font-size: 2.5rem; 
      letter-spacing: -1px; 
      color: #0f172a;
      font-weight: 800;
    }
    header p { color: #64748b; margin-top: 10px; font-size: 1.1rem; }

    /* 3. 그리드 레이아웃 */
    .container { max-width: 1300px; margin: 0 auto; padding: 0 20px 60px; }
    .grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
      gap: 30px; 
    }

    /* 4. 카드 디자인 (도감 느낌) */
    .card { 
      background: #ffffff; 
      border-radius: 20px; 
      overflow: hidden; 
      box-shadow: 0 4px 20px rgba(0,0,0,0.05);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      border: 1px solid #f1f5f9;
      display: flex;
      flex-direction: column;
    }
    .card:hover { 
      transform: translateY(-10px); 
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); 
    }

    /* 이미지 영역 */
    .img-box { 
      width: 100%; 
      height: 320px; 
      background: #ffffff;
      padding: 20px;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      justify-content: center;
      border-bottom: 1px solid #f1f5f9;
    }
    .img-box img { 
      max-width: 100%; 
      max-height: 100%; 
      object-fit: contain;
      filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));
    }

    /* 정보 영역 */
    .content { padding: 25px; text-align: left; flex-grow: 1; }
    .manufac-tag { 
      display: inline-block; 
      background: #f1f5f9; 
      color: #475569; 
      font-size: 0.75rem; 
      padding: 4px 10px; 
      border-radius: 6px; 
      font-weight: 600;
      text-transform: uppercase;
      margin-bottom: 10px;
    }
    .char-name { 
      font-size: 1.25rem; 
      font-weight: 700; 
      color: #1e293b; 
      margin-bottom: 4px; 
      display: block;
    }
    .series-name { font-size: 0.9rem; color: #64748b; margin-bottom: 15px; }
    
    /* 상세 설명 (J열 전용) */
    .description { 
      font-size: 0.85rem; 
      color: #475569; 
      background: #f8fafc;
      padding: 12px;
      border-radius: 8px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-top: 10px;
    }

    #status { text-align: center; padding: 50px; font-size: 1.2rem; color: #94a3b8; }
  </style>
</head>
<body>

  <header>
    <h1>FIGURE ARCHIVE</h1>
    <p>Personal Collector's Encyclopedia</p>
  </header>

  <div class="container">
    <div id="status">박물관 데이터를 불러오는 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    function parseCSV(text) {
      const regex = /(?!\s*$)\s*(?:'([^']*)'|"([^"]*)"|([^,]*))\s*(?:,|$)/g;
      const rows = [];
      let row = [];
      text.replace(/\r?\n/g, '\n').split('\n').forEach(line => {
        row = [];
        line.replace(regex, (m0, m1, m2, m3) => {
          row.push(m1 !== undefined ? m1 : (m2 !== undefined ? m2 : m3));
          return '';
        });
        if (row.length > 0) rows.push(row);
      });
      return rows;
    }

    async function loadDatabase() {
      const status = document.getElementById("status");
      const grid = document.getElementById("figureGrid");

      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        const rows = parseCSV(csvText);
        
        status.style.display = "none";
        grid.innerHTML = ""; 

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          if (cols.length < 9) continue; 

          // 열 설정: A(0)=ID, B(1)=제조사, C(2)=시리즈, D(3)=캐릭터명, I(8)=파일명, J(9)=설명
          const manufacturer = cols[1]?.trim() || "Brand";
          const series       = cols[2]?.trim() || "Series";
          const character    = cols[3]?.trim() || "Figure";
          const fileName     = cols[8]?.trim();
          const desc         = cols[9]?.trim() || "상세 정보가 아직 업데이트되지 않았습니다.";

          if (!fileName) continue;

          const imgSrc = `${imageBaseURL}${encodeURIComponent(fileName)}.jpg`;

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <div class="img-box">
              <img src="${imgSrc}" loading="lazy" onerror="this.src='https://placehold.co/400x500/f8fafc/94a3b8?text=No+Image'">
            </div>
            <div class="content">
              <span class="manufac-tag">${manufacturer}</span>
              <span class="char-name">${character}</span>
              <div class="series-name">${series}</div>
              <div class="description">${desc}</div>
            </div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        status.innerHTML = "데이터를 불러오지 못했습니다. 다시 시도해주세요.";
      }
    }

    loadDatabase();
  </script>
</body>
</html>
