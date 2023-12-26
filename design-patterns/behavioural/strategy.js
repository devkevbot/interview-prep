class Person {
  constructor(lastName, age, married) {
    this.lastName = lastName;
    this.age = age;
    this.married = married;
  }

  /**
   * @returns {string}
   */
  getLastName() {
    return this.lastName;
  }

  /**
   * @returns {number}
   */
  getAge() {
    return this.age;
  }

  /**
   * @returns {boolean}
   */
  isMarried() {
    return this.married;
  }
}

class PersonFilter {
  /**
   * @param {Person} person
   * @returns {boolean}
   */
  apply(person) {
    throw new Error("Abstract method 'apply' must be implemented.");
  }
}

class AdultFilter extends PersonFilter {
  apply(person) {
    return person.getAge() >= 18;
  }
}

class SeniorFilter extends PersonFilter {
  apply(person) {
    return person.getAge() >= 65;
  }
}

class MarriedFilter extends PersonFilter {
  apply(person) {
    return person.isMarried();
  }
}

class PeopleCounter {
  /**
   * @param {PersonFilter} filter
   */
  setFilter(filter) {
    if (!(filter instanceof PersonFilter)) {
      throw new Error("Filter must be an instance of PersonFilter");
    }
    this.filter = filter;
  }

  /**
   * @param {Person[]} people
   * @returns {number}
   */
  count(people) {
    // Implement method here
    return people.filter(this.filter.apply).length;
  }
}
