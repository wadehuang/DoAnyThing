# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dispatching'
        db.create_table(u'core_dispatching', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Dispatching'])

        # Adding model 'OrderDetails'
        db.create_table(u'core_orderdetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Order'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item'])),
            ('item_quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('comment', self.gf('django.db.models.fields.TextField')(default=True)),
        ))
        db.send_create_signal(u'core', ['OrderDetails'])

        # Deleting field 'Order.item'
        db.delete_column(u'core_order', 'item_id')

        # Deleting field 'Order.item_quantity'
        db.delete_column(u'core_order', 'item_quantity')

        # Adding field 'Order.dispatching_time'
        db.add_column(u'core_order', 'dispatching_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2013, 10, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'Order.order_from_time'
        db.add_column(u'core_order', 'order_from_time',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 10, 5, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Order.order_to_time'
        db.add_column(u'core_order', 'order_to_time',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 10, 5, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.user_type'
        db.add_column(u'core_userprofile', 'user_type',
                      self.gf('django.db.models.fields.IntegerField')(default=3),
                      keep_default=False)


        # Changing field 'UserProfile.tel_number'
        db.alter_column(u'core_userprofile', 'tel_number', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting model 'Dispatching'
        db.delete_table(u'core_dispatching')

        # Deleting model 'OrderDetails'
        db.delete_table(u'core_orderdetails')


        # User chose to not deal with backwards NULL issues for 'Order.item'
        raise RuntimeError("Cannot reverse this migration. 'Order.item' and its values cannot be restored.")
        # Adding field 'Order.item_quantity'
        db.add_column(u'core_order', 'item_quantity',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'Order.dispatching_time'
        db.delete_column(u'core_order', 'dispatching_time')

        # Deleting field 'Order.order_from_time'
        db.delete_column(u'core_order', 'order_from_time')

        # Deleting field 'Order.order_to_time'
        db.delete_column(u'core_order', 'order_to_time')

        # Deleting field 'UserProfile.user_type'
        db.delete_column(u'core_userprofile', 'user_type')


        # User chose to not deal with backwards NULL issues for 'UserProfile.tel_number'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.tel_number' and its values cannot be restored.")

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
        u'core.dispatching': {
            'Meta': {'object_name': 'Dispatching'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
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
            'dispatching_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_send': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_from_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {}),
            'order_to_time': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UserAddress']"})
        },
        u'core.orderdetails': {
            'Meta': {'object_name': 'OrderDetails'},
            'comment': ('django.db.models.fields.TextField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']"}),
            'item_quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Order']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
            'tel_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_type': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        }
    }

    complete_apps = ['core']