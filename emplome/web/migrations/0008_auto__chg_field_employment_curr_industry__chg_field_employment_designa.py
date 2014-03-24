# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Employment.curr_industry'
        db.alter_column(u'web_employment', 'curr_industry', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Employment.designation'
        db.alter_column(u'web_employment', 'designation', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Employment.skills'
        db.alter_column(u'web_employment', 'skills', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'JobPosting.mail_id'
        db.alter_column(u'web_jobposting', 'mail_id', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'JobPosting.specialization'
        db.alter_column(u'web_jobposting', 'specialization', self.gf('django.db.models.fields.CharField')(max_length=70, null=True))

        # Changing field 'JobPosting.job_location'
        db.alter_column(u'web_jobposting', 'job_location', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'JobPosting.role'
        db.alter_column(u'web_jobposting', 'role', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'JobPosting.job_title'
        db.alter_column(u'web_jobposting', 'job_title', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'JobPosting.function'
        db.alter_column(u'web_jobposting', 'function', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'JobPosting.education_req'
        db.alter_column(u'web_jobposting', 'education_req', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'JobPosting.job_details'
        db.alter_column(u'web_jobposting', 'job_details', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'JobPosting.phone'
        db.alter_column(u'web_jobposting', 'phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'JobPosting.nationality'
        db.alter_column(u'web_jobposting', 'nationality', self.gf('django.db.models.fields.CharField')(max_length=70, null=True))

        # Changing field 'JobPosting.name'
        db.alter_column(u'web_jobposting', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'JobPosting.skills'
        db.alter_column(u'web_jobposting', 'skills', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'JobPosting.industry'
        db.alter_column(u'web_jobposting', 'industry', self.gf('django.db.models.fields.CharField')(max_length=70))

        # Changing field 'UserProfile.city'
        db.alter_column(u'web_userprofile', 'city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'UserProfile.land_num'
        db.alter_column(u'web_userprofile', 'land_num', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'UserProfile.marital_status'
        db.alter_column(u'web_userprofile', 'marital_status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.user_type'
        db.alter_column(u'web_userprofile', 'user_type', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'UserProfile.religion'
        db.alter_column(u'web_userprofile', 'religion', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.current_location'
        db.alter_column(u'web_userprofile', 'current_location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'UserProfile.nationality'
        db.alter_column(u'web_userprofile', 'nationality', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'UserProfile.Alt_mail'
        db.alter_column(u'web_userprofile', 'Alt_mail', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'UserProfile.country'
        db.alter_column(u'web_userprofile', 'country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
    def backwards(self, orm):

        # Changing field 'Employment.curr_industry'
        db.alter_column(u'web_employment', 'curr_industry', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Employment.designation'
        db.alter_column(u'web_employment', 'designation', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Employment.skills'
        db.alter_column(u'web_employment', 'skills', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'JobPosting.mail_id'
        db.alter_column(u'web_jobposting', 'mail_id', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'JobPosting.specialization'
        db.alter_column(u'web_jobposting', 'specialization', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'JobPosting.job_location'
        db.alter_column(u'web_jobposting', 'job_location', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'JobPosting.role'
        db.alter_column(u'web_jobposting', 'role', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'JobPosting.job_title'
        db.alter_column(u'web_jobposting', 'job_title', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'JobPosting.function'
        db.alter_column(u'web_jobposting', 'function', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'JobPosting.education_req'
        db.alter_column(u'web_jobposting', 'education_req', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'JobPosting.job_details'
        db.alter_column(u'web_jobposting', 'job_details', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'JobPosting.phone'
        db.alter_column(u'web_jobposting', 'phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'JobPosting.nationality'
        db.alter_column(u'web_jobposting', 'nationality', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'JobPosting.name'
        db.alter_column(u'web_jobposting', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'JobPosting.skills'
        db.alter_column(u'web_jobposting', 'skills', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'JobPosting.industry'
        db.alter_column(u'web_jobposting', 'industry', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'UserProfile.city'
        db.alter_column(u'web_userprofile', 'city', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.land_num'
        db.alter_column(u'web_userprofile', 'land_num', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'UserProfile.marital_status'
        db.alter_column(u'web_userprofile', 'marital_status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'UserProfile.user_type'
        db.alter_column(u'web_userprofile', 'user_type', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'UserProfile.religion'
        db.alter_column(u'web_userprofile', 'religion', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'UserProfile.current_location'
        db.alter_column(u'web_userprofile', 'current_location', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'UserProfile.nationality'
        db.alter_column(u'web_userprofile', 'nationality', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'UserProfile.Alt_mail'
        db.alter_column(u'web_userprofile', 'Alt_mail', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'UserProfile.country'
        db.alter_column(u'web_userprofile', 'country', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))
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
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.education': {
            'Meta': {'object_name': 'Education'},
            'basic_edu': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'doctorate': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masters': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'pass_year_basic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pass_year_masters': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.employment': {
            'Meta': {'object_name': 'Employment'},
            'curr_industry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'exp_mnths': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exp_yrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.jobposting': {
            'Meta': {'object_name': 'JobPosting'},
            'company_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.CompanyProfile']"}),
            'company_profile': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'education_req': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'exp_req_max': ('django.db.models.fields.IntegerField', [], {}),
            'exp_req_min': ('django.db.models.fields.IntegerField', [], {}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'job_details': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'job_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mail_id': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'web.userprofile': {
            'Alt_mail': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'current_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_num': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['web']