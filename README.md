<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figure Museum - Interactive</title>
  <style>
    body { font-family: 'Pretendard', sans-serif; background-color: #f1f3f5; margin: 0; padding: 0; }
    header { background: #1a1a1a; color: white; padding: 40px 20px; text-align: center; margin-bottom: 30px; }
    .container { max-width: 1200px; margin: 0 auto; padding: 0 20px 60px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }

    /* 카드 스타일 */
    .card { background: #fff; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.05); cursor: pointer; transition: all 0.3s ease; border: 1px solid #e9ecef; }
    .card:hover { transform: translateY(-5px); }

    /* 이미지 영역 */
    .img-box { width: 100%; height: 300px; background: #fff; display: flex; align-items: center; justify-content: center; padding: 15px; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }

    /* 카드 기본 정보 */
    .content { padding: 20px; background: white; }
    .manufac { color: #868e96; font-size: 0.75rem; font-weight: bold; }
    .char-name { font-size: 1.1rem; font-weight: 800; margin: 5px 0; }
    .series { font-size: 0.85rem; color: #495057; }

    /* 💡 메모장 영역 */
    .memo-section {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease-out;
      background: #fff9db;
      border-top: 1px dashed #fab005;
    }
    .card.active .memo-section {
      max-height: 500px; /* 텍스트가 길어도 충분히 열리게 조절 */
    }
    .memo-content { padding: 20px; font-size: 0.9rem; color: #5c940d; line-height: 1.7; white-space: pre-wrap; }
    .memo-title { font-weight: bold; color: #f08c00; display: block; margin-bottom: 8px; border-bottom: 1px solid #ffe066; padding-bottom: 5px; }

    #status { text-align: center; padding: 50px; font-weight: bold; color: #999; }
  </style>
</head>
<body>

  <header>
    <h1>FIGURE MUSEUM</h1>
    <p>사진을 클릭하면 상세 메모를 확인할 수 있습니다.</p>
  </header>

  <div class="container">
    <div id="status">박물관 데이터를 불러오는 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    // CSV 파싱 함수 (쉼표 포함 데이터 완벽 처리)
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
          
          // 데이터가 너무 적은 행만 건너뜁니다 (안전장치 완화)
          if (cols.length < 4) continue;

          const manufacturer = cols[1]?.trim() || "Brand";
          const series       = cols[2]?.trim() || "Series";
          const character    = cols[3]?.trim() || "Figure Name";
          const fileName     = cols[8]?.trim(); // I열
          const description  = cols[9]?.trim() || "상세 정보가 아직 입력되지 않았습니다. 🖋️"; // J열

          if (!fileName) continue;

          const imgSrc = `${imageBaseURL}${encodeURIComponent(fileName)}.jpg`;

          const card = document.createElement("div");
          card.className = "card";
          
          // 클릭 시 열고 닫기 이벤트
          card.onclick = function() {
            this.classList.toggle('active');
          };

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
        console.error(err);
        status.innerText = "데이터 로드 실패. 시트 주소를 확인하세요.";
      }
    }

    loadDatabase();
  </script>
</body>
</html>
