function f() {
    let date = new Date();
    var e = (Date.parse(date)) / 1e3 + "";
    const c = require("./616C1636AB6B1EDF070A7E310FF4F110");
    console.log(c)
    e = c.MD5("zfsw_" + e.substring(0, e.length - 1)).toString()
    console.log(e)
}
f()
