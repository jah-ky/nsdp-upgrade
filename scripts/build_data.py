from sdg.open_sdg import open_sdg_build
from alter_meta import alter_meta
from alter_data import alter_data
from indicator_callback import indicator_callback

open_sdg_build(config='config_data.yml',
    alter_meta=alter_meta,
    alter_data=alter_data,
    indicator_callback=indicator_callback
)
