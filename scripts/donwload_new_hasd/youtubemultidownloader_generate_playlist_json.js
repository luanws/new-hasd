var aArray = document.querySelectorAll('a')
aArray = Array.prototype.slice.call(aArray)
aArray = aArray.filter(a => a.text === 'MP4 720P')
var urls = aArray.map(a => a.href)
JSON.stringify(urls)