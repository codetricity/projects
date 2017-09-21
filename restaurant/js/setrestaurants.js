function allRestaurants() {
    findRestaurant(restaurants);
}

function breakfast() {
    var breakfastRestaurants = [];
    for (var i = 0; i < restaurants.length; i++) {
        if (restaurants[i].meal == 'breakfast'){
            breakfastRestaurants.push(restaurants[i]);
        }
    }
    findRestaurant(breakfastRestaurants);
}

function lunch() {
    var lunchRestaurants = [];
    for (var i = 0; i < restaurants.length; i++) {
        if (restaurants[i].meal == "lunch"){
            lunchRestaurants.push(restaurants[i]);
        }
    }
    findRestaurant(lunchRestaurants);
}

function snack() {
    var restaurants = [
        restaurant1,
        restaurant5
    ];
    findRestaurant(restaurants);
}

function dinner() {
    var restaurants = [
        restaurant3
    ];
    findRestaurant(restaurants);
}