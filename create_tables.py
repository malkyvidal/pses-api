import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table_continentes = "CREATE TABLE  IF NOT EXISTS continentes (id INTEGER PRIMARY KEY,nombre text )"
create_Table_Paises = "CREATE TABLE IF NOT EXISTS paises (id INTEGER PRIMARY KEY , nombre text, capital text, id_cont int)"
create_Table_Usuarios = "CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_continentes)
cursor.execute(create_Table_Paises)

cursor.execute(create_Table_Usuarios)

insert_usuario = "INSERT INTO usuarios values(null,?,?)"

cursor.execute(insert_usuario,('pypauser','aabb1122'))


continentes = [('AFRICA',),('AMERICA',),('ASIA',),('EUROPA',),('OCEANIA',)] 
insert_cont = "INSERT INTO continentes VALUES(null,?)"
cursor.executemany(insert_cont,continentes)

insert_paises = "INSERT INTO paises VALUES(null,?,?,?)"

paises = [('ANGOLA','LUANDA',1),
('ARGELIA','ARGEL',1),
('BENIN','PORTO-NOVO',1),
('BOTSUANA','GABERONES',1),
('BURKINA FASO','UAGADUGÚ',1),
('BURUNDI','BUYUMBURA',1),
('CABO VERDE','PRAIA',1),
('CAMERÚN','YAUNDÉ',1),
('CHAD','YAMENA',1),
('COMORAS','MORONI',1),
('COSTA DE MARFIL','YAMUSUKRO, ABIYÁN',1),
('EGIPTO','EL CAIRO',1),
('ERITREA','ASMARA',1),
('ETIOPÍA','ADÍS ABEBA',1),
('GABÓN','LIBREVILLE',1),
('GAMBIA','BANJUL',1),
('GHANA','ACCRA',1),
('GUINEA','CONAKRY',1),
('GUINEA ECUATORIAL','MALABO',1),
('GUINEA-BISSAU','BISSAU',1),
('KENIA','NAIROBI',1),
('LESOTO','MASERU',1),
('LIBERIA','MONROVIA',1),
('LIBIA','TRÍPOLI',1),
('MADAGASCAR','ANTANANARIVO',1),
('MALAUI','LILONGÜE',1),
('MALI','BAMAKO',1),
('MARRUECOS','RABAT',1),
('MAURICIO','PORT LOUIS',1),
('MAURITANIA','NUAKCHOT',1),
('MOZAMBIQUE','MAPUTO',1),
('NAMIBIA','WINDHOEK',1),
('NÍGER','NIAMEY',1),
('NIGERIA','ABUYA',1),
('REPÚBLICA CENTROAFRICANA','BANGUI',1),
('REPÚBLICA DEL CONGO','BRAZZAVILLE',1),
('REPÚBLICA DEMOCRÁTICA DEL CONGO','KINSHASA',1),
('REPÚBLICA SAHARAUI','EL AAIÚN',1),
('RUANDA','KIGALI',1),
('SANTO TOMÉ Y PRÍNCIPE','SANTO TOMÉ',1),
('SENEGAL','DAKAR',1),
('SEYCHELLES','VICTORIA',1),
('SIERRA LEONA','FREETOWN',1),
('SOMALIA','MOGADISCIO',1),
('SUAZILANDIA','MBABANE',1),
('SUDÁFRICA','PRETORIA, CIUDAD DEL CABO, BLOEMFONTEIN',1),
('SUDÁN DEL NORTE','JARTUM',1),
('SUDÁN DEL SUR','YUBA',1),
('TANZANIA','DODOMA',1),
('TOGO','LOMÉ',1),
('TÚNEZ','TÚNEZ',1),
('UGANDA','KAMPALA',1),
('YIBUTI','YIBUTI',1),
('ZAMBIA','LUSAKA',1),
('ZIMBABUE','HARARE',1),
('ANTIGUA Y BARBUDA','SAINT JOHNS',2),
('ARGENTINA','BUENOS AIRES',2),
('BAHAMAS','NASSAU',2),
('BARBADOS','BRIDGETOWN',2),
('BELICE','BELMOPÁN',2),
('BOLIVIA','SUCRE, LA PAZ',2),
('BRASIL','BRASILIA',2),
('CANADÁ','OTTAWA',2),
('CHILE','SANTIAGO DE CHILE',2),
('COLOMBIA','BOGOTÁ',2),
('COSTA RICA','SAN JOSÉ',2),
('CUBA','LA HABANA',2),
('DOMINICA','ROSEAU',2),
('ECUADOR','QUITO',2),
('EL SALVADOR','SAN SALVADOR',2),
('ESTADOS UNIDOS','WASHINGTON D. C.',2),
('GRANADA','SAINT GEORGES',2),
('GUATEMALA','CIUDAD DE GUATEMALA',2),
('GUYANA','GEORGETOWN',2),
('HAITÍ','PUERTO PRÍNCIPE',2),
('HONDURAS','TEGUCIGALPA',2),
('JAMAICA','KINGSTON',2),
('MÉXICO','MÉXICO D. F.',2),
('NICARAGUA','MANAGUA',2),
('PANAMÁ','CIUDAD DE PANAMÁ',2),
('PARAGUAY','ASUNCIÓN',2),
('PERÚ','LIMA',2),
('PUERTO RICO','SAN JUAN',2),
('REPÚBLICA DOMINICANA','SANTO DOMINGO',2),
('SAN CRISTÓBAL Y NIEVES','BASSETERRE',2),
('SAN VICENTE Y LAS GRANADINAS','KINGSTOWN',2),
('SANTA LUCÍA','CASTRIES',2),
('SURINAM','PARAMARIBO',2),
('TRINIDAD Y TOBAGO','PUERTO ESPAÑA',2),
('URUGUAY','MONTEVIDEO',2),
('VENEZUELA','CARACAS',2),
('AFGANISTÁN','KABUL',3),
('ARABIA SAUDITA','RIAD',3),
('BANGLADÉS','DACA',3),
('BARÉIN','MANAMÁ',3),
('BRUNEI','BANDAR SERI BEGAWAN',3),
('BUTÁN','TIMBU',3),
('CAMBOYA','PNON PEHN',3),
('CATAR','DOHA',3),
('CHINA','PEKÍN',3),
('CHIPRE','NICOSIA',3),
('COREA DEL NORTE','PYONGYANG',3),
('COREA DEL SUR','SEÚL',3),
('EMIRATOS ARABES UNIDOS','ABU DABI',3),
('FILIPINAS','MANILA',3),
('INDIA','NUEVA DELHI',3),
('INDONESIA','YAKARTA',3),
('IRÁN','TEHERÁN',3),
('IRAQ','BAGDAD',3),
('ISRAEL','JERUSALÉN',3),
('JAPÓN','TOKIO',3),
('JORDANIA','AMMÁN',3),
('KAZAJISTÁN','ASTANÁ',3),
('KIRGUISTÁN','BISKEK',3),
('KUWAIT','CIUDAD DE KUWAIT',3),
('LAOS','VIENTIÁN',3),
('LÍBANO','BEIRUT',3),
('MALASIA','KUALA LUMPUR',3),
('MALDIVAS','MALÉ',3),
('MONGOLIA','ULAN BATOR',3),
('MYANMAR (BIRMANIA)','NAYPYIDAW',3),
('NEPAL','KATMANDÚ',3),
('OMÁN','MASCATE',3),
('PAKISTÁN','ISLAMABAD',3),
('PALESTINA','RAMALA',3),
('SINGAPUR','SINGAPUR',3),
('SIRIA','DAMASCO',3),
('SRI LANKA','COLOMBO',3),
('TAILANDIA','BANGKOK',3),
('TAIWAN','TAIPEH',3),
('TAYIKISTÁN','DUSAMBÉ',3),
('TIMOR ORIENTAL','DILI',3),
('TURKMENISTÁN','ASJABAD',3),
('TURQUÍA','ANKARA',3),
('UZBEKISTÁN','TASHKENT',3),
('VIETNAM','HANOI',3),
('YEMEN','SANÁ',3),
('ALBANIA','TIRANA',4),
('ALEMANIA','BERLÍN',4),
('ANDORRA','ANDORRA LA VIEJA',4),
('ARMENIA','EREVÁN',4),
('AUSTRIA','VIENA',4),
('AZERBAIYÁN','BAKÚ',4),
('BÉLGICA','BRUSELAS',4),
('BIELORRUSIA','MINSK',4),
('BOSNIA Y HERZEGOVINA','SARAJEVO',4),
('BULGARIA','SOFÍA',4),
('CROACIA','ZAGREB',4),
('DINAMARCA','COPENHAGUE',4),
('ESLOVAQUIA','BRATISLAVA',4),
('ESLOVENIA','LUBLIJANA',4),
('ESPAÑA','MADRID',4),
('ESTONIA','TALLÍN',4),
('FINLANDIA','HELSINKI',4),
('FRANCIA','PARÍS',4),
('GEORGIA','TIFLIS',4),
('GRECIA','ATENAS',4),
('HUNGRÍA','BUDAPEST',4),
('IRLANDA','DUBLÍN',4),
('ISLANDIA','REIKIAVIK',4),
('ITALIA','ROMA',4),
('LETONIA','RIGA',4),
('LIECHTENSTEIN','VADUZ',4),
('LITUANIA','VILNA',4),
('LUXEMBURGO','LUXEMBURGO',4),
('MALTA','LA VALETA',4),
('MOLDAVIA','CHISINAU',4),
('MÓNACO','MÓNACO',4),
('MONTENEGRO','PODGORICA',4),
('NORUEGA','OSLO',4),
('PAÍSES BAJOS','AMSTERDAM',4),
('POLONIA','VARSOVIA',4),
('PORTUGAL','LISBOA',4),
('REINO UNIDO','LONDRES',4),
('REPÚBLICA CHECA','PRAGA',4),
('REPÚBLICA DE MACEDONIA','SKOPJE',4),
('RUMANIA','BUCAREST',4),
('RUSIA','MOSCÚ',4),
('SAN MARINO','CIUDAD DE SAN MARINO',4),
('SERBIA','BELGRADO',4),
('SUECIA','ESTOCOLMO',4),
('SUIZA','BERNA',4),
('UCRANIA','KIEV',4),
('VATICANO','CIUDAD DEL VATICANO',4),
('AUSTRALIA','CANBERRA',5),
('FIYI','SUVA',5),
('ISLAS MARSHALL','MAJURO',5),
('ISLAS SALOMÓN','HONIARA',5),
('KIRIBATI','TARAWA',5),
('MICRONESIA','PALIKIR',5),
('NAURU','YAREN',5),
('NUEVA ZELANDA','WELLINGTON',5),
('PALAOS','MELEKEOK',5),
('PAPÚA NUEVA GUINEA','PORT MORESBY',5),
('SAMOA','APIA',5),
('TONGA','NUKU ALOFA',5),
('TUVALU','FUNAFUTI',5),
('VANUATU','PORT VILA',5)]





cursor.executemany(insert_paises,paises)


connection.commit()
connection.close()
