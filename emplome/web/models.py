from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

USER_TYPE = (
	('admin', 'Admin'),
	('employer', 'Employer'),
	('job_seeker', 'Job Seeker'),
)
GENDER = (
	('male', 'Male'),
	('female', 'Female'),
)

COUNTRY_CHOICES = (
    ('Afghanistan', 'Afghanistan'),
    ('Akrotiri', 'Akrotiri'),
    ('Albania','Albania'),
    ('Algeria','Algeria'),
    ('American Samoa','American Samoa'),
    ('Andorra','Andorra'),
    ('Anguilla','Anguilla'),
    ('Antarctica','Antarctica'),
    ('Antigua and Barbuda','Antigua and Barbuda'),
    ('Argentina','Argentina'),
    ('Armenia','Armenia'),
    ('Aruba','Aruba'),
    ('Ashmore and Cartier Islands','Ashmore and Cartier Islands'),
    ('Australia','Australia'),
    ('Austria','Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas','Bahamas'),
    ('Bahrain','Bahrain'),
    ('Bangladesh','Bangladesh'),
    ('Barbados','Barbados'),
    ('Bassas da India','Bassas da India'),
    ('Belarus','Belarus'),
    ('Belgium','Belgium'),
    ('Belize','Belize'),
    ('Benin','Benin'),
    ('Bermuda','Bermuda'),
    ('Bhutan','Bhutan'),
    ('Bolivia','Bolivia'),
    ('Bosnia and Herzegovina','Bosnia and Herzegovina'),
    ('Botswana','Botswana'),
    ('Bouvet Island','Bouvet Island'),
    ('Brazil','Brazil'),
    ('British Indian Ocean Territory','British Indian Ocean Territory'),
    ('British Virgin Islands','British Virgin Islands'),
    ('Brunei','Brunei'),
    ('Bulgaria','Bulgaria'),
    ('Burkina Faso','Burkina Faso'),
    ('Burma','Burma'),
    ('Burundi','Burundi'),
    ('Cambodia','Cambodia'),
    ('Cameroon','Cameroon'),
    ('Canada','Canada'),
    ('Cape Verde','Cape Verde'),
    ('Cayman Islands','Cayman Islands'),
    ('Central African Republic','Central African Republic'),
    ('Chad','Chad'),
    ('Chile','Chile'),
    ('China','China'),
    ('Christmas Island','Christmas Island'),
    ('Clipperton Island','Clipperton Island'),
    ('Cocos (Keeling) Islands','Cocos (Keeling) Islands'),
    ('Colombia','Colombia'),
    ('Comoros','Comoros'),
    ('Congo, Democratic Republic of the','Congo, Democratic Republic of the'),
    ('Congo, Republic of the','Congo, Republic of the'),
    ('Cook Islands','Cook Islands'),
    ('Coral Sea Islands','Coral Sea Islands'),
    ('Costa Rica','Costa Rica'),
    ( "Cote d'Ivoire", "Cote d'Ivoire"),
    ('Croatia','Croatia'),
    ('Cuba','Cuba'),
    ('Cyprus','Cyprus'),
    ('Czech Republic','Czech Republic'),
    ('Denmark','Denmark'),
    ('Dhekelia','Dhekelia'),
    ('Djibouti','Djibouti'),
    ('Dominica','Dominica'),
    ('Dominican Republic','Dominican Republic'),
    ('Ecuador','Ecuador'),
    ('Egypt','Egypt'),
    ('El Salvador','El Salvador'),
    ('Equatorial Guinea','Equatorial Guinea'),
    ('Eritrea','Eritrea'),
    ('Estonia','Estonia'),
    ('Ethiopia','Ethiopia'),
    ('Europa Island','Europa Island'),
    ('Falkland Islands (Islas Malvinas)','Falkland Islands (Islas Malvinas)'),
    ('Faroe Islands','Faroe Islands'),
    ('Fiji','Fiji'),
    ('Finland','Finland'),
    ('France','France'),
    ('French Guiana','French Guiana'),
    ('French Polynesia','French Polynesia'),
    ('French Southern and Antarctic Lands','French Southern and Antarctic Lands'),
    ('Gabon','Gabon'),
    ('Gambia, The','Gambia, The'),
    ('Gaza Strip','Gaza Strip'),
    ('Georgia','Georgia'),
    ('Germany','Germany'),
    ('Ghana','Ghana'),
    ('Gibraltar','Gibraltar'),
    ('Glorioso Islands','Glorioso Islands'),
    ('Greece','Greece'),
    ('Greenland','Greenland'),
    ('Grenada','Grenada'),
    ('Guadeloupe','Guadeloupe'),
    ('Guam','Guam'),
    ('Guatemala','Guatemala'),
    ('Guernsey','Guernsey'),
    ('Guinea','Guinea'),
    ('Guinea-Bissau','Guinea-Bissau'),
    ('Guyana','Guyana'),
    ('Haiti','Haiti'),
    ('Heard Island and McDonald Islands','Heard Island and McDonald Islands'),
    ('Holy See (Vatican City)','Holy See (Vatican City)'),
    ('Honduras','Honduras'),
    ('Hong Kong','Hong Kong'),
    ('Hungary','Hungary'),
    ('Iceland','Iceland'),
    ('India','India'),
    ('Indonesia','Indonesia'),
    ('Iran','Iran'),
    ('Iraq','Iraq'),
    ('Ireland','Ireland'),
    ('Isle of Man','Isle of Man'),
    ('Israel','Israel'),
    ('Italy','Italy'),
    ('Jamaica','Jamaica'),
    ('Jan Mayen','Jan Mayen'),
    ('Japan','Japan'),
    ('Jersey','Jersey'),
    ('Jordan','Jordan'),
    ('Juan de Nova Island','Juan de Nova Island'),
    ('Kazakhstan','Kazakhstan'),
    ('Kenya','Kenya'),
    ('Kiribati','Kiribati'),
    ('Korea, North','Korea, North'),
    ('Korea, South','Korea, South'),
    ('Kuwait','Kuwait'),
    ('Kyrgyzstan','Kyrgyzstan'),
    ('Laos','Laos'),
    ('Latvia','Latvia'),
    ('Lebanon','Lebanon'),
    ('Lesotho','Lesotho'),
    ('Liberia','Liberia'),
    ('Libya','Libya'),
    ('Liechtenstein','Liechtenstein'),
    ('Lithuania','Lithuania'),
    ('Luxembourg','Luxembourg'),
    ('Macau','Macau'),
    ('Macedonia','Macedonia'),
    ('Madagascar','Madagascar'),
    ('Malawi','Malawi'),
    ('Malaysia','Malaysia'),
    ('Maldives','Maldives'),
    ('Mali','Mali'),
    ('Malta','Malta'),
    ('Marshall Islands','Marshall Islands'),
    ('Martinique','Martinique'),
    ('Mauritania','Mauritania'),
    ('Mauritius','Mauritius'),
    ('Mayotte','Mayotte'),
    ('Mexico','Mexico'),
    ('Micronesia, Federated States of','Micronesia, Federated States of'),
    ('Moldova','Moldova'),
    ('Monaco','Monaco'),
    ('Mongolia','Mongolia'),
    ('Montserrat','Montserrat'),
    ('Morocco','Morocco'),
    ('Mozambique','Mozambique'),
    ('Namibia','Namibia'),
    ('Nauru','Nauru'),
    ('Navassa Island','Navassa Island'),
    ('Nepal','Nepal'),
    ('Netherlands','Netherlands'),
    ('Netherlands Antilles','Netherlands Antilles'),
    ('New Caledonia','New Caledonia'),
    ('New Zealand','New Zealand'),
    ('Nicaragua','Nicaragua'),
    ('Niger','Niger'),
    ('Nigeria','Nigeria'),
    ('Niue','Niue'),
    ('Norfolk Island','Norfolk Island'),
    ('Northern Mariana Islands','Northern Mariana Islands'),
    ('Norway','Norway'),
    ('Oman','Oman'),
    ('Pakistan','Pakistan'),
    ('Palau','Palau'),
    ('Panama','Panama'),
    ('Papua New Guinea','Papua New Guinea'),
    ('Paracel Islands','Paracel Islands'),
    ('Paraguay','Paraguay'),
    ('Peru','Peru'),
    ('Philippines','Philippines'),
    ('Pitcairn Islands','Pitcairn Islands'),
    ('Poland','Poland'),    
    ('Portugal','Portugal'),
    ('Puerto Rico','Puerto Rico'),
    ('Qatar','Qatar'),
    ('Reunion','Reunion'),
    ('Romania','Romania'),
    ('Russia','Russia'),
    ('Rwanda','Rwanda'),
    ('Saint Helena','Saint Helena'),
    ('Saint Kitts and Nevis','Saint Kitts and Nevis'),
    ('Saint Lucia','Saint Lucia'),
    ('Saint Pierre and Miquelon','Saint Pierre and Miquelon'),
    ('Saint Vincent and the Grenadines','Saint Vincent and the Grenadines'),
    ('Samoa','Samoa'),
    ('San Marino','San Marino'),
    ('Sao Tome and Principe','Sao Tome and Principe'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Senegal','Senegal'),
    ('Serbia and Montenegro','Serbia and Montenegro'),
    ('Seychelles','Seychelles'),
    ('Sierra Leone','Sierra Leone'),
    ('Singapore','Singapore'),
    ('Slovakia','Slovakia'),
    ('Slovenia','Slovenia'),
    ('Solomon Islands','Solomon Islands'),
    ('Somalia','Somalia'),
    ('South Africa','South Africa'),
    ('South Georgia and the South Sandwich Islands','South Georgia and the South Sandwich Islands'),
    ('Spain','Spain'),
    ('Spratly Islands','Spratly Islands'),
    ('Sri Lanka','Sri Lanka'),
    ('Sudan','Sudan'),
    ('Suriname','Suriname'),
    ('Svalbard','Svalbard'),
    ('Swaziland','Swaziland'),
    ('Sweden','Sweden'),
    ('Switzerland','Switzerland'),
    ('Syria','Syria'),
    ('Taiwan','Taiwan'),
    ('Tajikistan','Tajikistan'),
    ('Tanzania','Tanzania'),
    ('Thailand','Thailand'),
    ('Timor-Leste','Timor-Leste'),
    ('Togo','Togo'),
    ('Tokelau','Tokelau'),
    ('Tonga','Tonga'),
    ('Trinidad and Tobago','Trinidad and Tobago'),
    ('Tromelin Island','Tromelin Island'),
    ('Tunisia','Tunisia'),
    ('Turkey','Turkey'),
    ('Turkmenistan','Turkmenistan'),
    ('Turks and Caicos Islands','Turks and Caicos Islands'),
    ('Tuvalu','Tuvalu'),
    ('Uganda','Uganda'),
    ('Ukraine','Ukraine'),
    ('United Arab Emirates','United Arab Emirates'),
    ('United Kingdom','United Kingdom'),
    ('United States','United States'),
    ('Uruguay','Uruguay'),
    ('Uzbekistan','Uzbekistan'),
    ('Vanuatu','Vanuatu'),
    ('Venezuela','Venezuela'),
    ('Vietnam','Vietnam'),
    ('Virgin Islands','Virgin Islands'),
    ('Wake Island','Wake Island'),
    ('Wallis and Futuna','Wallis and Futuna'),
    ('West Bank','West Bank'),
    ('Western Sahara','Western Sahara'),
    ('Yemen','Yemen'),
    ('Zambia','Zambia'),
    ('Zimbabwe','Zimbabwe'),
)

INDUSTRY = (
    ('Automotive/ Ancillaries', 'Automotive/ Ancillaries'),
    ('Banking/ Financial Services', 'Banking/ Financial Services'),
    ('Bio Technology & Life Sciences', 'Bio Technology & Life Sciences'),
    ('Chemicals/Petrochemicals', 'Bio Technology & Life Sciences'),
    ('Construction', 'Construction'),
    ('FMCG', 'FMCG'),
    ('Education', 'Education'),
    ('Entertainment/ Media/ Publishing', 'Entertainment/ Media/ Publishing'),
    ('Insurance', 'Insurance'),
    ('ITES/BPO', 'ITES/BPO'),
    ('IT/ Computers - Hardware', 'IT/ Computers - Hardware'),
    ('IT/ Computers - Software', 'IT/ Computers - Software'),
    ('KPO/Analytics', 'KPO/Analytics'),
    ('Machinery/ Equipment Mfg.', 'Machinery/ Equipment Mfg.'),
    ('Oil/ Gas/ Petroleum', 'Oil/ Gas/ Petroleum'),
    ('Pharmaceuticals', 'Pharmaceuticals'),
    ('Plastic/ Rubber', 'Plastic/ Rubber'),
    ('Power/Energy', 'Power/Energy'),
    ('Real Estate', 'Real Estate'),
    ('Retailing', 'Retailing'),
    ('Telecom', 'Telecom'),
    ('Advertising/PR/Events', 'Advertising/PR/Events'),
    ('Agriculture/ Dairy Based', 'Agriculture/ Dairy Based'),
    ('Aviation/Aerospace', 'Aviation/Aerospace'),
    ('Beauty/Fitness/PersonalCare/SPA', 'Beauty/Fitness/PersonalCare/SPA'),
    ('Beverages/ Liquor', 'Beverages/ Liquor'),
    ('Cement', 'Cement'),
    ('Ceramics & Sanitary Ware', 'Ceramics & Sanitary Ware'),
    ('Consultancy', 'Consultancy'),
    ('Courier/ Freight/ Transportation', 'Courier/ Freight/ Transportation'),
    ('Dotcom', 'Dotcom'),
    ('Electrical/Switchgear', 'Electrical/Switchgear'),
    ('Engineering, Procurement, Construction', 'Engineering, Procurement, Construction'),
    ('Environmental Service', 'Environmental Service'),
    ('Facility management', 'Facility management'),
    ('Fertilizer/ Pesticides', 'Fertilizer/ Pesticides'),
    ('Food & Packaged Food', 'Food & Packaged Food'),
    ('Textiles / Yarn / Fabrics / Garments', 'Textiles / Yarn / Fabrics / Garments'),
    ('Gems & Jewellery', 'Gems & Jewellery'),
    ('Government/ PSU/ Defence', 'Government/ PSU/ Defence'),
    ('Consumer Electronics/Appliances', 'Consumer Electronics/Appliances'),
    ('Hospitals/ Health Care', 'Hospitals/ Health Care'),
    ('Hotels/ Restaurant', 'Hotels/ Restaurant'),
    ('Import / Export', 'Import / Export'),
    ('Iron/ Steel', 'Iron/ Steel'),
    ('ISP', 'ISP'),
    ('Law Enforcement/Security Services', 'Law Enforcement/Security Services'),
    ('Leather', 'Leather'),
    ('Market Research','Market Research'),
    ('Med', 'Med'),
    ('Medical Transcription', 'Medical Transcription'),
    ('Mining', 'Mining'),
    ('NGO', 'NGO'),
    ('Non-Ferrous Metals (Aluminium, Zinc etc.)', 'Non-Ferrous Metals (Aluminium, Zinc etc.)'),
    ('Office Equipment/Automation', 'Office Equipment/Automation'),
    ('Paints', 'Paints'),
    ('Paper', 'Paper'),
    ('Printing/ Packaging', 'Printing/ Packaging'),
    ('Public Relations (PR)', 'Public Relations (PR)'),
    ('Shipping/ Marine Services', 'Shipping/ Marine Services'),
    ('Travel/ Tourism', 'Travel/ Tourism'),
    ('Tyres', 'Tyres'),
    ('Wood', 'Wood'),
    ('Other', 'Other'),
    ('Any', 'Any'),
)

FUNCTIONS = (
        ('Construction', 'Construction'),
        ('Banking/Financial Services/Broking', 'Banking/Financial Services/Broking'),
        ('Oil & Gas/Petroleum', 'Oil & Gas/Petroleum'),
        ('IT - Software Services', 'IT - Software Services'),
        ('Medical/Healthcare/Diagnistics/Medical Devices', 'Medical/Healthcare/Diagnistics/Medical Devices'),
        ('Hotels/Hospitality/Tourism/Recreative', 'Hotels/Hospitality/Tourism/Recreative'),
        ('Advertising/Pr/Events', 'Advertising/Pr/Events'),
        ('Agriculture/Dairy/Poultry', 'Agriculture/Dairy/Poultry'),
        ('Hotels/Hospitality/Tourism/Recreative', 'Hotels/Hospitality/Tourism/Recreative'),
        ('Air Conditioning/Rion', 'Air Conditioning/Rion'),
        ('Airline/Aviation', 'Airline/Aviation'),
        ('Architecture/Interior Designing', 'Architecture/Interior Designing'),
        ('Automotive/Auto Ancillary', 'Automotive/Auto Ancillary'),
        ('Chemicals/PetroChemical', 'Chemicals/PetroChemical'),
        ('Consumer Durables/Consumer Electronics', 'Consumer Durables/Consumer Electronics'),
        ('Courier/Logistics/Transportation/Warehousing', 'Courier/Logistics/Transportation/Warehousing'),
        ('Defence/Militarnmenty/Government', 'Defence/Militarnmenty/Government'),
        ('Education/Training/Teaching', 'Education/Training/Teaching'),
        ('Export/Import/General Trading', 'Export/Import/General Trading'),
        ('Fertilizers/Pesticides', 'Fertilizers/Pesticides'),
        ('FMGG/Foods/Beverage', 'FMGG/Foods/Beverage'),
        ('Fresher - No industry Experience/Not Employed/Intern', 'Fresher - No industry Experience/Not Employed/Intern'),
        ('Gems & Jwellery', 'Gems & Jwellery'),
        ('Industrial Products/Heavy Machinery', 'Industrial Products/Heavy Machinery'),
        ('Insurance', 'Insurance'),
        ('Internet/E-Commerece/Dotcom', 'Internet/E-Commerece/Dotcom'),
        ('IT - Hardware & Networking', 'IT - Hardware & Networking'),
        ('Media/Entertainment/Publishing', 'Media/Entertainment/Publishing'),
        ('Metals/Steel/Iron/Aluminium/Foundry/Electroplating', 'Metals/Steel/Iron/Aluminium/Foundry/Electroplating'),
        ('Mining/Forestry/Fishing', 'Mining/Forestry/Fishing'),
        ('NGO/Social Services', 'NGO/Social Services'),
        ('Office Automation/Equipment/Stationary', 'Office Automation/Equipment/Stationary'),
        ('Paper', 'Paper'),
        ('Pharma/Biotech/Clinical Research', 'Pharma/Biotech/Clinical Research'),
        ('Plastics/Rubber', 'Plastics/Rubber'),
        ('Power/Energy', 'Power/Energy'),
        ('Printing/Packing', 'Printing/Packing'),
        ('Real Estate', 'Real Estate'),
        ('Recruitment/Placement Firm', 'Recruitment/Placement Firm'),
        ('Restaurants/Catering', 'Restaurants/Catering'),
        ('Retail', 'Retail'),
        ('Security/Law Enforcement', 'Security/Law Enforcement'),
        ('Shipping/Freight', 'Shipping/Freight'),
        ('Telecom/ISP', 'Telecom/ISP'),
        ('Textiles/Garments/Accesories/Fashion', 'Textiles/Garments/Accesories/Fashion'),
        ('Tyres', 'Tyres'),
)

MARITAL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widow(er)', 'Widow(er)'),

)

