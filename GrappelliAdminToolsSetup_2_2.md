Grappelli is not only a skin for django.contrib.admin. It is a skin for django-admin-tools too. Thus grappelli has it's old bookmarks feature back. Additionally you can customize the order and hierarchy of the admin index and app\_index, add modules like "Recent Actions", and some more very nice features from admin-tools.

Basically it works like described in the admin-tools docu http://packages.python.org/django-admin-tools/ but some things are different or not (yet) supported when using admin-tools with grappelli...

_Note: We suggest to work around the current limitations (compared to the original feature set of admin\_tools). But patches to add admin\_tools features to grappelli are very welcome._

### special/additional css classes ###

  * collapse, open/close works as opt. in for dashboard modules. pretty much the same as with inlines.

  * Every direct children of the dashboard needs a css class named "column\_1", "column\_2" or "column\_3". This css class defines where the module is rendered.

```
#poject's/dashboard.py
class CustomIndexDashboard(Dashboard):
    
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        
        self.children.append(modules.LinkList(
            title=_('Media Management'),
            css_classes=['column_1'],
            children=[
                {
                    'title': _('Django FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                    'description': 'Python programming language rocks !',
                },
            ]
        ))
        
        self.children.append(modules.AppList(
            title=_('User...'),
            models=('django.contrib.auth.models.User',),
            css_classes=['column_1', 'collapse', 'open'],
        ))
        
        self.children.append(modules.AppList(
            title=_('Administration'),
            include_list=('django.contrib',),
            css_classes=['column_1', 'collapse', 'closed'],
        ))
        
        self.children.append(modules.AppList(
            title=_('Administration'),
            exclude_list=('django.contrib',),
            css_classes=['column_1', 'collapse', 'closed'],
        ))
        ...
```


### supported with grappelli ###
Here a list of all admin\_tools features that work with grappelli as skin:

  * admin/index and admin/app\_index customization
  * menu customization
  * bookmarks in menu

### not supported with grappelli ###
Features not (yet) implemented in grappelli. some of them will be implemented some of them not. we will announce new features asap.

  * drag&drop and delete of dashboard modules (pretty much all the user can customize isn't implemented)
  * Group class: templates ignore display setting (‘tabs’, ‘accordion’, ‘stacked’). looks always the same
  * fly out menus
  * ...