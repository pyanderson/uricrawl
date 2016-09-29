# ============================================================================
#
#    Filename:  {{ filename }}
#
#         Url:  {{ url }}
#
{%- for line in description -%}
	{%- if loop.index == 1 %}
# Description:  {{ line }}
	{%- else %}
#	        {{ line }}
	{%- endif %}
{%- endfor %}
#
{%- for line in _input -%}
	{%- if loop.index == 1 %}
#       Input:  {{ line }}
	{%- else %}
# 	        {{ line }}
	{%- endif %}
{%- endfor %}
#
{%- for line in _output -%}
	{%- if loop.index == 1 %}
#      Output:  {{ line }}
	{%- else %}
#  	        {{ line }}
	{%- endif %}
{%- endfor %}
#
#     Version:  1.0
#     Created:  {{ created }}
#    Revision:  none
#    Compiler:  Python 3.4.0
#
#      Author:  {{ author }}
#
# ============================================================================

