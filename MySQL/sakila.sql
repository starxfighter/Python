use sakila;

select city.city_id, city.city, customer.first_name, customer.last_name, address.address, customer.email
from customer
	join address
		on customer.address_id = address.address_id
	join city
		on city.city_id = address.city_id
where city.city_id = 312;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name
from film
	join film_category
		on film.film_id = film_category.film_id
	join category
		on category.category_id = film_category.category_id
where category.name = "Comedy";

select actor.actor_id, CONCAT(actor.first_name, "--", actor.last_name) as Actor, film.title, film.description, film.release_year
from actor	
	join film_actor
		on film_actor.actor_id = actor.actor_id
	join film	
		on film.film_id = film_actor.film_id
where actor.actor_id = 5;

select customer.store_id, address.city_id, CONCAT(customer.first_name, '__' , customer.last_name) as Customer, customer.email, address.address
from customer
	join address
		on address.address_id = customer.address_id
where customer.store_id = 1
and
address.city_id in (1,42,312,459);

select film.title, film.description, film.release_year, film.rating, film.special_features, actor.actor_id
from film
	join film_actor
		on film.film_id = film_actor.film_id
	join actor
		on actor.actor_id = film_actor.actor_id
where film.rating = "G" and
film.special_features  like '%Behind the Scenes%' and
actor.actor_id = 15;

select film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name, actor.last_update
from film
	join film_actor
		on film.film_id = film_actor.film_id
	join actor
		on film_actor.actor_id = actor.actor_id
where film.film_id = 369;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
from film
	join film_category
		on film.film_id = film_category.film_id
	join category
		on film_category.category_id = category.category_id
where category.name = "Drama" and
film.rental_rate = 2.99;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name , CONCAT(actor.first_name, " ", actor.last_name) as Actor
from film
	join film_category
		on film.film_id = film_category.film_id
	join category
		on film_category.category_id = category.category_id
	join film_actor
		on film.film_id = film_actor.film_id
	join actor
		on film_actor.actor_id = actor.actor_id
where category.name = "Action" and
CONCAT(actor.first_name, " ", actor.last_name) = "SANDRA KILMER";
    

























