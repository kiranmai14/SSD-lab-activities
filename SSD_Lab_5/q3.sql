select d.Mgr_ssn as Manager_ssn , count(d.Mgr_ssn) as Number_of_projects
from DEPARTMENT d , PROJECT pd
where  d.Dnumber = pd.Dnum and 
pd.Dnum IN (select p.Dnum from PROJECT p where p.Pname = 'ProductY')
group by d.Mgr_ssn;