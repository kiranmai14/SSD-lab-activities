var http = require("http");
var dt = require("./service.js");
var url = require("url");
let port = 8080;
http
  .createServer(function (req, res) {
    res.writeHead(200, { "Content-Type": "application/json" });
    let q = url.parse(req.url, true).query;
    qdata = q.query;
    if (qdata == 1) {
      let result = dt.GetHighestMarks();
      res.write(JSON.stringify(result));
    } else if (qdata == 2) {
      let index = q.index;
      let result = dt.GetSubjectiToppers(index);
      res.write(JSON.stringify(result));
    } else {
      let result = "invalid query";
      res.write(JSON.stringify(result));
    }
    return res.end();
  })
  .listen(port, () => {
    console.log("Server is now lisning on port " + port);
  });
