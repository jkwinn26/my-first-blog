from django import template 
from django.core import urlresolvers
from django.contrib.auth.models import Group 
import re

register = template.Library()

@register.simple_tag(takes_context=True)
def is_app(context, app_name, return_value=' active', **kwargs):
    resolve_str = str(urlresolvers.resolve(context.get('request').path))
    #ResolverMatch(func=blog.views.post_detail, args=(), kwargs={'pk': u'2'}, url_name=post_detail, app_name=None, namespaces=[])
    m = re.search('func=(\w+)\.', resolve_str)
    return 'active' if m.group(1) == app_name else ''
    
#@register.simple_tag(takes_context=False)
#def test(user):
#    return user.first_name + " " + user.last_name + "(" + str(user.groups) + ")"
#    return user.groups.all()
    
#@register.filter(name='in_groups')
#def in_groups(user, group_name_csv):
#    group_name_list = [group_name_csv.strip() for group_name_csv in group_name_csv.split(',')]
#    groups = []
#    for group_name in group_name_list:
#        groups.append(Group.objects.get(name=group_name))
##    for group in user.groups.all():
##        if any(group in groups):
##            return True
##    return False
#    return True if any(group in groups for group in user.groups.all()) else False)