YEARS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),
)

MONTHS =(
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),

)


# LOCATION = (
#     ('United Arab Emirates', 'United Arab Emirates'),
#     ('Abu Dhabi', 'Abu Dhabi'),
#     ('Ajman', 'Ajman'),
#     ('Al Ain', 'Al Ain'),
#     ('Dubai', 'Dubai'),
#     ('Fujairah', 'Fujairah'),
#     ('Ras Al Khaimah', 'Ras Al Khaimah'),
#     ('Sharjah', 'Sharjah'),
#     ('Umm Al Qaiwain', 'Umm Al Qaiwain'),
#     - Other
#     ('Saudi Arabia', 'Saudi Arabia'
#     Abha
#     Abu Areesh
#     Alahsa
#     Albaha
#     Alkharj
#     Alqasim
#     Alqunfithah
#     Altaif
#     Al Madina Al Munawarah
#     Arar
#     Aseer
#     Buraidah
#     Dammam
#     Eastern Province
#     Haeil
#     Hafr Albaten
#     Hofof
#     Jazan
#     Jeddah
#     Jizan
#     Jouf
#     Jubail
#     Jubail/ Al Jubail
#     Khamis Mushait
#     Khobar
#     Makkah Al Mukarramah
#     Mecca
#     Medina
#     Najran
#     Onaizah
#     Qaseem
#     Qatif
#     Riyadh
#     Sabia
#     Sakaka
#     Tabouk
#     Yanbu
#      - Other
#     Qatar
#     Doha
#      - Other
#     Bahrain
#     Manama
#      - Other
#     Oman
#     Ibri
#     Khasab
#     Muscat
#     Nizwa
#     Salalah
#     Sohar
#     Sur
#     Zufar
#      - Other
#     Kuwait
#     Al Ahmadi
#     Al Farawaniyah
#     Al Jahra
#     Al Kuwait
#     Al Zour Mina Saud
#     Hawali
#     Joint Operations Wafra
#      - Other
#     Lebanon
#     Beirut
#     Bekaa
#     Saidon
#     Tripoli
#     Other
#     Jordan
#     Ajloun
#     Amman
#     Aqaba
#     Irbid
#     Jerash
#     Karak
#     Maan
#     Madaba
#     Mafraq
#     Salt
#     Tafila
#     Zarqa
#      - Other
#     Egypt
#     Alexandria
#     Asyut
#     Cairo
#     Damietta
#     Hurghada
#     Ismailia
#     Luxor
#     Port Said
#     Sharm el Sheikh
#     Suez
#      - Other
#     Iraq
#     Al Nagaf
#     Baghdad
#     Basra
#     Erbil
#     Hillah
#     Karbala
#     Kirkuk
#     Mosul
#     Sulaymaniyah
#     Other
#     Afghanistan
#     Africa
#     Algeria
#     Angola
#     Australia
#     Bangladesh
#     Belgium
#     Benin
#     Botswana
#     Burkina Faso
#     Burundi
#     Cameroon
#     Canada
#     Cape Verde
#     Central African Republic
#     Chad
#     China
#     Cote d Ivoire
#     Democratic Republic of Congo
#     Djibouti
#     Equatorial Guinea
#     Eritrea
#     Ethiopia
#     France
#     Gabon
#     Gambia
#     Germany
#     Ghana
#     Guinea
#     Guinea Bissau
#     Hongkong
#     India
#     Indonesia
#     Ireland
#     Japan
#     Kenya
#     Lesotho
#     Liberia
#     Libya
#     Macau
#     Madagascar
#     Malawi
#     Malaysia
#     Maldives
#     Mali
#     Mauritania
#     Mauritius
#     Mexico
#     Morocco
#     Mozambique
#     Namibia
#     Nepal
#     Netherlands
#     New Zealand
#     Niger
#     Nigeria
#     Pakistan
#     Philippines
#     Republic of Congo
#     Russia
#     Rwanda
#     Senegal
#     Seychelles
#     Sierra Leone
#     Singapore
#     Somalia
#     South Africa
#     South Korea
#     Spain
#     SriLanka
#     Sudan
#     Swaziland
#     Sweden
#     Switzerland
#     Taiwan
#     Tanzania
#     Thailand
#     Togo
#     Tunisia
#     UK
#     US
#     Uganda
#     Vietnam
#     Yemen
#     Zambia
#     Zimbabwe
#     Other International

