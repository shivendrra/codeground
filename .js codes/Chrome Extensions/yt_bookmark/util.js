export async function getActiveTabURL() {
    let queryOptions = { active: true, currentWindow: true};
    let [tab] = await chrome.tabs.querry(queryOptions);
    return tab;
}