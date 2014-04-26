 function validateEmail(email) { 
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function search_by_location(search_type){
  if (search_type == 'location') {
    var url = '/search/?location=location';
    document.location.href = url;
  }
  if (search_type == 'skills') {
    var url = '/search/?skills=skills';
    document.location.href = url;
  }
}

function search_by_skills(search_type){
  if (search_type == 'skills') {
    var url = '/search/?skills=skills';
    document.skills.href = url;
  }
}

function search_by_function(search_type){
  if (search_type == 'function') {
    var url = '/search/?function=function';
    document.function.href = url;
  }
}

function search_by_industry(search_type){
  if (search_type == 'industry') {
    var url = '/search/?industry=industry';
    document.industry.href = url;
  }
}

function validation($scope) {

    if ($scope.skill == '' || $scope.skill == undefined) {
        $scope.is_keyword = true;
        $scope.is_location = false;
        $scope.is_exp = false;
        $scope.is_function = false;
        return false;
    } else if ($scope.job_location == '' || $scope.job_location ==undefined) {
        $scope.is_location = true;
        $scope.is_keyword = false;
        $scope.is_exp = false;
        $scope.is_function = false;
        return false;
    } else if ($scope.experience == 'select') {
        $scope.is_exp = true;
        $scope.is_location = false;
        $scope.is_keyword = false;
        $scope.is_function = false;
        return false;
    } else if ($scope.functional_area == 'select') {
        $scope.is_function = true;
        $scope.is_keyword = false;
        $scope.is_location = false;
        $scope.is_exp = false;
        return false;
    }
    return true;
}

function search_job($scope, search_option) {
    if (search_option) {
        $scope.error_flag = false;
        $scope.error_message = '';
        if(search_option == 'location') {
            console.log('in location')
            if (($scope.search.location == '' || $scope.search.location == undefined)) {
                $scope.error_flag = true;
                $scope.error_message = 'Please enter value for the location';
                
            }  else {
                $scope.error_flag = false;
                $scope.error_message = '';
                var url = '/search/jobs/?location='+$scope.search.location;
                document.location.href = url;
            }
        } else if (search_option == 'skills') {
            if (($scope.search.keyword == '' || $scope.search.keyword == undefined)) {
                $scope.error_flag = true;
                $scope.error_message = 'Please enter value for the skills';
                
            }  else {
                $scope.error_flag = false;
                $scope.error_message = '';
                var url = '/search/jobs/?skills='+$scope.search.keyword;
                document.location.href = url;
            }
        } else {
            if (($scope.search.keyword == '' || $scope.search.keyword == undefined) && ($scope.search.location == '' || $scope.search.location == undefined) && ($scope.search.experience == '' || $scope.search.experience == undefined) && ($scope.search.function_name == '' || $scope.search.function_name == undefined)) {
                $scope.error_flag = true;
                $scope.error_message = 'Please enter value for the any of the criteria';
                $scope.alert_style = {border: '1px solid #FF0000'};
                
            }  else {
                $scope.alert_style = {};
                $scope.error_flag = false;
                $scope.error_message = '';
                var url = '/search/jobs/?location='+$scope.search.location+'&skills='+$scope.search.keyword+'&experience='+$scope.search.experience+'&function='+$scope.search.function_name+'&industry='+$scope.search.industry+'&search=true';
                document.location.href = url;
            }
        }
        
    } else {
      $scope.is_valid = validation($scope);
      if ($scope.is_valid) {
          $scope.is_keyword = false;
          $scope.is_location = false;
          $scope.is_exp = false;
          $scope.is_function = false;
          var url = '/search/jobs/?location='+$scope.job_location+'&skills='+$scope.skill+'&experience='+$scope.experience+'&function='+$scope.functional_area;
          document.location.href = url;
      }
    }
    
}


function get_countries($scope){
    $scope.countries = [
          'Afghanistan',
          'Albania',
          'Algeria',
          'American Samoa',
          'Andorra',
          'Angola',
          'Antarctica',
          'Antigua and Barbuda',
          'Argentina',
          'Armenia',
          'Aruba',
          'Ashmore and Cartier Islands',
          'Australia',
          'Austria',
          'Azerbaijan',
          'Bahamas',
          'Bahrain',
          'Bangladesh',
          'Barbados',
          'Bassas da India',
          'Belarus',
          'Belgium',
          'Belize',
          'Benin',
          'Bhutan',
          'Bolivia',
          'Bosnia and Herzegovina',
          'Botswana',
          'Bouvet Island',
          'Brazil',
          'Brunei',
          'Bulgaria',
          'Burkina Faso',
          'Burma',
          'Burundi',
          'Cambodia',
          'Cameroon',
          'Canada',
          'Cape Verde',
          'Central African Republic',
          'Chad',
          'Chile',
          'China',
          'Colombia',
          'Comoros',
          'Democratic Republic of the Congo',
          'Republic of the Congo',
          'Coral Sea Islands',
          'Costa Rica',
          "Cote d'Ivoire",
          'Croatia',
          'Cuba',
          'Cyprus',
          'Czech Republic',
          'Denmark',
          'Djibouti',
          'Dominica',
          'Dominican Republic',
          'Ecuador',
          'Egypt',
          'El Salvador',
          'Equatorial Guinea',
          'Eritrea',
          'Estonia',
          'Ethiopia',
          'Europa Island',
          'Fiji',
          'Finland',
          'France',
          'French Southern and Antarctic Lands',
          'Gabon',
          'Gambia',
          'Gaza Strip',
          'Georgia',
          'Germany',
          'Ghana',
          'Glorioso Islands',
          'Greece',
          'Grenada',
          'Guatemala',
          'Guinea',
          'Guinea-Bissau',
          'Guyana',
          'Haiti',
          'Holy See (Vatican City)',
          'Honduras',
          'Hong Kong (China)',
          'Hungary',
          'Iceland',
          'India',
          'Indonesia',
          'Iran',
          'Iraq',
          'Ireland',
          'Israel',
          'Italy',
          'Jamaica',
          'Jan Mayen',
          'Japan',
          'Jordan',
          'Juan de Nova Island',
          'Kazakhstan',
          'Kenya',
          'Kiribati',
          'Korea, North',
          'Korea, South',
          'Kuwait',
          'Kyrgyzstan',
          'Laos',
          'Latvia',
          'Lebanon',
          'Lesotho',
          'Liberia',
          'Libya',
          'Liechtenstein',
          'Lithuania',
          'Luxembourg',
          'Macau (China)',
          'Macedonia',
          'Madagascar',
          'Malawi',
          'Malaysia',
          'Maldives',
          'Mali',
          'Malta',
          'Marshall Islands',
          'Mauritania',
          'Mauritius',
          'Mexico',
          'Federated States of Micronesia',
          'Moldova',
          'Monaco',
          'Mongolia',
          'Morocco',
          'Mozambique',
          'Namibia',
          'Nauru',
          'Nepal',
          'Netherlands',
          'Netherlands Antilles',
          'New Zealand',
          'Nicaragua',
          'Niger',
          'Nigeria',
          'Norway',
          'Oman',
          'Pakistan',
          'Palau',
          'Panama',
          'Papua New Guinea',
          'Paracel Islands',
          'Paraguay',
          'Peru',
          'Philippines',
          'Poland',
          'Portugal',
          'Qatar',
          'Reunion',
          'Romania',
          'Russia',
          'Rwanda',
          'Saint Helena',
          'Saint Kitts and Nevis',
          'Saint Lucia',
          'Saint Vincent and the Grenadines',
          'Samoa',
          'San Marino',
          'Sao Tome and Principe',
          'Saudi Arabia',
          'Senegal',
          'Serbia',
          'Seychelles',
          'Sierra Leone',
          'Singapore',
          'Slovakia',
          'Slovenia',
          'Solomon Islands',
          'Somalia',
          'South Africa',
          'Spain',
          'Spratly Islands',
          'Sri Lanka',
          'Sudan',
          'Suriname',
          'Svalbard',
          'Swaziland',
          'Sweden',
          'Switzerland',
          'Syria',
          'Taiwan',
          'Tajikistan',
          'Tanzania',
          'Thailand',
          'Timor-Leste',
          'Togo',
          'Tonga',
          'Trinidad and Tobago',
          'Tromelin Island',
          'Tunisia',
          'Turkey',
          'Turkmenistan',
          'Tuvalu',
          'Uganda',
          'Ukraine',
          'United Arab Emirates',
          'United Kingdom',
          'United States',
          'Uruguay',
          'Uzbekistan',
          'Vanuatu',
          'Venezuela',
          'Vietnam',
          'West Bank',
          'Western Sahara',
          'Yemen',
          'Zambia',
          'Zimbabwe ', 
          'Other',
    ]
}

function get_basic_education($scope){
    $scope.basic_education = [
        'Diploma',
        'Intermediate Schooling',
        'Secondary Schooling',
        'Bachelor of Architecture',
        'Bachelor of Arts',
        'Bachelor of Business Administration',
        'Bachelor of Commerce'  ,
        'Bachelor of Dental Sugery' ,
        'Bachelor of Education' ,
        'Bachelor of Hotel Management'  ,
        'Bachelor of Laws (LLB)'    ,
        'Bachelor of Pharmacy'  ,
        'Bachelor of Science'   ,
        'Bachelor of Technology/Engineering'    ,
        'Bachelor of Vetirenary Science'    ,
        'Bachelor of Computer Application'  ,
        'MBBS',        
        'Other',
    ]
}

function get_masters_education($scope){
    $scope.masters_education = [
        'Chartered Accountant',
        'CA Inter',
        'Chartered Financial Analyst',
        'Company Secretary',
        'Doctor of Medicine (MD)',
        'Doctor of Surgery (MS)',
        'Inst. of Cost & Works Accountants',
        'ICWA Inter',
        'Master of Architecture',
        'Master of Arts',
        'Master of Commerce',
        'Master of Education',
        'Master of Laws (LLM)',
        'Master of Pharmacy',
        'Master of Technology/Engineering',
        'Master of Vetirenary Science',
        'Master of Computer Application',
        'MBA/PG Diploma in Business Mgmt ',
        'Other',
    ]

}

function get_education_required($scope){
    $scope.education_required = [
        'Diploma',
        'Intermediate Schooling',
        'Secondary Schooling',
        'Bachelor of Architecture',
        'Bachelor of Arts',
        'Bachelor of Business Administration',
        'Bachelor of Commerce'  ,
        'Bachelor of Dental Sugery' ,
        'Bachelor of Education' ,
        'Bachelor of Hotel Management'  ,
        'Bachelor of Laws (LLB)'    ,
        'Bachelor of Pharmacy'  ,
        'Bachelor of Science'   ,
        'Bachelor of Technology/Engineering'    ,
        'Bachelor of Vetirenary Science'    ,
        'Bachelor of Computer Application'  ,
        'MBBS',
        'Chartered Accountant',
        'CA Inter',
        'Chartered Financial Analyst',
        'Company Secretary',
        'Doctor of Medicine (MD)',
        'Doctor of Surgery (MS)',
        'Inst. of Cost & Works Accountants',
        'ICWA Inter',
        'Master of Architecture',
        'Master of Arts',
        'Master of Commerce',
        'Master of Education',
        'Master of Laws (LLM)',
        'Master of Pharmacy',
        'Master of Technology/Engineering',
        'Master of Vetirenary Science',
        'Master of Computer Application',
        'MBA/PG Diploma in Business Mgmt ',
        'Other',
    ]

}

function get_nationalities($scope){
    $scope.nationalities = [

        'Afganistani',
        'Albanian',
        'Algerian',
        'American Samoa',
        'Andorra',
        'Angola',
        'Anguilla',
        'Antarctican',
        'Antigua and Barbuda',
        'Argentina',
        'Armenian',
        'Aruba',
        'Australian',
        'Austrian',
        'Azerbaijan',
        'Bahamas',
        'Bahraini',
        'Bangladeshi',
        'Barbados',
        'Belarus',
        'Belgium',
        'Belize',
        'Benin',
        'Bermuda',
        'Bhutani',
        'Bolivian',
        'Bosnia and Herzegovinan',
        'Botswana',
        'Bouvet Island',
        'Brazilian',
        'British Indian Ocean Territory',
        'Brunei Darussalam',
        'Bulgarian',
        'Burkina Faso',
        'Burundi',
        'Cambodian',
        'Cameroon',
        'Canadian',
        'Cape Verde',
        'Cayman Islands',
        'Central African Republic',
        'Chad',
        'Chile',
        'Chinese',
        'Christmas Island',
        'Cocos (Keeling) Islands',
        'Colombian',
        'Comoros',
        'Congo',
        'Cook Islands',
        'Costa Rica',
        "Cote D'Ivoire",
        'Croatia',
        'Cuban',
        'Cyprus',
        'Czech Republic',
        'Denmark',
        'Djibouti',
        'Dominica',
        'Dominican Republic',
        'Ecuador',
        'Egyptian',
        'El Salvador',
        'Emirati',
        'Equatorial Guinea',
        'Eritrea',
        'Estonia',
        'Ethiopian',
        'Falkland Islands (Malvinas)',
        'Faroe Islands',
        'Fiji',
        'Filipino',
        'Finland',
        'French',
        'French Guiana',
        'French Polynesia',
        'French Southern Territories',
        'Gabon',
        'Georgian',
        'German',
        'Ghana',
        'Gibraltar',
        'Greece',
        'Greenland',
        'Grenada',
        'Guadeloupe',
        'Guam',
        'Guinean',
        'Guinea-Bissau',
        'Guyana',
        'Haiti',
        'Heard Island and Mcdonald Islands',
        'Holy See (Vatican City State)',
        'Honduras',
        'Hong Kong',
        'Hungarian',
        'Iceland',
        'Indian',
        'Indonesian',
        'Iranian',
        'Ireland',
        'Israeli',
        'Japanese',
        'Jordanian',
        'Kazakhstani',
        'Kenyan',
        'Kiribati',
        "Korea, Democratic People's Republic of",
        'Korea, Republic of',
        'Kuwaiti',
        'Kyrgyzstani',
        "Lao People's Democratic Republic",
        'Latvian',
        'Lebanese',
        'Lesotho',
        'Liberian',
        'Libyan Arab Jamahiriya',
        'Liechtenstein',
        'Lithuania',
        'Luxembourg',
        'Macao',
        'Macedonia, the Former Yugoslav Republic of',
        'Madagascar',
        'Malawi',
        'Malaysian',
        'Maldives',
        'Mali',
        'Malta',
        'Marshall Islands',
        'Martinique',
        'Mauritanian',
        'Mauritius',
        'Mayotte',
        'Mexican',
        'Micronesia, Federated States of',
        'Moldova, Republic of',
        'Monaco',
        'Mongolian',
        'Montserrat',
        'Moroccan',
        'Mozambique',
        'Myanmar',
        'Namibia',
        'Nauru',
        'Nepalese',
        'Netherlands',
        'Netherlands Antilles',
        'New Caledonia',
        'New Zealand',
        'Nicaragua',
        'Niger',
        'Nigerian',
        'Niue',
        'Norfolk Island',
        'Northern Mariana Islan',
        'Norway',
        'Omani',
        'Pakistani',
        'Palau',
        'Palestinian',
        'Panama',
        'Papua New Guinea',
        'Paraguay',
        'Peru',
        'Pitcairn',
        'Poland',
        'Portugal',
        'Puerto Rico',
        'Qatari',
        'Reunion',
        'Romanian',
        'Russian',
        'Rwanda',
        'Saint Helena',
        'Saint Kitts and Nevis',
        'Saint Lucia',
        'Saint Pierre and Miquelon',
        'Saint Vincent and the Grenadines',
        'Samoa',
        'San Marino',
        'Sao Tome and Principe',
        'Saudi',
        'Senegal',
        'Serbia and Montenegro',
        'Seychelles',
        'Sierra Leone',
        'Singaporean',
        'Slovakian',
        'Slovenian',
        'Solomon - Islands   ',
        'Somalian',
        'South African',
        'South Georgia and the South Sandwich Islands',
        'Spanish',
        'Sri Lankan',
        'Sudanese',
        'Suriname',
        'Svalbard and Jan Mayen',
        'Swaziland',
        'Sweden',
        'Switzerland',
        'Syrian',
        'Taiwanese',
        'Tajikistan',
        'Tanzania, United Republic of',
        'Thai',
        'Timor-Leste',
        'Togo',
        'Tokelau',
        'Tonga',
        'Trinidad and Tobago',
        'Tunisia',
        'Turkish',
        'Turkmenistan',
        'Turks and Caicos Islands',
        'Tuvalu',
        'Uganda',
        'Ukraine',
        'United Kingdom',
        'United States',
        'United States Minor Outlying Islands',
        'Uruguay',
        'Uzbekistani',
        'Vanuatu',
        'Venezuela',
        'Vietnamese',
        'Virgin Islands, British',
        'Virgin Islands, U.s.',
        'Wallis and Futuna',
        'Western Sahara',
        'Yemeni',
        'Zambian',
        'Zimbabwe',
        'Other',
        
    ]
}


function get_industries($scope){
    $scope.industries = [
    'Automotive/ Ancillaries',
        'Banking/ Financial Services',
        'Bio Technology and Life Sciences',
        'Chemicals/Petrochemicals',
        'Construction',
        'FMCG',
        'Education',
        'Entertainment/ Media/ Publishing',
        'Insurance',
        'ITES/BPO',
        'IT/ Computers - Hardware',
        'IT/ Computers - Software',
        'KPO/Analytics',
        'Machinery/ Equipment Mfg.',
        'Oil/ Gas/ Petroleum',
        'Pharmaceuticals',
        'Plastic/ Rubber',
        'Power/Energy',
        'Real Estate',
        'Retailing',
        'Telecom',
        'Advertising/PR/Events',
        'Agriculture/ Dairy Based',
        'Aviation/Aerospace',
        'Beauty/Fitness/PersonalCare/SPA',
        'Beverages/ Liquor',
        'Cement',
        'Ceramics and Sanitary Ware',
        'Consultancy',
        'Courier/ Freight/ Transportation',
        'Dotcom',
        'Electrical/Switchgear',
        'Engineering, Procurement, Construction',
        'Environmental Service',
        'Facility management',
        'Fertilizer/ Pesticides',
        'Food and Packaged Food',
        'Textiles / Yarn / Fabrics / Garments',
        'Gems/ Jewellery',
        'Government/ PSU/ Defence',
        'Consumer Electronics/Appliances',
        'Hospitals/ Health Care',
        'Hotels/ Restaurant',
        'Import / Export',
        'Iron/ Steel',
        'ISP',
        'Law Enforcement/Security Services',
        'Leather',
        'Market Research',
        'Medical Transcription',
        'Mining',
        'NGO',
        'Non-Ferrous Metals',
        'Office Equipment/Automation',
        'Paints',
        'Paper',
        'Printing/ Packaging',
        'Public Relations (PR)',
        'Import / Export',
        'Iron/ Steel',
        'ISP',
        'Law Enforcement/Security Services',
        'Leather',
        'Market Research',
        'Medical Transcription',
        'Mining',
        'NGO',
        'Import / Export',
        'Iron/ Steel',
        'ISP',
        'Law Enforcement/Security Services',
        'Leather',
        'Market Research',
        'Medical Transcription',
        'Mining',
        'NGO',
        'Shipping/ Marine Services',
        'Travel/ Tourism',
        'Tyres',
        'Wood',
        'Travel/ Tourism',
        'Other',
        
    ]
}


function get_functions($scope){
    $scope.functions = [
        'Construction',
        'Banking/Financial Services/Broking',
        'Oil/ Gas/ Petroleum',
        'IT - Software Services',
        'Medical/Healthcare/Diagnistics/Medical Devices',
        'Hotels/Hospitality/Tourism/Recreative',
        'Advertising/Pr/Events',
        'Agriculture/Dairy/Poultry',
        'Hotels/Hospitality/Tourism/Recreative',
        'Air Conditioning/Refrigeration',
        'Airline/Aviation',
        'Architecture/Interior Designing',
        'Automotive/Auto Ancillary',
        'Chemicals/PetroChemical',
        'Consumer Durables/Consumer Electronics',
        'Courier/Logistics/Transportation/Warehousing',
        'Defence/Militarnmenty/Government',
        'Education/Training/Teaching',
        'Export/Import/General Trading',
        'Fertilizers/Pesticides',
        'FMGG/Foods/Beverage',
        'Fresher - No industry Experience/Not Employed/Intern',
        'Gems/ Jwellery',
        'Industrial Products/Heavy Machinery',
        'Insurance',
        'Internet/E-Commerece/Dotcom',
        'IT - Hardware and Networking',
        'Media/Entertainment/Publishing',
        'Metals/Steel/Iron/Aluminium/Foundry/Electroplating',
        'Mining/Forestry/Fishing',
        'NGO/Social Services',
        'Office Automation/Equipment/Stationary',
        'Paper',
        'Pharma/Biotech/Clinical Research',
        'Plastics/Rubber',
        'Power/Energy',
        'Printing/Packing',
        'Real Estate',
        'Recruitment/Placement Firm',
        'Restaurants/Catering',
        'Retail',
        'Security/Law Enforcement',
        'Shipping/Freight',
        'Telecom/ISP',
        'Textiles/Garments/Accesories/Fashion',
        'Tyres',
        'Other',
    ]
}

function get_currencies($scope){
    $scope.currencies = ['US Dollars',
        'UK Pound',
        'Indian Rupees', 
        'UAE Dhirhams',
        'Dinar',        
        'Riyal',
        'Australian Dollars',
        'Singapore Dollars',
        'Sri Lankan Rupee',
        'Euro',        
        'Yen',       
    ]
}

function HomeController($scope, $element, $http, $timeout, share, $location)
{
    $scope.is_keyword = false;
    $scope.is_location = false;
    $scope.is_exp = false;
    $scope.is_function = false;
    $scope.experiences = [];
    $scope.experience = 'select';
    $scope.functional_area = 'select';

    $scope.init = function(csrf_token) {
        $scope.csrf_token = csrf_token;
        for(var i=0; i<=30; i++) {
            $scope.experiences.push(i);
        }
        get_functions($scope);
    }
    $scope.post_cv = function(){
        document.location.href = '/job_seeker_registration/';
    }
    $scope.job_search  = function() {
        search_job($scope, '');
    }
}

function JobSeekerController($scope, $element, $http, $timeout) {

    $scope.year = [];
    $scope.months =[];
    $scope.experience =[];

    $scope.is_valid = false;
    $scope.error_flag = false;
    $scope.error_message = '';

    $scope.certificate_img = {};
    $scope.certificate_img.src = "";

    $scope.photo_img = {};
    $scope.photo_img.src = "";

    $scope.resume_doc = {};
    $scope.resume_doc.src = "";

  $scope.checkbox = false;

    $scope.seeker = {
        'id': 0,
        'email': '',
        'password': '', 
        'password1': '',
        'first_name': '',
        'gender': '',
        'dob':'',
        'marital_status': '',
        'nationality': '',
        'country': '',
        'city': '',
        'mobile': '',
        'alt_email': '',
        'basic_edu': '',
        'pass_year_basic': '',
        'masters_edu': '',
        'pass_year_masters': '',
        'doctrate': '',
        'resume_title': '',
        'resume_text': '',
        'resume': '',
    }

    $scope.seeker1 = {
        'years': '',
        'months': '',
        'salary': '',
        'designation': '',
        'industry': '',
        'functions': '',
        'skills': '',
        'certificate_img': '',
        'profile_photo': '',
    }

    $scope.init = function(csrf_token, user_id, profile_edit) {
        $scope.csrf_token = csrf_token;
        $scope.user_id = user_id;
        $scope.profile_edit = profile_edit;
        get_countries($scope);
        get_nationalities($scope);
        get_industries($scope);
        get_functions($scope);
        get_basic_education($scope);
        get_masters_education($scope);
        for(var i=1970; i<=2014; i++){
            $scope.year.push(i);
        }
        for(var i=0; i<=50; i++){
            $scope.experience.push(i);
        }
        if(profile_edit){
            $http.get('/profile/details/'+$scope.user_id+'/').success(function(data)
            {
                $scope.seeker = data.seeker[0]; 
                $('#dob').val($scope.seeker.dob);
                $scope.seeker1 = data.seeker1[0];
                $scope.seeker.id = $scope.user_id;
            }).error(function(data, status)
            {
                console.log(data || "Request failed");
            });
        }
    }
    
    $scope.form_validation = function(){
        var letters = /^[A-Za-z]+$/;  
        $scope.seeker.dob = $('#dob').val();
        if ($scope.resume_doc.src){
            $scope.seeker.resume = $scope.resume_doc.src; 
        }
        if (!(validateEmail($scope.seeker.email))){
            $scope.error_flag = true;
            $scope.error_message = 'Please provide a Valid Email Id';
            return false;
        } else if (($scope.user_id == '' || $scope.user_id == undefined) && ($scope.seeker.password == '' || $scope.seeker.password == undefined)) {
            $scope.error_flag = true;
            $scope.error_message = 'Please provide a Password';
            return false;
        } else if (($scope.user_id == '' || $scope.user_id == undefined) && ($scope.seeker.password1 == '' || $scope.seeker.password1 == undefined)) {
            $scope.error_flag = true;
            $scope.error_message = 'Please Re-enter the Password';
            return false;
        } else if (($scope.user_id == '' || $scope.user_id == undefined) && ($scope.seeker.password != $scope.seeker.password1)) {
            $scope.error_flag = true;
            $scope.error_message = 'Please enter the Password Correctly';
            return false;
        } else if ($scope.seeker.first_name == '' || $scope.seeker.first_name == undefined){
            $scope.error_flag = true;
            $scope.error_message = 'Please enter your Name';
            return false;
        } else if ($scope.seeker.gender == '' || $scope.seeker.gender == undefined){
            $scope.error_flag = true;
            $scope.error_message = 'Please provide your Gender';
            return false;
        } else if ($scope.seeker.dob == '' || $scope.seeker.dob == undefined){
            $scope.error_flag = true;
            $scope.error_message = 'Please provide your Date of Birth';
            return false;
        } else if ($scope.seeker.marital_status == '' || $scope.seeker.marital_status == undefined || $scope.seeker.marital_status == 'select'){
            $scope.error_flag = true;
            $scope.error_message = 'Please select your Marital Status';
            return false;
        } else if ($scope.seeker.nationality == '' || $scope.seeker.nationality == undefined || $scope.seeker.nationality == 'select'){
            $scope.error_flag = true;
            $scope.error_message = 'Please select your Nationality';
            return false;
        } else if ($scope.seeker.country == '' || $scope.seeker.country == undefined || $scope.seeker.country == 'select'){
            $scope.error_flag = true;
            $scope.error_message = 'Please select Country';
            return false;
        } else if ($scope.seeker.city == '' || $scope.seeker.city == undefined){
            $scope.error_flag = true;
            $scope.error_message = 'Please enter your city';
            return false;
        } else if ($scope.seeker.mobile == '' || $scope.seeker.mobile == undefined || $scope.seeker.mobile.match(letters)) {
            $scope.error_flag = true;
            $scope.error_message = 'Please enter a Valid Mobile Number';
            return false;
        } else if ($scope.seeker.basic_edu == '' || $scope.seeker.basic_edu == undefined || $scope.seeker.basic_edu == "select Bachelor's/Diploma/School" || $scope.basic_edu == "Bachelor's Course" || $scope.basic_edu == 'Diploma Course' || $scope.basic_edu == 'Schooling'){
            $scope.error_flag = true;
            $scope.error_message = 'Please select Basic Education';
            return false;
        } else if ($scope.seeker.pass_year_basic == '' || $scope.seeker.pass_year_basic == undefined || $scope.seeker.pass_year_basic == 'select'){
            $scope.error_flag = true;
            $scope.error_message = 'Please select the Year of Passing';
            return false;
        } else if ($scope.seeker.resume_title == '' || $scope.seeker.resume_title == undefined){
            $scope.error_flag = true;
            $scope.error_message = 'Please give a Title for your Resume';
            return false;
        } else if (($scope.seeker.resume == undefined || $scope.seeker.resume == '') && ($scope.seeker.resume_text == undefined || $scope.seeker.resume_text == '')){
            $scope.error_flag = true;
            $scope.error_message = 'Please Attach or Copy Paste your Resume';
            return false;
        }
        return true;
    }

  
    $scope.form_validation_more_info = function(){     

        if (($scope.seeker1.salary != '' || $scope.seeker1.salary != undefined) && $scope.seeker1.salary != Number($scope.seeker1.salary)){
         
              $scope.error_flag = true;
              $scope.error_message = 'Please enter a Valid Amount for Salary';
              return false;
        }   
        if ($scope.seeker1.skills == '' || $scope.seeker1.skills == undefined){
            $scope.error_flag = true;
            $scope.error_message = 'Please enter Skills';
            return false;
        } else if ($scope.checkbox == false){
            $scope.error_flag = true;
            $scope.error_message = 'Please Agree with our Privacy Policy and Terms & Conditions';
            return false;
        } 
        return true; 
    }


    $scope.save_reg = function(){
        
        $scope.is_valid = $scope.form_validation();
        if ($scope.is_valid) {
            $scope.error_flag = false;
            $scope.error_message = '';
            if ($scope.seeker.doctrate == null) {
                $scope.seeker.doctrate = '';
            }
            if ($scope.seeker.resume_text == null) {
                $scope.seeker.resume_text = '';
            }
            if ($scope.seeker.alt_email == null) {
                $scope.seeker.alt_email = '';
            }
            if ($scope.seeker.pass_year_masters == null) {
                $scope.seeker.pass_year_masters = '';
            }           

            var file = $scope.resume_doc.src;
            params = {
                'seeker':angular.toJson($scope.seeker),
                "csrfmiddlewaretoken" : $scope.csrf_token,              
            }
            var fd = new FormData();
            fd.append('resume_doc', $scope.resume_doc.src);
            for(var key in params){
                fd.append(key, params[key]);            
            }
            var url = "/job_seeker_registration/";
            $http.post(url, fd, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined
                }
            }).success(function(data, status){
                $scope.user_id = data.user_id;

                
                if(data.result == 'error') {
                    $scope.error_flag = true;
                    $scope.error_message = data.message;
                } else {
                    $scope.error_flag = true;
                    $scope.error_message = 'Successfully Completed the First Step of Registration. Proceed to the Next Step';
                    $http.get('/profile/details/'+$scope.user_id+'/').success(function(data)
                    {
                        $scope.seeker = data.seeker[0]; 
                        $scope.seeker1 = data.seeker1[0];
                        $scope.seeker.id = $scope.user_id;
                    }).error(function(data, status)
                    {
                        console.log(data || "Request failed");
                    });
                }
                
            }).error(function(data, status){
                $scope.error_flag = true;
                $scope.error_message = data.message;
            });
        }     
    }    

    $scope.save_reg_more = function(){

    $scope.is_valid = $scope.form_validation_more_info();
        if ($scope.is_valid) {
            if ($scope.seeker1.years == null) {
                $scope.seeker1.years = '';
            }
            if ($scope.seeker1.months == null) {
                $scope.seeker1.months = '';
            }
            if($scope.seeker1.designation == null){
                $scope.seeker1.designation = '';
            }
            if($scope.seeker1.salary == null){
                $scope.seeker1.salary = '';
            }
            if($scope.seeker1.functions == null){
                $scope.seeker1.functions = '';
            }
            if($scope.seeker1.industry == null){
                $scope.seeker1.industry = '';
            }            
            $scope.error_flag = false;
            $scope.error_message = '';


            var file = $scope.photo_img.src;
            var file = $scope.certificate_img.src;
            params = {
                'seeker1':angular.toJson($scope.seeker1),
                'user_id': $scope.user_id,
                "csrfmiddlewaretoken" : $scope.csrf_token,              
            }
            var fd = new FormData();
            fd.append('photo_img', $scope.photo_img.src)
            fd.append('certificate_img', $scope.certificate_img.src)
            for(var key in params){
                fd.append(key, params[key]);          
            }
            var url = "/job_seeker_registration_more_info/"+$scope.user_id+'/';
            $http.post(url, fd, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined
                }
            }).success(function(data, status){ 
                $scope.error_flag = true;
                $scope.error_message = 'Successfully Completed Registration';            
                console.log("Successfully Saved");
              
            }).error(function(data, status){           

            });
        }    
    }

    $scope.reg_next =function(){
        document.location.href = '/job_seeker_registration_more_info/'+$scope.user_id+'/';
    }

    $scope.view_profile = function() {
        var url = '/profile/'+$scope.user_id+'/';
        document.location.href = url;
    }
}

