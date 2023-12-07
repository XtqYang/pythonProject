var e = 'zfsw_167695658'
var r = r || function (t) {
    var r = {}, i = r.lib = {}, n = function () {
        }, s = i.Base = {
            extend: function (t) {
                n.prototype = this;
                var e = new n();
                return t && e.mixIn(t), e.hasOwnProperty("init") || (e.init = function () {
                    e.$super.init.apply(this, arguments);
                }), e.init.prototype = e, e.$super = this, e;
            },
            mixIn: function (t) {
                for (var e in t) t.hasOwnProperty(e) && (this[e] = t[e]);
                t.hasOwnProperty("toString") && (this.toString = t.toString);
            },
        },
        o = i.WordArray = s.extend({
            // t处理点1
            init: function (t, e) {
                // t起点
                t = this.words = t || [], this.sigBytes = null != e ? e : 4 * t.length;
            },
            toString: function (t) {
                return (t || a).stringify(this);
            },
            concat: function (t) {
                var e = this.words, r = t.words, i = 0;
                if (t = t.sigBytes, this.clamp(), i % 4) for (var n = 0; n < t; n++) e[i + n >>> 2] |= (r[n >>> 2] >>> 24 - n % 4 * 8 & 255) << 24 - (i + n) % 4 * 8; else if (65535 < r.length) for (n = 0; n < t; n += 4) e[i + n >>> 2] = r[n >>> 2]; else e.push.apply(e, r);
                // 此处使e,r都等于t
                return this.sigBytes += t, this;
            },
            clamp: function () {
                var e = this.words, r = this.sigBytes;
                e[r >>> 2] &= 4294967295 << 32 - r % 4 * 8, e.length = t.ceil(r / 4);
            },
        }),
        c = r.enc = {}, a = c.Hex = {
            stringify: function (t) {
                var e = t.words;
                for (var r = [], i = 0; i < 16; i++) {
                    var n = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                    r.push((n >>> 4).toString(16)), r.push((15 & n).toString(16));
                }
                // zfsw_加密的出口
                return r.join("");
            },
        }, f = c.Latin1 = {
            parse: function (t) {
                // 处理返回的zfsw_167782207  3
                for (var e = t.length, r = [], i = 0; i < e; i++) r[i >>> 2] |= (255 & t.charCodeAt(i)) << 24 - i % 4 * 8;
                // 这里的r就是t
                return new o.init(r, e);
            }
        }, h = c.Utf8 = {
            parse: function (t) {
                // 处理返回的zfsw_167782207   2
                return f.parse(unescape(encodeURIComponent(t)));
            }
        },
        u = i.BufferedBlockAlgorithm = s.extend({
            reset: function () {
                this._data = new o.init(), this._nDataBytes = 0;
            },
            _append: function (t) {
                // 处理返回的zfsw_167782207
                "string" == typeof t && (t = h.parse(t)), this._data.concat(t), this._nDataBytes += t.sigBytes;
            },
            _process: function (e) {
                var r = this._data, i = r.words, n = r.sigBytes, s = this.blockSize, c = n / (4 * s);
                if (e = (e ? t.ceil(c) : t.max((0 | c) - this._minBufferSize, 0)) * s, n = t.min(4 * e, n), e) {
                    for (var a = 0; a < e; a += s) {
                        // 对e关键的
                        this._doProcessBlock(i, a);
                    }
                    a = i.splice(0, e), r.sigBytes -= n;
                }
                return new o.init(a, n);
            },
            _minBufferSize: 0
        });
    // a对象，因为被extend对象包裹所以包含其对象
    i.Hasher = u.extend({
        cfg: s.extend(),        // 自定义包含extend对象
        init: function (t) {
            this.cfg = this.cfg.extend(t), this.reset();
        },
        reset: function () {
            u.reset.call(this), this._doReset();
        },
        finalize: function (t) {
        // 返回t=zfsw_167782207
            return t && this._append(t), this._doFinalize();
        },
        blockSize: 16,//a对象结束

        // 处理e和t
        _createHelper: function (t) {
            return function (e, r) {
                return new t.init(r).finalize(e);
            };
        },
        _createHmacHelper: function (t) {
            return function (e, r) {
                return new p.HMAC.init(t, r).finalize(e);
            };
        }
    });
    var p = r.algo = {};
    // 返回对象
    return r;
}(Math);


