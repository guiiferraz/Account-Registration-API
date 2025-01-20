-- > Obs < --
    """ O PostgreSQL é sensível a valores com Maisculas, minusculas e aspas. """

-- > Crate databas < --

create database "Database_example"

-- > table(s) < -- 

create table "Accounts"(
    id serial primary key,
    name varchar(30),
    number int,
);

-- > values example < --

insert into "Accounts" ("Name", "Number") values("Aizen", 1234); 

-- > select example < --

select * from "Accounts";
select * from "Accounts" Where "Name" = 'Name_example'

-- > reduct auto increment value  <--
select setval("Accounts_id_seq", 1, false)

-- > drop tables exampl < --
drop table "Accounts"; -- > DANGER! < --