function RecruiterController($scope, $element, $http, $timeout) {
    $scope.error_flag = false;
    $scope.error_message = '';
    $scope.user_already_exists = false;
	$scope.init = function(csrf_token, user_id) {
		$scope.csrf_token = csrf_token;
        $scope.user_id = user_id;
        get_industries($scope);
    	   get_countries($scope);

        $scope.recruiter = {
            'name' : '',
            'industry' : '',
            'email' : '',
            'country' : '',
            'password' : '',
            'mobile' : '',
            'phone' : '',
            'city': '',
            'description': '',

        } 
        if (user_id) {
            $scope.user_already_exists = true;
            $http.get('/profile/details/'+$scope.user_id+'/').success(function(data)
            {
                $scope.recruiter = data.recruiter[0]; 
                $('#last_date').val($scope.recruiter.last_date);
                $('#post_date').val($scope.recruiter.post_date);
                
            }).error(function(data, status)
            {
                console.log(data || "Request failed");
            });
        }
    }
    $scope.recruiter_validation = function(){
        var letters = /^[A-Za-z]+$/;  
        if ($scope.recruiter.name == '' || $scope.recruiter.name == undefined) {
            $scope.error_flag = true;
            $scope.error_message = 'Please enter the Company Name';
            return false;
        } else if (!(validateEmail($scope.recruiter.email))){
            $scope.error_flag = true;
            $scope.error_message = 'Please provide a valid Email Id';
            return false;
        } else if ($scope.recruiter.industry == '' || $scope.recruiter.industry == undefined) {
            $scope.error_flag = true;
            $scope.error_message = 'Please choose the Type of Industry';
            return false;
        } else if (($scope.user_id == '' || $scope.user_id == undefined) && ($scope.recruiter.password == '' || $scope.recruiter.password == undefined)) {
            $scope.error_flag = true;
            $scope.error_message = 'Please provide a Password';
            return false;
        } else if ($scope.recruiter.mobile == '' || $scope.recruiter.mobile == undefined || $scope.recruiter.mobile.match(letters)) {
            $scope.error_flag = true;
            $scope.error_message = 'Please provide a Valid Mobile Number';
            return false;        
        } else if ($scope.recruiter.phone != '' || $scope.recruiter.phone != undefined) {
            if ($scope.recruiter.phone.match(letters)) {
              $scope.error_flag = true;
              $scope.error_message = 'Please enter a Valid Land no.';
              return false;
            }
        } 
        return true;
    }

    $scope.save_profile = function(){
        $scope.is_valid = $scope.recruiter_validation();
        if ($scope.is_valid) {
            $scope.error_flag = false;
            $scope.error_message = '';
            
            if ($scope.recruiter.description == null){
                $scope.recruiter.description = '';
            }
            if ($scope.user_id) {
                var url = '/edit_profile/recruiter/'+$scope.user_id+'/';
            } else {
                var url = '/recruiter-registration/';
            }
                
            params = {
                'recruiter':angular.toJson($scope.recruiter),
                "csrfmiddlewaretoken" : $scope.csrf_token,
            }
            var fd = new FormData();
            for(var key in params){
                fd.append(key, params[key]);          
            }
            $http.post(url, fd, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined
                }
            }).success(function(data, status){
                if ($scope.user_id) {
                  document.location.href = '/profile/'+$scope.user_id+'/';
                } else {
                  document.location.href = '/';
                } 
            }).error(function(data, status){
                $scope.error_flag = true;
                $scope.error_message = data.message;
                return false;
            });
        }
    }
}

