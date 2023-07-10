from radis import calc_spectrum
import matplotlib.pyplot as plt
import time

time_list, timeC_list, lines_list = [], [], []
time_list_va, timeC_list_va, lines_list_va = [], [], []
wmin = 1300
for engine in ['vaex', 'pandas']:
    for w_range in [10, 30, 100, 150, 500, 600]: #[100, 200, 500, 900]:
    # for w_range in [ 50, 1300 ]:
        t0=time.time()
        s = calc_spectrum(wmin, wmin + w_range,         # cm-1
                      molecule='H2O',
                      isotope='1,2,3',
                      pressure=1.01325,   # bar
                      Tgas=1000,           # K
                      mole_fraction=0.1,
                    #   wstep='auto',
                    #   path_length=1,      # cm
                      databank='hitemp',  # or 'hitemp', 'geisa', 'exomol'
                      engine=engine,
                      )

        t1=time.time()
        # time.sleep(5)
        if engine == "vaex":
            timeC_list_va.append(s.conditions['calculation_time'])
            lines_list_va.append(s.conditions['lines_calculated'])
            time_list_va.append(t1 - t0)
            # lines_list_va.append(s.conditions['lines_calculated']+s.conditions['lines_cutoff'])
        else:
            timeC_list.append(s.conditions['calculation_time'])
            lines_list.append(s.conditions['lines_calculated'])
            time_list.append(t1 - t0)
            # lines_list.append(s.conditions['lines_calculated']+s.conditions['lines_cutoff'])

plt.figure()
plt.plot(lines_list, time_list, 'k', label='pandas total')
plt.plot(lines_list, timeC_list, 'k--', label='pandas computation')
plt.plot(lines_list_va, time_list_va, 'r', label='vaex total')
plt.plot(lines_list_va, timeC_list_va, 'r--', label='vaex computation')
plt.ylabel('Time [s]')
plt.xlabel('Number of lines')
plt.legend()
plt.show()
# print('Time taken : '+str(t1 - t0))
#
# print(s.conditions['lines_calculated'])
