const search_input = document.querySelector(".search-input");
const grids = document.querySelectorAll(".grid")
const search_task = document.querySelector(".search-task");
const grids_id = document.querySelectorAll("#grid")

if (search_input){
    search_input.addEventListener("input",function(){
    const query = this.value.toLowerCase()
    grids.forEach((grid) =>{
        const contentElement = grid.querySelector(".search-span");
        const title = contentElement ? contentElement.textContent.toLowerCase() : ""
        grid.style.display = title.includes(query) ? '' : 'none';
    })
})
}
if (search_task){
    search_task.addEventListener("input",function(){
        const query = this.value.toLowerCase()
        grids_id.forEach((grid) =>{
            const contentElement = grid.querySelector(".subject-search");
            const title = contentElement ? contentElement.textContent.toLowerCase() : ""
            grid.style.display = title.includes(query) ? '' : "none";
        })
    })
    
}


var stringToColor = function stringToColor(str) {
    var hash = 0;
    var color = '#';
    var i;
    var value;
    var strLength;

    if(!str) {
        return color + '333333';
    }

    strLength = str.length;

    for (i = 0; i < strLength; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }

    for (i = 0; i < 3; i++) {
        value = (hash >> (i * 8)) & 0xFF;
        color += ('00' + value.toString(16)).slice(-2);
    }

    return color;
};
var element_names = document.querySelector("#name")
var naming = element_names.innerHTML
var letter = naming.slice(0, 1);
var backgroundColors = stringToColor(letter);
var element_avatar = document.querySelector("#avatar");
element_avatar.innerHTML = letter
element_avatar.style.backgroundColor = backgroundColors