const hero = {
    firstName: "Bilbo",
    secondName: "Begins",
    creatureType: "Hobbit",
    height: "120cm",
    weight: "30kg",
}

console.log(hero.firstName)
console.log(hero.secondName)
console.log(hero.creatureType)
console.log(hero.height)
console.log(hero.weight)

hero.height = "125cm"
hero.weight = "35kg"

console.log(hero)

hero.inWhatMovie = "The Hobbit"

delete hero.creatureType

