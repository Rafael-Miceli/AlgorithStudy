var problem = require("../problem");

describe("Second Right Most Zero Bit", function() {
  var a; 

  it("37 equal to 8", function() {    
    
    var result = problem.secondMostRightZeroBit(37);    
    expect(result).toBe(8);

  });

  it("1073741824 equal to 2", function() {    
    
    var result = problem.secondMostRightZeroBit(1073741824);    
    expect(result).toBe(2);
    
  });

  it("83748 equal to 2", function() {    
    
    var result = problem.secondMostRightZeroBit(83748);    
    expect(result).toBe(2);
    
  });

  it("4 equal to 2", function() {    
    
    var result = problem.secondMostRightZeroBit(4);    
    expect(result).toBe(2);
    
  });

  it("728782938 equal to 4", function() {    
    
    var result = problem.secondMostRightZeroBit(728782938);    
    expect(result).toBe(4);
    
  });
});

describe("Second Right Most Zero Bit 2", function() {
  var a; 

  it("37 equal to 8", function() {    
    
    var result = problem.secondMostRightZeroBit_2(37);    
    expect(result).toBe(8);

  });

  it("1073741824 equal to 2", function() {    
    
    var result = problem.secondMostRightZeroBit_2(1073741824);    
    expect(result).toBe(2);
    
  });

  it("83748 equal to 2", function() {    
    
    var result = problem.secondMostRightZeroBit_2(83748);    
    expect(result).toBe(2);
    
  });

  it("4 equal to 2", function() {    
    
    var result = problem.secondMostRightZeroBit_2(4);    
    expect(result).toBe(2);
    
  });

  it("728782938 equal to 4", function() {    
    
    var result = problem.secondMostRightZeroBit_2(728782938);    
    expect(result).toBe(4);
    
  });
});