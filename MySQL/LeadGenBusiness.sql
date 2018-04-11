use lead_gen_business;

select monthname(charged_datetime) as Month, sum(amount) as Revenue
from billing
where monthname(charged_datetime) = "March";

select client_id, sum(amount) 
from billing
where client_id = 2;

select domain_name as website, client_id
from sites
where client_id =10;

select client_id, COUNT(domain_name), monthname(created_datetime), year(created_datetime)
from sites
where client_id = 1
group by monthname(created_datetime);

select domain_name as website, count(leads.leads_id), leads.registered_datetime as date_generated
from sites
 join leads
	on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-02-16'
group  by domain_name;

select concat(clients.first_name, " ", clients.last_name) as client_name, count(leads.leads_id) as number_of_leads
from leads
	join sites	
		on sites.site_id = leads.site_id
	join clients
		on clients.client_id = sites.client_id
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by clients.client_id;

select concat(clients.first_name, " ", clients.last_name) as client_name, count(leads.leads_id) as number_of_leads, monthname(leads.registered_datetime)
from leads
	join sites
		on  sites.site_id = leads.site_id
	join clients
		on clients.client_id = sites.client_id
where leads.registered_datetime between '2011-01-01' and '2011-07-01'
group by clients.client_id
order by monthname(leads.registered_datetime);

select concat(clients.first_name, " ", clients.last_name) as client_name, domain_name, count(leads.leads_id) as number_of_leads, leads.registered_datetime
from leads
	join sites
		on  sites.site_id = leads.site_id
	join clients
		on clients.client_id = sites.client_id
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by domain_name
order by clients.client_id;
	
select concat(clients.first_name, " ", clients.last_name) as client_name, domain_name, count(leads.leads_id) as number_of_leads, leads.registered_datetime
from leads
	join sites
		on  sites.site_id = leads.site_id
	join clients
		on clients.client_id = sites.client_id
group by domain_name
order by clients.client_id;

select concat(clients.first_name, " ", clients.last_name) as client_name, sum(billing.amount), monthname(charged_datetime) as month_charge, year(charged_datetime) as year_charge
from clients
	join billing
		on clients.client_id = billing.client_id
group by monthname(charged_datetime), year(charged_datetime), clients.client_id
order by clients.client_id;

select concat(clients.first_name, " ", clients.last_name) as client_name, group_concat(domain_name separator ' / ') as sites
from clients
	join sites
		on clients.client_id = sites.client_id
group by clients.client_id
order by clients.client_id;





