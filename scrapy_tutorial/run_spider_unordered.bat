SET URL1="https://www.glassdoor.com/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm"

del /f temp.json
scrapy crawl count -a url=%URL1%
scrapy crawl fetch -o temp.json
copy /y temp.json result_unordered.json

del /f temp.json
