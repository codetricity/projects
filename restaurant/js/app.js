function findRestaurant(restaurants) {

    
    var length = restaurants.length;
    var randomNum = Math.floor(Math.random() * length);
    
    var restaurantInfo = document.getElementById("restaurantInfo");
    restaurantInfo.innerHTML = restaurants[randomNum].name;
    restaurantInfo.href = restaurants[randomNum].url;
    var meal = document.getElementById("meal");
    meal.innerHTML = restaurants[randomNum].meal;
    var favorite = document.getElementById("favorite");
    favorite.innerHTML = restaurants[randomNum].favorite;
    var foodImage = document.getElementById("foodImage");
    foodImage.src = restaurants[randomNum].img;
    var restaurantImage = document.getElementById("restaurantImage");
    restaurantImage.src = restaurants[randomNum].img2;
    };