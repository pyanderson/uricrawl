import os
import sys
from jinja2 import Environment, FileSystemLoader


def cast_for_python2(x):
    return x.encode('ascii', 'replace')


def normalize_text(list_extracted, colsize=50):
    text = (''.join(list_extracted).strip().replace('\n', ' ').
            replace('\t', ' ').replace('  ', ' '))
    words = text.split()
    result = []
    line = ""
    if sys.version_info[0] > 2:
        cast = str
    else:
        cast = cast_for_python2
    for w in words:
        w = cast(w)
        if len(line) + len(w) > colsize:
            result.append(line[:-1])
            line = w + ' '
        else:
            line += w + ' '
    result.append(line[:-1])
    return result


def create_file(context, template):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template)))
    template = env.get_template(os.path.basename(template))
    with open(context['filename'], 'w') as f:
        f.write(template.render(**context))


def gen_filename(pattern, context):
    return (pattern.replace('{{number}}', context['number'])
            .replace('{{title}}', context['title']))
