# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompanyProfile'
        db.create_table(u'web_companyprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('industry_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['CompanyProfile'])

        # Adding model 'Job'
        db.create_table(u'web_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recruiter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.CompanyProfile'], null=True, blank=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ref_code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('job_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('education_req', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('specialization', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mail_id', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('posting_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('exp_req_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('exp_req_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'web', ['Job'])

        # Adding model 'Employment'
        db.create_table(u'web_employment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exp_yrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('exp_mnths', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('salary', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('curr_industry', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Employment'])

        # Adding model 'Education'
        db.create_table(u'web_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('basic_edu', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pass_year_basic', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('masters', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('pass_year_masters', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('doctrate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('resume_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('resume', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('resume_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('certificate', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Education'])

        # Adding model 'UserProfile'
        db.create_table(u'web_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('land_num', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'web', ['UserProfile'])

        # Adding model 'JobSeekerProfile'
        db.create_table(u'web_jobseekerprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alt_mail', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('education', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Education'], null=True, blank=True)),
            ('employment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Employment'], null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['JobSeekerProfile'])

        # Adding M2M table for field applied_jobs on 'JobSeekerProfile'
        db.create_table(u'web_jobseekerprofile_applied_jobs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('jobseekerprofile', models.ForeignKey(orm[u'web.jobseekerprofile'], null=False)),
            ('job', models.ForeignKey(orm[u'web.job'], null=False))
        ))
        db.create_unique(u'web_jobseekerprofile_applied_jobs', ['jobseekerprofile_id', 'job_id'])

        # Adding model 'RecruiterProfile'
        db.create_table(u'web_recruiterprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.CompanyProfile'], null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['RecruiterProfile'])

        # Adding model 'SuccessStory'
        db.create_table(u'web_successstory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('story', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'web', ['SuccessStory'])

        # Adding model 'Recommendation'
        db.create_table(u'web_recommendation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recommendation_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Recommendation'])

    def backwards(self, orm):
        # Deleting model 'CompanyProfile'
        db.delete_table(u'web_companyprofile')

        # Deleting model 'Job'
        db.delete_table(u'web_job')

        # Deleting model 'Employment'
        db.delete_table(u'web_employment')

        # Deleting model 'Education'
        db.delete_table(u'web_education')

        # Deleting model 'UserProfile'
        db.delete_table(u'web_userprofile')

        # Deleting model 'JobSeekerProfile'
        db.delete_table(u'web_jobseekerprofile')

        # Removing M2M table for field applied_jobs on 'JobSeekerProfile'
        db.delete_table('web_jobseekerprofile_applied_jobs')

        # Deleting model 'RecruiterProfile'
        db.delete_table(u'web_recruiterprofile')

        # Deleting model 'SuccessStory'
        db.delete_table(u'web_successstory')

        # Deleting model 'Recommendation'
        db.delete_table(u'web_recommendation')

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
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.education': {
            'Meta': {'object_name': 'Education'},
            'basic_edu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'certificate': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'doctrate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masters': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pass_year_basic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pass_year_masters': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resume_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resume_title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.employment': {
            'Meta': {'object_name': 'Employment'},
            'curr_industry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'exp_mnths': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exp_yrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'web.job': {
            'Meta': {'object_name': 'Job'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'education_req': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'exp_req_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exp_req_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'mail_id': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'posting_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'recruiter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'ref_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'web.jobseekerprofile': {
            'Meta': {'object_name': 'JobSeekerProfile'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alt_mail': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'applied_jobs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web.Job']", 'symmetrical': 'False'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Education']", 'null': 'True', 'blank': 'True'}),
            'employment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Employment']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'web.recommendation': {
            'Meta': {'object_name': 'Recommendation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recommendation_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'web.recruiterprofile': {
            'Meta': {'object_name': 'RecruiterProfile'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.successstory': {
            'Meta': {'object_name': 'SuccessStory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'story': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'web.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_num': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['web']