<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figure Museum</title>
  <style>
    body { font-family: 'Pretendard', sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }
    header { background: #1a1a1a; color: white; padding: 40px 20px; text-align: center; }
    .container { max-width: 1200px; margin: 20px auto; padding: 0 20px 60px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
    
    .card { background: #fff; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.05); cursor: pointer; border: 1px solid #e9ecef; transition: transform 0.2s; }
    .card:hover { transform: translateY(-5px); }
    
    .img-box { width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; padding: 15px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 20px; border-top: 1px solid #f1f3f5; }
    .manufac { color: #adb5bd; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
    .char-name { font-size: 1.15rem; font-weight: 800; margin: 5px 0; color: #212529; }
    .series { font-size: 0.85rem; color: #495057; }

    /* 메모장 영역 */
    .memo-section {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease-out;
      background: #fff9db;
    }
    .card.active .memo-section {
      max-height: 600px;
    }
    .memo-content { 
      padding: 20px; 
      font-size: 0.9rem; 
      color: #5c940d; 
      line-height: 1.7; 
      white-space: pre-wrap; 
      border-top: 1px dashed #fab005;
    }
    .memo-title { font-weight: bold; color: #f08c00; display: block; margin-bottom: 8px; border-bottom: 1px solid #ffe066; padding-bottom: 5px; }

    #status { text-align: center; padding: 50px; font-weight: bold; color: #999; }
  </style>
</head>
<body>

  <header>
    <h1>FIGURE MUSEUM</h1>
    <p>수집가의 도감을 확인해 보세요.</p>
  </header>

  <div class="container">
    <div id="status">데이터 로딩 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    // 💡 보내주신 최신 CSV 주소로 교체했습니다.
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadDatabase() {
      const grid = document.getElementById("figureGrid");
      const status = document.getElementById("status");

      try {
        const response = await fetch(csvURL);
        if (!response.ok) throw new Error("네트워크 응답에 문제가 있습니다.");
        
        const csvText = await response.text();
        const rows = csvText.split(/\r?\n/).map(row => {
          // 쉼표가 포함된 데이터를 안전하게 나누는 정규식
          const regex = /(?!\s*$)\s*(?:'([^']*)'|"([^"]*)"|([^,]*))\s*(?:,|$)/g;
          const parts = [];
          let m;
          while (m = regex.exec(row)) {
            parts.push(m[1] || m[2] || m[3] || "");
          }
          return parts;
        });

        status.style.display = "none";
        grid.innerHTML = "";

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          // I열(8번) 파일명이 없으면 건너뜀
          const fileName = cols[8]?.trim();
          if (!fileName) continue;

          const manufacturer = cols[1]?.trim() || "N/A";
          const series = cols[2]?.trim() || "N/A";
          const character = cols[3]?.trim() || "Unknown";
          const desc = cols[9]?.trim() || "상세 메모가 아직 없습니다. 🖋️";

          const card = document.createElement("div");
          card.className = "card";
          card.onclick = function() { this.classList.toggle('active'); };
          
          card.innerHTML = `
            <div class="img-box">
              <img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" 
                   loading="lazy" 
                   onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'">
            </div>
            <div class="content">
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${character}</div>
              <div class="series">${series}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content">
                <span class="memo-title">Collector's Note</span>
                ${desc}
              </div>
            </div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        status.innerHTML = `<div style="color:red">에러 발생: ${err.message}<br>시트 주소를 다시 확인해 주세요.</div>`;
      }
    }

    loadDatabase();
  </script>
</body>
</html>s
