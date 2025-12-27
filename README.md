<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figure Museum</title>
  <style>
    body { font-family: sans-serif; background-color: #f1f3f5; margin: 0; padding: 0; }
    header { background: #1a1a1a; color: white; padding: 30px; text-align: center; }
    .container { max-width: 1200px; margin: 20px auto; padding: 0 20px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
    .card { background: #fff; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.05); cursor: pointer; border: 1px solid #e9ecef; }
    .img-box { width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; padding: 10px; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .content { padding: 15px; border-top: 1px solid #eee; }
    .manufac { color: #888; font-size: 0.7rem; font-weight: bold; }
    .char-name { font-size: 1.1rem; font-weight: bold; margin: 5px 0; }
    .memo-section { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; background: #fff9db; }
    .card.active .memo-section { max-height: 500px; }
    .memo-content { padding: 15px; font-size: 0.9rem; color: #444; border-top: 1px dashed #ffd43b; }
  </style>
</head>
<body>
  <header><h1>FIGURE MUSEUM</h1></header>
  <div class="container">
    <div id="figureGrid" class="grid">데이터를 불러오고 있습니다...</div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadDatabase() {
      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        
        // 💡 가장 단순하고 강력한 줄바꿈 분리
        const rows = csvText.split("\n").map(row => row.split(","));
        const grid = document.getElementById("figureGrid");
        grid.innerHTML = "";

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          // 💡 파일명이 들어있는 I열(8번)이 비어있으면 건너뜁니다.
          const fileName = cols[8]?.trim();
          if (!fileName) continue;

          const manufacturer = cols[1]?.trim() || "Brand";
          const series = cols[2]?.trim() || "Series";
          const character = cols[3]?.trim() || "Character";
          // J열(9번) 설명글 (없으면 기본 문구)
          const desc = cols[9]?.trim() || "수집가의 메모가 아직 없습니다.";

          const card = document.createElement("div");
          card.className = "card";
          card.onclick = function() { this.classList.toggle('active'); };
          
          card.innerHTML = `
            <div class="img-box"><img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg"></div>
            <div class="content">
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${character}</div>
              <div style="font-size:0.8rem; color:#666;">${series}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content"><strong>[Collector's Note]</strong><br>${desc}</div>
            </div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        document.getElementById("figureGrid").innerHTML = "에러 발생: " + err;
      }
    }
    loadDatabase();
  </script>
</body>
</html>
