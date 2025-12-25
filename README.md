<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 데이터베이스</title>
  <style>
    body { font-family: 'Apple SD Gothic Neo', sans-serif; background: #f4f7f6; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #2c3e50; margin-bottom: 30px; }
    .grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); 
      gap: 20px; max-width: 1200px; margin: 0 auto; 
    }
    .card { 
      background: white; padding: 15px; border-radius: 12px; 
      box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; 
    }
    .card img { 
      width: 100%; height: 220px; object-fit: contain; 
      background: #fafafa; border-radius: 8px; margin-bottom: 12px;
    }
    .name { font-weight: bold; font-size: 1.1em; color: #333; margin-bottom: 5px; }
    .info { font-size: 0.85em; color: #7f8c8d; line-height: 1.4; }
  </style>
</head>
<body>

  <h1>나의 피규어 컬렉션</h1>
  <div id="status" style="text-align: center; color: #666;">데이터를 불러오는 중...</div>
  <div id="figureGrid" class="grid"></div>

  <script>
    // 1. 구글 시트 CSV 주소 (게시된 주소 확인)
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";
    
    // 2. 이미지 폴더 주소
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadDatabase() {
      const status = document.getElementById("status");
      const grid = document.getElementById("figureGrid");

      try {
        const response = await fetch(csvURL);
        const data = await response.text();
        
        // 줄바꿈으로 행 나누기
        const rows = data.split(/\r?\n/).map(row => row.split(','));
        
        status.style.display = "none";
        grid.innerHTML = ""; 

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          
          // 데이터가 I열(index 8)까지 없는 행은 무시
          if (cols.length < 9) continue; 

          // 열 정보 매칭
          const manufacturer = cols[1]?.replace(/"/g, "").trim(); // B열
          const series       = cols[2]?.replace(/"/g, "").trim(); // C열
          const character    = cols[3]?.replace(/"/g, "").trim(); // D열 (캐릭터명)
          const fileName     = cols[8]?.replace(/"/g, "").trim(); // I열 (이미지파일명)

          if (!fileName) continue;

          // 한글 파일명을 웹 주소 형식으로 변환
          const imgSrc = `${imageBaseURL}${encodeURIComponent(fileName)}.jpg`;

          // 주소가 잘 만들어졌는지 콘솔에 출력 (F12에서 확인)
          console.log(`[${i}] 캐릭터: ${character} | 경로: ${imgSrc}`);

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <img src="${imgSrc}" alt="${character}" onerror="this.src='https://placehold.co/200x220?text=No+Image'">
            <div class="name">${character}</div>
            <div class="info">${manufacturer}<br>${series}</div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        console.error("데이터 로드 실패:", err);
        status.innerHTML = "데이터를 불러오지 못했습니다. CSV 주소를 확인해주세요.";
      }
    }

    loadDatabase();
  </script>
</body>
</html>
