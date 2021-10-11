select distinct CONCAT(m.Fname,' ',m.Minit,' ',m.Lname) as 'Full Name', m.Ssn as ssn,m.Dno as 'Dept. Id' , d.Dname as 'Dept. Name'
from EMPLOYEE e, DEPARTMENT d,EMPLOYEE m
where m.Ssn = d.Mgr_ssn and d.Dnumber = m.Dno and e.Dno = d.Dnumber and 
e.Ssn IN ( select  distinct wo.Essn from WORKS_ON wo group by wo.Essn having sum(Hours) < 40.0 );