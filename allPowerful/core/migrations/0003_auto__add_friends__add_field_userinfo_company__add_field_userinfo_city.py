# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Friends'
        db.create_table(u'core_friends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_set', to=orm['core.UserInfo'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friends_set', to=orm['core.UserInfo'])),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Friends'])

        # Adding field 'UserInfo.company'
        db.add_column(u'core_userinfo', 'company',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserInfo.city'
        db.add_column(u'core_userinfo', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserInfo.expert_in'
        db.add_column(u'core_userinfo', 'expert_in',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'UserInfo.gender'
        db.add_column(u'core_userinfo', 'gender',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2),
                      keep_default=False)

        # Adding field 'UserInfo.birthday'
        db.add_column(u'core_userinfo', 'birthday',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserInfo.industry'
        db.add_column(u'core_userinfo', 'industry',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Friends'
        db.delete_table(u'core_friends')

        # Deleting field 'UserInfo.company'
        db.delete_column(u'core_userinfo', 'company')

        # Deleting field 'UserInfo.city'
        db.delete_column(u'core_userinfo', 'city')

        # Deleting field 'UserInfo.expert_in'
        db.delete_column(u'core_userinfo', 'expert_in')

        # Deleting field 'UserInfo.gender'
        db.delete_column(u'core_userinfo', 'gender')

        # Deleting field 'UserInfo.birthday'
        db.delete_column(u'core_userinfo', 'birthday')

        # Deleting field 'UserInfo.industry'
        db.delete_column(u'core_userinfo', 'industry')


    models = {
        u'core.friends': {
            'Meta': {'object_name': 'Friends'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friends_set'", 'to': u"orm['core.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_set'", 'to': u"orm['core.UserInfo']"})
        },
        u'core.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'avatar': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'expert_in': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_online': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'marital_status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['core']