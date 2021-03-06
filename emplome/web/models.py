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
    ('Angola', 'Angola'),
    ('Antartica','Antartica'),
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
    ('Other', 'Other'),
)

NATIONALITY = (
    ('Afganistani', 'Afganistani'),
    ('Albanian', 'Albanian'),
    ('Algerian', 'Algerian'),
    ('American Samoa', 'American Samoa'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Anguilla', 'Anguilla'),
    ('Antarctican', 'Antarctican'),
    ('Antigua and Barbuda', 'Antigua and Barbuda'),
    ('Argentina', 'Argentina'),
    ('Armenian', 'Armenian'),
    ('Aruba', 'Aruba'),
    ('Australian', 'Australian'),
    ('Austrian', 'Austrian'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahamas', 'Bahamas'),
    ('Bahraini', 'Bahraini'),
    ('Bangladeshi', 'Bangladeshi'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bermuda', 'Bermuda'),
    ('Bhutani', 'Bhutani'),
    ('Bolivian', 'Bolivian'),
    ('Bosnia and Herzegovinan', 'Bosnia and Herzegovinan'),
    ('Botswana', 'Botswana'),
    ('Bouvet Island', 'Bouvet Island'),
    ('Brazilian', 'Brazilian'),
    ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
    ('Brunei Darussalam', 'Brunei Darussalam'),
    ('Bulgarian', 'Bulgarian'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Cambodian', 'Cambodian'),
    ('Cameroon', 'Cameroon'),
    ('Canadian', 'Canadian'),
    ('Cape Verde', 'Cape Verde'),
    ('Cayman Islands', 'Cayman Islands'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('Chinese', 'Chinese'),
    ('Christmas Island', 'Christmas Island'),
    ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
    ('Colombian', 'Colombian'),
    ('Comoros', 'Comoros'),
    ('Congo', 'Congo'),
    ('Cook Islands', 'Cook Islands'),
    ('Costa Rica', 'Costa Rica'),
    ("Cote D'Ivoire", "Cote D'Ivoire"),
    ('Croatia', 'Croatia'),
    ('Cuban', 'Cuban'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('Ecuador', 'Ecuador'),
    ('Egyptian', 'Egyptian'),
    ('El Salvador', 'El Salvador'),
    ('Emirati', 'Emirati'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Ethiopian', 'Ethiopian'),
    ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
    ('Faroe Islands', 'Faroe Islands'),
    ('Fiji', 'Fiji'),
    ('Filipino', 'Filipino'),
    ('Finland', 'Finland'),
    ('French', 'French'),
    ('French Guiana', 'French Guiana'),
    ('French Polynesia', 'French Polynesia'),
    ('French Southern Territories', 'French Southern Territories'),
    ('Gabon', 'Gabon'),
    ('Georgian', 'Georgian'),
    ('German', 'German'),
    ('Ghana', 'Ghana'),
    ('Gibraltar', 'Gibraltar'),
    ('Greece', 'Greece'),
    ('Greenland', 'Greenland'),
    ('Grenada', 'Grenada'),
    ('Guadeloupe', 'Guadeloupe'),
    ('Guam', 'Guam'),
    ('Guinean', 'Guinean'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Heard Island and Mcdonald Islands', 'Heard Island and Mcdonald Islands'),
    ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
    ('Honduras', 'Honduras'),
    ('Hong Kong', 'Hong Kong'),
    ('Hungarian', 'Hungarian'),
    ('Iceland', 'Iceland'),
    ('Indian', 'Indian'),
    ('Indonesian', 'Indonesian'),
    ('Iranian', 'Iranian'),
    ('Ireland', 'Ireland'),
    ('Israeli', 'Israeli'),
    ('Japanese', 'Japanese'),
    ('Jordanian', 'Jordanian'),
    ('Kazakhstani', 'Kazakhstani'),
    ('Kenyan', 'Kenyan'),
    ('Kiribati', 'Kiribati'),
    ("Korea, Democratic People's Republic of", "Korea, Democratic People's Republic of"),
    ('Korea, Republic of', 'Korea, Republic of'),
    ('Kuwaiti', 'Kuwaiti'),
    ('Kyrgyzstani', 'Kyrgyzstani'),
    ("Lao People's Democratic Republic", "Lao People's Democratic Republic"),
    ('Latvian', 'Latvian'),
    ('Lebanese', 'Lebanese'),
    ('Lesotho', 'Lesotho'),
    ('Liberian', 'Liberian'),
    ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Macao', 'Macao'),
    ('Macedonia, the Former Yugoslav Republic of', 'Macedonia, the Former Yugoslav Republic of'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysian', 'Malaysian'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Martinique', 'Martinique'),
    ('Mauritanian', 'Mauritanian'),
    ('Mauritius', 'Mauritius'),
    ('Mayotte', 'Mayotte'),
    ('Mexican', 'Mexican'),
    ('Micronesia, Federated States of', 'Micronesia, Federated States of'),
    ('Moldova, Republic of', 'Moldova, Republic of'),
    ('Monaco', 'Monaco'),
    ('Mongolian', 'Mongolian'),
    ('Montserrat', 'Montserrat'),
    ('Moroccan', 'Moroccan'),
    ('Mozambique', 'Mozambique'),
    ('Myanmar', 'Myanmar'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepalese', 'Nepalese'),
    ('Netherlands', 'Netherlands'),
    ('Netherlands Antilles', 'Netherlands Antilles'),
    ('New Caledonia', 'New Caledonia'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigerian', 'Nigerian'),
    ('Niue', 'Niue'),
    ('Norfolk Island', 'Norfolk Island'),
    ('Northern Mariana Islan', 'Northern Mariana Islan'),
    ('Norway', 'Norway'),
    ('Omani', 'Omani'),
    ('Pakistani', 'Pakistani'),
    ('Palau', 'Palau'),
    ('Palestinian', 'Palestinian'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Pitcairn', 'Pitcairn'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Puerto Rico', 'Puerto Rico'),
    ('Qatari', 'Qatari'),
    ('Reunion', 'Reunion'),
    ('Romanian', 'Romanian'),
    ('Russian', 'Russian'),
    ('Rwanda', 'Rwanda'),
    ('Saint Helena', 'Saint Helena'),
    ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
    ('Saint Lucia', 'Saint Lucia'),
    ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
    ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Saudi', 'Saudi'),
    ('Senegal', 'Senegal'),
    ('Serbia and Montenegro', 'Serbia and Montenegro'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singaporean', 'Singaporean'),
    ('Slovakian', 'Slovakian'),
    ('Slovenian', 'Slovenian'),
    ('Solomon - Islands   ', 'Solomon - Islands   '),
    ('Somalian', 'Somalian'),
    ('South African', 'South African'),
    ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'),
    ('Spanish', 'Spanish'),
    ('Sri Lankan', 'Sri Lankan'),
    ('Sudanese', 'Sudanese'),
    ('Suriname', 'Suriname'),
    ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'),
    ('Swaziland', 'Swaziland'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syrian', 'Syrian'),
    ('Taiwanese', 'Taiwanese'),
    ('Tajikistan', 'Tajikistan'),
    ('Tanzania, United Republic of', 'Tanzania, United Republic of'),
    ('Thai', 'Thai'),
    ('Timor-Leste', 'Timor-Leste'),
    ('Togo', 'Togo'),
    ('Tokelau', 'Tokelau'),
    ('Tonga', 'Tonga'),
    ('Trinidad and Tobago', 'Trinidad and Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkish', 'Turkish'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Kingdom', 'United Kingdom'),
    ('United States', 'United States'),
    ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistani', 'Uzbekistani'),
    ('Vanuatu', 'Vanuatu'),
    ('Venezuela', 'Venezuela'),
    ('Vietnamese', 'Vietnamese'),
    ('Virgin Islands, British', 'Virgin Islands, British'),
    ('Virgin Islands, U.s.', 'Virgin Islands, U.s.'),
    ('Wallis and Futuna', 'Wallis and Futuna'),
    ('Western Sahara', 'Western Sahara'),
    ('Yemeni', 'Yemeni'),
    ('Zambian', 'Zambian'),
    ('Zimbabwe', 'Zimbabwe'),
    ('Other', 'Other'),
    ('Any', 'Any')

)


INDUSTRY = (
    ('Automotive/ Ancillaries', 'Automotive/ Ancillaries'),
    ('Banking/ Financial Services', 'Banking/ Financial Services'),
    ('Bio Technology and Life Sciences', 'Bio Technology and Life Sciences'),
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
    ('Ceramics and Sanitary Ware', 'Ceramics and Sanitary Ware'),
    ('Consultancy', 'Consultancy'),
    ('Courier/ Freight/ Transportation', 'Courier/ Freight/ Transportation'),
    ('Dotcom', 'Dotcom'),
    ('Electrical/Switchgear', 'Electrical/Switchgear'),
    ('Engineering, Procurement, Construction', 'Engineering, Procurement, Construction'),
    ('Environmental Service', 'Environmental Service'),
    ('Facility management', 'Facility management'),
    ('Fertilizer/ Pesticides', 'Fertilizer/ Pesticides'),
    ('Food and Packaged Food', 'Food and Packaged Food'),
    ('Textiles / Yarn / Fabrics / Garments', 'Textiles / Yarn / Fabrics / Garments'),
    ('Gems/ Jewellery', 'Gems/ Jewellery'),
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
        ('Oil/ Gas/ Petroleum', 'Oil/ Gas/ Petroleum'),
        ('IT - Software Services', 'IT - Software Services'),
        ('Medical/Healthcare/Diagnistics/Medical Devices', 'Medical/Healthcare/Diagnistics/Medical Devices'),
        ('Hotels/Hospitality/Tourism/Recreative', 'Hotels/Hospitality/Tourism/Recreative'),
        ('Advertising/Pr/Events', 'Advertising/Pr/Events'),
        ('Agriculture/Dairy/Poultry', 'Agriculture/Dairy/Poultry'),
        ('Hotels/Hospitality/Tourism/Recreative', 'Hotels/Hospitality/Tourism/Recreative'),
        ('Air Conditioning/Refrigeration', 'Air Conditioning/Refrigeration'),
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
        ('Gems/ Jwellery', 'Gems/ Jwellery'),
        ('Industrial Products/Heavy Machinery', 'Industrial Products/Heavy Machinery'),
        ('Insurance', 'Insurance'),
        ('Internet/E-Commerece/Dotcom', 'Internet/E-Commerece/Dotcom'),
        ('IT - Hardware and Networking', 'IT - Hardware and Networking'),
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
        ('Other', 'Other'),
)

MARITAL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widow(er)', 'Widow(er)'),

)

YEARS = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
    (26, '26'),
    (27, '27'),
    (28, '28'),
    (29, '29'),
    (30, '30'),
    (31, '31'),
    (32, '32'),
    (33, '33'),
    (34, '34'),
    (35, '35'),
    (36, '36'),
    (37, '37'),
    (38, '38'),
    (39, '39'),
    (40, '40'),
    (41, '41'),
    (42, '42'),
    (43, '43'),
    (44, '44'),
    (45, '45'),
    (46, '46'),
    (47, '47'),
    (48, '48'),
    (49, '49'),
    (50, '50'),
)

MONTHS =(
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),

)


BASIC_EDU = (
    ('Diploma', 'Diploma'),
    ('Intermediate Schooling', 'Intermediate Schooling'),
    ('Secondary Schooling', 'Secondary Schooling'),
    ('Bachelor of Architecture', 'Bachelor of Architecture'),
    ('Bachelor of Arts', 'Bachelor of Arts'),
    ('Bachelor of Business Administration', 'Bachelor of Business Administration'),
    ('Bachelor of Commerce', 'Bachelor of Commerce'),
    ('Bachelor of Dental Sugery', 'Bachelor of Dental Sugery'),
    ('Bachelor of Education', 'Bachelor of Education'),
    ('Bachelor of Hotel Management', 'Bachelor of Hotel Management'),
    ('Bachelor of Laws (LLB)', 'Bachelor of Laws (LLB)'),
    ('Bachelor of Pharmacy', 'Bachelor of Pharmacy'),
    ('Bachelor of Science', 'Bachelor of Science'),
    ('Bachelor of Technology/Engineering', 'Bachelor of Technology/Engineering'),
    ('Bachelor of Vetirenary Science', 'Bachelor of Vetirenary Science'),
    ('Bachelor of Computer Application', 'Bachelor of Computer Application'),
    ('MBBS', 'MBBS'),
    ('Other', 'Other'),
)


MASTERS_EDU = (
    ('Chartered Accountant', 'Chartered Accountant'),
    ('CA Inter', 'CA Inter'),
    ('Chartered Financial Analyst', 'Chartered Financial Analyst'),
    ('Company Secretary', 'Company Secretary'),
    ('Doctor of Medicine (MD)', 'Doctor of Medicine (MD)'),
    ('Doctor of Surgery (MS)', 'Doctor of Surgery (MS)'),
    ('Inst. of Cost & Works Accountants', 'Inst. of Cost & Works Accountants'),
    ('ICWA Inter', 'ICWA Inter'),
    ('Master of Architecture', 'Master of Architecture'),
    ('Master of Arts', 'Master of Arts'),
    ('Master of Commerce', 'Master of Commerce'),
    ('Master of Education', 'Master of Education'),
    ('Master of Laws (LLM)', 'Master of Laws (LLM)'),
    ('Master of Pharmacy', 'Master of Pharmacy'),
    ('Master of Science', 'Master of Science'),
    ('Master of Technology/Engineering', 'Master of Technology/Engineering'),
    ('Master of Vetirenary Science', 'Master of Vetirenary Science'),
    ('Master of Computer Application', 'Master of Computer Application'),
    ('MBA/PG Diploma in Business Mgmt ', 'MBA/PG Diploma in Business Mgmt '),
    ('Other', 'Other'),

)

EDUCATION_REQUIRED = (
    ('Diploma', 'Diploma'),
    ('Intermediate Schooling', 'Intermediate Schooling'),
    ('Secondary Schooling', 'Secondary Schooling'),
    ('Bachelor of Architecture', 'Bachelor of Architecture'),
    ('Bachelor of Arts', 'Bachelor of Arts'),
    ('Bachelor of Business Administration', 'Bachelor of Business Administration'),
    ('Bachelor of Commerce', 'Bachelor of Commerce'),
    ('Bachelor of Dental Sugery', 'Bachelor of Dental Sugery'),
    ('Bachelor of Education', 'Bachelor of Education'),
    ('Bachelor of Hotel Management', 'Bachelor of Hotel Management'),
    ('Bachelor of Laws (LLB)', 'Bachelor of Laws (LLB)'),
    ('Bachelor of Pharmacy', 'Bachelor of Pharmacy'),
    ('Bachelor of Science', 'Bachelor of Science'),
    ('Bachelor of Technology/Engineering', 'Bachelor of Technology/Engineering'),
    ('Bachelor of Vetirenary Science', 'Bachelor of Vetirenary Science'),
    ('Bachelor of Computer Application', 'Bachelor of Computer Application'),
    ('MBBS', 'MBBS'),
    ('Chartered Accountant', 'Chartered Accountant'),
    ('CA Inter', 'CA Inter'),
    ('Chartered Financial Analyst', 'Chartered Financial Analyst'),
    ('Company Secretary', 'Company Secretary'),
    ('Doctor of Medicine (MD)', 'Doctor of Medicine (MD)'),
    ('Doctor of Surgery (MS)', 'Doctor of Surgery (MS)'),
    ('Inst. of Cost & Works Accountants', 'Inst. of Cost & Works Accountants'),
    ('ICWA Inter', 'ICWA Inter'),
    ('Master of Architecture', 'Master of Architecture'),
    ('Master of Arts', 'Master of Arts'),
    ('Master of Commerce', 'Master of Commerce'),
    ('Master of Education', 'Master of Education'),
    ('Master of Laws (LLM)', 'Master of Laws (LLM)'),
    ('Master of Pharmacy', 'Master of Pharmacy'),
    ('Master of Technology/Engineering', 'Master of Technology/Engineering'),
    ('Master of Vetirenary Science', 'Master of Vetirenary Science'),
    ('Master of Computer Application', 'Master of Computer Application'),
    ('MBA/PG Diploma in Business Mgmt ', 'MBA/PG Diploma in Business Mgmt '),
    ('Other', 'Other'),
)

CURRENCIES = (
    ('US Dollars', 'US Dollars'),
    ('UK Pound', 'UK Pound'),
    ('Indian Rupees', 'Indian Rupees'), 
    ('UAE Dhirhams', 'UAE Dhirhams'),
    ('Dinar', 'Dinar'),
    ('Riyal', 'Riyal'),
    ('Australian Dollars','Australian Dollars'),
    ('Singapore Dollars','Singapore Dollars'),
    ('Sri Lankan Rupee', 'Sri Lankan Rupee'),
    ('Euro', 'Euro'),        
    ('Yen', 'Yen'),       
)

SPECIALIZATION = (
    ('General (College Proprietary)', 'General (College Proprietary)'),
    ('Academic / General', 'Academic / General'),
    ('Commercial', 'Commercial'),
    ('Technical','Technical'),
    ('Vocational', 'Vocational'),
    ('Religion', 'Religion'),
    ('Aircraft Maintenance', 'Aircraft Maintenance'),
    ('Architecture','Architecture'),
    ('Autoclave Operation', 'Autoclave Operation'),
    ('Cement Technology', 'Cement Technology'),
    ('Chemical', 'Chemical'),
    ('Civil', 'Civil'),
    ('Computers', 'Computers'),
    ('Construction Technology', 'Construction Technology'),
    ('Drilling & Exploration Technology', 'Drilling & Exploration Technology'),
    ('Electrical', 'Electrical'),
    ('Electronics', 'Electronics'),
    ('Engineering', 'Engineering'),
    ('Export/Import', 'Export/Import'),
    ('Fashion Designing/Other Designing', 'Fashion Designing/Other Designing'),
    ('Foundry & Forging', 'Foundry & Forging'),
    ('Graphic/ Web Designing', 'Graphic/ Web Designing'),
    ('Hotel Management', 'Hotel Management'),
    ('Instrumentation & Control', 'Instrumentation & Control'),
    ('Insurance', 'Insurance'),
    ('Jewelery Design & Manufacturing', 'Jewelery Design & Manufacturing'),
    ('Machine Tool Maintenance & Repair', 'Machine Tool Maintenance & Repair'),
    ('Management', 'Management'),
    ('Mechanical', 'Mechanical'),
    ('Medical Instrumentation', 'Medical Instrumentation'),
    ('Medical Lab Technology', 'Medical Lab Technology'),
    ('Petrochemical Technology', 'Petrochemical Technology'),
    ('Process Instrumentation', 'Process Instrumentation'),
    ('Production Technology', 'Production Technology'),
    ('Refinery & Petro Chemical Technology', 'Refinery & Petro Chemical Technology'),
    ('Refrigeration & Airconditioning', 'Refrigeration & Airconditioning'),
    ('Surface Coating Technology', 'Surface Coating Technology'),
    ('Survey Engineering', 'Survey Engineering'),
    ('Telecommunication', 'Telecommunication'),
    ('Tool & Die Technology', 'Tool & Die Technology'),
    ('Tourism', 'Tourism'),
    ('Videography', 'Videography'),
    ('Visual Arts', 'Visual Arts'),
    ('Vocational Course', 'Vocational Course'),
    ('Welding Technology', 'Welding Technology'),
    ('Architecture', 'Architecture'),
    ('Arabic', 'Arabic'),
    ('Arts & Humanities', 'Arts & Humanities'),
    ('Communication', 'Communication'),
    ('Economics', 'Economics'),
    ('English', 'English'),
    ('Film', 'Film'),
    ('Fine arts', 'Fine arts'),
    ('Hindi', 'Hindi'),
    ('History', 'History'),
    ('Journalism', 'Journalism'),
    ('Middle Eastern Studies', 'Middle Eastern Studies'),
    ('Political Science', 'Political Science'),
    ('PR/Advertising', 'PR/Advertising'),
    ('Psychology', 'Psychology'),
    ('Sociology', 'Sociology'),
    ('Statistics', 'Statistics'),
    ('Urdu', 'Urdu'),
    ('Vocational Course', 'Vocational Course'),
    ('Management', 'Management'),    
    ('Commerce', 'Commerce'),      
    ('Dentistry', 'Dentistry'),    
    ('Education', 'Education'),
    ('Religious Education', 'Religious Education'),     
    ('Hotel Management', 'Hotel Management'),     
    ('Law', 'Law'),
    ('Pharmacy', 'Pharmacy'),
    ('Agriculture', 'Agriculture'),
    ('Anthropology', 'Anthropology'),
    ('Bio-Chemistry', 'Bio-Chemistry'),
    ('Biology', 'Biology'),
    ('Botany', 'Botany'),
    ('Chemistry', 'Chemistry'),
    ('Computers', 'Computers'),
    ('Dairy', 'Dairy'),
    ('Technology', 'Technology'),
    ('Electronics', 'Electronics'),
    ('Environmental science', 'Environmental science'),
    ('Food Technology', 'Food Technology'),
    ('Geology', 'Geology'),
    ('Home Science', 'Home Science'),
    ('Maths', 'Maths'),
    ('Microbiology', 'Microbiology'),
    ('Nursing', 'Nursing'),
    ('Physics', 'Physics'),
    ('Statistics', 'Statistics'),
    ('Zoology', 'Zoology'),
    ('General', 'General'),
    ('Automobile', 'Automobile'),
    ('Aviation', 'Aviation'),
    ('Bio-Chemistry', 'Bio-Chemistry'),
    ('Bio-Technology', 'Bio-Technology'),
    ('Biomedical', 'Biomedical'),
    ('Ceramics', 'Ceramics'),
    ('Chemical', 'Chemical'),  
    ('Electronics/Telecomunication', 'Electronics/Telecomunication'),
    ('Energy', 'Energy'),
    ('Environmental', 'Environmental'),
    ('Instrumentation', 'Instrumentation'),
    ('Marine', 'Marine'),
    ('Metallurgy', 'Metallurgy'),
    ('Mineral', 'Mineral'),
    ('Mining', 'Mining'),
    ('Nuclear', 'Nuclear'),
    ('Paint/Oil', 'Paint/Oil'),
    ('Petroleum', 'Petroleum'),
    ('Plastics', 'Plastics'),
    ('Production/Industrial', 'Production/Industrial'),
    ('Textile', 'Textile'),
    ('Other Engineering', 'Other Engineering'),
    ('Veterinary Sciences', 'Veterinary Sciences'),
    ('Computers', 'Computers'),
    ('Medicine', 'Medicine'),   
    ('Chartered Accountant', 'Chartered Accountant'), 
    ('Finance', 'Finance'),
    ('Company Secretary', 'Company Secretary'),
    ('Anatomy', 'Anatomy'),
    ('Anesthesiology', 'Anesthesiology'),
    ('Aviation Medicine', 'Aviation Medicine'),
    ('Biochemistry', 'Biochemistry'),
    ('Bio-Physics', 'Bio-Physics'),
    ('Blood Banking & Immuno. Haem', 'Blood Banking & Immuno. Haem'),
    ('Critical Care Medicine', 'Critical Care Medicine'),
    ('Community Health Administration', 'Community Health Administration'),
    ('Community Medicine', 'Community Medicine'),
    ('Dermatology', 'Dermatology'),
    ('Forensic Medicine', 'Forensic Medicine'),
    ('General Medicine', 'General Medicine'),
    ('Geriatrics', 'Geriatrics'),
    ('Gynecology', 'Gynecology'),
    ('Health Administration', 'Health Administration'),
    ('Hospital Administration', 'Hospital Administration'),
    ('Lab Medicine', 'Lab Medicine'),
    ('Leprosy', 'Leprosy'),
    ('Maternity & Child Health', 'Maternity & Child Health'),
    ('Microbiology', 'Microbiology'),
    ('Nuclear Medicine', 'Nuclear Medicine'),
    ('Obstetrics', 'Obstetrics'),
    ('Ophthalmology', 'Ophthalmology'),
    ('Pathology', 'Pathology'),
    ('Pediatrics', 'Pediatrics'),
    ('Pharmacology', 'Pharmacology'),
    ('Physical Medicine & Rehabilitation', 'Physical Medicine & Rehabilitation'),
    ('Physiology', 'Physiology'),
    ('Psychiatry', 'Psychiatry'),
    ('Pulmonary Medicine', 'Pulmonary Medicine'),
    ('R & D', 'R & D'),
    ('Radio Diagnosis', 'Radio Diagnosis'),
    ('Radio Therapy', 'Radio Therapy'),
    ('Radiology', 'Radiology'),
    ('Social and Preventive Medicine', 'Social and Preventive Medicine'),
    ('Tropical Medicine', 'Tropical Medicine'),
    ('Tuberculosis & Chest Diseases', 'Tuberculosis & Chest Diseases'),
    ('Veneriology', 'Veneriology'),  
    ('Anaesthesia', 'Anaesthesia'),
    ('Anatomy', 'Anatomy'),
    ('Cardiology', 'Cardiology'),
    ('Dermatology', 'Dermatology'),
    ('ENT', 'ENT'),
    ('General Surgery', 'General Surgery'),
    ('Gyneocology', 'Gyneocology'),
    ('Hepatology', 'Hepatology'),
    ('Immunology Microbiology', 'Immunology Microbiology'),
    ('Neonatal', 'Neonatal'),
    ('Nephrology/Urology', 'Nephrology/Urology'),
    ('Obstretrics', 'Obstretrics'),
    ('Oncology', 'Oncology'),
    ('Opthalmology', 'Opthalmology'),
    ('Orthopedic', 'Orthopedic'),
    ('Pathology', 'Pathology'),
    ('Pediatrics', 'Pediatrics'),
    ('Psychiatry/Psychology', 'Psychiatry/Psychology'),
    ('Radiology', 'Radiology'),
    ('Rheumatology', 'Rheumatology'), 
    ('Cost & Works Accountant', 'Cost & Works Accountant'),
    ('Anthropology', 'Anthropology'),   
    ('Advertising/Mass Communication', 'Advertising/Mass Communication'),
    ('HR/Industrial Relations', 'HR/Industrial Relations'),
    ('Information Technology', 'Information Technology'),
    ('International Business', 'International Business'),
    ('Marketing', 'Marketing'),
    ('Systems', 'Systems'),
    ('Other', 'Other'),
)
    

class CompanyProfile(models.Model):

    company_name = models.CharField('Company Name', max_length=50, null=True, blank=True)
    industry_type = models.CharField('Industry Type', max_length=50)
    description = models.CharField('Description', max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.company_name

    class Meta:

        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfile'


class Job(models.Model):

    recruiter = models.ForeignKey(User)
    company = models.ForeignKey(CompanyProfile, null=True, blank=True)
    job_title = models.CharField('Job Title', max_length=50)
    ref_code = models.CharField('Ref Code', max_length=15, null=True, blank=True)
    summary = models.CharField('Summary', max_length=500)
    document = models.FileField (upload_to = "uploads/doc/", null=True, blank=True)
    skills = models.CharField('Skills Required', null=True, blank=True, max_length=50)
    order = models.IntegerField('Order', default=0)
    industry = models.CharField('Industry', max_length=70, choices=INDUSTRY)
    job_location = models.CharField('Job Location', max_length=50, choices=COUNTRY_CHOICES)
    function = models.CharField('Function', max_length=70, choices=FUNCTIONS)
    education_req = models.CharField('Education Required', max_length=70, choices=EDUCATION_REQUIRED)
    specialization = models.CharField('Specialization', max_length=70, null=True, blank=True)
    nationality = models.CharField('Nationality', max_length=70, null=True, blank=True, choices=NATIONALITY)
    name = models.CharField('Name', max_length=50)
    phone = models.CharField('Phone', max_length=50,null=True, blank=True)
    mail_id = models.CharField('Email Id', max_length=70)
    posting_date = models.DateField('Posting Date', null=True, blank=True)
    last_date = models.DateField('Last Date', null=True, blank=True)
    exp_req_min = models.IntegerField('Experience Required Min', null=True, blank=True, choices=YEARS)
    exp_req_max = models.IntegerField('Experience Required Max', null=True, blank=True, choices=YEARS)
    is_featured = models.BooleanField('Is Featured', default=False)
    description = models.TextField('Description', null=True, blank=True)
    is_publish = models.BooleanField('Publish', default=False)
    salary = models.IntegerField('Salary', null=True, blank=True)
    currency = models.CharField('Currency', max_length=30, null=True, blank=True, choices=CURRENCIES)

    def __unicode__(self):
        return self.job_title

    class Meta:

        verbose_name = 'JobPosting'
        verbose_name_plural = 'JobPosting'

class PreviousEmployer(models.Model):
    previous_employer_name = models.CharField('Employer name', max_length=100, null=True, blank=True)

    def __unicode__(self):

        return self.previous_employer_name

class Employment(models.Model):

    exp_yrs = models.IntegerField('Experience in Years',null=True, blank=True, choices=YEARS)
    exp_mnths = models.IntegerField('Experience in Months',null=True, blank=True, choices=MONTHS)
    salary = models.IntegerField('Salary', null=True, blank=True)
    currency = models.CharField('Currency', max_length=30, null=True, blank=True, choices=CURRENCIES)
    designation = models.CharField('Designation', null=True, blank=True, max_length=50)
    skills = models.CharField('Key Skills', null=True, blank=True, max_length=50)
    curr_industry = models.CharField('Current Industry', null=True, blank=True, max_length=50, choices=INDUSTRY)
    function = models.CharField('Function', null=True, blank=True, max_length=50, choices=FUNCTIONS)
    previous_employer = models.ManyToManyField(PreviousEmployer, null=True, blank=True)


    def __unicode__(self):
        return str(self.skills)

    class Meta:

        verbose_name = 'Employment'
        verbose_name_plural = 'Employment'

class Doctorate(models.Model):
    doctorate_name = models.CharField('Doctorate name', null=True, blank=True, max_length=100)

    def __unicode__(self):
        return self.doctorate_name

class Certificates(models.Model):
    certificate_name = models.FileField(upload_to = "uploads/certificates/", null=True, blank=True)

    # def __unicode__(self):
    #     return self.certificate_name


class Education(models.Model):
    
    basic_edu = models.CharField('Basic Education', max_length=50, choices=BASIC_EDU)
    
    pass_year_basic = models.IntegerField('Basic Pass Year', null=True, blank=True)
    basic_edu_specialization = models.CharField('Basic Education Specialization', null=True, blank=True, choices=SPECIALIZATION, max_length=100)
    masters = models.CharField('Masters', null=True, blank=True, max_length=50, choices=MASTERS_EDU)
    pass_year_masters = models.IntegerField('Masters pass Year', null=True, blank=True)
    masters_specialization = models.CharField('Masters Specialization', null=True, blank=True, choices=SPECIALIZATION, max_length=100)
    doctrate = models.ManyToManyField(Doctorate,null=True, blank=True)
    resume_title = models.CharField('Resume Title', max_length=50)
    resume = models.FileField(upload_to = "uploads/resumes/", null=True, blank=True)
    resume_text = models.TextField('Resume Text', blank=True, null=True)
    certificate = models.ManyToManyField(Certificates, null=True, blank=True)

    def __unicode__(self):
        return str(self.basic_edu)

    class Meta:

        verbose_name = 'Education'
        verbose_name_plural = 'Education'

class UserProfile(models.Model):
    
    user = models.ForeignKey(User)
    user_type = models.CharField('User Type', max_length=50, choices=USER_TYPE)
    country = models.CharField('Country', null=True, blank=True, max_length=50, choices=COUNTRY_CHOICES)
    city = models.CharField('City', null=True, blank=True, max_length=50)
    mobile = models.CharField ('Mobile', max_length=20)
    land_num = models.CharField('Land Phone', blank=True, max_length=20)
    
    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'


class JobSeekerProfile(models.Model):

    profile = models.ForeignKey(UserProfile)
    gender = models.CharField('Gender', max_length=7, choices=GENDER)
    nationality = models.CharField('Nationality', max_length=50, choices=NATIONALITY)
    alt_mail = models.CharField('Alternate Email Id', null=True, blank=True, max_length=50)
    photo = models.FileField( upload_to = "uploads/photos/", null=True, blank=True)
    marital_status = models.CharField('Marital Status', null=True, blank=True, max_length=20, choices=MARITAL_STATUS)
    dob = models.DateTimeField('DOB', null=True, blank=True)
    age = models.IntegerField('Age', null=True, blank=True)
    education = models.ForeignKey(Education, null=True, blank=True)
    employment = models.ForeignKey(Employment, null=True, blank=True)
    applied_jobs  = models.ManyToManyField(Job)

    def __unicode__(self):
        return self.profile.user.username

    class Meta:
        verbose_name = 'JobSeekerProfile'
        verbose_name_plural = 'JobSeekerProfile'

class RecruiterProfile(models.Model):

    profile = models.ForeignKey(UserProfile)
    company = models.ForeignKey(CompanyProfile, null=True, blank=True)

    def __unicode__(self):
        return self.profile.user.username

    class Meta:
        verbose_name = 'RecruiterProfile'
        verbose_name_plural = 'RecruiterProfile'


class SuccessStory(models.Model):

    title = models.CharField('Title', max_length=50, null=True, blank=True)
    story = models.TextField('Story', null=True, blank=True)
    publish = models.BooleanField('Publish', default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        
        verbose_name = 'SuccessStory'
        verbose_name_plural = 'SuccessStory'


class Recommendation(models.Model):

    recommendation_data = models.TextField('Recommendation', null=True, blank=True)

    def __unicode__(self):
        return self.recommendation_data

    class Meta:

        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendation' 

       