select CONCAT(edup.Fname,' ',edup.Minit,' ',edup.Lname) as 'Full Name' , edup.Ssn as ssn, edup.Dno as 'Dept. Id',count(e.Super_ssn) as 'Dept. Number of employees'
from EMPLOYEE e,EMPLOYEE edup 
where e.Super_ssn = edup.Ssn
group by edup.Ssn
order by edup.Fname , edup.Minit , edup.Lname;
