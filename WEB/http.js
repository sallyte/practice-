var http = require('http');

// 서버 생성
http.createServer(function (req, res) {
  // 응답 헤더 설정
  res.writeHead(200, {'Content-Type': 'text/html'});
  // 응답 메시지
  res.write('Hello World!');
  res.end();
}).listen(8080); /// 8080포트 사용