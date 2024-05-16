chrome.webRequest.onBeforeRequest.addListener(
    function(details){ return{ cancel: details.url.indexOf(default_filters) != -1 }},
        {urls: ["<all_urls>"]},
        ["blocking"]
)    

default_filters = [
    "://*.doubleclick.net/*",
    "://*.zedo.com/*",
    "://*.partner.googleadservices.com/*",
    "://*.googlesyndication.com/*",
    "://*.google-analytics.com/*",
    "://*.adbrite.com/*",
    "://*.exponential.com/*",
    "://*.quantserve.com/*",
    "://*.creative.ak.fbcdn.net/*",
    "://*.scorecardresearch.com/*",
]

let state = false;
chrome.browserAction.onBeforeRequest.addListener(function(tab) {
  if (!state) {
    chrome.tabs.insertCSS(null, { file: "dark_mode.css" });
    state = !state;
    return;
  }
  chrome.tabs.insertCSS(null, { file: "light_mode.css" });
  state = !state;
});