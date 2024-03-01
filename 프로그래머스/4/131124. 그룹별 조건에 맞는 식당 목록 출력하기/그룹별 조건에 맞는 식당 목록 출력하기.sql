with sub as (
    select member_id 
                  from rest_review
                 group by member_id
                 order by count(rest_id) desc
                  limit 1
                 )

select member_name,review_text,date_format(review_date,'%Y-%m-%d')
from member_profile join rest_review using(member_id)
where member_id in (select member_id from sub)
order by review_date,review_text;