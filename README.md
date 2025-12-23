<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Figure DB</title>

  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f5f5f5;
      margin: 0;
      padding: 20px;
    }
    h1 {
      text-align: center;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    .card {
      background: white;
      padding: 10px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      text-align: center;
    }
    .card img {
      width: 100%;
      height: 200px;
      object-fit: contain;
    }
    .name {
      margin-top: 8px;
      font-weight: bold;
    }
    .manufacturer {
      font-size: 0.9em;
      color: #666;
    }
  </style>
</head>

<body>

  <h1>피규어 데이터베이스</h1>

  <!-- 카드들이 들어갈 자리 -->
  <div class="grid" id="figureGrid"></div>

  <script>
    const sheetURL =
      "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEdK-zeaaFdfpd-3KmkuvWvjfJ836zpU6iXd-Duapx8ZXjewYF80U88jICtyzhOGpkS1JozinX2f3w/pubhtml";

    fetch(sheetURL)
      .then(res => res.text())
      .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const rows = doc.querySelectorAll("table tr");

        const grid = document.getElementById("figureGrid");

        rows.forEach((row, index) => {
          if (index === 0) return;

          const cols = row.querySelectorAll("td");
          if (cols.length < 4) return;

          const manufacturer = cols[0].innerText.trim();
          const series = cols[1].innerText.trim();
          const character = cols[2].innerText.trim();
          const imageFile = cols[3].innerText.trim();

          const card = document.createElement("div");
          card.className = "card";

          card.innerHTML = `
            <img src="images/${imageFile}.jpg" alt="${character}">
            <div class="name">${series} - ${character}</div>
            <div class="manufacturer">${manufacturer}</div>
          `;

          grid.appendChild(card);
        });
      });
  </script>

</body>
</html>
