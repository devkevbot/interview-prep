class Coffee {
  /**
   * @returns {number} The cost of the coffee.
   */
  getCost() {
    throw new Error("Method getCost() must be implemented.");
  }
}

class SimpleCoffee extends Coffee {
  /**
   * @returns {number} The cost of the simple coffee.
   */
  getCost() {
    return 1.1;
  }
}

class CoffeeDecorator extends Coffee {
  /**
   * @param {Coffee} coffee The coffee to be decorated.
   */
  constructor(coffee) {
    super();
    this.decoratedCoffee = coffee;
  }

  /**
   * @returns {number} The cost of the decorated coffee.
   */
  getCost() {
    return this.decoratedCoffee.getCost();
  }
}

class MilkDecorator extends CoffeeDecorator {
  /**
   * @param {Coffee} coffee The coffee to add milk to.
   */
  constructor(coffee) {
    super(coffee);
  }

  /**
   * @returns {number} The cost of the coffee with milk.
   */
  getCost() {
    return super.getCost() + 0.5;
  }
}

class SugarDecorator extends CoffeeDecorator {
  /**
   * @param {Coffee} coffee The coffee to add sugar to.
   */
  constructor(coffee) {
    super(coffee);
  }

  /**
   * @returns {number} The cost of the coffee with sugar.
   */
  getCost() {
    return super.getCost() + 0.2;
  }
}

class CreamDecorator extends CoffeeDecorator {
  /**
   * @param {Coffee} coffee The coffee to add cream to.
   */
  constructor(coffee) {
    super(coffee);
  }

  /**
   * @returns {number} The cost of the coffee with cream.
   */
  getCost() {
    return super.getCost() + 0.7;
  }
}
