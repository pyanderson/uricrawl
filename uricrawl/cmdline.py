import sys
import os
import argparse
from scrapy.crawler import CrawlerProcess
from uricrawl.spiders import ProblemSpider


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description='A tool do download problems from URI(Uri Online Judge)'
        ' and generate code files.',
        usage='uricrawl [problems separated by space] {opcional} -t or '
        '--template [filepaths of templates separated by space]'
    )
    parser.add_argument(
        'problems',
        metavar='P',
        nargs='+',
        type=int,
        help='List of problems to download.',
    )
    parser.add_argument(
        '-t', '--template',
        nargs='+',
        help='List your templates to gen code files. (Check docs to context)'
    )
    parser.add_argument(
        '-nd', '--no-default',
        action='store_true',
        help='Disable c, c++ and python default templates.'
    )
    parser.add_argument(
        '-l', '--language',
        default='en',
        choices=['en', 'pt', 'es'],
        help='Choose language used to render inside code files.'
    )
    parser.add_argument(
        '-pl', '--programming-language',
        nargs='+',
        default=['c', 'cpp', 'py'],
        choices=['c', 'cpp', 'py'],
        help='Choose the templates programming languages.'
    )
    parser.add_argument(
        '-np', '--name-pattern',
        action='store',
        default='{{number}}-{{title}}',
        help='Define the pattern used to name your code files.'
    )
    if len(argv) == 0:
        parser.print_help()
        return
    args = parser.parse_args(argv)
    # normalize language
    language = ''
    if args.language != 'pt':
        language = '_' + args.language
    # generate start urls for all problems
    start_urls = []
    for problem in args.problems:
        start_urls.append('https://www.urionlinejudge.com.br/'
                          'repository/UOJ_%s%s.html' % (str(problem),
                                                        language))
    # check templates
    templates = []
    if args.template:
        for template in args.template:
            template = os.path.expanduser(template)
            if os.path.isfile(template):
                templates.append(os.path.abspath(template))
    elif args.no_default:
        print('Must be set at least one template.')
        return
    # crawler configurations
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'LOG_LEVEL': 'ERROR'
    })
    process.crawl(
        ProblemSpider,
        start_urls=start_urls,
        default_template=not args.no_default,
        name_pattern=args.name_pattern,
        programming_languages=args.programming_language,
        templates=templates
    )
    # fun.start()
    process.start()
