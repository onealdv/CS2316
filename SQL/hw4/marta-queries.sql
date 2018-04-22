
use marta;

-- What is the stop_name where the most people got on?


select stops.stop_name, max(passenger_data.on_number) as on_number
from stops natural join passenger_data
group by stops.stop_id
having on_number = (select max(passenger_data.on_number) as on_number
                    from stops naturaly join passenger_data
                    group by stops.stop_id
                    order by on_number desc
                    limit 1)
;
-- What is the stop_name where the most people got off?
select stops.stop_name, max(passenger_data.off_number) as off_number
from stops natural join passenger_data
group by stops.stop_id
having off_number = (select max(passenger_data.off_number) as off_number
                    from stops naturaly join passenger_data
                    group by stops.stop_id
                    order by off_number desc
                    limit 1)
;

