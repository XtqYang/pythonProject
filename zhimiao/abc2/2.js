function makeDelay(t) {
    return 100 * Math.ceil(10 * Math.random()) + t
}
const c = makeDelay(1e3);
console.log(c)