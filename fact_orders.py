from datetime import date

from sqlalchemy import VARCHAR


CREATE TABLE `Histori Transaksi` (
  `order_id` int(45) NOT NULL,
  `order_date` date(45) NOT NULL,
  `user_id` VARCHAR(11) NOT NULL,
  `order_total` int(11) NOT NULL,
 PRIMARY KEY (`id`));