def read_from_file(sday, eday, filename):
    from netCDF4 import Dataset                     # For reading data
    import numpy as np

    data_in = Dataset(filename)
    data_dict = dict();
    data_dict['time'] = data_in.variables['time'][:]-366.
    data_dict['day_for_plot'] = "day %d" % int(data_dict['time'][eday-1])
    data_dict['h'] = -data_in.variables['HBLT'][:,0,0]/100
    data_dict["w'T'_raw"] = data_in.variables['VTTF_norm'][:,:,0,0]
    data_dict['zl'] = -data_in.variables['z_w_bot'][:]/100
    data_dict["temperature"] = data_in.variables['TEMP'][:,:,0,0]
    data_dict["w'T'"] = [1.0]
    for wt in data_dict["w'T'_raw"][sday-1,:]:
        data_dict["w'T'"].append(float(wt))
    for t in range(sday,eday):
        data_dict["w'T'"][1:] = data_dict["w'T'"][1:] + data_dict["w'T'_raw"][t,:]
    data_dict["w'T'"] = np.array(data_dict["w'T'"])
    data_dict["w'T'"][1:] = data_dict["w'T'"][1:]/(eday - sday + 1)
    data_dict['zplot'] = [0.0]
    for z in data_dict['zl']:
        data_dict['zplot'].append(float(z))
    return data_dict
