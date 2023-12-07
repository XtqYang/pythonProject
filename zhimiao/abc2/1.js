const c = require("./616C1636AB6B1EDF070A7E310FF4F110");
d = ""
l = ""

function b(e) {
    // 传入需要加密的数据e，返回加密后的数据
    return new Promise(function (t, s) {
        // l密钥，a是将秘钥转换成Utf8字节数组
        var a = c.enc.Utf8.parse(l);
        t(c.AES.encrypt(e, a, {
            // d偏移量
            iv: d,
            mode: c.mode.CBC,
            padding: c.pad.Pkcs7
        }).ciphertext.toString());
    });
}

b(e="11111111111111")