function  JobPostingController($scope,$element,$http,$timeout){
    $scope.Min = [];
    $scope.Max = [];
    $scope.edit =1;
    $scope.is_new_company = false;
    $scope.existing_job = '------Copy From existing job----';
    $scope.jobpost = {
        'title':'',
        'code': '',
        'company': '',
        'summary': '',
        'details': '',
        'salary': '',
        'currency': '',
        'skills': '',
        'location': '-select-',
        'industry': '-select-',
        'function': '-select-',
        'requirement': '-select-',
        'specialisation': '',
        'nationality': '',
        'last_date': '',
        'post_date': '',
        'name': '',
        'phone': '',
        'email': '',
        'profile': '',
        'min':'-min-',
        'max':'-max-',
    }

	$scope.init = function(csrf_token,id) {
		$scope.csrf_token = csrf_token;
		$scope.product_pdf = {};
    $scope.product_pdf.src = "";
		get_countries($scope);
		get_nationalities($scope);
		get_industries($scope);
		get_functions($scope);
		get_education_required($scope);
    get_currencies($scope);
    $scope.job_id = id;
    for(var i=0; i<=50; i++){
        $scope.Min.push(i);
        $scope.Max.push(i);
    } 
    $http.get('/companies/').success(function(data)
    {
        $scope.companies = data.companies; 
    }).error(function(data, status)
    {
        console.log(data || "Request failed");
    });

    if ($scope.job_id){
      $http.get('/job/details/'+$scope.job_id+'/').success(function(data)
            {
                $scope.jobpost = data.jobpost[0]; 
                console.log(data.jobpost[0]);
                console.log($scope.jobpost);
                $('#last_date').val($scope.jobpost.last_date);
                $('#post_date').val($scope.jobpost.post_date);
            }).error(function(data, status)
            {
                console.log(data || "Request failed");
            });
    }
		
  }

  $scope.form_validation_postjob = function(){
    var letters = /^[A-Za-z]+$/;  
    $scope.jobpost.last_date = $('#last_date').val();
    $scope.jobpost.post_date = $('#post_date').val();
    if ($scope.jobpost.company == 'other'){
        $scope.jobpost.company = $scope.new_company 
    }    
    if ($scope.jobpost.title == ''|| $scope.jobpost.title == undefined){
      $scope.error_flag = true;
      $scope.error_message = 'Please provide a Job Title';
      return false;
    } else if ($scope.jobpost.code == '' || $scope.jobpost.code == undefined) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide Reference Code';
      return false;
    } else if ($scope.jobpost.company == 'other' || $scope.jobpost.company == '' || $scope.jobpost.company == undefined) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide Company Name';
      return false; 
    }  else if ($scope.jobpost.summary == '' || $scope.jobpost.summary == undefined) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide Job summary';
      return false;
    }  else if ($scope.jobpost.salary != '' && ($scope.jobpost.currency == '' || $scope.jobpost.currency == undefined)) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Currency';
      return false;
    } else if ($scope.jobpost.skills == '' || $scope.jobpost.skills == undefined) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Required Skills';
      return false;
    } else if ($scope.jobpost.min != 0 ) {
      if($scope.jobpost.min == '' || $scope.jobpost.min == undefined || $scope.jobpost.min == '-min-'){
        console.log('$scope.jobpost.min', $scope.jobpost.min, $scope.jobpost.min == '' , $scope.jobpost.min == undefined, $scope.jobpost.min == '-min-');
        $scope.error_flag = true;
        $scope.error_message = 'Please provide the minimum Experience Required';
        return false;
      }
    } else if ($scope.jobpost.max != 0 ) {
      if($scope.jobpost.max == '' || $scope.jobpost.max == undefined || $scope.jobpost.max == '-min-'){
        $scope.error_flag = true;
        $scope.error_message = 'Please provide the maximum Experience Required';
        return false;
      }
    } else if ($scope.jobpost.location == '' || $scope.jobpost.location == undefined || $scope.jobpost.location == '-select-') {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Job location';
      return false;
    } else if ($scope.jobpost.industry == '' || $scope.jobpost.industry == undefined || $scope.jobpost.industry == '-select-') {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Industry';
      return false;
    } else if ($scope.jobpost.function == '' || $scope.jobpost.function == undefined || $scope.jobpost.function == '-select-') {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Category/Function';
      return false;
    } else if ($scope.jobpost.requirement == '' || $scope.jobpost.requirement == undefined || $scope.jobpost.requirement == '-select-') {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Education Required';
      return false;
    } else if ($scope.jobpost.nationality == '' || $scope.jobpost.nationality == undefined || $scope.jobpost.nationality == '-select-') {
      $scope.error_flag = true;
      $scope.error_message = 'Please select your Nationality';
      return false;
    } else if ($scope.jobpost.name == '' || $scope.jobpost.name == undefined) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Name of the Job Owner';
      return false;
    } else if ($scope.jobpost.phone == '' || $scope.jobpost.phone == undefined || $scope.jobpost.phone.match(letters)) {
      $scope.error_flag = true;
      $scope.error_message = 'Please enter a Valid Phone Number';
      return false;
    } else if (!(validateEmail($scope.jobpost.email))) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide a Valid Email Id';
      return false;
    } else if ($scope.jobpost.profile == '' || $scope.jobpost.profile == undefined) {
      $scope.error_flag = true;
      $scope.error_message = 'Please provide the Company Profile';
      return false;
    } 
    return true;
  }


    $scope.save_job = function(){

      $scope.jobpost.last_date = $('#last_date').val();
      $scope.jobpost.post_date = $('#post_date').val();
        $scope.is_valid = $scope.form_validation_postjob();
        if ($scope.is_valid) {
          $scope.error_flag = false;
          $scope.error_message = '';
          if ($scope.jobpost.post_date == null) {
            $scope.jobpost.post_date = '';
          }
          if ($scope.jobpost.last_date == null) {
            $scope.jobpost.last_date = '';
          }
            var file = $scope.product_pdf.src;
            var edit =$scope.edit;
            params = {
                    'jobpost':angular.toJson($scope.jobpost),
                    "csrfmiddlewaretoken" : $scope.csrf_token,
                }
            var fd = new FormData();
            fd.append('product_pdf', $scope.product_pdf.src);
            for(var key in params){
              fd.append(key, params[key]);
            }
            if($scope.job_id) {
              var url = "/recruiter/post-jobs/edit/"+$scope.job_id+"/";
            } else {
              if(edit == 1){
                  var url = "/recruiter/post-jobs/";               
              }
              
            } 
            $http.post(url, fd, {
                    transformRequest: angular.identity,
                    headers: {'Content-Type': undefined
                    }
                    
                }).success(function(data, status){
                    $scope.id = data.id;
                    $scope.edit = $scope.edit + 1;  
                    
                    var url = '/posted_jobs/';
                    document.location.href = url;

              }).error(function(data, status){
                  console.log(data);
            });
          
        }
        
    }
    
    $scope.view_posted_jobs = function() {
        var url = '/posted_jobs/';
        document.location.href = url;
    }

    $scope.get_company_name = function(){
        if($scope.jobpost.company == 'other'){
          $scope.is_new_company = true;
        }
        
    }
}

function  SearchController($scope,$element,$http,$timeout){

    $scope.experiences = [];

    $scope.alert_style = {};
    
    $scope.search = {
        'keyword' : '',
        'location' : '',
        'experience' : '',
        'function_name' : '',
        'industry' : '',
    }

    $scope.init = function(csrf_token) {
        $scope.csrf_token = csrf_token;
        get_functions($scope);
        get_industries($scope);

        for(var i=0; i<=50; i++){
            $scope.experiences.push(i);
        }
    }

    $scope.search = function(search_type){
        search_job($scope, search_type);
    } 

    $scope.search_cv = function() {
        if (($scope.resume_title == '' || $scope.resume_title == undefined) && ($scope.age == '' || $scope.age == undefined) && ($scope.keyword == '' || $scope.keyword == undefined)) {
                $scope.error_flag = true;
                $scope.error_message = 'Please enter value for the any of the criteria';
                $scope.alert_style = {border: '1px solid #FF0000'};
                
        }  else {
            $scope.alert_style = {};
            $scope.error_flag = false;
            $scope.error_message = '';
            var url = '/search_cv/?cv_title='+$scope.resume_title+'&age='+$scope.age+'&keyword='+$scope.keyword;
            document.location.href = url;
        }

    }
}