import getpass
import os
import scrapy
from datetime import datetime
from slugify import slugify
from uricrawl.utils import normalize_text, create_file, gen_filename


class ProblemSpider(scrapy.Spider):
    name = 'problemspider'

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse,
                                 errback=self.errback_problem,
                                 dont_filter=True)

    def parse(self, response):
        context = {
            'number': response.css('title ::text').re_first(r'\d+'),
            'title': slugify(response.css('h1 ::text').extract_first()),
            'url': response.url,
            'description': normalize_text(
                response.css('div.description ::text').extract()),
            '_input': normalize_text(
                response.css('div.input ::text').extract()),
            '_output': normalize_text(
                response.css('div.output ::text').extract()),
            'created': datetime.now().strftime('%x %X'),
            'author': getpass.getuser()
        }
        filename = gen_filename(self.name_pattern, context)
        if self.default_template:
            dirname = os.path.dirname(__file__)
            if 'c' in self.programming_languages:
                context['filename'] = filename + '.c'
                create_file(context,
                            os.path.join(dirname, 'template.c'))
            if 'cpp' in self.programming_languages:
                context['filename'] = filename + '.cpp'
                create_file(context,
                            os.path.join(dirname, 'template.cpp'))
            if 'py' in self.programming_languages:
                context['filename'] = filename + '.py'
                create_file(context,
                            os.path.join(dirname, 'template.py'))
        for template in self.templates:
            _filename, file_extension = os.path.splitext(template)
            context['filename'] = filename + file_extension
            create_file(context, template)
        print('%s [%s] INFO: Code files for %s problem were generated.'
              % (datetime.now().strftime('%Y-%m-%d %X'), self.name,
                 context['number']))

    def errback_problem(self, failure):
        self.logger.error('Failure to crawl: %s' % failure.value.response.url)

# All problems for future
# class AllProblemsSpider(scrapy.Spider):
#     name = 'allproblemsspider'
#     start_urls = ['https://www.urionlinejudge.com.br/judge/en/problems/all']
#
#     def parse(self, response):
#         for problem in response.css('tbody tr'):
#             if problem.css('td ::attr(colspan)'):
#                 break
#             problem_url = problem.css('td.id > a ::attr(href)').
#             extract_first()
#             category_url = problem.css('td.large > a::attr(href)').
#             extract()[1]
#             number = problem.css('td.id > a ::text').extract_first()
#             info = problem.css('td.large > a ::text').extract()
#             name, category = info[0], info[1]
#             solved = problem.css('td.small ::text').re_first(r'\d+.?\d*')
#             level = problem.css('td.tiny ::text').extract()[1]
#             print('{0:4} {1:35} {2:35} {3:6} {4:1}'.format(
#                 number, name, category, solved, level))
#             print(problem_url, category_url)
#         next_page = response.css('li.next > a::attr(href)').extract_first()
#         if next_page:
#             yield scrapy.Request(
#                 'https://www.urionlinejudge.com.br' + next_page,
#                 callback=self.parse)
