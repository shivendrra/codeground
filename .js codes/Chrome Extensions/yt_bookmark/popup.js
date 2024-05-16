import { getActiveTabURL} from"./util.js"

const addNewBookmark = () => {};
const viewBookmarks = () => {};
const onPlay = () => {};
const onDelete = () => {};
const setBookmarkAttributes = () => {};

// to display all the bookmarks
document.addEventListener("DOMContentLoaded", async () => {
    const activeTab = await getActiveTabURL();  //to check the active tab
    const queryParameters = activeTab.url.split("?")[1];  //ckeck the active tab and get its url
    const urlPara = new URLSearchParams(queryParameters);   //urlsearchParam to get unique identifier

    const currentVideo = urlPara.get("v");
    
    // check if it's youtube video
    if(activeTab.url.includes("youtube.com/watch") && currentVideo) {
        chrome.storage.sync.get([currentVideo], (data) => {
            const currentVideoBookmarks = data[currentVideo] ? JSON.parse(data[currentVideo]): [];
        })
    }

    else {
        
    }
});