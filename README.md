<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figure Museum - Search Edition</title>
  <style>
    body { font-family: 'Pretendard', sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }
    
    /* 1. 고정 헤더 & 검색바 영역 */
    header { 
      background: #1a1a1a; color: white; padding: 30px 20px; text-align: center;
      position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    header h1 { margin: 0 0 15px 0; font-size: 1.8rem; }
    
    .search-container {
      max-width: 600px; margin: 0 auto; display: flex; gap: 10px;
    }
    #searchInput {
      flex: 1; padding: 12px 20px; border-radius: 25px; border: none; outline: none;
      font-size: 1rem; box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
    }

    /* 2. 컨테이너 & 그리드 */
    .container { max-width: 1200px; margin: 30px auto; padding: 0 20px 60px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
    
    /* 3. 카드 디자인 */
    .card { background: #fff; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.05); cursor: pointer; border: 1px solid #e9ecef; transition: 0.3s; }
    .card:hover { transform: translateY(-5px); }
    .card.hidden { display: none; } /* 검색 필터용 */
    
    .img-box { width: 100%; height: 300px; display: flex; align-items: center; justify-content: center; padding: 15px; background: #fff; box-sizing: border-box; }
    .img-box img { max-width: 100%; max-height: 100%; object-fit: contain; }
    
    .content { padding: 20px; border-top: 1px solid #f1f3f5; }
    .manufac { color: #adb5bd; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
    .char-name { font-size: 1.15rem; font-weight: 800; margin: 5px 0; color: #212529; }
    .series { font-size: 0.85rem; color: #495057; }

    /* 메모장 */
    .memo-section { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out; background: #fff9db; }
    .card.active .memo-section { max-height: 600px; }
    .memo-content { padding: 20px; font-size: 0.9rem; color: #5c940d; line-height: 1.7; white-space: pre-wrap; border-top: 1px dashed #fab005; }
    .memo-title { font-weight: bold; color: #f08c00; display: block; margin-bottom: 8px; border-bottom: 1px solid #ffe066; padding-bottom: 5px; }

    #status { text-align: center; padding: 50px; font-weight: bold; color: #999; }
  </style>
</head>
<body>

  <header>
    <h1>NIKKE FIGURE ARCHIVE</h1>
    <div class="search-container">
      <input type="text" id="searchInput" placeholder="캐릭터명 또는 제조사 검색..." onkeyup="filterFigures()">
    </div>
  </header>

  <div class="container">
    <div id="status">데이터 로딩 중...</div>
    <div id="figureGrid" class="grid"></div>
  </div>

  <script>
    const csvURL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pub?gid=477168885&single=true&output=csv";
    const imageBaseURL = "https://bosswise.github.io/figure-DB/images/";

    async function loadDatabase() {
      const grid = document.getElementById("figureGrid");
      const status = document.getElementById("status");

      try {
        const response = await fetch(csvURL);
        const csvText = await response.text();
        const rows = csvText.split(/\r?\n/).map(row => {
          const regex = /(?!\s*$)\s*(?:'([^']*)'|"([^"]*)"|([^,]*))\s*(?:,|$)/g;
          const parts = [];
          let m;
          while (m = regex.exec(row)) { parts.push(m[1] || m[2] || m[3] || ""); }
          return parts;
        });

        status.style.display = "none";
        grid.innerHTML = "";

        for (let i = 1; i < rows.length; i++) {
          const cols = rows[i];
          const fileName = cols[8]?.trim();
          if (!fileName) continue;

          const manufacturer = cols[1]?.trim() || "";
          const series = cols[2]?.trim() || "";
          const character = cols[3]?.trim() || "";
          const desc = cols[9]?.trim() || "상세 메모가 아직 없습니다.";

          const card = document.createElement("div");
          card.className = "card";
          // 검색을 위해 데이터 속성 추가
          card.setAttribute("data-search", `${character} ${manufacturer} ${series}`.toLowerCase());
          card.onclick = function() { this.classList.toggle('active'); };
          
          card.innerHTML = `
            <div class="img-box">
              <img src="${imageBaseURL}${encodeURIComponent(fileName)}.jpg" onerror="this.src='https://placehold.co/400x400/fff/ccc?text=No+Image'">
            </div>
            <div class="content">
              <div class="manufac">${manufacturer}</div>
              <div class="char-name">${character}</div>
              <div class="series">${series}</div>
            </div>
            <div class="memo-section">
              <div class="memo-content"><span class="memo-title">Collector's Note</span>${desc}</div>
            </div>
          `;
          grid.appendChild(card);
        }
      } catch (err) {
        status.innerHTML = "데이터 로딩 실패";
      }
    }

    // 💡 실시간 필터링 함수
    function filterFigures() {
      const query = document.getElementById("searchInput").value.toLowerCase();
      const cards = document.querySelectorAll(".card");
      
      cards.forEach(card => {
        const content = card.getAttribute("data-search");
        if (content.includes(query)) {
          card.classList.remove("hidden");
        } else {
          card.classList.add("hidden");
        }
      });
    }

    loadDatabase();
  </script>
</body>
</html>
