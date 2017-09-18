function findRestaurant() {
    
    
    var restaurant1 = {
        "name": "iCrave", 
        "url": "https://www.yelp.com/biz/icrave-capitola-2",
        "meal": "snack",
        "favorite": "mango milk tea",
        "img": "img/bubbletea.jpg",
        "img2": "img/icrave.jpg"};
    
    var restaurant2 = {
        "name": "Sushi Garden",
        "url": "https://www.yelp.com/biz/sushi-garden-capitola",
        "meal": "lunch",
        "favorite": "sushi",
        "img": "img/sushi.jpg",
        "img2": "img/sushigarden.jpg"};
    
    var restaurant3 = {
        "name": "Asian Express",
        "url": "https://www.yelp.com/biz/asian-express-capitola-2",
        "meal": "dinner",
        "favorite": "beef pho w/ mango bubble tea",
        "img": "img/pho.jpg",
        "img2": "img/asianexpress.jpg"};
    
    var restaurant4 = {
        "name": "Avenue Cafe",
        "url": "https://www.yelp.com/biz/avenue-cafe-capitola",
        "meal": "breakfast",
        "favorite": "carnitas quesdilla",
        "img": "img/quesadilla.jpg",
        "img2": "img/avenuecafe.jpg"
    
    }
    
    
    
    var restaurants = [
        restaurant1,
        restaurant2,
        restaurant3,
        restaurant4,
    ];
    
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