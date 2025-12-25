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
        
        // CSV 파싱
        const rows = csvText.split(/\r?\n/).map(row => row.split(','));
        
        status.style.display = "none";
        grid.innerHTML = ""; 

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          
          // 데이터가 적어도 I열(index 8)까지는 있어야 하므로 체크 강화
          if (cols.length < 9) continue; 

          // 열 순서: A(0)=제조사, B(1)=시리즈, C(2)=캐릭터명, ..., I(8)=파일명수식결과
          const manufacturer = cols[0]?.replace(/"/g, "").trim();
          const series       = cols[1]?.replace(/"/g, "").trim();
          const character    = cols[2]?.replace(/"/g, "").trim();
          
          // 💡 파일명 수식이 있는 I열(8번 인덱스)을 가져옵니다.
          const fileName     = cols[8]?.replace(/"/g, "").trim();

          if (!fileName) continue;

          // 한글 파일명 인코딩 및 주소 생성
          const encodedFileName = encodeURIComponent(fileName);
          const imgSrc = `${imageBaseURL}${encodedFileName}.jpg`;

          // [디버깅] F12 콘솔에서 주소를 확인해보세요.
          console.log(`[${i}] 캐릭터: ${character} | 파일명(I열): ${fileName} | 주소: ${imgSrc}`);

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
        status.innerHTML = "데이터 로딩 중 오류가 발생했습니다. (F12 콘솔 확인)";
      }
    }

    loadDatabase();
  </script>
</body>
</html>
