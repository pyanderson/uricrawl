import os
from jinja2 import Environment, FileSystemLoader


def normalize_text(list_extracted, colsize=50):
    text = (''.join(list_extracted).strip().replace('\n', ' ').
            replace('\t', ' ').replace('  ', ' '))
    words = text.split()
    result = []
    line = ""
    for w in words:
        if len(line) + len(w) > colsize:
            result.append(line[:-1])
            line = w + ' '
        else:
            line += w + ' '
    result.append(line[:-1])
    return result


def create_file(context, template):
    env = Environment(loader=FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'templates')))
    template = env.get_template(template)
    with open(context['filename'], 'w') as f:
        f.write(template.render(**context))


def gen_filename(pattern, context):
    return (pattern.replace('{{number}}', context['number'])
            .replace('{{title}}', context['title']))
