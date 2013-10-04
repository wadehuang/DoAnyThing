# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'core_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('avatar', self.gf('django.db.models.fields.TextField')(default='')),
            ('marital_status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_online', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('expert_in', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('birthday', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('tel_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['UserProfile'])

        # Adding model 'Friends'
        db.create_table(u'core_friends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Friends'])

        # Adding model 'Item'
        db.create_table(u'core_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Item'])

        # Adding model 'UserAddress'
        db.create_table(u'core_useraddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('user_address', self.gf('django.db.models.fields.TextField')()),
            ('recipient_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('tel_number', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'core', ['UserAddress'])

        # Adding model 'Order'
        db.create_table(u'core_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')()),
            ('item_quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('is_send', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='')),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dispatching_cost', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('user_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UserAddress'])),
        ))
        db.send_create_signal(u'core', ['Order'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'core_userprofile')

        # Deleting model 'Friends'
        db.delete_table(u'core_friends')

        # Deleting model 'Item'
        db.delete_table(u'core_item')

        # Deleting model 'UserAddress'
        db.delete_table(u'core_useraddress')

        # Deleting model 'Order'
        db.delete_table(u'core_order')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.friends': {
            'Meta': {'object_name': 'Friends'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.item': {
            'Meta': {'object_name': 'Item'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.order': {
            'Meta': {'object_name': 'Order'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dispatching_cost': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_send': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']"}),
            'item_quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UserAddress']"})
        },
        u'core.useraddress': {
            'Meta': {'object_name': 'UserAddress'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tel_number': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'user_address': ('django.db.models.fields.TextField', [], {})
        },
        u'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'expert_in': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_online': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'marital_status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'tel_number': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['core']