CREATE DATABASE admission;

USE admission;

CREATE TABLE IF NOT EXISTS application (
application_id INT(16) NOT NULL AUTO_INCREMENT,
abit_id INT(16) NOT NULL,
abit_passport INT(16) NOT NULL,
abit_certificate INT(16) NOT NULL,
abit_name VARCHAR(256) NOT NULL,
PRIMARY KEY (application_id)
);

CREATE TABLE IF NOT EXISTS docs (
docs_id INT(16) NOT NULL AUTO_INCREMENT,
abit_id INT(16) NOT NULL,
abit_passport INT(16) NOT NULL,
abit_certificate INT(16) NOT NULL,
abit_name VARCHAR(256) NOT NULL,
application_id INT(16) NOT NULL,
PRIMARY KEY (docs_id, abit_passport, abit_certificate),
FOREIGN KEY (application_id) REFERENCES application (application_id)
);

CREATE TABLE IF NOT EXISTS abit (
abit_id INT(16) NOT NULL AUTO_INCREMENT,
abit_passport INT(16) NOT NULL,
abit_certificate INT(16) NOT NULL,
abit_class INT(2) NOT NULL,
abit_name VARCHAR(256) NOT NULL,
application_id INT(16) NOT NULL,
speciality_code INT(16) NOT NULL,
studying_form VARCHAR(16) NOT NULL,
exam_balls INT(4) NOT NULL,
docs_id INT(16) NOT NULL,
PRIMARY KEY (abit_id),
FOREIGN KEY (docs_id, abit_passport, abit_certificate) REFERENCES docs (docs_id, abit_passport, abit_certificate)
);

ALTER TABLE application
ADD FOREIGN KEY (abit_id) REFERENCES abit (abit_id);

CREATE TABLE IF NOT EXISTS exam (
exam_id INT(16) NOT NULL AUTO_INCREMENT,
exam_prof INT(4) NOT NULL,
exam_other INT(4) NOT NULL,
abit_id INT(16) NOT NULL,
PRIMARY KEY (exam_id),
FOREIGN KEY (abit_id) REFERENCES abit (abit_id) 
);

CREATE TABLE IF NOT EXISTS faculty (
faculty_code INT(16) NOT NULL,
faculty_name VARCHAR(256) NOT NULL,
cathedra_code INT(16) NOT NULL,
PRIMARY KEY (faculty_code)
);

CREATE TABLE IF NOT EXISTS cathedra (
cathedra_code INT(16) NOT NULL,
cathedra_name VARCHAR(256) NOT NULL,
faculty_code INT(16) NOT NULL,
speciality_code INT(16) NOT NULL,
PRIMARY KEY (cathedra_code),
FOREIGN KEY (faculty_code) REFERENCES faculty (faculty_code)
);

ALTER TABLE faculty
ADD FOREIGN KEY (cathedra_code) REFERENCES cathedra (cathedra_code);

CREATE TABLE IF NOT EXISTS speciality (
speciality_code INT(16) NOT NULL,
speciality_name VARCHAR(256) NOT NULL,
speciality_free_places INT(8) NOT NULL,
speciality_application_number INT(8) NOT NULL,
speciality_passing_score INT(4) NOT NULL,
cathedra_code INT(16) NOT NULL,
PRIMARY KEY (speciality_code),
FOREIGN KEY (cathedra_code) REFERENCES cathedra (cathedra_code)
);

ALTER TABLE cathedra
ADD FOREIGN KEY (speciality_code) REFERENCES speciality (speciality_code);

CREATE TABLE IF NOT EXISTS secretary (
secretary_code INT(16) NOT NULL,
secretary_name VARCHAR(256) NOT NULL,
application_id INT(16) NOT NULL,
PRIMARY KEY (secretary_code),
FOREIGN KEY (application_id) REFERENCES application (application_id)
);

CREATE TABLE IF NOT EXISTS studying_form (
abit_id INT(16) NOT NULL,
is_budget boolean,
is_contract boolean,
FOREIGN KEY (abit_id) REFERENCES abit (abit_id)
);

SET foreign_key_checks = 0; -- switch off foreign_key_checks to simplify INSERT INTO

INSERT INTO application(abit_id, abit_passport, abit_certificate, abit_name) VALUES
('1', '400', '230', 'Pelevin'),
('2', '401', '231', 'Nabokov'),
('3', '402', '232', 'Dostoevsky'),
('4', '403', '233', 'Griboedov'),
('5', '404', '234','Mayakovsky');

INSERT INTO abit(application_id, abit_passport, abit_certificate, abit_name, abit_class, speciality_code, studying_form, exam_balls, docs_id) VALUES
('1', '400', '230', 'Pelevin', '9', '111', 'budget', '285', '1'),
('2', '401', '231', 'Nabokov', '11', '112', 'budget', '270', '2'),
('3', '402', '232', 'Dostoevsky', '9', '111', 'contract', '250', '3'),
('4', '403', '233', 'Griboedov', '11', '112', 'contract', '260', '4'),
('5', '404', '234','Mayakovsky', '9', '111', 'budget', '300', '5');

INSERT INTO docs(abit_id, abit_passport, abit_certificate, abit_name, application_id) VALUES
('1', '400', '230', 'Pelevin', '1'),
('2', '401', '231', 'Nabokov', '2'),
('3', '402', '232', 'Dostoevsky', '3'),
('4', '403', '233', 'Griboedov', '4'),
('5', '404', '234','Mayakovsky', '5');

INSERT INTO exam(abit_id, exam_prof, exam_other) VALUES
('1', '185', '100'),
('2', '170', '100'),
('3', '150', '100'),
('4', '160', '100'),
('5', '200', '100');

INSERT INTO faculty VALUES
('1201', 'LITERATURE', '120'),
('1202', 'POETRY', '121');

INSERT INTO cathedra VALUES
('120', 'POSTMODERN AND FUTURISM', '1201', '111'),
('121', 'CLASSICAL', '1202', '112');

INSERT INTO speciality VALUES
('111', 'WRITER', '20', '253', '280', '120'),
('112', 'POETRY', '15', '384', '265', '121');

INSERT INTO secretary VALUES
('244582', 'Belinsky', '1'),
('244743', 'Gogol', '2'),
('234756', 'Derzhavin', '3'),
('245768', 'Platon', '4'),
('244777', 'Pushkin', '5');

INSERT INTO studying_form(abit_id, is_budget, is_contract) VALUES
('1', '1', '0'),
('2', '1', '0'),
('3', '0', '1'),
('4', '0', '1'),
('5', '1', '0');

SET foreign_key_checks = 1; -- switch on foreign_key_checks
