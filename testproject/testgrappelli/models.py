from django.db import models

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class GrappelliRelatedFields(models.Model):
    char_test   = models.CharField(u"Test name", max_length=255)
    fk_test     = models.ForeignKey(Site, verbose_name=u"FK Autocomplete")
    gr_test     = models.ForeignKey(User, verbose_name=u"ForeignKey", null=True, blank=True)
    gr_m2m      = models.ManyToManyField(User, verbose_name=u"ManyToManyField", null=True, blank=True, related_name="m2m_user")
    m2m_test    = models.ManyToManyField(Site, verbose_name=u"M2M Autocomplete", blank=True, null=True, related_name="m2m_site")
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey("content_type", "object_id")

    def __unicode__(self):
        return u'%s' % self.fk_test

    class Meta:
        verbose_name = u'Related fields test'
        verbose_name_plural = u'Related fields tests'


class GrappelliEnhancedFields(models.Model):
    char_test   = models.CharField(u"CharField", max_length=255, blank=True)
    mce_test    = models.TextField(u"TinyMCE", blank=True)

    def __unicode__(self):
        return u'%s' % self.char_test

    class Meta:
        verbose_name = u'Enhanced fields test'
        verbose_name_plural = u'Enhanced fields tests'
