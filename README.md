<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Figure DB</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

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

  <!-- 🔥 JS가 데이터를 꽂아 넣을 자리 -->
  <div class="grid" id="figureGrid"></div>

  <script>
    const


