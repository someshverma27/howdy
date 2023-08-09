import numpy as np
from radis.spectrum.utils import CONVOLUTED_QUANTITIES

def solve():
    from radis import SpectrumFactory

    sf_vaex = SpectrumFactory(
        wavelength_min=4200,
        wavelength_max=4500,
        cutoff=1e-23,
        molecule="CO2",
        dataframe_type="pandas",
    )
    sf_vaex.fetch_databank("hitran")
    s_vaex = sf_vaex.eq_spectrum(Tgas=2000)  # failing on the 08/03/2023 - minouHub

    sf_pd = SpectrumFactory(
        wavelength_min=4200,
        wavelength_max=4500,
        cutoff=1e-23,
        molecule="CO2",
        dataframe_type="vaex",
    )
    sf_pd.fetch_databank("hitran",output="vaex")
    s_pd = sf_pd.eq_spectrum(Tgas=2000)

    for column in sf_pd.df1.columns:
        assert np.all(sf_vaex.df1[column] == sf_pd.df1[column].to_numpy())

    for spec_quantity in CONVOLUTED_QUANTITIES:
        assert np.allclose(
            s_vaex.get(spec_quantity)[1], s_pd.get(spec_quantity)[1], equal_nan=True
        )

solve()