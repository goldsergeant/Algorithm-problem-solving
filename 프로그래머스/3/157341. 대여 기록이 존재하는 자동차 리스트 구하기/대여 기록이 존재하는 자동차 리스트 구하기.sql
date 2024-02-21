select distinct(car_id) 
from CAR_RENTAL_COMPANY_CAR
where car_id in (select car_id 
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                where start_date like '%-10-%' and car_type ='세단')
order by car_id desc;
                 