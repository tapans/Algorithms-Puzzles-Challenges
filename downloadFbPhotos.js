function downloadURL(url, name){
	link = document.createElement("a");
	link.download=name;
	link.href=url;
	link.click();
}


function downloadFbPhotos(){
	//download form photos page of fb

	element=document.getElementsByClassName("uiMediaThumbImg");
	numPics = element.length;
	for (i=0; i<numPics; i++){
		tempOuterHTML = element[i].outerHTML;
		encodedUrl = tempOuterHTML.substring(tempOuterHTML.indexOf("url(")+4, tempOuterHTML.indexOf(");"));
		url = encodedUrl.replace(/&amp;/g, '&');
		downloadURL(url, "pic"+i);
	}
}
