console.log("Me importou");


exports.secondMostRightZeroBit = function SecondMostRightZeroBit(n) {
    return Math.pow(2, ((n | n + 1) ^ ((n | n + 1) | (n | n + 1) + 1)).toString(2).length - 1);
};


