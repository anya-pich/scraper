import scrapy

class HorseSpider(scrapy.Spider):
	name = 'ike' # names need to be unique in a project

	def start_requests(self):
		urls = ['https://treehouse-projects.github.io/horse-land/index.html', 'https://treehouse-projects.github.io/horse-land/mustang.html']
		return [scrapy.Request(url=url, callback=self.parse) for url in urls]

	def parse(self, response):
		url = response.url
		page = url.split('/')[-1]
		filename = 'horses-%s' % page
		print('URL is: {}'.format(url))
		with open(filename, 'wb') as file:
			file.write(response.body)
		print('Saved file %s' % filename)