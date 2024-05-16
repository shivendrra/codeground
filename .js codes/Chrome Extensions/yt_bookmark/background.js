// listner to check the tab and export the data to content.js
chrome.tabs.onUpdate.addListener((tabId, tab) => {
    if (tab.url && tab.url.includes("youtube.com/watch")){
        const queryPara = tab.url.split("?")[1];
        const urlPara = new URLSearchParams(queryPara);

        chrome.tab.sendMessage(tabId, {
            type: "NEW",
            videoId: urlPara.get("v")
        });
    }
})