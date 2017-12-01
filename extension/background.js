chrome.browserAction.onClicked.addListener(function(tab) {

  chrome.tabs.insertCSS(null, {file: 'blackout.css'}, function() {

    chrome.tabs.executeScript(null, {file: 'blackout.js'});

  });

});