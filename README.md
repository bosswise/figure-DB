<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 데이터베이스</title>
  <style>
    body { font-family: sans-serif; background: #f4f7f6; margin: 0; padding: 20px; }
    h1 { text-align: center; }
    .grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); 
      gap: 20px; 
      max-width: 1200px; 
      margin: 20px auto; 
    }
    .card { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
    .card img { width: 100%; height: 200px; object-fit: contain; background: #eee; }
    .error-msg { color: red; text-align: center; padding: 20px; border: 1px solid red; background: #fff1f1; }
  </style>
</head>
<body>

  <h1>나의 피규어 DB</h1>
  <div id="status">데이터를 불러오는 중...</div>
  <div id="figureGrid" class="grid"></div>

  <script>
    // 1. 실제 본인의 CSV 주소인지 다시 확인 (현재 주소는 이전 대화 기반)
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadData() {
      const status = document.getElementById("status");
      const grid = document.getElementById("figureGrid");

      try {
        const response = await fetch(csvURL);
        if (!response.ok) throw new Error("구글 시트를 불러올 수 없습니다. URL을 확인하세요.");
        
        const data = await response.text();
        // 줄 바꿈 문자를 처리하여 행으로 분리
        const rows = data.split(/\r?\n/).map(row => row.split(','));
        
        if (rows.length <= 1) {
          status.innerHTML = "<div class='error-msg'>시트에 데이터가 없거나 형식이 잘못되었습니다.</div>";
          return;
        }

        status.style.display = "none"; // 성공하면 로딩 문구 삭제
        grid.innerHTML = ""; 

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          if (cols.length < 3) continue; 

          // 열 번호 다시 체크: A=0, B=1, C=2, D=3
          const manufacturer = cols[0]?.replace(/"/g, "").trim(); 
          const series       = cols[1]?.replace(/"/g, "").trim();
          const character    = cols[2]?.replace(/"/g, "").trim();
          const fileName     = cols[3]?.replace(/"/g, "").trim(); 

          if (!fileName) continue;

          // 이미지 주소 생성
          const imgSrc = `${imageBaseURL}${fileName}.jpg`;

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <img src="${imgSrc}" alt="${character}" onerror="this.src='https://placehold.co/200x200?text=No+Image'">
            <div style="font-weight:bold; margin-top:10px;">${character}</div>
            <div style="font-size:0.8em; color:gray;">${manufacturer} / ${series}</div>
          `;
          grid.appendChild(card);
        }
      } catch (error) {
        status.innerHTML = `<div class='error-msg'>오류 발생: ${error.message}</div>`;
        console.error(error);
      }
    }

    loadData();
  </script>
</body>
</html>
