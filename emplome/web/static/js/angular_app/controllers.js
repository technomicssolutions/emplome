function get_countries($scope){
    $scope.countries = [
          'Afghanistan',
          'Albania',
          'Algeria',
          'American Samoa',
          'Andorra',
          'Angola',
          // 'Antarctica',
          'Antigua and Barbuda',
          'Argentina',
          'Armenia',
          // 'Aruba',
          // 'Ashmore and Cartier Islands',
          'Australia',
          'Austria',
          'Azerbaijan',
          'Bahamas',
          'Bahrain',
          'Bangladesh',
          'Barbados',
          // 'Bassas da India',
          'Belarus',
          'Belgium',
          'Belize',
          'Benin',
          'Bhutan',
          'Bolivia',
          'Bosnia and Herzegovina',
          'Botswana',
          // 'Bouvet Island',
          'Brazil',
          'Brunei',
          'Bulgaria',
          'Burkina Faso',
          // 'Burma',
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
          // 'Coral Sea Islands',
          'Costa Rica',
          // "Cote d'Ivoire",
          'Croatia',
          'Cuba',
          'Cyprus',
          'Czech Republic',
          // 'Denmark',
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
          // 'Europa Island',
          'Fiji',
          'Finland',
          'France',
          // 'French Southern and Antarctic Lands',
          'Gabon',
          'Gambia',
          // 'Gaza Strip',
          'Georgia',
          'Germany',
          'Ghana',
          // 'Glorioso Islands',
          'Greece',
          'Grenada',
          'Guatemala',
          'Guinea',
          'Guinea-Bissau',
          'Guyana',
          'Haiti',
          // 'Holy See (Vatican City)',
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
          // 'Jan Mayen',
          'Japan',
          'Jordan',
          // 'Juan de Nova Island',
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
          // 'Netherlands',
          // 'Netherlands Antilles',
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
          // 'Paracel Islands',
          'Paraguay',
          'Peru',
          // 'Philippines',
          'Poland',
          'Portugal',
          'Qatar',
          // 'Reunion',
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
          // 'Spratly Islands',
          'Sri Lanka',
          'Sudan',
          'Suriname',
          // 'Svalbard',
          'Swaziland',
          'Sweden',
          'Switzerland',
          'Syria',
          'Taiwan',
          'Tajikistan',
          'Tanzania',
          'Thailand',
          // 'Timor-Leste',
          'Togo',
          'Tonga',
          'Trinidad and Tobago',
          // 'Tromelin Island',
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
          // 'West Bank',
          // 'Western Sahara',
          'Yemen',
          'Zambia',
          'Zimbabwe ', 
    ]
}



function HomeController($scope, $element, $http, $timeout, share, $location)
{
  
}
function Registration($scope)
{
	
}

function JobSeekerController($scope, $element, $http, $timeout) {


	$scope.init = function(csrf_token) {
		$scope.csrf_token = csrf_token;
		get_countries($scope);
		
	}
}
