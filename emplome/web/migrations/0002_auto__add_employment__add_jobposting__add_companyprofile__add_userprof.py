# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employment'
        db.create_table(u'web_employment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('land_num', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('exp_mnths', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('salary', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('industry_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('curr_industry', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Employment'])

        # Adding model 'JobPosting'
        db.create_table(u'web_jobposting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('posting_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('exp_req', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['JobPosting'])

        # Adding model 'CompanyProfile'
        db.create_table(u'web_companyprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('employer_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('industry_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mobile', self.gf('django.db.models.fields.IntegerField')()),
            ('land_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['CompanyProfile'])

        # Adding model 'UserProfile'
        db.create_table(u'web_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('curr_loc', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('mob', self.gf('django.db.models.fields.IntegerField')()),
            ('land_num', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('mail_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('Alt_mail', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['UserProfile'])

        # Adding model 'Education'
        db.create_table(u'web_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('basic_edu', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('basic_spl', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('masters', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('master_spl', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('doctorate', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Education'])

    def backwards(self, orm):
        # Deleting model 'Employment'
        db.delete_table(u'web_employment')

        # Deleting model 'JobPosting'
        db.delete_table(u'web_jobposting')

        # Deleting model 'CompanyProfile'
        db.delete_table(u'web_companyprofile')

        # Deleting model 'UserProfile'
        db.delete_table(u'web_userprofile')

        # Deleting model 'Education'
        db.delete_table(u'web_education')

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
        u'web.companyprofile': {
            'Meta': {'object_name': 'CompanyProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'employer_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'land_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.education': {
            'Meta': {'object_name': 'Education'},
            'basic_edu': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'basic_spl': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'doctorate': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master_spl': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'masters': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.employment': {
            'Meta': {'object_name': 'Employment'},
            'curr_industry': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'exp_mnths': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'land_num': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'salary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.jobposting': {
            'Meta': {'object_name': 'JobPosting'},
            'exp_req': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'posting_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'web.userprofile': {
            'Alt_mail': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'curr_loc': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_num': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'mail_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'mob': ('django.db.models.fields.IntegerField', [], {}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['web']