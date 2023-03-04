-- 코드를 입력하세요
SELECT history_id,round(daily_fee*
                        (CASE
            WHEN DATEDIFF(END_DATE,START_DATE)+1 < 7 THEN 1
            WHEN DATEDIFF(END_DATE,START_DATE)+1 < 30 THEN 0.95
            WHEN DATEDIFF(END_DATE,START_DATE)+1 < 90 THEN 0.92
            ELSE 0.85
         END) *(datediff(end_date,start_date)+1)
                        ) as fee from car_rental_company_car c1 join car_rental_company_rental_history c2 on c1.car_id=c2.car_id join car_rental_company_discount_plan c3 on c1.car_type=c3.car_type where c1.car_type='트럭' group by history_id order by fee desc,history_id desc;