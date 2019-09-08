-- Using the Google Cloud Platform USA Names dataset
-- https://console.cloud.google.com/marketplace/details/social-security-administration/us-names?q=usa%20names
-- https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=usa_names&page=dataset

#standardSQL

SELECT
  state,
  gender,
  year,
  name,
  number
FROM
  `bigquery-public-data.usa_names.usa_1910_current`