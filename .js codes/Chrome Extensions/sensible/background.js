chrome.browserAction.OnClicked.addEventListener(btnClicked);
function btnClicked(tab){
    let msg = {
        txt: "hello"
    }
    chrome.tabs.sendMessage(tab.id, msg);
}