.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price)
  FROM inventory
  GROUP BY item;


CREATE TABLE best_deals AS
  SELECT name, min(MSRP/rating) as Cost_performance
  FROM products
  GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT b.name, l.store
  FROM best_deals as b, lowest_prices as l
  WHERE b.name = l.item;


CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs)
  FROM shopping_list, stores
  WHERE shopping_list.store = stores.store;
