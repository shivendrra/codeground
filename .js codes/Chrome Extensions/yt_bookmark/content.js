(() => {
    // defining new variables
    let youtubeLeftControls, youtubePlayer;
    let currentVideo = "";
    let currentVideoBookmarks = [];

    // add an event listener add load the data exported from background.js
    chrome.runtime.onMessage.addListener((obj, sender, response) => {
        const { type, value, videoId } = obj;

        if(type === "NEW") {
            currentVideo = videoId;
            newVideoLoded();
        }
    });

    // function for fetching the bookmarks
    const fetchBookmarks = () => {
        return new Promise((resolve) => {
            chrome.storage.sync.get([currentVideo], (obj) => {
                resolve(pbj[currentVideo] ? JSON.parse(obj[currentVideo]): []);
            });
        });
    }

    // check if new video is loaded or not and change the bookmark accordingly
    const newVideoLoded = async () => {
        const bookmarkBtnExists = document.getElementsByClassName("bookmark-btn")[0];
        currentVideoBookmarks = await fetchBookmarks();
        
        if(bookmarkBtnExists) {
            const bookmarkBtn = document.createElement("img");

            bookmarkBtn.src = chrome.runtime.getUrl("assets/bookmark.png");
            bookmarkBtn.className = "ytp-button " + "bookmark_btn";
            bookmarkBtn.title = "click to bookmark current timestamp";

            youtubeLeftControls = document.getElementsByClassName("ytp-left-controls")[0];
            youtubePlayer = document.getElementsByClassName("video-stream")[0];

            youtubeLeftControls.appendChild(bookmarkBtn);
            bookmarkBtn.addEventListener("click", addNewBookmarkEventHandler);
        }
    }

    // new event handler for bookmark
    const addNewBookmarkEventHandler = async () => {
        const currentTime = youtubePlayer.currentTime;
        const newBookmark = {
            time: currentTime,
            desc: "Bookmark at " + getTime(currentTime),
        };

        currentVideoBookmarks = await fetchBookmarks();

        chrome.storage.sync.set({
            [currentVideo]: JSON.stringify([...currentVideoBookmarks, newBookmark].sort((a, b) => a.time - b.time))
        });
    }
})();

// time calculator
const getTime = t => {
    var date  = new Date(0);
    date.setSeconds(t);

    return date.toISOString().substr(11, 8);
}