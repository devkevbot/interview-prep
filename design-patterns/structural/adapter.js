class SquareHole {
  /**
   * @param {number} sideLength
   */
  constructor(sideLength) {
    this.sideLength = sideLength;
  }

  /**
   * @param {Square} square
   * @return {boolean}
   */
  canFit(square) {
    return this.sideLength >= square.getSideLength();
  }
}

class Square {
  /**
   * @param {number} sideLength
   */
  constructor(sideLength = 0) {
    this.sideLength = sideLength;
  }

  /**
   * @return {number}
   */
  getSideLength() {
    return this.sideLength;
  }
}

class Circle {
  /**
   * @param {number} radius
   */
  constructor(radius) {
    this.radius = radius;
  }

  /**
   * @return {number}
   */
  getRadius() {
    return this.radius;
  }
}

class CircleToSquareAdapter extends Square {
  /**
   * @param {Circle} circle
   */
  constructor(circle) {
    super();
    this.circle = circle;
  }

  /**
   * @return {number}
   */
  getSideLength() {
    return 2 * this.circle.getRadius();
  }
}
