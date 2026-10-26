import glob
import rasterio
raster_fodder = sorted(glob.glob(rf"B:\GCWM\MIRCA-OS_FAO_compareation\MIRCA-OS_2020\MIRCA-OS_Fodder_*.tif"))
gap_year = 4
for i in range(len(raster_fodder)-1):
    for j in range(gap_year):

        year = int(raster_fodder[i].split("_")[-1].replace(".tif", ""))+j+1

        with rasterio.open(raster_fodder[i]) as pre, rasterio.open(raster_fodder[i+1]) as lat:

            previous = pre.read(1).astype("float32")
            later = lat.read(1).astype("float32")
            prof = pre.profile
            fodder = previous + (later - previous)/(gap_year+1)*(j+1)
            out_put_path = rf"B:\GCWM\MIRCA-OS_FAO_compareation\scale_factor\MIRCA-OS_Fodder_{year}.tif"

            with rasterio.open(
                out_put_path,
                "w",
                **prof
            )as dst:
                dst.write(fodder, 1)