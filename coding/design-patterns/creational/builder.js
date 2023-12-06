class Meal {
  constructor() {
    this.cost = 0.0;
    this.takeOut = false;
    this.main = "";
    this.drink = "";
  }

  getCost() {
    return this.cost;
  }

  getTakeOut() {
    return this.takeOut;
  }

  getMain() {
    return this.main;
  }

  getDrink() {
    return this.drink;
  }

  setCost(cost) {
    this.cost = cost;
  }

  setTakeOut(takeOut) {
    this.takeOut = takeOut;
  }

  setMain(main) {
    this.main = main;
  }

  setDrink(drink) {
    this.drink = drink;
  }
}

class MealBuilder {
  constructor() {
    this.meal = new Meal();
  }

  /**
   * @param {number} cost
   * @return {MealBuilder}
   */
  addCost(cost) {
    this.meal.setCost(cost);
    return this;
  }

  /**
   * @param {boolean} takeOut
   * @return {MealBuilder}
   */
  addTakeOut(takeOut) {
    this.meal.setTakeOut(takeOut);
    return this;
  }

  /**
   * @param {string} main
   * @return {MealBuilder}
   */
  addMainCourse(main) {
    this.meal.setMain(main);
    return this;
  }

  /**
   * @param {string} drink
   * @return {MealBuilder}
   */
  addDrink(drink) {
    this.meal.setDrink(drink);
    return this;
  }

  /**
   * @return {Meal}
   */
  build() {
    return this.meal;
  }
}