# )



class UserProfile(models.Model):
	user = models.ForeignKey(User)
	user_type = models.CharField('User Type', max_length=20, choices=USER_TYPE)
	gender = models.CharField('Gender', max_length=1, choices=GENDER)
	nationality = models.CharField('Nationality', max_length=20, choices=COUNTRY_CHOICES)
	current_location = models.CharField('Current Loction', null=True, blank=True, max_length=20, choices=COUNTRY_CHOICES)
	country = models.CharField('Country', null=True, blank=True, max_length=20, choices=COUNTRY_CHOICES)
	city = models.CharField('City', null=True, blank=True, max_length=20)
	mobile = models.IntegerField ('Mobile')
	land_num = models.IntegerField('Land Phone', blank=True)
	# mail_id = models.CharField('Email Id', max_length=25)
	Alt_mail = models.CharField('Alternate Email Id', null=True, blank=True, max_length=25)
	religion = models.CharField('Religion', null=True, blank=True, max_length=10)
	marital_status = models.CharField('Marital Status', null=True, blank=True, max_length=10, choices=MARITAL_STATUS)

	def __unicode__(self):
		return self.user.username

	class Meta:
		verbose_name = 'UserProfile'
		verbose_name_plural = 'UserProfile'



class Employment(models.Model):
	user = models.ForeignKey(UserProfile)
	exp_yrs = models.IntegerField('Experience in Years',null=True, blank=True, choices=YEARS)
	exp_mnths = models.IntegerField('Experience in Months',null=True, blank=True, choices=MONTHS)
	salary = models.IntegerField('Salary', null=True, blank=True)
	designation = models.CharField('Designation', null=True, blank=True, max_length=15)
	# industry_type = models.CharField('Industry Type', null=True, blank=True, max_length=20, choices=INDUSTRY)
	skills = models.CharField('Key Skills', null=True, blank=True, max_length=20)
	curr_industry = models.CharField('Current Industry', null=True, blank=True, max_length=20, choices=INDUSTRY)

	def __unicode__(self):
		return self.user.username

	class Meta:

		verbose_name = 'Employment'
		verbose_name_plural = 'Employment'



