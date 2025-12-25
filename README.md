<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 데이터베이스</title>
  <style>
    body { font-family: 'Apple SD Gothic Neo', sans-serif; background: #f4f7f6; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #2c3e50; }
    .grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); 
      gap: 20px; 
      max-width: 1200px; 
      margin: 20px auto; 
    }
    .card { 
      background: white; 
      padding: 15px; 
      border-radius: 10px; 
      box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
      text-align: center;
    }
    .card img { 
      width: 100%; 
      height: 220px; 
      object-fit: contain; 
      background: #fafafa;
      border-radius: 5px;
    }
    .info-name { font-weight: bold; margin: 10px 0 5px; color: #333; }
    .info-sub { font-size: 0.85em; color: #7f8c8d; }
  </style>
</head>
<body>

  <h1>나의 피규어 DB</h1>
  <div id="figureGrid" class="grid">
    <p style="text-align: center; grid-column: 1/-1;">데이터 로딩 중...</p>
  </div>

  <script>
    // 1. 본인의 구글 시트 CSV 주소로 교체하세요
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";
    
    // 2. 본인의 GitHub Pages 이미지 폴더 주소
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadData() {
      try {
        const response = await fetch(csvURL);
        const data = await response.text();
        const rows = data.split('\n').map(row => row.split(','));
        const grid = document.getElementById("figureGrid");
        grid.innerHTML = ""; 

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          if (cols.length < 3) continue; 

          // 열 순서 설정 (0부터 시작: A=0, B=1, C=2, D=3, E=4)
          const manufacturer = cols[0]?.trim(); // A열: 제조사
          const series       = cols[1]?.trim(); // B열: 시리즈
          const character    = cols[2]?.trim(); // C열: 캐릭터 이름 (표시용)
          const fileName     = cols[3]?.trim(); // D열: 파일명 수식 결과 (hobby-sakura_...)

          if (!fileName) continue;

          // 최종 이미지 경로 생성 (.jpg를 여기서 붙여줍니다)
          const imgSrc = `${imageBaseURL}${fileName}.jpg`;

          // 콘솔에서 실제 생성된 주소가 맞는지 확인 가능
          console.log(`[확인] 캐릭터: ${character} | 경로: ${imgSrc}`);

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <img src="${imgSrc}" alt="${character}" onerror="this.src='https://placehold.co/200x220?text=No+Image'">
            <div class="info-name">${character}</div>
            <div class="info-sub">${manufacturer} / ${series}</div>
          `;
          grid.appendChild(card);
        }
      } catch (error) {
        console.error("데이터 로드 실패:", error);
      }
    }

    loadData();
  </script>
</body>
</html>
