use friendship;
 
insert into users (first_name, last_name, created_at, updated_at)
values ("Chris", "Baker", NOW(), NOW());
 
insert into users (first_name, last_name, created_at, updated_at)
values ("Diana", "Smith", NOW(), NOW());
 
insert into users (first_name, last_name, created_at, updated_at)
values ("James", "Johnson", NOW(), NOW());
 
insert into users (first_name, last_name, created_at, updated_at)
values ("Jessica", "Davidson", NOW(), NOW());

insert into friendships (user_id, freind_id1, created_at, updated_at)
values (1,4,now(), now());

insert into friendships (user_id, freind_id1, created_at, updated_at)
values (1,3,now(), now());

insert into friendships (user_id, freind_id1, created_at, updated_at)
values (1,2,now(), now());

insert into friendships (user_id, freind_id1, created_at, updated_at)
values (2,1,now(), now());

insert into friendships (user_id, freind_id1, created_at, updated_at)
values (3,1,now(), now());

insert into friendships (user_id, freind_id1, created_at, updated_at)
values (4,1,now(), now());

select users2.first_name as friend_first_name, users2.last_name as friend_last_name, users.first_name, users.last_name
from users
left join friendships on friendships.freind_id1 = users.id
left join users as users2 on users2.id = friendships.User_id
order by users2.last_name asc;