// 加密算法
e, function (t) {
    function e(t, e, r, i, n, s, o) {
        return ((t = t + (e & r | ~e & i) + n + o) << s | t >>> 32 - s) + e;
    }

    function i(t, e, r, i, n, s, o) {
        return ((t = t + (e & i | r & ~i) + n + o) << s | t >>> 32 - s) + e;
    }

    function n(t, e, r, i, n, s, o) {
        return ((t = t + (e ^ r ^ i) + n + o) << s | t >>> 32 - s) + e;
    }

    function s(t, e, r, i, n, s, o) {
        return ((t = t + (r ^ (e | ~i)) + n + o) << s | t >>> 32 - s) + e;
    }

    for (var o = r, c = (f = o.lib).WordArray, a = f.Hasher, f = 943140919, h = [], u = 0; 64 > u; u++) h[u] = 4294967296 * t.abs(t.sin(u + 1)) | 0;

    f = f.MD5 = a.extend({
        _doReset: function () {
            // t初始值
            this._hash = new c.init([1732584193, 4023233417, 2562383102, 271733878]);
        },
        _doProcessBlock: function (t) {
            // t=2053534583,1597060663,925906227,875790336,,,,,,,,,,,1879048192,0
            for (var o = 0; 16 > o; o++) {
                var c = t[a = o];
                t[a] = 16711935 & (c << 8 | c >>> 24) | 4278255360 & (c << 24 | c >>> 8);
            }
            // a = 2004051578
            // o值是动态数组
            // t=2004051578,926298463,942747959,8402992,0,0,0,0,0,0,0,0,0,0,112,0
            // t是数组
            // 下面需要t和h变化
            o = this._hash.words;
            var f = (c = t[1], t[2]), u = t[3],
                z = e(1732584193, D = 4023233417, C = 2562383102, w = 271733878, 2004051578, 7, h[0]),
                w = e(w, z, D, 2562383102, c, 12, h[1]),
                C = e(2562383102, w, z, D, f, 17, h[2]),
                D = e(D, C, w, z, u, 22, h[3]);
            z = e(z, D, C, w, 0, 7, h[4]),
                w = e(w, z, D, C, 0, 12, h[5]),
                C = e(C, w, z, D, 0, 17, h[6]),
                D = e(D, C, w, z, 0, 22, h[7]),
                z = e(z, D, C, w, 0, 7, h[8]),
                w = e(w, z, D, C, 0, 12, h[9]),
                C = e(C, w, z, D, 0, 17, h[10]),
                D = e(D, C, w, z, 0, 22, h[11]),
                z = e(z, D, C, w, 0, 7, h[12]),
                w = e(w, z, D, C, 0, 12, h[13]),
                C = e(C, w, z, D, 112, 17, h[14]),
                z = i(z, D = e(D, C, w, z, 0, 22, h[15]), C, w, c, 5, h[16]),
                w = i(w, z, D, C, 0, 9, h[17]),
                C = i(C, w, z, D, 0, 14, h[18]),
                D = i(D, C, w, z, 2004051578, 20, h[19]),
                z = i(z, D, C, w, 0, 5, h[20]),
                w = i(w, z, D, C, 0, 9, h[21]),
                C = i(C, w, z, D, 0, 14, h[22]),
                D = i(D, C, w, z, 0, 20, h[23]),
                z = i(z, D, C, w, 0, 5, h[24]),
                w = i(w, z, D, C, 112, 9, h[25]),
                C = i(C, w, z, D, u, 14, h[26]),
                D = i(D, C, w, z, 0, 20, h[27]),
                z = i(z, D, C, w, 0, 5, h[28]),
                w = i(w, z, D, C, f, 9, h[29]),
                C = i(C, w, z, D, 0, 14, h[30]),
                z = n(z, D = i(D, C, w, z, 0, 20, h[31]), C, w, 0, 4, h[32]),
                w = n(w, z, D, C, 0, 11, h[33]),
                C = n(C, w, z, D, 0, 16, h[34]),
                D = n(D, C, w, z, 112, 23, h[35]),
                z = n(z, D, C, w, c, 4, h[36]),
                w = n(w, z, D, C, 0, 11, h[37]),
                C = n(C, w, z, D, 0, 16, h[38]),
                D = n(D, C, w, z, 0, 23, h[39]),
                z = n(z, D, C, w, 0, 4, h[40]),
                w = n(w, z, D, C, 2004051578, 11, h[41]),
                C = n(C, w, z, D, u, 16, h[42]),
                D = n(D, C, w, z, 0, 23, h[43]),
                z = n(z, D, C, w, 0, 4, h[44]),
                w = n(w, z, D, C, 0, 11, h[45]),
                C = n(C, w, z, D, 0, 16, h[46]),
                z = s(z, D = n(D, C, w, z, f, 23, h[47]), C, w, 2004051578, 6, h[48]),
                w = s(w, z, D, C, 0, 10, h[49]),
                C = s(C, w, z, D, 112, 15, h[50]),
                D = s(D, C, w, z, 0, 21, h[51]),
                z = s(z, D, C, w, 0, 6, h[52]),
                w = s(w, z, D, C, u, 10, h[53]),
                C = s(C, w, z, D, 0, 15, h[54]),
                D = s(D, C, w, z, c, 21, h[55]),
                z = s(z, D, C, w, 0, 6, h[56]),
                w = s(w, z, D, C, 0, 10, h[57]),
                C = s(C, w, z, D, 0, 15, h[58]),
                D = s(D, C, w, z, 0, 21, h[59]),
                z = s(z, D, C, w, 0, 6, h[60]),
                w = s(w, z, D, C, 0, 10, h[61]),
                C = s(C, w, z, D, f, 15, h[62]),
                D = s(D, C, w, z, 0, 21, h[63]);
            o[0] = o[0] + z | 0,
                o[1] = o[1] + D | 0,
                o[2] = o[2] + C | 0,
                o[3] = o[3] + w | 0;
        },
        _doFinalize: function () {
            var e = this._data, r = e.words, i = 8 * this._nDataBytes, n = 8 * e.sigBytes;
            r[n >>> 5] |= 128 << 24 - n % 32;
            var s = t.floor(i / 4294967296);
            for (r[15 + (n + 64 >>> 9 << 4)] = 16711935 & (s << 8 | s >>> 24) | 4278255360 & (s << 24 | s >>> 8),
                     r[14 + (n + 64 >>> 9 << 4)] = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8),
                     e.sigBytes = 4 * (r.length + 1), this._process(), r = (e = this._hash).words, i = 0; 4 > i; i++) n = r[i],
                r[i] = 16711935 & (n << 8 | n >>> 24) | 4278255360 & (n << 24 | n >>> 8);
            return e;
        },
    }), o.MD5 = a._createHelper(f), o.HmacMD5 = a._createHmacHelper(f);
}(Math), r.lib.Cipher || function () {
    var e = (l = r).lib, i = e.Base, s = e.BufferedBlockAlgorithm, a = e.Cipher = s.extend({
        cfg: i.extend(),
        _createHelper: function (t) {
        }
    });
    var f = l.mode = {}, u = (e.BlockCipherMode = i.extend()).extend();
    f = f.CBC = u, u = (l.pad = {}).Pkcs7 = {}, e.BlockCipher = a.extend({
        cfg: a.cfg.extend({
            mode: f,
            padding: u
        }),
        blockSize: 4
    });
}(), function () {
    for (var t = r, e = t.lib.BlockCipher, i = t.algo, y = 0; 256 > y; y++) l[y] = 128 > y ? y << 1 : y << 1 ^ 283;
    i = i.AES = e.extend({
        _doReset: function () {
            for (var t = (r = this._key).words, e = r.sigBytes / 4, r = 4 * ((this._nRounds = e + 6) + 1), i = this._keySchedule = [], s = 0; s < r; s++) if (s < e) i[s] = t[s]; else {
                var o = i[s - 1];
                s % e ? 6 < e && 4 == s % e && (o = n[o >>> 24] << 24 | n[o >>> 16 & 255] << 16 | n[o >>> 8 & 255] << 8 | n[255 & o]) : (o = n[(o = o << 8 | o >>> 24) >>> 24] << 24 | n[o >>> 16 & 255] << 16 | n[o >>> 8 & 255] << 8 | n[255 & o],
                    o ^= S[s / e | 0] << 24), i[s] = i[s - e] ^ o;
            }
            for (t = this._invKeySchedule = [], e = 0; e < r; e++) s = r - e, o = e % 4 ? i[s] : i[s - 4],
                t[e] = 4 > e || 4 >= s ? o : h[n[o >>> 24]] ^ u[n[o >>> 16 & 255]] ^ p[n[o >>> 8 & 255]] ^ d[n[255 & o]];
        },
        keySize: 8
    });
    t.AES = e._createHelper(i);
}(), module.exports = r;
