Title: Playing with GTFS - New Zones
Date: 2018-04-04 02:53
Modified: 2018-04-04 02:53
Category: Posts
Tags: openbus, gtfs, pandas, seaborn, partridge,
Authors: Dan Bareket
Summary: Very short notebook showing how to deal with the new MOT stop to zone mapping 

We have noticed a big change in how MOT uses the `zone_id` field. There are thousands of zones now, as compared to a few dozens that were there about three months ago.

I took a look at the `Tariff.zip` file in the FTP folder, and noticed that it now includes two files - `Tariff.txt`, which we knew from before, and a new file `StationToReformZone.txt` which includes a new mapping. This change is documented in MOT's [developers pdf](https://www.gov.il/BlobFolder/generalpage/gtfs_general_transit_feed_specifications/he/%D7%A1%D7%98%20%D7%A7%D7%91%D7%A6%D7%99%D7%9D%20-%20GTFS%20-%20%D7%94%D7%A1%D7%91%D7%A8%20%D7%9C%D7%9E%D7%A4%D7%AA%D7%97%D7%99%D7%9D_0.pdf).

There are examples and explanations in. The rest of this notebook just shows how to work with these changes by merging the partridge pandas dataframes.

{% notebook openbus_6_new_zone.ipynb %}
