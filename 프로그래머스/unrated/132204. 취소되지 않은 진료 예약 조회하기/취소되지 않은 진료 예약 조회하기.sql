-- 코드를 입력하세요
SELECT a.apnt_no,pt_name,p.pt_no,d.mcdp_cd,dr_name,apnt_ymd from patient p join appointment a on p.pt_no = a.pt_no join doctor d on a.mddr_id=d.dr_id where date(apnt_ymd)='2022-04-13' and apnt_cncl_yn='N' and a.mcdp_cd='cs' order by apnt_ymd;