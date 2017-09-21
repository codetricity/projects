function allRestaurants() {
    findRestaurant(restaurants);
}

function breakfast() {
    var breakfastRestaurants = [];
    for (var i = 0; i < restaurants.length; i++) {
        if (restaurants[i].meal == "breakfast") {
            breakfastRestaurants.push(restaurants[i]);
        }
    }
    findRestaurant(breakfastRestaurants);
}

function lunch() {
    var lunchRestaurants = [];
    for (var i = 0; i < restaurants.length; i++) {
        if (restaurants[i].meal == "lunch") {
            lunchRestaurants.push(restaurants[i]);
        }
    }
    findRestaurant(lunchRestaurants);
}

function snack() {
    var snackRestaurants = [];
    for (var i = 0; i < restaurants.length; i++) {
        if (restaurants[i].meal == "snack") {
            snackRestaurants.push(restaurants[i]);
        }
    }
    findRestaurant(snackRestaurants);
}

function dinner() {
    var dinnerRestaurants = [];
    for (var i = 0; i < restaurants.length; i++) {
        if (restaurants[i].meal == "dinner") {
            dinnerRestaurants.push(restaurants[i]);
        }
    }
    findRestaurant(dinnerRestaurants);
}