import geopandas as gpd
geodf = gpd.read_file("maps/SPH_KRAJ.shp")

geodf.to_file("maps/geojson", driver = "GeoJSON")
