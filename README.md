<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>개인 피규어 데이터베이스</title>
  <style>
    body { font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; background: #f0f2f5; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #1a1a1a; margin-bottom: 30px; }
    
    /* 그리드 설정: 화면 크기에 따라 자동으로 칸 조절 */
    .grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); 
      gap: 20px; 
      max-width: 1200px; 
      margin: 0 auto; 
    }

    /* 카드 스타일 */
    .card { 
      background: white; 
      padding: 15px; 
      border-radius: 12px; 
      box-shadow: 0 4px 12px rgba(0,0,0,0.08); 
      text-align: center; 
      transition: transform 0.2s ease;
    }
    .card:hover { transform: translateY(-5px); }
    
    /* 이미지 설정 */
    .card img { 
      width: 100%; 
      height: 200px; 
      object-fit: contain; /* 이미지 비율 유지 */
      border-radius: 8px; 
      background: #f9f9f9;
      margin-bottom: 10px;
    }

    .character { font-weight: bold; font-size: 1.1em; color: #333; margin: 5px 0; }
    .series { font-size: 0.9em; color: #666; }
    .manufacturer { font-size: 0.8em; color: #999; margin-top: 5px; }
  </style>
</head>
<body>

  <h1>나의 피규어 컬렉션</h1>
  <div id="figureGrid" class="grid">
    <p style="text-align: center; grid-column: 1/-1;">데이터를 불러오는 중...</p>
  </div>

  <script>
    // ⚠️ [주의] 아래 URL을 본인의 '웹에 게시(CSV)' 주소로 교체하세요!
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";

    async function loadDatabase() {
      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        
        // CSV 줄 단위로 나누기
        const rows = csvText.split('\n').map(row => row.split(','));
        const grid = document.getElementById("figureGrid");
        grid.innerHTML = ""; // 로딩 메시지 삭제

        // 두 번째 줄(index 1)부터 반복
        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          if (cols.length < 4) continue; // 데이터가 부족한 행은 건너뜀

          // 열 순서: A(0)=제조사, B(1)=시리즈, C(2)=캐릭터이름, D(3)=이미지파일명
          const manufacturer = cols[0].trim();
          const series = cols[1].trim();
          const character = cols[2].trim();
          const fileName = cols[3].trim(); 

          // 이미지 경로 생성 (확장자 .jpg 강제 추가)
          const imgSrc = `images/${fileName}.jpg`;

          // [디버깅] 이미지가 안 보인다면 F12 콘솔창에서 이 로그를 확인하세요.
          console.log(`피규어: ${character} | 경로: ${imgSrc}`);

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <img src="${imgSrc}" 
                 alt="${character}" 
                 onerror="this.src='https://placehold.co/200x200?text=No+Image'">
            <div class="character">${character}</div>
            <div class="series">${series}</div>
            <div class="manufacturer">${manufacturer}</div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        console.error("데이터 로드 에러:", err);
        document.getElementById("figureGrid").innerHTML = "데이터를 불러오지 못했습니다. 콘솔을 확인하세요.";
      }
    }

    loadDatabase();
  </script>
</body>
</html>
