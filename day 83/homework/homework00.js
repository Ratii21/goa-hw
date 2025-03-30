function random(lst){
    // Math.random() აბრუნებს რიცხვს 0-დან 1-მდე (მაგ: 0.534...)
    // Math.random() * names.length -> სია 0-დან names.length-მდე (მაგ: 0-დან 5-მდე)
    // Math.floor() აკლებს ათწილადს და იღებს მთელ რიცხვს (მაგ: 2.76 -> 2)
    const index = Math.floor(Math.random() * names.length);

    return lst[randomIndex];
}
