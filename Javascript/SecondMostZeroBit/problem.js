
exports.secondMostRightZeroBit = function(n) {
    return Math.pow(2, ((n | n + 1) ^ ((n | n + 1) | (n | n + 1) + 1)).toString(2).length - 1);
};

exports.secondMostRightZeroBit_2 = function(n) {
    return ~(n |= -~n) & -~n;
}
