// Heavily borrowing from: Cory Forsyth, Hacking the Browser, NYU ITP
// LINK: https://github.com/ITPNYU/hacking-the-browser/blob/master/caps-detector/caps-detector.js

(function() {
	
	var BLACKOUTCLASS = "grapevine";


	if (!document.querySelector('.' + BLACKOUTCLASS)) {

		blackOut();
		
	}

	function blackOut(){

		function getTextNodes() {

			// Helpful documentation on .createTreeWalker(): https://developer.mozilla.org/en-US/docs/Web/API/Document/createTreeWalker
			// I usually use jquery for a lot of this, but seems like TreeWalker is at least sometimes faster: https://codepen.io/mjwwit/pen/YZbJEN
			// Helpful for contextualizing different ways of doing the same goddamn thing: http://www.dev-n-design.com/toddlerwilliams.com/blog/uncategorized/dom-traversal-jquery-vs-plain-javascript/
			// Are my tools and methods ancient, or nah? The web is a mess. 
			// This is also why it takes me so long to do everything. The learning and the unlearning.

			var nodeList = [];

			var walker = document.createTreeWalker(document, NodeFilter.SHOW_TEXT, null, null);
		    var node = walker.nextNode();

		    while (node) {

		      var parentNode = node.parentNode;
		      var parentTagName = parentNode.tagName;
		      if (parentTagName !== "SCRIPT" && parentTagName !== "STYLE" && parentTagName !== "TITLE") {
		        nodeList.push(node);

		      }
		      node = walker.nextNode();
		    }

		    return nodeList;
		}

		function getRelevantNodes() {
			return getTextNodes().filter(containsAnonymity); 
		}

		function containsAnonymity(node) {

			// a very cool project I'm borrowing these phrases from: https://github.com/markschaver/anonymous-2.0/blob/master/anonymous-phrases.txt
			var anonPhrases = ["a Democratic operative close to",
									"a House Democratic aide",
									"a House Republican aide",
									"a Republican operative close to",
									"a Senate Democratic aide",
									"a Senate Republican aide",
									"a person briefed on the matter",
									"a person close to",
									"a person familiar with the matter",
									"a person familiar with the situation",
									"a person involved in the negotiations",
									"a senior Democratic aide",
									"a senior Democratic committee aide",
									"a senior Republican aide",
									"a senior Republican committee aide",
									"a source close to",
									"a source familiar with the situation",
									"a source involved in the negotiations",
									"a source said",
									"according to a person close to",
									"according to a person familar with",
									"according to a person familiar with",
									"according to a person who was briefed on the matter",
									"according to a person with direct knowledge",
									"according to one person who was briefed on the matter",
									"according to people briefed on the matter",
									"according to people close to",
									"according to people familiar with",
									"according to people who were briefed on the matter",
									"according to people with direct knowledge",
									"according to someone close to",
									"according to someone close to",
									"according to someone familiar with",
									"according to three people familiar with",
									"according to two people familiar with",
									"according to two people with direct knowledge",
									"an aide familiar with the situation",
									"an aide involved in the negotiations",
									"an anonymous source",
									"an official close to",
									"an official familiar with the situation",
									"an official involved in the negotiations",
									"asked not to be identified",
									"asked not to be named",
									"asked that I identify her by her first name",
									"asked that I identify her by her last name",
									"asked that I identify her only by her first name",
									"asked that I identify her only by her last name",
									"asked that I identify him by his first name",
									"asked that I identify him by his last name",
									"asked that I identify him only by his first name",
									"asked that I identify him only by his last name",
									"asked that her name not be used",
									"asked that his name not be used",
									"asked to be identified by her first name",
									"asked to be identified by her last name",
									"asked to be identified by his first name",
									"asked to be identified by his last name",
									"asked to be identified only by her first name",
									"asked to be identified only by her last name",
									"asked to be identified only by his first name",
									"asked to be identified only by his last name",
									"asked to remain anonymous",
									"chose to remain anonymous",
									"comment off the record",
									"declined to be identified",
									"declined to be named",
									"declined to give her first name",
									"declined to give her last name",
									"declined to give her name",
									"declined to give his first name",
									"declined to give his last name",
									"declined to give his name",
									"declined to provide her first name",
									"declined to provide her last name",
									"declined to provide his first name",
									"declined to provide his last name",
									"declined to speak for attribution",
									"did not want her first name used",
									"did not want her last name used",
									"did not want her name used",
									"did not want his first name used",
									"did not want his last name used",
									"did not want his name used",
									"did not want to be identified",
									"did not wish to be identified",
									"executive briefed on the matter",
									"insisted on anonymity",
									"not authorized to speak on the record",
									"official briefed on the matter",
									"officials briefed on the matter",
									"on a condition of anonymity",
									"on condition of anonymity",
									"on the condition of anonymity",
									"people briefed on the matter",
									"people familiar with the matter",
									"person briefed on the matter",
									"refused to be identified",
									"refused to be named",
									"refused to give her name",
									"refused to give his name",
									"refused to speak for attribution",
									"requested anonymity",
									"senior administration officials said",
									"source briefed on the matter",
									"sources briefed on the matter",
									"sources close to",
									"sources familiar with the matter",
									"sources said",
									"sources with specific knowledge",
									"speak off the record",
									"speaking off the record",
									"speaking on background",
									"spoke off the record",
									"spoke on background",
									"the source said",
									"would not speak for attribution",
									"wouldn't give her name",
									"wouldn't give his name",
									"sources familiar with"
									]

			// cory: skip if no text content
		    if (!node.textContent) { return false; }

		    // cory: skip is all whitespace
		    if (node.textContent.replace(/\s+/g,'').length === 0) { return false; }

		    // regular expression to isolate sentences that contain anonymity indicators 

		    for (var i = 0, len = anonPhrases.length; i < len; i++) {

		    		var TEXT_REGEX = new RegExp(".*"+anonPhrases[i]+".*");	

		    	if (node.textContent.match(TEXT_REGEX)) {

		    		return true; 

				}
			
			}

			return false;

		} // end of containsAnonymity

	    function addBlackOutClass(node) {
	    	// this is roughly what cory does, but I'm not sure if this is what I want. Instead of the whole node, I may just want to grab the sentence and add a span tag around it... if that is possible. 

	    	if (node.parentNode) {

	      		node.parentNode.classList.add(BLACKOUTCLASS);

	    	}
	    } // end of addBlackOutClass

	    var sentences = getRelevantNodes();
	    sentences.forEach(addBlackOutClass);

	} // end of blackOut
})();
