# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Employment.land_num'
        db.delete_column(u'web_employment', 'land_num')

        # Adding field 'Employment.exp_yrs'
        db.add_column(u'web_employment', 'exp_yrs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Employment.exp_mnths'
        db.alter_column(u'web_employment', 'exp_mnths', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Deleting field 'JobPosting.skills'
        db.delete_column(u'web_jobposting', 'skills')

        # Deleting field 'JobPosting.job_type'
        db.delete_column(u'web_jobposting', 'job_type')

        # Deleting field 'JobPosting.exp_req'
        db.delete_column(u'web_jobposting', 'exp_req')

        # Deleting field 'JobPosting.last_date'
        db.delete_column(u'web_jobposting', 'last_date')

        # Deleting field 'JobPosting.posting_date'
        db.delete_column(u'web_jobposting', 'posting_date')

        # Adding field 'JobPosting.job_title'
        db.add_column(u'web_jobposting', 'job_title',
                      self.gf('django.db.models.fields.CharField')(default=-12, max_length=20),
                      keep_default=False)

        # Adding field 'JobPosting.ref_code'
        db.add_column(u'web_jobposting', 'ref_code',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=10),
                      keep_default=False)

        # Adding field 'JobPosting.job_details'
        db.add_column(u'web_jobposting', 'job_details',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobPosting.document'
        db.add_column(u'web_jobposting', 'document',
                      self.gf('django.db.models.fields.files.FileField')(max_length=20000, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'CompanyProfile.employer_name'
        db.delete_column(u'web_companyprofile', 'employer_name')

        # Deleting field 'UserProfile.mob'
        db.delete_column(u'web_userprofile', 'mob')

        # Deleting field 'UserProfile.curr_loc'
        db.delete_column(u'web_userprofile', 'curr_loc')

        # Adding field 'UserProfile.current_location'
        db.add_column(u'web_userprofile', 'current_location',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.mobile'
        db.add_column(u'web_userprofile', 'mobile',
                      self.gf('django.db.models.fields.IntegerField')(default=432),
                      keep_default=False)

        # Adding field 'Education.resume'
        db.add_column(u'web_education', 'resume',
                      self.gf('django.db.models.fields.files.FileField')(max_length=20000, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Employment.land_num'
        raise RuntimeError("Cannot reverse this migration. 'Employment.land_num' and its values cannot be restored.")
        # Deleting field 'Employment.exp_yrs'
        db.delete_column(u'web_employment', 'exp_yrs')


        # User chose to not deal with backwards NULL issues for 'Employment.exp_mnths'
        raise RuntimeError("Cannot reverse this migration. 'Employment.exp_mnths' and its values cannot be restored.")
        # Adding field 'JobPosting.skills'
        db.add_column(u'web_jobposting', 'skills',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'JobPosting.job_type'
        raise RuntimeError("Cannot reverse this migration. 'JobPosting.job_type' and its values cannot be restored.")
        # Adding field 'JobPosting.exp_req'
        db.add_column(u'web_jobposting', 'exp_req',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobPosting.last_date'
        db.add_column(u'web_jobposting', 'last_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobPosting.posting_date'
        db.add_column(u'web_jobposting', 'posting_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'JobPosting.job_title'
        db.delete_column(u'web_jobposting', 'job_title')

        # Deleting field 'JobPosting.ref_code'
        db.delete_column(u'web_jobposting', 'ref_code')

        # Deleting field 'JobPosting.job_details'
        db.delete_column(u'web_jobposting', 'job_details')

        # Deleting field 'JobPosting.document'
        db.delete_column(u'web_jobposting', 'document')


        # User chose to not deal with backwards NULL issues for 'CompanyProfile.employer_name'
        raise RuntimeError("Cannot reverse this migration. 'CompanyProfile.employer_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'UserProfile.mob'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.mob' and its values cannot be restored.")
        # Adding field 'UserProfile.curr_loc'
        db.add_column(u'web_userprofile', 'curr_loc',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'UserProfile.current_location'
        db.delete_column(u'web_userprofile', 'current_location')

        # Deleting field 'UserProfile.mobile'
        db.delete_column(u'web_userprofile', 'mobile')

        # Deleting field 'Education.resume'
        db.delete_column(u'web_education', 'resume')

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
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.employment': {
            'Meta': {'object_name': 'Employment'},
            'curr_industry': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'exp_mnths': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exp_yrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.jobposting': {
            'Meta': {'object_name': 'JobPosting'},
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_details': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ref_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'web.userprofile': {
            'Alt_mail': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'current_location': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_num': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'mail_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['web']