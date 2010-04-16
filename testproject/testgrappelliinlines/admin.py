# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from django.conf import settings

from testgrappelli.models import *
from testgrappelliinlines.models import *

# Related Fields  -----------------------------------------------------------------------------------

# Related Fields / Tabular

class GrappelliRelatedFieldsTabularInline(admin.TabularInline):
    model = GrappelliRelatedFieldsInline
    classes = ('ui-collapsible-all-opened', )
    allow_add = True
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                'fk_test', 'gr_test', 'gr_m2m', 'content_type', 'object_id',
            )
        }),
    )

class GrappelliRelatedFieldsTabularTestAdmin(admin.ModelAdmin):
    list_display = ('char_test',)
    inlines = [GrappelliRelatedFieldsTabularInline]

    class Media:
        verbose_name = u'Related fields test'
        verbose_name_plural = u'Related fields tests'

admin.site.register(GrappelliRelatedFieldsTabularTest, GrappelliRelatedFieldsTabularTestAdmin)

# Enhanced Fields  -----------------------------------------------------------------------------------

# Enhanced Fields / Tabular

class GrappelliEnhancedFieldsTabularInline(admin.TabularInline):
    model = GrappelliEnhancedFieldsInline
    classes = ('ui-collapsible-all-opened', )
    allow_add = True
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                'slug_test', 'slug_test2', 'mce_test', 
            )
        }),
    )

class GrappelliEnhancedFieldsTabularTestAdmin(admin.ModelAdmin):
    list_display = ('char_test',)
    inlines = [GrappelliEnhancedFieldsTabularInline]

    class Media:
        verbose_name = u'Enhanced fields test'
        verbose_name_plural = u'Enhanced fields tests'
        js = [
            settings.ADMIN_MEDIA_PREFIX + 'jquery/tinymce/jscripts/tiny_mce/tiny_mce.js',
            settings.ADMIN_MEDIA_PREFIX + 'tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(GrappelliEnhancedFieldsTabularTest, GrappelliEnhancedFieldsTabularTestAdmin)
