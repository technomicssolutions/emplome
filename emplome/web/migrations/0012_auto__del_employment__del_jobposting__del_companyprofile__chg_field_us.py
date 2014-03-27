# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Employment'
        db.delete_table(u'web_employment')

        # Deleting model 'JobPosting'
        db.delete_table(u'web_jobposting')

        # Deleting model 'CompanyProfile'
        db.delete_table(u'web_companyprofile')


        # Changing field 'UserProfile.gender'
        db.alter_column(u'web_userprofile', 'gender', self.gf('django.db.models.fields.CharField')(max_length=7))

        # Changing field 'Education.masters'
        db.alter_column(u'web_education', 'masters', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Education.doctorate'
        db.alter_column(u'web_education', 'doctorate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
    def backwards(self, orm):
        # Adding model 'Employment'
        db.create_table(u'web_employment', (
            ('curr_industry', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('salary', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('exp_mnths', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exp_yrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Employment'])

        # Adding model 'JobPosting'
        db.create_table(u'web_jobposting', (
            ('education_req', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('mail_id', self.gf('django.db.models.fields.CharField')(max_length=70)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specialization', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('job_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('company_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.CompanyProfile'])),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=20000, null=True, blank=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('exp_req_min', self.gf('django.db.models.fields.IntegerField')()),
            ('exp_req_max', self.gf('django.db.models.fields.IntegerField')()),
            ('job_details', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('ref_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('company_profile', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'web', ['JobPosting'])

        # Adding model 'CompanyProfile'
        db.create_table(u'web_companyprofile', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('industry_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'web', ['CompanyProfile'])


        # Changing field 'UserProfile.gender'
        db.alter_column(u'web_userprofile', 'gender', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Education.masters'
        db.alter_column(u'web_education', 'masters', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Education.doctorate'
        db.alter_column(u'web_education', 'doctorate', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))
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
        u'web.education': {
            'Meta': {'object_name': 'Education'},
            'basic_edu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'certificate': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'doctorate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masters': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pass_year_basic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pass_year_masters': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'resume_text': ('django.db.models.fields.CharField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'resume_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'userprofile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'alt_mail': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'current_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_num': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['web']