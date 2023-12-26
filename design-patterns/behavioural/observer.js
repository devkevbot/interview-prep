class Observer {
  /**
   * @param {string} itemName
   */
  notify(itemName) {
    throw new Error("Method 'notify()' must be implemented.");
  }
}

class Customer extends Observer {
  /**
   * @param {string} name
   */
  constructor(name) {
    super();
    this.name = name;
    this.notifications = 0;
  }

  /**
   * @param {string} itemName
   */
  notify(itemName) {
    this.notifications += 1;
  }

  /**
   * @return {number}
   */
  countNotifications() {
    return this.notifications;
  }
}

class OnlineStoreItem {
  /**
   * @param {string} itemName
   * @param {number} stock
   */
  constructor(itemName, stock) {
    this.itemName = itemName;
    this.stock = stock;
    this.observers = [];
  }

  /**
   * @param {Observer} observer
   */
  subscribe(observer) {
    this.observers.push(observer);
  }

  /**
   * @param {Observer} observer
   */
  unsubscribe(observer) {
    const index = this.observers.indexOf(observer);
    if (index > -1) {
      this.observers.splice(index, 1);
    }
  }

  /**
   * @param {number} newStock
   */
  updateStock(newStock) {
    const oldStock = this.stock;
    this.stock = newStock;

    if (oldStock === 0 && newStock > 0) {
      this.notifyObservers();
    }
  }

  notifyObservers() {
    this.observers.forEach((observer) => {
      observer.notify(this.itemName);
    });
  }
}
