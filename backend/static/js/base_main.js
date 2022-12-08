// COLLECT DATA:
var sidebar = document.getElementById("sidebar");
var blockSidebar = document.getElementById("block_sidebar");
var pageContent = document.getElementById("page_content");
var page = document.getElementById("page");
var hiddenLists = document.getElementsByClassName("hidden_list");
let hiddenListMenus = document.querySelectorAll('[class*="list_menu"]');
var menuItems = document.getElementsByClassName("sidebar_menu_submenu");



// SIDEBAR - CLOSE / OPEN SUBMENU ITEMS WITH COOKIES:
for(let i=0; i<menuItems.length; i++) {
    let toggleButton = menuItems[i];
    let subMenu = toggleButton.nextElementSibling;
    let subMenuIcon = toggleButton.querySelector(".sidebar_menu_link_submenu_icon");
 
    toggleButton.addEventListener("click", function(event) {
       
        if(subMenu.classList.contains("submenu_hidden") === false) {
            subMenu.classList.add("submenu_hidden");
            subMenuIcon.classList.remove("rotate");
            document.cookie = "open_menu_action=false;path=/";
        } else {
            for(let i=0; i<menuItems.length; i++) {
                let activeElementInside = menuItems[i].nextElementSibling
                let subMenuIconInside = menuItems[i].querySelector(".sidebar_menu_link_submenu_icon");
                activeElementInside.classList.add("submenu_hidden");
                subMenuIconInside.classList.remove("rotate");
            }
            subMenu.classList.remove("submenu_hidden");
            subMenuIcon.classList.add("rotate");
            document.cookie = "open_menu_action=" + i + ";path=/";
        } 
 
    });
 
}



// SIDEBAR ACTION - SHOW HIDE WHOLE MENU WITH COOKIES:
blockSidebar.addEventListener("click", function(event) {

    if(sidebar.classList.contains("blocked_bigbar") === false) {
        sidebar.classList.add("blocked_bigbar");
        document.cookie = "sidebar=true;path=/";
    } else {
        sidebar.classList.remove("blocked_bigbar");
        document.cookie = "sidebar=false;path=/";
    }

});

sidebar.addEventListener("mouseenter", function(event) {
    sidebar.classList.add("bigbar");
});

sidebar.addEventListener("mouseleave", function(event) {
    sidebar.classList.remove("bigbar");
});



// HIDDEN LIST ACTION - SHOW HIDE ITEM PANEL MENU:
for(let i=0; i<hiddenLists.length; i++) {
    let hiddenList = hiddenLists[i]
    let hiddenListButton = hiddenList.querySelector('[class*="list_button"]');
    let hiddenListMenu = hiddenList.querySelector('[class*="list_menu"]');

    hiddenListButton.addEventListener("click", function(event) {
        
        if(hiddenListMenu.classList.contains("show") === true) {
            hiddenListMenu.classList.remove("show");
        } else {
            for(let i=0; i<hiddenListMenus.length; i++) {
                hiddenListMenus[i].classList.remove("show");
            }
            hiddenListMenu.classList.add("show");
        }
    });

}



// PAGE ACTION - CHANGE LIGHT / DARK COLORS:
var lightColor = document.getElementById("page_color_light");
var darkColor = document.getElementById("page_color_dark");
var page = document.getElementById("page");

lightColor.addEventListener("click", function(event) {

    if(page.classList.contains("dark") === true) {
        page.classList.remove("dark");
        lightColor.classList.add("active");
        darkColor.classList.remove("active");
        document.cookie = "dark_site=false;path=/";
    }

});

darkColor.addEventListener("click", function(event) {

    if(page.classList.contains("dark") === false) {
        page.classList.add("dark");
        darkColor.classList.add("active");
        lightColor.classList.remove("active");
        document.cookie = "dark_site=true;path=/";
    }

});




// MAIN COOKIES READER:
function cookies() {

    var cookies = document.cookie.split(";");

    for(let i=0; i<cookies.length; i++) {
        let cookie = cookies[i].split("=");

        // SHOW HIDE WHOLE MENU WITH COOKIES:
        if(cookie[0] === "sidebar" || cookie[0] === " sidebar") {
            if(cookie[1] == "true") {
                sidebar.classList.add("blocked_bigbar");
            };
        } else if(cookie[0] === "open_menu_action" || cookie[0] === " open_menu_action") {
            if(cookie[1] != "false") {
                let menu_number = parseInt(cookie[1]);
                for(let i=0; i<menuItems.length; i++) {
                    if(i === menu_number) {
                        let activeElement = menuItems[i].nextElementSibling;
                        activeElement.classList.remove("submenu_hidden");
                    }
                }
            }
        } else if(cookie[0] === "dark_site" || cookie[0] === " dark_site") {
            if(cookie[1] == "true") {
                page.classList.add("dark");
                darkColor.classList.add("active");
                lightColor.classList.remove("active");
            } else {
                page.classList.remove("dark");
                lightColor.classList.add("active");
                darkColor.classList.remove("active");
            }
        };

    };

    // Allow animations on page:
    setTimeout(function() {
        page.classList.add("animated");
    }, 100);

}

// FUNCTION EXECUTER:
cookies()



// TABS:
var boxTabs = document.getElementsByClassName("box_item_object_tab");

for(let i=0; i<boxTabs.length; i++) {
    let boxTab = boxTabs[i];
    let boxTabHeader = boxTab.querySelector(".box_item_tabs");
    let boxTabHeaderItems = boxTabHeader.children;

    for(let i=0; i<boxTabHeaderItems.length; i++) {
        let boxTabHeaderItem = boxTabHeaderItems[i];

        boxTabHeaderItem.addEventListener("click", function(event) {
            let value = boxTabHeaderItem.attributes.for.value;
            let toActivate = document.getElementById(value);
            let activeItem = boxTab.querySelector(".active_tab_item");
            let activeTab = boxTab.querySelector(".active_tab");

            activeItem.classList.remove("active_tab_item");
            activeTab.classList.remove("active_tab");
            toActivate.classList.add("active_tab_item");
            boxTabHeaderItem.classList.add("active_tab");

        })

    }

}


function resizeGridItem(item){
    grid = document.getElementsByClassName("grid")[0];
    rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
    rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap'));
    rowSpan = Math.ceil((item.querySelector('.content').getBoundingClientRect().height+rowGap)/(rowHeight+rowGap));
      item.style.gridRowEnd = "span "+rowSpan;
  }
  
  function resizeAllGridItems(){
    allItems = document.getElementsByClassName("item");
    for(x=0;x<allItems.length;x++){
      resizeGridItem(allItems[x]);
    }
  }


  //https://medium.com/@andybarefoot/a-masonry-style-layout-using-css-grid-8c663d355ebb