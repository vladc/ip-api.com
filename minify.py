import codecs, json, os
from urllib2 import Request, urlopen
from urllib import urlencode

replacements = {
	'contentDiv': 'c',
	'headerClass': 'h',
	'footerClass': 'f',
	'submitText': 'b',
	'resultDiv': 'r',
	'resultText': 'e',
	'geoDiv': 'g',
	'headerText': 't',
	'queryLabel': 'l',
	'resultTbody': 'o',
	'docsDiv': 'd',
	'translationsDiv': 's',
	'ajax(': 'a(',
	'getRequest': 'gr',
	'jsonParse': 'j',
	'byId(': 'x(',
	'newElement(': 'ne(',
	'updateElement(': 'o(',
	'updateTable(': 'z(',
	'makeClickable(': 'ma(',
	'ie8_fix(': 'ix(',
	'ie8_fix_div': 'i8',
	'nullFunction': 'nf',
	'setMap': 'ms',
	'unSetMap': 'mu',
	'MapOpacity': 'mo',
	'get_internal': 'gi',
	'get_dns': 'gd',
	'delayed_dns_internal': 'di',
	'getBrowserGeo': 'g',
	'query(': 'q(',
	'currentQuery': 'cq',
	'setLanguage': 'sl',
	'getLanguage': 'gl',
	'defaultLanguage': 'dl',
	'translations': 'lo',
	'protocol': 'p',
	'myIp': 'mi',
	'currentLanguage': 'cl',
	'init(': 'k(',
	'footerLanguages': 'i',
	'contact(': 'cn('
}

f = codecs.open('source.html', 'r', 'utf-8')
contents = f.read()
f.close()

for what, to in replacements.iteritems():
	contents = contents.replace(what, to)

post = {
	'code': contents.encode('utf-8'),
	'options[removeEmptyAttributes]': 'false',
	'options[useShortDoctype]': 'true',
	'options[removeEmptyElements]': 'false',
	'options[customAttrAssign]': '',
	'options[removeScriptTypeAttributes]': 'true',
	'options[collapseBooleanAttributes]': 'false',
	'options[removeCommentsFromCDATA]': 'false',
	'options[removeComments]': 'false',
	'options[minifyCSS]': 'true',
	'options[keepClosingSlash]': 'false',
	'options[minifyJS]': 'true',
	'options[ignoreCustomComments]': '',
	'options[customAttrCollapse]': '',
	'options[removeStyleLinkTypeAttributes]': 'true',
	'options[minifyURLs]': 'true',
	'options[maxLineLength]': '',
	'options[removeAttributeQuotes]': 'false',
	'options[removeCDATASectionsFromCDATA]': 'false',
	'options[preserveLineBreaks]': 'false',
	'options[removeOptionalTags]': 'false',
	'options[processScripts]': '',
	'options[caseSensitive]': 'true',
	'options[removeIgnored]': 'false',
	'options[conservativeCollapse]': 'false',
	'options[removeRedundantAttributes]': 'true',
	'options[customAttrSurround]': '',
	'options[collapseWhitespace]': 'true',
	'options[preventAttributesEscaping]': 'true',
	'options[lint]': 'false'
}

req = urlopen(Request('http://refresh-sf.herokuapp.com/html/', data=urlencode(post)))
contents = json.loads(req.read())['code']

contents += "<!-- https://github.com/vladc/ip-api.com -->"
out = codecs.open('index.html', 'w', 'utf-8')
out.write(contents)
out.close()

print 'original:', os.stat('source.html').st_size, 'minified:', os.stat('index.html').st_size