class Education(models.Model):
	user = models.ForeignKey(UserProfile)
	basic_edu = models.CharField('Basic Education', max_length=15)
	basic_spl = models.CharField('Specialisation1', max_length=20)
	masters = models.CharField('Masters', null=True, blank=True, max_length=15)
	master_spl = models.CharField('Specialisation2', null=True, blank=True, max_length=20)
	doctorate = models.CharField('Doctorate', null=True, blank=True, max_length=20)
	resume = models.FileField (upload_to = "uploads/files/", max_length=20000,  null=True, blank=True)

	def __unicode__(self):
		return self.user.username

	class Meta:

		verbose_name = 'Education'
		verbose_name_plural = 'Education'



class CompanyProfile(models.Model):

	user = models.ForeignKey(UserProfile)
	#employer_name = models.CharField('Employer Name', max_length=15)
	company_name = models.CharField('Company Name', max_length=20)
	industry_type = models.CharField('Industry Type', max_length=20)

	def __unicode__(self):
		return self.company_name

	class Meta:

		verbose_name = 'CompanyProfile'
		verbose_name_plural = 'CompanyProfile'



class JobPosting(models.Model):
	job_title = models.CharField('Job Title', max_length=20)
	ref_code = models.CharField('Ref Code', max_length=10)
	job_details = models.CharField('Job Details', max_length=100,null=True, blank=True)
	document = models.FileField (upload_to = "uploads/files/", max_length=20000, null=True, blank=True)
	order = models.IntegerField('Order')
    #posting_date = models.DateTimeField('Posting Date', null=True, blank=True)
	#last_date = models.DateTimeField('Last Date', null=True, blank=True)
	#exp_req = models.IntegerField('Experience Required', null=True, blank=True)
	#skills = models.CharField('Skills Required', null=True, blank=True, max_length=20)

	def __unicode__(self):
		return self.job_type

	class Meta:

		verbose_name = 'JobPosting'
		verbose_name_plural = 'JobPosting'


		
