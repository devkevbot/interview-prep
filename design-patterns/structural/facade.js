class Order {
  /**
   * @param {string} contents
   * @param {boolean} takeOut
   */
  constructor(contents, takeOut) {
    this.contents = contents;
    this.takeOut = takeOut;
  }

  /**
   * @return {string}
   */
  getOrder() {
    return this.contents;
  }

  /**
   * @return {boolean}
   */
  isTakeOut() {
    return this.takeOut;
  }
}

class Cashier {
  /**
   * @param {string} contents
   * @param {boolean} takeOut
   * @return {Order}
   */
  takeOrder(contents, takeOut) {
    return new Order(contents, takeOut);
  }
}

class Food {
  /**
   * @param {string} order
   */
  constructor(order) {
    this.contents = order;
  }

  /**
   * @return {string}
   */
  getFood() {
    return this.contents;
  }
}

class Chef {
  /**
   * @param {Order} order
   * @return {Food}
   */
  prepareFood(order) {
    return new Food(order.getOrder());
  }
}

class PackagedFood extends Food {
  /**
   * @param {Food} food
   */
  constructor(food) {
    super(food.getFood() + " in a bag");
  }
}

class KitchenStaff {
  /**
   * @param {Food} food
   * @return {PackagedFood}
   */
  packageOrder(food) {
    return new PackagedFood(food);
  }
}

class DriveThruFacade {
  constructor() {
    this.cashier = new Cashier();
    this.chef = new Chef();
    this.kitchenStaff = new KitchenStaff();
  }

  /**
   * @param {string} orderContents
   * @param {boolean} takeOut
   * @return {Food}
   */
  takeOrder(orderContents, takeOut) {
    let order = this.cashier.takeOrder(orderContents, takeOut);
    let food = this.chef.prepareFood(order);
    if (order.isTakeOut()) {
      return this.kitchenStaff.packageOrder(food);
    }
    return food;
  }
}
