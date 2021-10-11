select  dt.Dnumber as 'Dept. Id', dt.Dname as 'Dept. Name' , count(*) as 'Number of locations'
from DEPARTMENT dt , DEPT_LOCATIONS loc
where dt.Dnumber = loc.Dnumber and 
dt.Mgr_ssn IN (select  distinct d.Essn from DEPENDENT d where d.Sex = 'F' group by d.Essn having count(d.Essn) > 1)
group by (dt.Dnumber);