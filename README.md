<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>피규어 데이터베이스</title>
  <style>
    body { font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; background: #f0f2f5; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #1a1a1a; margin-bottom: 30px; }
    
    .grid { 
      display: grid; 
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); 
      gap: 20px; 
      max-width: 1200px; 
      margin: 0 auto; 
    }

    .card { 
      background: white; 
      padding: 15px; 
      border-radius: 12px; 
      box-shadow: 0 4px 12px rgba(0,0,0,0.08); 
      text-align: center; 
      transition: transform 0.2s ease;
    }
    .card:hover { transform: translateY(-5px); }
    
    .card img { 
      width: 100%; 
      height: 220px; 
      object-fit: contain; 
      border-radius: 8px; 
      background: #f9f9f9;
      margin-bottom: 12px;
    }

    .character { font-weight: bold; font-size: 1.1em; color: #333; margin: 5px 0; }
    .info-sub { font-size: 0.85em; color: #666; line-height: 1.4; }
  </style>
</head>
<body>

  <h1>나의 피규어 컬렉션</h1>
  <div id="status" style="text-align: center; color: #666;">데이터 로딩 중...</div>
  <div id="figureGrid" class="grid"></div>

  <script>
    // 1. 구글 시트 CSV 주소 (게시된 주소)
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";
    
    // 2. 깃허브 페이지 이미지 폴더 기본 주소
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadDatabase() {
      const status = document.getElementById("status");
      const grid = document.getElementById("figureGrid");

      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        
        // CSV 파싱 (줄바꿈과 쉼표 처리)
        const rows = csvText.split(/\r?\n/).map(row => row.split(','));
        
        status.style.display = "none";
        grid.innerHTML = ""; 

        // i=1 (두 번째 줄)부터 시작
        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          if (cols.length < 4) continue; 

          // 시트 열 순서: A(0)=제조사, B(1)=시리즈, C(2)=캐릭터명, D(3)=파일명
          const manufacturer = cols[0]?.replace(/"/g, "").trim();
          const series       = cols[1]?.replace(/"/g, "").trim();
          const character    = cols[2]?.replace(/"/g, "").trim();
          const fileName     = cols[3]?.replace(/"/g, "").trim();

          if (!fileName) continue;

          // 💡 핵심: 한글 파일명을 웹 주소용으로 변환 (인코딩)
          const encodedFileName = encodeURIComponent(fileName);
          const imgSrc = `${imageBaseURL}${encodedFileName}.jpg`;

          // [디버깅용] 주소가 잘 만들어졌는지 콘솔에 출력
          console.log(`[${i}] ${character} 이미지 주소: ${imgSrc}`);

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <img src="${imgSrc}" 
                 alt="${character}" 
                 onerror="this.onerror=null; this.src='https://placehold.co/200x220?text=No+Image'">
            <div class="character">${character}</div>
            <div class="info-sub">${manufacturer}<br>${series}</div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        console.error("데이터 로드 실패:", err);
        status.innerHTML = "데이터를 불러오는 중 오류가 발생했습니다.";
      }
    }

    loadDatabase();
  </script>
</body>
</html>
