let mysql = require("mysql");
const c = require("./616C1636AB6B1EDF070A7E310FF4F110");

// 当前时间戳
function f5() {
    // 返回当前毫秒时间戳
    var myDate = new Date();
    let t = myDate.getTime() + "";
    // 返回毫秒的最后4位,即为秒
    let s = t.substring(9, 13);
    // s = 1111 + ""
    // 类型转换
    return parseInt(s)
}

function f3() {
    console.log("连接开始=" + f5())

    let connection = mysql.createConnection({
        host: "localhost",
        port: 3306,
        user: "root",
        password: "hy064872",
        database: "pyth"
    });
    connection.connect((err) => {
        if (err) {
            console.error("数据库连接失败" + err.stack);
            return;
        }
        console.log("数据库连接成功");
    });
    return connection
}

function f() {
    // 提前秒数
    t = 0.8
    const c = require("./616C1636AB6B1EDF070A7E310FF4F110");
    var e = (Date.parse(new Date)) / 1e3 + t + "";
    e = c.MD5("zfsw_" + e.substring(0, e.length - 1)).toString()
    return e;
}

// 插入数据
// async node.js mapLimit
async function f2() {
    // 先执行删除
    let a = await f1();
    // let columns=f();
    // 再插入数据
    let sql = "insert into school(tim) values(?)";//?是占位符
    await new Promise((resolve) => {
        //设置参数
        let params = [f()];
        a.query(sql, params, (err) => {
            if (err) {
                console.error("插入失败" + err.message);
            }
            resolve(1)
            console.log("插入" + f() + "成功");
        });
    });
    // 执行完成后需要关闭连接
    // a.end()
    a.end()
    console.log("连接结束=" + f5())

}

async function f1() {
    let connection = f3();
    let sql2 = "truncate table school"
    connection.query(sql2, (err) => {
        if (err) {
            console.log("清空失败" + err.message);
        }
        console.log('清空成功');
    });
    return connection
}

async function f4() {
    let i = 0
    while (i < 99999999) {
        let number1 = f5();
        console.log("当前毫秒=" + number1)

        if (1111 === number1) {
            console.log("执行")
            await f2().catch((e) => {
                console.log(e.message)
            });
        }
        i++
    }
}

f4()



