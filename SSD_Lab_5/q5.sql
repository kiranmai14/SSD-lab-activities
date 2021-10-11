select d.Mgr_ssn as 'Manager ssn' , d.Dnumber as 'Dept. Id' , count(*) as 'Number of Dependents'
from DEPARTMENT d , DEPENDENT p
where d.Mgr_ssn = p.Essn and
d.Dnumber IN (select  distinct loc.Dnumber from DEPT_LOCATIONS loc  group by loc.Dnumber having count(loc.Dnumber) > 1)
group by d.Mgr_ssn,d.Dnumber