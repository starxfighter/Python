use world;

select country.name, countrylanguage.language, countrylanguage.Percentage
from country
left join countrylanguage on country.code = countrylanguage.countrycode
where countrylanguage.language = 'Slovene' 
order by country.name desc;

select country.name, count(*) as num_of_cities
from country
left join city on country.code = city.countrycode
group by country.name
order by country.name desc;

select city.name, city.population
from country 
left join city on country.code = city.CountryCode
where city.population > 500000 and country.code = "MEX"
order by city.population desc;

select country.name, cl.Language, cl.Percentage
from country
left join countrylanguage as cl on country.code = cl.CountryCode
where cl.Percentage >= 89.0
order by cl.Percentage desc, country.name asc;

select country.name, country.SurfaceArea as surface_area, country.population
from country
where country.SurfaceArea < 501 and country.population > 100000
order by country.name asc;

select country.name, country.GovernmentForm as Government, country.Capital, country.LifeExpectancy as Life_Exp
from country
where country.GovernmentForm = "Constitutional Monarchy" and country.capital > 200 and country.LifeExpectancy >= 75.0
order by country.name asc;

select country.name, city.name, city.District, city.Population
from country
left join city on country.code = city.CountryCode
where country.code = "ARG" and city.District = "Buenos Aires" and city.population >= 500000
order by city.name asc; 

select region, count(*) as Countries
from country
group by region
order by countries desc;