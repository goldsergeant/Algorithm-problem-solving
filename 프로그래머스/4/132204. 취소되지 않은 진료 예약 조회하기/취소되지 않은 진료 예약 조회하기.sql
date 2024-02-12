select apnt_no,pt_name,a.pt_no,a.mcdp_cd,dr_name,apnt_ymd
from patient p join appointment a on p.pt_no = a.pt_no join doctor d on a.mddr_id = d.dr_id
where apnt_ymd like '2022-04-13%' and apnt_cncl_yn='N'
order by apnt_ymd;