# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JobSeekerProfile'
        db.create_table(u'web_jobseekerprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.UserProfile'])),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('current_location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('alt_mail', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=20000, null=True, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
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

        # Deleting field 'Job.user'
        db.delete_column(u'web_job', 'user_id')

        # Adding field 'Job.recruiter'
        db.add_column(u'web_job', 'recruiter',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'UserProfile.gender'
        db.delete_column(u'web_userprofile', 'gender')

        # Deleting field 'UserProfile.photo'
        db.delete_column(u'web_userprofile', 'photo')

        # Deleting field 'UserProfile.religion'
        db.delete_column(u'web_userprofile', 'religion')

        # Deleting field 'UserProfile.dob'
        db.delete_column(u'web_userprofile', 'dob')

        # Deleting field 'UserProfile.age'
        db.delete_column(u'web_userprofile', 'age')

        # Deleting field 'UserProfile.marital_status'
        db.delete_column(u'web_userprofile', 'marital_status')

        # Deleting field 'UserProfile.current_location'
        db.delete_column(u'web_userprofile', 'current_location')

        # Deleting field 'UserProfile.alt_mail'
        db.delete_column(u'web_userprofile', 'alt_mail')

        # Deleting field 'UserProfile.nationality'
        db.delete_column(u'web_userprofile', 'nationality')

        # Deleting field 'UserProfile.company'
        db.delete_column(u'web_userprofile', 'company_id')

        # Removing M2M table for field applied_jobs on 'UserProfile'
        db.delete_table('web_userprofile_applied_jobs')

    def backwards(self, orm):
        # Deleting model 'JobSeekerProfile'
        db.delete_table(u'web_jobseekerprofile')

        # Removing M2M table for field applied_jobs on 'JobSeekerProfile'
        db.delete_table('web_jobseekerprofile_applied_jobs')

        # Deleting model 'RecruiterProfile'
        db.delete_table(u'web_recruiterprofile')


        # User chose to not deal with backwards NULL issues for 'Job.user'
        raise RuntimeError("Cannot reverse this migration. 'Job.user' and its values cannot be restored.")
        # Deleting field 'Job.recruiter'
        db.delete_column(u'web_job', 'recruiter_id')


        # User chose to not deal with backwards NULL issues for 'UserProfile.gender'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.gender' and its values cannot be restored.")
        # Adding field 'UserProfile.photo'
        db.add_column(u'web_userprofile', 'photo',
                      self.gf('django.db.models.fields.files.FileField')(max_length=20000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.religion'
        db.add_column(u'web_userprofile', 'religion',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.dob'
        db.add_column(u'web_userprofile', 'dob',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.age'
        db.add_column(u'web_userprofile', 'age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.marital_status'
        db.add_column(u'web_userprofile', 'marital_status',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.current_location'
        db.add_column(u'web_userprofile', 'current_location',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.alt_mail'
        db.add_column(u'web_userprofile', 'alt_mail',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'UserProfile.nationality'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.nationality' and its values cannot be restored.")
        # Adding field 'UserProfile.company'
        db.add_column(u'web_userprofile', 'company',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.CompanyProfile'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field applied_jobs on 'UserProfile'
        db.create_table(u'web_userprofile_applied_jobs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'web.userprofile'], null=False)),
            ('job', models.ForeignKey(orm[u'web.job'], null=False))
        ))
        db.create_unique(u'web_userprofile_applied_jobs', ['userprofile_id', 'job_id'])

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
            'certificate': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'doctrate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'masters': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pass_year_basic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pass_year_masters': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            'resume_text': ('django.db.models.fields.CharField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'resume_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'userprofile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
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
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'userprofile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.UserProfile']"})
        },
        u'web.job': {
            'Meta': {'object_name': 'Job'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1500', 'null': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
            'education_req': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'exp_req_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exp_req_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_post': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'web.jobseekerprofile': {
            'Meta': {'object_name': 'JobSeekerProfile'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alt_mail': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'applied_jobs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web.Job']", 'symmetrical': 'False'}),
            'current_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'}),
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