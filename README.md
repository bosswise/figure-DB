<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <title>My Figure Database</title>
  <style>
    body { font-family: 'Apple SD Gothic Neo', sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #333; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 20px; margin-top: 20px; }
    .card { background: white; padding: 15px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; transition: transform 0.2s; }
    .card:hover { transform: translateY(-5px); }
    .card img { width: 100%; height: 200px; object-fit: contain; border-radius: 8px; background: #eee; }
    .name { margin-top: 12px; font-weight: bold; font-size: 1.1em; }
    .series { font-size: 0.9em; color: #555; margin: 4px 0; }
    .manufacturer { font-size: 0.85em; color: #888; }
  </style>
</head>
<body>

  <h1>피규어 데이터베이스</h1>
  <div id="figureGrid" class="grid">
    <p style="text-align: center; grid-column: 1/-1;">데이터를 불러오는 중입니다...</p>
  </div>

  <script>
    // ⚠️ 중요: 구글 시트에서 [파일] -> [공유] -> [웹에 게시] -> [쉼표로 구분된 값(.csv)] 선택 후 나온 URL을 여기에 넣으세요.
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-A3Uq98Wz65pCHoXjL7p89kO0zVvYnCshfF6I7_9MvNq13pI8wL8L8yU_K_tQyN6Z6V3bM_S8V_Vw/pub?output=csv";

    async function fetchSheetData() {
      try {
        const response = await fetch(csvURL);
        const data = await response.text();
        
        // CSV 데이터 파싱 (쉼표로 구분)
        const rows = data.split('\n').map(row => row.split(','));
        const grid = document.getElementById("figureGrid");
        grid.innerHTML = ""; // 로딩 문구 제거

        // index 0은 헤더이므로 i = 1부터 시작
        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          if (cols.length < 4) continue;

          // 시트 순서: 제조사(0), 시리즈(1), 캐릭터(2), 파일명(3)
          const manufacturer = cols[0].trim();
          const series = cols[1].trim();
          const character = cols[2].trim();
          const imageFile = cols[3].trim(); 

          // 이미지가 없을 때를 대비한 처리
          // 윈도우 파일 확장자 문제를 피하기 위해 여기서 .jpg를 붙임
          const imgSrc = `images/${imageFile}.jpg`;

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <img src="${imgSrc}" alt="${character}" onerror="this.src='https://via.placeholder.com/200x200?text=No+Image'">
            <div class="name">${character}</div>
            <div class="series">${series}</div>
            <div class="manufacturer">${manufacturer}</div>
          `;
          grid.appendChild(card);
        }
      } catch (error) {
        console.error("데이터 로드 실패:", error);
        document.getElementById("figureGrid").innerHTML = "데이터를 불러오는 데 실패했습니다. CSV URL을 확인해주세요.";
      }
    }

    fetchSheetData();
  </script>
</body>
</html>
