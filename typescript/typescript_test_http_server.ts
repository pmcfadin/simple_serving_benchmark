import * as http from 'http';

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('<html><body>This is a web page.</body></html>');
});

server.listen(8080);
